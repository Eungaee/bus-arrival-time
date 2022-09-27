import requests

key = '3k3sFRnb8vB+l4p0/pSEXOWru/YT/aPSVGIcrnxMcQThAGGsm14PuTwVG3Akan8Oryk235DrTJAtGf9hmQX3LA=='
url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute'
stationId = '115000133'
busRouteId = '100100307'
ord = '14'
params ={'serviceKey' : key, 'stId':stationId, 'busRouteId':busRouteId, 'ord':ord}
response = requests.get(url, params).content.decode('utf-8')

arrivalStartIndex1 = response.find('<arrmsg1>') + 9
arrivalEndIndex1 = response.find('</arrmsg1>')
arrivalStartIndex2 = response.find('<arrmsg2>') + 9
arrivalEndIndex2 = response.find('</arrmsg2')
print(response[arrivalStartIndex1:arrivalEndIndex1])
print(response[arrivalStartIndex2:arrivalEndIndex2])