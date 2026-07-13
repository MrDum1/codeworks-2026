#!/bin/bash
for i in {0..255} ; do echo -en "\e[37;5;${i}m ${i} \e[0m" ; done ; echo
