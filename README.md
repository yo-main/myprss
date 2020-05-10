# MYPRSS

A small reader for rss feeds.

I find rss feeds quite convenient to read news or other stuff.

This small utility will allows you to manage your favorites rss feeds and read them.

In order to display hyperlinks in a beautiful way, myprss is using a feature that might not be available in all terminal.

myprss is using click as an argument parser, so it's quite easy to add autocompletion for your shell.
Documentation is available here: https://click.palletsprojects.com/en/7.x/bashcomplete/#shell-completion

tl;dr
```
# on zsh
mkdir -p ~/.config/myprss
_MYPRSS_COMPLETE=source_zsh myprss > ~/.config/myprss/myprss-complete.sh
echo 'source ~/.config/myprss/myprss-completion.sh' >> ~/.zshrc

# on bash
mkdir -p ~/.config/myprss
_MYPRSS_COMPLETE=source_bash myprss > ~/.config/myprss/myprss-complete.sh
echo 'source ~/.config/myprss/myprss-completion.sh' >> ~/.bashrc
```
