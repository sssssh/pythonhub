# python2
# from urllib import urlopen
# howto fetch internet resources using the urllib package
import urllib.request
import urllib.parse

# Fetching URLs
with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    print(type(html))  # <class 'bytes'>


# retrieve a resource via URL and store it in temporary location
local_filename, headers = urllib.request.urlretrieve('http://python.org/')
print('--', local_filename, type(local_filename))
print('==', headers, type(headers))
html = open(local_filename)
print('++', html)


#
req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
    the_page = response.read()


#
req = urllib.request.Request('ftp://example.com/')


# Data

# post
url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python'}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()

# get
data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)  # The order may differ from below.
url = 'http://www.example.com/example.cgi'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)


# Handling Exceptions
# URLEorror
req = urllib.request.Request('http://www.pretend_server.org')
try:
    urllib.request.urlopen(req)
except urllib.error.URLEorror as e:
    print(e.reason)  # (4, 'getaddrinfo failed')

# HTTPError
# Error Codes
# Table mapping response codes to messages
# entries have the from {code: (shortmessage, longmessage)}
response = {
    100: ('Continue', 'Request received, please continue'),
    101: ('Switching Protocols',
          'Switching to new protocol; obey Upgrade header'),

    200: ('OK', 'Request fulfilled, document follows'),
    201: ('Created', 'Document created, URL follows'),
    202: ('Accepted',
          'Request accepted, processing continues off-line'),
    203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
    204: ('No Content', 'Request fulfilled, nothing follows'),
    205: ('Reset Content', 'Clear input form for further input.'),
    206: ('Partial Content', 'Partial content follows.'),

    300: ('Multiple Choices',
          'Object has several resources -- see URI list'),
    301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
    302: ('Found', 'Object moved temporarily -- see URI list'),
    303: ('See Other', 'Object moved -- see Method and URL list'),
    304: ('Not Modified',
          'Document has not changed since given time'),
    305: ('Use Proxy',
          'You must use proxy specified in Location to access this '
          'resource.'),
    307: ('Temporary Redirect',
          'Object moved temporarily -- see URI list'),
    400: ('Bad Request',
          'Bad request syntax or unsupported method'),
    401: ('Unauthorized',
          'No permission -- see charging schemes'),
    402: ('Payment Required',
          'No payment -- see charging schemes'),
    403: ('Forbidden',
          'Request forbidden -- authorization will not help'),
    404: ('Not Found', 'Nothing matches the given URI'),
    405: ('Method Not Allowed',
          'Specified method is invalid for this server.'),
    406: ('Not Acceptable', 'URI not available in preferred format.'),
    407: ('Proxy Authentication Required', 'You must authenticate with '
          'this proxy before proceeding.'),
    408: ('Request Timeout' 'Request timed out; try again later.'),
    409: ('Conflict', 'Request conflict.'),
    410: ('Gone',
          'URI no longer exists and has been permanently removed.'),
    411: ('Length Required', 'Client must specify Content-Length.'),
    412: ('Precondition Failed', 'Precondition in headers is false.'),
    413: ('Request Entity Too Large', 'Entity is too large.'),
    414: ('Request-URI Too Long', 'URI is too long.'),
    415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
    416: ('Requested Range Not Satisfiable',
          'Cannot satisfy request range.'),
    417: ('Expectation Failed',
          'Expect condition could not be satisfied.'),

    500: ('Internal Server Error', 'Server got itself in trouble'),
    501: ('Not Implemented',
          'Server does not support this operation'),
    502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
    503: ('Service Unavailable',
          'The server cannot process the request due to a high load'),
    504: ('Gateway Timeout',
          'The gateway server did not receive a timely response'),
    505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
    }

req = urllib.request.Request('http://www.python.org/fish.html')
try:
    urllib.Request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read())


# Wrapping it Up
# 1
from urllib.request import Request, urlopen
from urllib.error import URLEorror, HTTPError
req = Request(someurl)
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLEorror as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    # everything is fine


# 2
try:
    response = urlopen(req)
except URLEorror as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    # everything is fine

    
# Basic Authentication
# created a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# add the username and password.
# if we knew the realm, we could use it insted of None
top_level_url = "http://example.com/foo/"
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
opener.open(a_url)

# install the opener
# now all calls to urllib.request.urlopen use our opener
urllib.request.install_opener(opener)


# Proxies
proxy_support = urllib.request.ProxyHandler({})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)


# Sockets and Layers
import socket

# timeout in seconds
timeout = 10
socket.setdefaulttimeout(timeout)


# this call to urllib.request.urlopen now uses the default timeout
# we have set in the socket module
req = urllib.request.Request('http://www.voidspace.org.uk')
response = urllib.request.urlopen(req)
