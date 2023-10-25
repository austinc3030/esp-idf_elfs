#!/bin/bash

sudo apt-get install -y automake bison flex gawk gcc gettext git gperf grep help2man \
    libffi-dev libncurses-dev libncurses5-dev libncursesw5-dev libssl-dev libtool \
    libtool-bin make python2.7 python3 python3-cryptography python3-dev python3-future \
    python3-pip python3-pyparsing python3-serial python3-setuptools texinfo wget cmake

wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
sudo python2.7 get-pip.py
pip install --upgrade setuptools
pip2.7 install --upgrade setuptools
pip2.7 install pyserial==2.7
rm -rf get-pip.py
