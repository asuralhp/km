# Visual Studio Code



## Install
- Windows `winget install --id Git.Git -e --source winget`
- MacOS `brew install git`
    - Github CLI `brew install gh`
      - login `gh auth login`
      - credential `gh auth setup-git`

## Setup

- Initialization
    ```
    git init
    git add -A
    git commit -m "Init"
    git branch -M main
    ```
- Clone `git clone https://github.com/libgit2/libgit2`


## Read
- All Log `git log --all --decorate --oneline --graph`
- All Branch `git branch -a`
- All Remote `git remote -v`
- Configuration `git config --list`
  - Show Origin `git config --list --show-origin`

## References
- ![threetreem](threetreem.jpg)

## Useful Links
