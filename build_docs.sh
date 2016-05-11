#!/bin/bash

set -o pipefail
set -e

cd ./docs
make clean
make html
