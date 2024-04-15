# Visual Studio Code



## Install
- Windows : `winget install --id Git.Git -e --source winget`
- MacOS : `brew install git`
    - Github CLI : `brew install gh`
      - login : `gh auth login`
      - credential : `gh auth setup-git`

## Setup

- Initialization : 
    ```
    git init
    git add -A
    git commit -m "Init"
    git branch -M main
    ```
- Clone : `git clone https://github.com/libgit2/libgit2`
- Clone Recursive : `git clone --recursive --shallow-submodules https://github.com/libgit2/libgit2`


## Read
- All Log ADOG : `git log --all --decorate --oneline --graph`
- All Branch : `git branch -a`
- All Remote : `git remote -v`
- Configuration : `git config --list`
  - Show Origin : `git config --list --show-origin`

## References
- ![threetreem](threetreem.jpg)

## Useful Links
- [Git Branching Visual Learning](https://pcottle.github.io/learnGitBranching/)

## Github
- Limit : 
  Product                    | Maximum file size
  ----------------------------|------------------:
  GitHub Free                |            2 GB
  GitHub Pro                 |            2 GB
  GitHub Team                |            4 GB
  GitHub Enterprise Cloud    |            5 GB