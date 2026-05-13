#!/bin/bash

echo "arguments: $@"

EXIT=$@
echo $EXIT >> ~/Zeti/paramlog.txt 2>&1
