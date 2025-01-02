# GLFW

## Setup
### Windows
  - download source code
  - open cmake
    - choose glfw folder(not src)
    - choose build (create build folder in glfw folder)
    - configure
    - generate
  - open build/sln
  - build
  - copy build/src/Debug/glfw.lib
  - copy glfw/include folder
  - create GLFW and paste
  - refer to how to link static lib in Visual Studio(./source/Visual Studio)
  - paste Starting code from Documentation
  - anotate glClear

### MacOS (Easy)
  - Brew : `brew install glfw`
### MacOS
  - Download -> download `macOS pre-compiled binaries`
  - copy lib from `./lib-arm64` to `./GLFW/lib` in project folder
  - copy include from `./include` to `./GLFW` in project folder
  - reference header as `"./GLFW/glfw3"`
  - add include and linker path for compiler 
    ```
    APP_INCLUDES:= -I../GLFW/include/
    APP_LINKERS:= -L../GLFW/lib/ -lglfw3 -framework Cocoa -framework IOKit
    ```
- ### Linux


## Useful Links

- [GLFW Official](https://www.glfw.org)

