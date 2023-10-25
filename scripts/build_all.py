#!/usr/bin/python3

import glob
import os
import subprocess


# Which branches to build and/or analyze
all = False
non_idf = False
x86_only = False
arm_or_x86 = True

# Build and/or Analyze
build = True
analyze = True

non_idf_branches = [ 'release/v2.0',     # Non-idf branches use an older make structure
                     'release/v2.1',
                     'release/v3.0',
                     'release/v3.1',
                     'release/v3.2',
                     'release/v3.3' ]

esp_idf_branches_x86_only = [ 'release/v4.0',
                              'release/v4.1',
                              'release/v4.3' ]

esp_idf_branches_arm_or_x86 = [ #'release/v4.4',
                                #'release/v5.0',
                                'release/v5.1' ]

# Create list of branches to build
branches_to_build = []
if all:
    branches_to_build.extend(non_idf_branches)
    branches_to_build.extend(esp_idf_branches_x86_only)
    branches_to_build.extend(esp_idf_branches_arm_or_x86)
else:
    if non_idf:
        branches_to_build.extend(non_idf_branches)
    if x86_only:
        branches_to_build.extend(esp_idf_branches_x86_only)
    if arm_or_x86:
        branches_to_build.extend(esp_idf_branches_arm_or_x86)

# Get current dir
base_dir = os.getcwd()

# Paths
esp_idf_path = os.path.join(base_dir, "esp-idf")
esp_idf_examples_path = os.path.join(esp_idf_path, "examples")
elf_out_parent_path = base_dir
esp_idf_export_path = os.path.join(esp_idf_path, "export.sh")
esp_idf_source_command = "source " + esp_idf_export_path + "\n"
idf_tools_path = os.path.join(esp_idf_path, "idf_tools_dir")

if not os.path.exists(elf_out_parent_path):
    os.mkdir(elf_out_parent_path)

for branch in branches_to_build:

    os.chdir(esp_idf_path)
    subprocess.run(["git", "submodule", "deinit", "-f", "--all"])
    subprocess.run(["git", "clean", "-ffdx"])
    subprocess.run(["git", "checkout", "-f", branch])
    subprocess.run(["git", "submodule", "update", "--init", "--recursive"])
    
    if os.path.exists(idf_tools_path):
        print(idf_tools_path)
        subprocess.run(["rm", "-rf", idf_tools_path])
    
    os.mkdir(idf_tools_path)

    # Need a helper script to handle exports
    if branch in non_idf_branches:
        os.chdir(idf_tools_path)
        install_helper_script = open("install_helper.sh", "a")
        install_helper_script.write("#!/bin/bash\n")
        if branch in ["release/v2.0", "release/v2.1"]:
            install_helper_script.write("wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz\n")
            install_helper_script.write("tar -xzf xtensa-esp32-elf-linux64-1.22.0-61-gab8375a-5.2.0.tar.gz\n")
        elif branch in ['release/v3.0', 'release/v3.1', 'release/v3.2']:
            install_helper_script.write("wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz\n")
            install_helper_script.write("tar -xzf xtensa-esp32-elf-linux64-1.22.0-80-g6c4433a-5.2.0.tar.gz\n")
        elif branch == 'release/v3.3':
            install_helper_script.write("wget https://dl.espressif.com/dl/xtensa-esp32-elf-linux64-1.22.0-97-gc752ad5-5.2.0.tar.gz\n")
            install_helper_script.write("tar -xzf xtensa-esp32-elf-linux64-1.22.0-97-gc752ad5-5.2.0.tar.gz\n")
        if os.path.exists(os.path.join(esp_idf_path, "requirements.txt")):
            install_helper_script.write("pip2.7 install -r" + os.path.join(esp_idf_path, "requirements.txt") + "\n")
    else:
        # Need a helper script to handle exports
        install_helper_script = open("install_helper.sh", "a")
        install_helper_script.write("#!/bin/bash\n")
        install_helper_script.write("export IDF_TOOLS_PATH=" + idf_tools_path + "/\n")
        install_helper_script.write("./install.sh\n")
        install_helper_script.write(esp_idf_source_command)
    
    install_helper_script.close()
    
    subprocess.run(["chmod", "+x", "./install_helper.sh"], stdout=open(os.devnull, 'wb'))

    subprocess.run(["./install_helper.sh"])

    os.chdir(base_dir)

    branch_escaped = branch.replace("/", "_")

    elf_out_child_path = os.path.join(elf_out_parent_path, branch_escaped)

    if not os.path.exists(elf_out_child_path):
        os.mkdir(elf_out_child_path)

    os.chdir(esp_idf_examples_path)
    example_project_glob = glob.glob('./**/README.md', recursive=True)

    example_projects = []
    for index, example_project in enumerate(example_project_glob):
        full_path = os.path.dirname(os.path.normpath(os.path.join(esp_idf_examples_path, example_project)))
        
        if not full_path == esp_idf_examples_path:
            example_projects.append(full_path)

    example_project_count = len(example_projects) - 1

    for index, example_project in enumerate(example_projects):
        os.chdir(example_project)
        if not os.path.isfile("build_helper.sh"):
            if branch in non_idf_branches:
                build_helper_script = open("build_helper.sh", "a")
                build_helper_script.write("#!/bin/bash\n")
                build_helper_script.write("export PATH=$PATH:" + os.path.join(idf_tools_path, "xtensa-esp32-elf", "bin") + "\n")
                build_helper_script.write("export IDF_PATH=" + esp_idf_path + "\n")
                build_helper_script.write("export IDF_CCACHE_ENABLE=1\n")
                build_helper_script.write("make defconfig\n")
                build_helper_script.write('sed -i "s/python/python2.7/" sdkconfig\n')
                build_helper_script.write("make\n")
                build_helper_script.close()
            else:
                build_helper_script = open("build_helper.sh", "a")
                build_helper_script.write("#!/bin/bash\n")
                build_helper_script.write("export IDF_TOOLS_PATH=" + idf_tools_path + "/\n")
                build_helper_script.write(esp_idf_source_command)
                build_helper_script.write("idf.py build\n")
                build_helper_script.close()

        subprocess.run(["chmod", "+x", "./build_helper.sh"], stdout=open(os.devnull, 'wb'))
        subprocess.run(["./build_helper.sh"])

    os.chdir(esp_idf_path)

    elf_glob = glob.glob('./**/*.elf', recursive=True)
    elf_count = len(elf_glob) - 1

    for index, elf in enumerate(elf_glob):
        elf = os.path.normpath(os.path.join(esp_idf_path, elf))

        if os.path.basename(elf) == "bootloader.elf":
            project_name = os.path.normpath(elf).split(os.path.sep)[-4]     # Bootloader
        else:
            project_name = os.path.normpath(elf).split(os.path.sep)[-3]     # App
        
        if "examples" in elf:
            elf_type = "example"
        elif "components" in elf:
            elf_type = "component"
        else:
            elf_type = "unknown"
        
        new_elf = os.path.normpath(elf).split(os.path.sep)
        new_elf[-1] = str(index) + "-" + elf_type + "-" + project_name + "-" + os.path.basename(elf)

        new_elf = os.path.normpath(os.path.join("/", *new_elf))
        os.rename(elf, new_elf)
        cp_cmd = ["cp", new_elf, elf_out_child_path]
        subprocess.run(cp_cmd)

# Cleanup
os.chdir(esp_idf_path)
subprocess.run(["git", "submodule", "deinit", "-f", "--all"])
subprocess.run(["git", "clean", "-ffdx"])
