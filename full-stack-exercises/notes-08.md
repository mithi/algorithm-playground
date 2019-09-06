## PostgreSQL
- PostgreSQL is a fast, feature-rich, open-source database application. It is a scalable application that we can use for development and production apps. We will be using PostgreSQL for most of our web-apps

```
sudo mkdir -p /etc/paths.d &&
```
```
echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp

```
- highly recommended to configure your system $PATH so that you can use the command line tool
- https://postgresapp.com/downloads.html

```
# open the PostgreSQL CLI
psql

# you should be greeted with a prompt that looks like this
psql (10.X)
Type "help" for help.

yourname=#

# type '/q' to quit
yourname=# \q
```

## SQLite
- SQLite is a small, lightweight database application that requires no configuration and stores the database as a stand-alone file
```
brew install sqlite

# open SQLite CLI with this command
sqlite3

#  you should see this output
# SQLite version 3.16.0 2016-11-04 19:09:39
# Enter ".help" for usage hints.
# Connected to a transient in-memory database.
# Use ".open FILENAME" to reopen on a persistent database.

# .q to quit
sqlite> .q
```

## Rails

```
# install rails
gem install rails

# verify installation
which rails # => /Users/username/.rbenv/shims/rails
```

# Node.js & NPM

- Node.js will be our local JavaScript engine. to run JavaScript code and run associated node commands.

- NVM (Node Version Manager) to install/manage Node.js. manage potential conflicts between versions and dependencies.

```
# download and run the official install script
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash

# update your terminal config (you will now have access to the nvm command)
source ~/.bashrc

# install a stable version of node
nvm install 10.13.0

# set version 10.13.0 as default version
nvm use 10.13.0

# verify install/config
which node # => /Users/username/.nvm/versions/node/v10.13.0/bin/node
```
