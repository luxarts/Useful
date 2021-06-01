### 1. Enable WSL
1. Open control panel
2. Programs and features
3. Enable or disable Windows's features
4. Check Windows Subsystem for Linux
### 2. Download a Linux distro from Microsoft Store
1. Open Microsoft Store
2. Search for a Linux distro (for example, Debian) and install
### 3. Update and upgrade your distro
1. Open the Linux distro installed, this will open a terminal 
2. Execute the following commands
  ```
  sudo apt-get update
  sudo apt-get upgrade
  ```
### 4. Install git and curl
1. Execute the following commands
  ```
  sudo apt-get install git
  sudo apt-get install curl
  ```
### 5. Install Zsh and oh-my-zsh
1. Execute the following commands
  ```
  sudo apt-get install zsh
  sudo apt-get install oh-my-zsh
  ```
### 6. Install Hyper
1. Go the [Hyper download page](https://hyper.is/)
2. Download and install the app
### 7. Add bash to Hyper terminal
1. Open a Hyper terminal
2. Right click > Preferences
3. Edit the `shell` parameter to `C:\\Windows\\System32\\bash.exe`
  ```
  shell: 'C:\\Windows\\System32\\bash.exe',
  ```
### 8. Fix folders background color
Follow these steps -> https://github.com/microsoft/vscode/issues/7556#issuecomment-225426411
