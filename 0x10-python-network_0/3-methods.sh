#!/bin/bash
# Displays allowed method for URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
