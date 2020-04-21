#!/bin/bash
path=/home/ky/Projects/randomPostRecommand
#path=/home/ky/Projects/randomPostRecommand/randomPostRecommand/bin

echo $(dirname $0)
source $path/randomPostRecommand/bin/activate
python crawl.py >> $path/test.log
