#!/bin/bash

# 1. Activate the virtual environment
# We use the 'source' command as per Bash standards to load the environment
source venv/Scripts/activate

# 2. Execute the test suite
# We point to our test file specifically. 
# Pytest automatically returns exit codes: 0 for success, 1 for failures.
pytest testApp.py

# 3. Handle the Exit Code
# $? is a special variable that captures the exit status of the last command
result=$?

if [ $result -eq 0 ]; then
  echo "CI Status: All tests passed. Proceeding..."
  exit 0
else
  echo "CI Status: Tests failed with exit code $result. Halting build."
  exit 1
fi