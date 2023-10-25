#!/usr/bin/python3

import glob
import os
import subprocess


base_dir = os.getcwd()

# Paths
esp_idf_path = os.path.join(base_dir, "esp-idf")
esp_idf_examples_path = os.path.join(esp_idf_path, "examples")
elf_out_child_path = os.path.join(base_dir, "release_v5.1")

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
    print(cp_cmd)
    subprocess.run(cp_cmd)
