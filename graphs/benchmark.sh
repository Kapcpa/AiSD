#!/bin/bash

/usr/bin/time -f "MEM=%M KB\nTIME=%e sec" python3 main.py --graphs --generate <<EOF
128
70
matrix
kahn
exit
EOF