# CMake

## Tips
- List Installed Modules : `cmake --help-module-list`

## Setup 
- Directory :
```
mkdir cmake-hello-world
cd cmake-hello-world
```

- main.cpp: `touch main.cpp`
```
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```
- CMakeList : `touch CMakeLists.txt`
```
cmake_minimum_required(VERSION 3.10)
project(hello-world)

add_executable(hello-world main.cpp)
```
- Build :
```
mkdir build
cd build
cmake ..
cmake -S my-project -B my-project/build   //Choose Build Folder
cmake -G "Xcode" ../  //Choose Generator
```

- Native Build : `make`
- Run Executable : `./hello-world`