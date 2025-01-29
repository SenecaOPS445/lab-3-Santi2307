#!/usr/bin/env python3
#Author ID:12116236
import subprocess

def free_space():
    """Returns the free disk space on the root directory."""
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, capture_output=True, text=True)
    return result.stdout.strip()

if __name__ == "__main__":
    print(free_space())
