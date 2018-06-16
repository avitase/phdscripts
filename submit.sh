#!/bin/bash

PYTHONPATH=$(pwd):/$PYTHONPATH

python createOptions.py && ganga submit.py
