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

#getStationNames()
def getStationNames(busRouteId):
    params = {'serviceKey': key, 'busRouteId': busRouteId, 'resultType': 'json'}
    response = requests.get(stationsURL, params).content.decode('utf-8')
    responseJson = json.loads(response)

    itemList = responseJson.get('msgBody').get('itemList')

    stationNames = []

    for i in range(len(itemList)):
        stationNames.append(itemList[i].get('stationNm'))

    return stationNames

#getStationInfo()
def getStationInfo(busRouteId, station):
    params = {'serviceKey': key, 'busRouteId': busRouteId, 'resultType': 'json'}
    response = requests.get(stationsURL, params).content.decode('utf-8')
    responseJson = json.loads(response)

    itemList = responseJson.get('msgBody').get('itemList')

    stationId = []
    nextStationId = []
    nextStationName = []
    ord = []

    for i in range(len(itemList)):
        if (itemList[i].get('stationNm') == station):
            stationId.append(itemList[i].get('station'))
            nextStationId.append(itemList[i+1].get('station'))
            nextStationName.append(itemList[i+1].get('stationNm'))
            ord.append(itemList[i].get('seq'))
    print(stationId, nextStationId, nextStationName, ord)
    return [stationId, nextStationId, nextStationName, ord]

#getArrivalTime()
def getArrivalTime(stationId, busRouteId, ord):
    params = {'serviceKey': key, 'stId': stationId, 'busRouteId': busRouteId, 'ord': ord, 'resultType': 'json'}
    response = requests.get(arrivalURL, params).content.decode('utf-8')
    responseJson = json.loads(response)

    firstArrival = responseJson.get('msgBody').get('itemList')[0].get('arrmsg1')
    secondArrival = responseJson.get('msgBody').get('itemList')[0].get('arrmsg2')

    return [firstArrival, secondArrival]

def getArrivalInfo(busNum, targetStation, direction):
    routeId = getRouteId(busNum)
    stationInfo = getStationInfo(routeId, targetStation)

    if direction == "한보구암":
        stationId = stationInfo[0][0]
        ord = stationInfo[3][0]
    elif direction == "한강타운":
        stationId = stationInfo[0][1]
        ord = stationInfo[3][1]
    else:
        print("올바른 방향을 입력해주세요.")
        return
    
    arrival = getArrivalTime(stationId, routeId, ord)
    
    return arrival

def main():
    busNum = str(input("도착 시간을 알고 싶은 버스 번호를 입력하세요: "))
    routeId = getRouteId(busNum)
    stationNames = getStationNames(routeId)
    print("\n----------------------------------------------------------------------------------------------------\n")
    print(f"{busNum}의 경유 정류소 목록\n{stationNames}\n")
    print("----------------------------------------------------------------------------------------------------\n")

    targetStation = input("정류소를 입력하세요: ")
    stationInfo = getStationInfo(routeId, targetStation)

    stationId = stationInfo[0]
    nextStationId = stationInfo[1]
    nextStationName = stationInfo[2]
    ord = stationInfo[3]

    arrival = [getArrivalTime(stationId[0], routeId, ord[0]), getArrivalTime(stationId[1], routeId, ord[1])]
    stationValue = input(f"1: {nextStationName[0]}\n2: {nextStationName[1]}\n가고싶은 다음정류장을 선택하세요: ")
    if stationValue == 1:
      print(f'"{targetStation}" 정류장에서 "{nextStationName[0]}" 정류장으로 가는 가장 가까운 {busNum} 버스는 "{arrival[0][0]}", 그 다음으로 가까운 {busNum} 버스는 "{arrival[0][1]}" 도착합니다.')
    elif stationValue == 2:
      print(f'"{targetStation}" 정류장에서 "{nextStationName[1]}" 정류장으로 가는 가장 가까운 {busNum} 버스는 "{arrival[1][1]}", 그 다음으로 가까운 {busNum} 버스는 "{arrival[1][1]}" 도착합니다.')

if __name__ == '__main__':
    main()