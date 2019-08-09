# Outline

- Check ruby style guide for preferred way of doing things
- Common enumerables, symbols, default arguments, option Hashes
- Splat operator, inject/reduce
- Variable scope and variable references
- Testing with rspec
- Pry, Byebug, Error types
- Blocks, procs, classes, monkey patching
- input/output, oop, syntactic sugar, recursion


# SETUP

### Stack
- Ruby on Rails on the backend/server
- PostgreSQL to house our database
- JavaScript + React + Redux for frontend rendering and logic.

### Recommended Basic Developer Tools

- Google Chrome Web Browser
- homebrew: 3rd party package manager
- Xcode: developer tools
- git: version control system
- VS Code: text-editor
- rbenv: a Ruby environment manager.
  - switch between versions of Ruby easily
  - setup default versions to use within project directories
- Bundler
  - to define project dependencies inside a Gemfile
  - commands to update, remove and install them.
- Pry repl
- Byebug
  - feature-rich debugging tool for Ruby
  - Halt the execution of your code and inspect/track variables and the flow of execution

```bash

# install HomeBrew
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# ----------------
# install git
# ----------------
$ brew install git

# makes git terminal output pretty
$ git config --global color.ui true

# this will mark you as the 'author' of each committed change
$ git config --global user.name "your name here"

# use the email associated with your GitHub account
$ git config --global user.email your_email_here

# ----------------
# install rbenv
# ----------------

brew install rbenv

# add to the PATH (rbenv commands are now available from terminal)
# .bashrc is the file that contains all of our terminal settings
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc

# initialize rbenv everytime you open a new console window (otherwise our system ruby version will take over when we start a new terminal session)
echo 'eval "$(rbenv init -)"' >> ~/.bashrc

# update current console window with new settings
source ~/.bashrc

# source .bashrc from .bash_profile (necessary on some machines)
echo 'source ~/.bashrc' >> ~/.bash_profile

# install Ruby version 2.5.1
rbenv install 2.5.1

# set version 2.5.1 to be our global default
rbenv global 2.5.1

# the 'rehash' command updates the environment to your configuration
rbenv rehash

# and let's verify everything is correct
# check the version
ruby -v # => 2.5.1

# check that we are using rbenv (this tells you where the version of ruby you are using is installed)
which ruby # => /Users/your-username/.rbenv/shims/ruby

# ----------------
# Install gems
# ----------------
$ gem install bundler pry byebug
```
