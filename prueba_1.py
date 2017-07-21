import urllib2
import json

response = urllib2.urlopen('http://localhost:4000')
result     = response.read()

print result
