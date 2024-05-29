#!/bin/bash

echo "Lines Char Bytes Filename"
ls test_*.py | xargs -I % wc %

echo
echo "Width,Height,Bytes,Filename"
ls img/*.png | xargs -I {} identify -format "%w,%h,%b,%f\n" {}
