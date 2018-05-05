# FunnerRetro Server

[![Build Status](https://travis-ci.org/carbonblack/funnerretro-server.svg?branch=master)](https://travis-ci.org/carbonblack/funnerretro-server)
[![Coverage Status](https://coveralls.io/repos/github/carbonblack/funnerretro-server/badge.svg?branch=master)](https://coveralls.io/github/carbonblack/funnerretro-server?branch=master)

This is the repo for the websocket server and user auth on FunnerRetro.

## Contributing

1. Install Go and Go Dep
2. `cd $GOPATH/src/`
3. `go get github.com/carbonblack/funnerretro-server`
4. Create a `.env` file in the root of this project and add `PORT` to it
    * `PORT=<some port>`
5. `dep ensure`
