import requests
import json

#init
key = '3k3sFRnb8vB+l4p0/pSEXOWru/YT/aPSVGIcrnxMcQThAGGsm14PuTwVG3Akan8Oryk235DrTJAtGf9hmQX3LA=='
stationsURL = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute'  # 노선별 경유 정류소
routeInfoURL = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList'  #노선번호에 해당하는 노선 목록
arrivalURL = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute'    #한 정류소의 특정 노선 도착예정정보

#getRouteId()
def getRouteId(num):
    params = {'serviceKey': key, 'strSrch': num, 'resultType': 'json'}
    response = requests.get(routeInfoURL, params).content.decode('utf-8')
    responseJson = json.loads(response)
    busRouteId = responseJson.get('msgBody').get('itemList')[0].get('busRouteId')
    return busRouteId

#getStationInfo()
def getStationInfo(busRouteId, station):
    params = {'serviceKey': key, 'busRouteId': busRouteId, 'resultType': 'json'}
    response = requests.get(stationsURL, params).content.decode('utf-8')
    responseJson = json.loads(response)
    itemList = responseJson.get('msgBody').get('itemList')
    stationId = []
    ord = []
    for i in range(len(itemList)):
        if (itemList[i].get('stationNm') == station):
            stationId.append(itemList[i].get('station'))
            ord.append(itemList[i].get('seq'))
    return [stationId, ord]

#getArrivalInfo()
def getArrivalInfo(stationId, busRouteId, ord):
    params = {'serviceKey': key, 'stId': stationId, 'busRouteId': busRouteId, 'ord': ord, 'resultType': 'json'}
    response = requests.get(arrivalURL, params).content.decode('utf-8')
    responseJson = json.loads(response)
    firstArrival = responseJson.get('msgBody').get('itemList')[0].get('arrmsg1')
    secondArrival = responseJson.get('msgBody').get('itemList')[0].get('arrmsg2')
    return [firstArrival, secondArrival]

def main():
    busNum = str(input('도착 정보를 알고 싶은 버스 번호: '))
    stationName = input('도착 정보를 알고 싶은 버스 정류장: ')
    routeId = getRouteId(busNum)
    stationInfo = getStationInfo(routeId, stationName)
    stationId = stationInfo[0][0]
    ord = stationInfo[1][0]
    result = getArrivalInfo(stationId, routeId, ord)
    print(f'"{stationName}" 정류장에서 가장 가까운 {busNum} 버스는 "{result[0]}", 그 다음으로 가까운 {busNum} 버스는 "{result[1]}" 도착합니다.')
    return result

while True:
    main()