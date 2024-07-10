# Compiler

## Basic

## LLVM
- [Offical Link](https://llvm.org)
- Setup :
  - go to [Clang](https://clang.llvm.org/get_started.html)
  - Clang Info -> Download
  - Latest version -> github release link
  - Downloads :
    - MacOS : `clang+llvm-xx.x.x-arm64-apple-darwin22.0.tar.xz`
    - Windows : `LLVM-xx.x.x-win64.exe`
- Setup MacOS (Easy) : zsh `clang --version` in terminal to trigger download prompt
- Setup MacOS (Brew) : zsh `brew install llvm`
  - Result:
    ```
    To use the bundled libc++ please add the following LDFLAGS:
    LDFLAGS="-L/opt/homebrew/opt/llvm/lib/c++ -Wl,-rpath,/opt/homebrew/opt/llvm/lib/c++"

    llvm is keg-only, which means it was not symlinked into /opt/homebrew,
    because macOS already provides this software and installing another version in
    parallel can cause all kinds of trouble.

    If you need to have llvm first in your PATH, run:
    echo 'export PATH="/opt/homebrew/opt/llvm/bin:$PATH"' >> ~/.zshrc

    For compilers to find llvm you may need to set:
    export LDFLAGS="-L/opt/homebrew/opt/llvm/lib"
    export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"

    ```
  - Add Path : `echo 'export PATH="/opt/homebrew/opt/llvm/bin:$PATH"' >> ~/.zshrc`

## Useful link
