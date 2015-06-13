# coding: utf-8

r = [u'あ']
print r # result: [u'\u3042']
print repr(r).decode('unicode-escape') # result: [u'あ']

s = ['ă']
print s # result: ['\xc4\x83']
t = unicode(s, 'utf-8')[0].encode('utf-8')
print t
print repr(s).decode('unicode-escape') # error

# ştiţi cum să output corect diacritice în List?