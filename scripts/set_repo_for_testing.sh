#!/bin/bash

cd esp-idf

git checkout release/v2.0
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v2.1
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v3.0
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v3.1
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v3.2
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v3.3
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v4.0
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v4.1
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v4.3
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v4.4
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v5.0
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v5.1
cd examples
mv get-started ../
rm -rf *
mv ../get-started ./
cd ../
git add .
git commit -m "clean"

git checkout release/v2.0
ls examples/
git checkout release/v2.1
ls examples/
git checkout release/v3.0
ls examples/
git checkout release/v3.1
ls examples/
git checkout release/v3.2
ls examples/
git checkout release/v3.3
ls examples/
git checkout release/v4.0
ls examples/
git checkout release/v4.1
ls examples/
git checkout release/v4.3
ls examples/
git checkout release/v4.4
ls examples/
git checkout release/v5.0
ls examples/
git checkout release/v5.1
ls examples/

git checkout master
cd ../
