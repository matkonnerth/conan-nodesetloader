# conan-nodesetloader

## Conan

conan is a package manager for C/C++ projects. More infos on conan on https://conan.io/

This repository provides the recipe for creating a conan package out of the nodesetloader sources.(https://github.com/matkonnerth/nodesetLoader)

Build for Linux is provided via Travis CI.

## Retrieving the packages

The binary packages are hosted at 
https://bintray.com/matkonnerth/cpprepo

Packages can retrieved via the lightweight conan client, therefore the repository has to be added:
conan remote add openRepo https://api.bintray.com/conan/matkonnerth/cpprepo

An example for using the open62541 conan package can be found here:
https://github.com/matkonnerth/modernOPC
