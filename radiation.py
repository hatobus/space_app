#coding:utf-8

from pygeocoder import Geocoder
from math import sin, cos, acos, radians

#入力した都市の緯度経度を求める
def geocoding(locate):
    results = Geocoder.geocode(locate)
    return results[0].coordinates


def latlng_to_xyz(lat, lng):
    rlat, rlng = radians(lat), radians(lng)
    coslat = cos(rlat)
    return coslat*cos(rlng), coslat*sin(rlng), sin(rlat)

# 二つの場所の距離を求める
def dist_on_sphere(pos0, pos1, radious=6378.137):
    xyz0, xyz1 = latlng_to_xyz(*pos0), latlng_to_xyz(*pos1)
    return acos(sum(x * y for x, y in zip(xyz0, xyz1)))*radious

def calc_flight_time(speed,distance):
    time = distance/speed # 単位はhour
    print('飛行時間は{0:.3f}時間です'.format(time))

if __name__ == '__main__':

    print('出発する都市名を入力 -> ')
    city1 = input()
    city1_loc = geocoding(city1)

    print(city1+'の緯度{0} 経度{1}'.format(city1_loc[0],city1_loc[1]))

    print('到着する都市を入力 ->')
    city2 = input()
    city2_loc = geocoding(city2)
    print(city2 + 'の緯度{0} 経度{1}'.format(city2_loc[0], city2_loc[1]))

    distance = dist_on_sphere(city1_loc,city2_loc) # 単位はkm
    print('二つの都市の距離は {0:.3f} km'.format(distance))


    if city1_loc[0] < city2_loc[0]:
        speed = 800 # 単位はkm/h
        calc_flight_time(speed,distance)
    else:
        speed = 1000 # 単位はkm/h
        calc_flight_time(speed,distance)
