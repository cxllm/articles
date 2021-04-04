## Node Version Manager
Node Version Manager is a version manager for node.js that is installed per every user on a system so that each user can have independent node.js versions. This guide will show you how to install it and how to use it to install node.js on your system.
### Why would you want to use it?
This tool provides cross distro compatibility, and allows for you to easily switch between different node.js versions with 1 command. I use it because often the version of node.js in the repositories are quite outdated for my needs, and if I want an up-to-date version, I need to download a binary from the node.js website which can get to be quite annoying every time I am setting up a server or a desktop system. NVM provides a quick and easy way to install node.js onto your system, which is why I like it.
### Installation
Using the cURL tool, we will fetch the latest file from their github, and execute this, which will automatically install node version manager to our home folder. (v0.38.0 is the latest version at time of writing, you may wish to check for a new version on the [nvm github](https://github.com/nvm-sh/nvm))
```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/nvm.sh | bash
```
This script provides us with a set of instructions for commands to run if we wish to use it in the same terminal
![](https://i.imgur.com/XRlTjM4.png)

In my case, because I use bash, I will execute these commands:
```sh
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```
Now we can use the `nvm` command
### Usage
Installing node.js latest version (which at time of writing is v15.13.0)
```
nvm install node
```
Installing node.js latest LTS Version (which at time of writing is v14.6.0)
```
nvm install --lts
```
Switching between versions, in this example, I will use v15
```
nvm use 15
```
Removing a version, I will once again use v15
```
nvm uninstall 15
```
I hope this guide helped with understanding how to use NVM 