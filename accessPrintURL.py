from http.client import HTTPConnection
con=HTTPConnection("w3resource.com")
con.request("GET", "/")
resp=con.getresponse()
print(resp)
printing=resp.read()
print(printing)