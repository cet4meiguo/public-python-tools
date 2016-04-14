#!/usr/bin/env python
#-*-coding:utf-8-*-
import ConfigParser
def filter():
	"""
		删除重复行内容
	"""
	config = ConfigParser.ConfigParser()
	with open('config.ini') as cfgfile:
		config.readfp(cfgfile)
		path = config.get('info','path')
		file = config.get('info','file')
	lines, sorted = open(path+file, 'r').readlines(), lambda a, cmp: a.sort(cmp=cmp) or a
	open(path+"filtered"+file, 'w').write(''.join([l[0] for l in sorted([(l, lines.index(l)) for l in set(lines)], lambda a,b: a[1]-b[1] )]))
filter()
raw_input('Press Enter to exit.')
