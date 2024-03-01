#!/bin/bash
# Send a GET request to the URL and store the response in a temporary file
curl -s -o /dev/null -w '%{size_download}' $1
