#! /env/python
# -*- coding: UTF-8 -*-

import sys

baseFileName = "base.txt"
serverFileName = 'server.conf'

fileBase = open(baseFileName, 'r')
fileServer = open(serverFileName, 'w')


def getIpset(dns="8.8.8.8#53"):
	for line in fileBase.xreadlines():
		fixLine = line.strip().strip("\r\n").strip("\r").strip("\n")
		# 空行跳过
		if fixLine == "":
			continue
		# 注释行复制
		if fixLine.startswith("#"):
			fileServer.write(fixLine + '\n')
		else:
			newLine = "server=/" + fixLine + '/' + dns + '\n'
			fileServer.write(newLine)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		dns = sys.argv[1]
		getIpset(dns=dns)
	else:
		getIpset()