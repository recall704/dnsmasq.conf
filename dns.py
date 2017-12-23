#! /env/python
# -*- coding: UTF-8 -*-

import sys

baseFileName = "base.txt"
dnsFileName = 'dns.conf'

fileBase = open(baseFileName, 'r')
fileDns = open(dnsFileName, 'w')


def getDns(ip="192.168.88.1"):
	for line in fileBase.xreadlines():
		fixLine = line.strip().strip("\r\n").strip("\r").strip("\n")
		# 空行跳过
		if fixLine == "":
			continue
		# 注释行复制
		if fixLine.startswith("#"):
			fileDns.write(fixLine + '\n')
		else:
			newLine = "address=/" + fixLine + '/' + ip + '\n'
			fileDns.write(newLine)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		ip = sys.argv[1]
		getDns(ip=ip)
	else:
		getDns()