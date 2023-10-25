# esp-idf_elfs

## esp-idf versions
```
branch              x86         arm64       build_all.py    
                    build       build        
--------------------------------------------------------
release/v2.0        +           -           +                      
release/v2.1        +           -           +                       
release/v3.0        +           -           +                       
release/v3.1        +           -           +                       
release/v3.2        +           -           +                       
release/v3.3        +           -           +                     
release/v4.0        +           -           +                      
release/v4.1        +           -           +
release/v4.2        -           -           -                      
release/v4.3        +           -           +
release/v4.4        +           +           +
release/v5.0        +           +           +
release/v5.1        +           +           +
```
* `x86 build` and `arm64 build` indicates which host arch can build the esp-idf example projects
* `build_all.py` means that signatures can be generated for the branch

## how to use
1. Clone this repo
    ```
    git clone https://github.com/austinc3030/esp-idf_elfs.git --recurse-submodules
    ```
2. Install dependencies, such as `pip2.7`, `pyserial==2.7`, etc.
    ```
    ./scripts/install_dependencies.sh
    ```
3. OPTIONAL: test first by running (This will reduce the number of examples and verify everything should run correctly)
    ```
    ./scripts/set_repo_for_testing.sh
    ```
- Note: after this, you should re-clone the repo from step 1 as I never made a script to undo the testing part
4. Build signatures
    ```
    ./scripts/build_all.py
    ```
and wait... for a while... like, days depending on your computer.

## notes
- 4.2
  - pip error during install.sh
    - prevents export.sh and idf.py
    - seems to be with `gevent`
