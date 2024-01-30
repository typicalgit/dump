#!/bin/bash
#
./extract.sh  "$(sed -n 1p lineno.txt)" "$(sed -n 2p lineno.txt)" workbook.txt
