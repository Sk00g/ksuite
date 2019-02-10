import http.client as client

print('...initializing')

conn = client.HTTPSConnection("api.openweathermap.org", timeout=1.0)

conn.request("GET", "/data/2.5/weather?id=5931800&APPID=4cb795818fcbf849f23882cc0947031b")
response = conn.getresponse()

response_data = response.read()

print(response_data)
print(response_data[:20])

print('\n\nStatus: %s | Reason: %s' % (response.status, response.reason))

print('...exiting')
