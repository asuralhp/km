# Visual Studio

## Package Management


- Brew
  - Installation :
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/$USER/.zprofile

  eval $(/opt/homebrew/bin/brew shellenv)

  brew help
  ```
  - List Packages : `brew list`
  - Get Package : `brew info <package_name>`
### Packages

- Git : `brew install git`
- CMake : `brew install cmake` 
- Blackhole : `brew install blackhole-2ch`
  - [BlackHole](https://github.com/ExistentialAudio/BlackHole) : recording internal audio
  - Audio MIDI Setup -> 
    - Add -> Multi-Output Device -> Tick all output -> check BlackHole 2ch Drift Correction (maybe)
    - Add -> Aggregate Device -> Tick all input -> check BlackHole 2ch Drift Correction (maybe)
  - Preference -> Sound -> Output -> Multi-Ouput
  - Record -> Options -> Aggregate
  - Tips : Zoom -> Input:Airpod, Output:Airpod


## HotKeys
  - Show Hidden <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>.</kbd>
  - Create New Folder : <kbd>CMD</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd>
  - Group to New Folder : <kbd>Ctrl</kbd> + <kbd>CMD</kbd> + <kbd>N</kbd>
  - Recent Opened : <kbd>CMD</kbd> + <kbd>N</kbd>

## External Monitor
  - [SpaceDesk](https://www.spacedesk.net)


  
  
## Setting
  - Tap 
    > Trackpad -> Tap to Click -> Checked
  - Three Finger 
    > Accessibility -> Trapad Options... -> Drag Option -> Three Finger Drag 
