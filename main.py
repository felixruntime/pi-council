#!/usr/bin/env python3

import sys
from agents.council import run_council

if __name__ == "__main__":

    question = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
    run_council(question)