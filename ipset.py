#! /env/python
# -*- coding: UTF-8 -*-

import sys

baseFileName = "base.txt"
ipsetFileName = 'ipset.conf'

fileBase = open(baseFileName, 'r')
fileIpset = open(ipsetFileName, 'w')


def getIpset(ipsetName="SS"):
	for line in fileBase.xreadlines():
		fixLine = line.strip().strip("\r\n").strip("\r").strip("\n")
		# 空行跳过
		if fixLine == "":
			continue
		# 注释行复制
		if fixLine.startswith("#"):
			fileIpset.write(fixLine + '\n')
		else:
			newLine = "ipset=/" + fixLine + '/' + ipsetName + '\n'
			fileIpset.write(newLine)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		ipsetName = sys.argv[1]
		getIpset(ipsetName=ipsetName)
	else:
		getIpset()