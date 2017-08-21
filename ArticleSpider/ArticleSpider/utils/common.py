#!user/bin/env python
# -*- coding:utf-8 -*-

import hashlib


def getmd5(url):
	m = hashlib.md5()
	if isinstance(url, str):
		m.update(url.encode('utf-8'))
	return m.hexdigest()
