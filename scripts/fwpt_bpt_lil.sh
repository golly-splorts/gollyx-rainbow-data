#!/bin/bash

gsed -i \
    -e 's/FWPT/LIL/g' \
    -e 's/Ft. Worth Piano Tuners/Louisville Illusionists/g' \
    -e 's/BTX/BPT/g' \
    -e 's/Baltimore Texas/Baltimore Piano Tuners/g' \
    season*/*.json
