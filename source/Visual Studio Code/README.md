# Visual Studio Code

## Install
- Windows `winget install --id=Microsoft.VisualStudioCode  -e`
- MacOS `brew install --cask visual-studio-code`

## Import
-  C/C++ -> General -> Additional Include Directories
- Linker -> General -> Additional Library Directories 
- Linker -> Input -> Additional Dependencies (.lib)
-  VC++ :
   -  Include Directories
   -  Library Directories
- [VC++ vs C++ Directories properties](https://stackoverflow.com/questions/6883276/what-is-the-difference-between-include-directories-and-additional-include-dir)
  - VC++ : Machine Level
  - C++ : Project Level
## Output
- Directory : Property -> General -> Output Directory




## Editor
- Palette <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>

- Split To  <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd><-</kbd> /<kbd>-></kbd>
  - MacOS : <kbd>CMD</kbd> + <kbd>\</kbd> 
- Move To : <kbd>Alt</kbd> + <kbd><-</kbd> / <kbd>-></kbd>
    - MacOS : <kbd>CMD</kbd>  + <kbd>Ctrl</kbd> + <kbd>-></kbd> / <kbd><-</kbd>
- Focus To Group :
    - MacOS : <kbd>CMD</kbd>  + <kbd>Opt</kbd> + <kbd>-></kbd> / <kbd><-</kbd>
- Extend Selection : <kbd>Shift</kbd> + <kbd>Alt</kbd> + <kbd>-></kbd> / <kbd><-</kbd>
  - MacOS : <kbd>Shift</kbd> + <kbd>Ctrl</kbd> + <kbd>CMD</kbd> + <kbd>-></kbd> / <kbd><-</kbd>
- Format Document <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>
## Extension 

- yzhang.markdown-all-in-one
- mhutchie.git-graph
- GitHub.copilot
- GitHub.copilot-chat
- bierner.markdown-preview-github-styles

### Install Offline
- Download from extension page
- Extension Tab -> Click ... -> Install from VSIX
## Setting

- "files.autoSave": "afterDelay"
- "editor.trimAutoWhitespace": false
