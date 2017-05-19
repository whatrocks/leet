#!/bin/bash

awk '$1=$1' < $1 | tr ' ' '\n' | sort | uniq -c | sort -k 1 -r | awk '{print $2" "$1}'