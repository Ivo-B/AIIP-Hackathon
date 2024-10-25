#!/bin/bash

start_time=$(date +%s.%N)

docker run --rm zen-of-python

end_time=$(date +%s.%N)

duration=$(echo "$end_time - $start_time" | bc)

echo "Container startup time and print the text of zen of python: $duration seconds"

