import folium
from html2image import Html2Image

geo_json = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"

def getMap(gpsXYList):
    foliumMap = folium.Map(
        location=[37.5695, 126.847],
        zoom_start=16,
        min_zoom=12,
        max_zoom=20,
        zoom_control=False,
        tiles="cartodbpositron"
    )

    folium.Marker([37.56965, 126.84646266139019],
        popup="한보구암마을아파트 방면 정류장",
        tooltip="한보구암마을아파트 방면 정류장",
        icon=folium.Icon(color='blue', icon='laptop', prefix='fa')
    ).add_to(foliumMap)

    folium.Marker([37.5695, 126.84740786191838],
        popup="한강타운아파트 방면 정류장",
        tooltip="한강타운아파트 방면 정류장",
        icon=folium.Icon(color='blue', icon='laptop', prefix='fa')
    ).add_to(foliumMap)

    for i in range(len(gpsXYList)):
        busMarker(gpsXYList[i][0], gpsXYList[i][1]).add_to(foliumMap)

    foliumMap.save('./foliumMap.html')
    Html2Image().screenshot(html_file='./foliumMap.html', save_as='foliumMap.png')

    return foliumMap


def busMarker(x, y):
    marker = folium.Marker([x, y],
        popup="Bus",
        tooltip="Bus",
        icon=folium.Icon(color='green', icon='bus-simple', prefix='fa')
    )

    return marker


def main():
    return

if __name__ == '__main__':
    main()