#!/bin/bash
OUT=output
rm -rf $OUT
mkdir -p $OUT
for i in {1..3}
  do
    echo "Unleash $i"
    ./run.sh >$OUT/out$i &
  done
echo "Wait"
wait
