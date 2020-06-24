#!/bin/bash
# Discovers and runs unit tests from 'tests' directory.
# Use -v for verbose output and -f to stop on first failure.

echo ">>> Running all tests"
echo

python -m unittest discover tests -fv
