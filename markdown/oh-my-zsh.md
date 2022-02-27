## Oh My ZSH

Oh My ZSH is "a delightful, open source, community-driven framework for managing your Zsh configuration", as stated by their website. And from my experience, I can honestly say that it lives up to its claims. It is very easy to use, and provides very good auto-completion, git integration and just an overall good look-and-feel. In this post, I'll go over how to install it and configure the themes and extensions.

### Installation

You can install Oh My ZSH on any system running a Linux or BSD-based kernel. These include any Linux OS (such as Ubuntu, Fedora, Arch etc.), MacOS, or WSL/CygWin.

First, you must install zsh, which can be found in most package managers as zsh, for example `sudo apt install zsh`, `sudo dnf install zsh` or `sudo pacman -S zsh`.

Then, run the Oh MY ZSH installation command,

```
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

This will show up with a prompt like this:
![](https://i.imgur.com/ME1OXkM.png)

Here you can choose to set ZSH as the default shell that launches on SSH and when you open a terminal. You can always change it back to bash afterwards with the `chsh` command.
To set ZSH as the default shell, press enter, and it should ask for your sudo password, and then bring you into a shell with a different theme than before:
![](https://i.imgur.com/dEQVZ48.png)

And that's how to install Oh My ZSH!

### Configuration

If you open the `~/.zshrc` file, you file a lot of configuration options that allow you to change things like themes, plugins and more. When I'm configuring Oh My ZSH, the main things I change are plugins and themes.

For themes, you can choose any from a number of official themes and unofficial too, you just have to clone these into the .oh-my-zsh folder in your home folder for that to work. To change the theme, navigate to the `ZSH_THEME` option, and change it to whatever theme you want. You can find a list of official themes [here](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes)

For plugins, you can enable any number of the official plugins supported by Oh My ZSH. Navigate to the `plugins=(git)` section, and add any plugins from [here](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins) that you would like enabled. I like to include the archlinux and npm plugins, as they provided detailed autocompletion on tab.

You can find more options for configuration on the [Oh My ZSH Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki) as I done the extensive options justice here by just discussing themes and plugins. I hope this article helped you with setting up Oh My ZSH.
