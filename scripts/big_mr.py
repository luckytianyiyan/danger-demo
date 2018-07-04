#!/usr/bin/python

import os

path = os.path.join("../DangerDemo", "ViewController.m")

with open(path, "a") as f:
	f.writelines(500 * "// big_mr\n")