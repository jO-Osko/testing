import sys

import os

def fac(a):
	if a == 0:
		return 1
	return a*fac(a-1)

if __name__ == "__main__":
	print(fac(69))
