import urllib2,cookielib

url = "http://www.baidu.com"

print 'test first method'

response1 = urllib2.urlopen(url)

print response1.getcode()



print 'test secnond method'
request = urllib2.Request(url)

request.add_header("user-agent",'Mozilla/5.0')
response2 = urllib2.urlopen(request)

print response1.getcode()

print 'test thired method'

jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
