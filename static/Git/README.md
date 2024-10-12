# Visual Studio Code

## Learn
[learngitbranching](https://learngitbranching.js.org/)

## Overview
![MainActions](static/MainActions.png)

## Install
- Windows : 
    - Git : `winget install --id Git.Git -e --source winget`
    - Github CLI : `winget install --id=GitHub.cli  -e`
- MacOS : 
    - Git : `brew install git`
    - Github CLI : `brew install gh`
     

## Setup
- Login :
    ```
    gh auth login
    gh auth setup-git
    ```
- Profile :
    ```
    git config --global user.email "asuralhp@gmail.com"
    git config --global user.name "asuralhp"
    ```
- Clone : `git clone https://github.com/libgit2/libgit2`
  - Recursive : `git clone --recursive --shallow-submodules https://github.com/libgit2/libgit2`
- Initialization (Optional if Repo exits): 
    ```
    git init
    git add -A
    git commit -m "Init"
    git branch -M main
    ```


## Read
- Check Status : `git status`
- Commit Log One Line : `git log --oneline`
- All Log ADOG : `git log --all --decorate --oneline --graph`
- All Branch : `git branch -a`
- All Remote : `git remote -v`
- Configuration : `git config --list`
  - Show Origin : `git config --list --show-origin`

## Reverse
- Uncommit Last : `git reset --soft HEAD^`
- Unstage File: `git reset <commit>`
  - ![GitReset](static/GitReset.png)
  - ![GitResetPost](static/GitResetPost.png)
- Unstage All: `git restore --staged`
  - ![GitRestore](static/GitRestore.png)
- Commit to Reset: `git revert`
  - ![GitRevert](static/GitRevert.png)

## References
- ![threetreem](static/threetreem.jpg)

## Useful Links
- [Git Branching Visual Learning](https://pcottle.github.io/learnGitBranching/)

## Github
- Limit : 
  Product                    | Maximum file size
  ---------------------------|------------------:
  GitHub Free                |            2 GB
  GitHub Pro                 |            2 GB
  GitHub Team                |            4 GB
  GitHub Enterprise Cloud    |            5 GB