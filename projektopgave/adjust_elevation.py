# https://requests.readthedocs.io/en/latest/user/quickstart/
# skal installeres ved at skrive denne kommando i cmd/powershell `pip install requests`
import requests

import gpxpy
import os

# ---------------->8
#skraldet fra https://www.programcreek.com/python/example/122591/gpxpy.parse Example 2

def read_gpx_file(filename):
    try:
        with open(filename, "r") as f:
            points_list = []
            prev_point = None
            head, tail = os.path.split(filename)
            code_route = tail.replace(".gpx", "")
            try:
                gpx = gpxpy.parse(f)
                for point in gpx.walk(only_points=True):
                    speed = point.speed_between(prev_point)
                    if speed is None:
                        speed = 0

                    time_difference = point.time_difference(prev_point)
                    if time_difference is None:
                        time_difference = 0

                    distance = point.distance_3d(prev_point)
                    if not distance:
                        distance = point.distance_2d(prev_point)
                    if distance is None:
                        distance = 0

                    # points_list.append([code_route, point.latitude, point.longitude, point.elevation,
                    #                             point.time, speed, time_difference, distance, gpx.name])

                    points_list.append({
                        'code_route': code_route, 
                        'point.latitude': point.latitude,
                        'point.longitude': point.longitude,
                        'point.elevation': point.elevation,
                        'point.time': point.time, 
                        'speed': speed, 
                        'time_difference': time_difference, 
                        'distance': distance, 
                        'gpx.name' : gpx.name,
                    })

                    

                    prev_point = point
            except Exception as e:
                raise TrackException('GPX file "' + filename + '" malformed', e)
    except FileNotFoundError as e:
        raise TrackException('GPX file "' + filename + '" not found', e) 

    return points_list
# 8<-------

# 8<----  https://github.com/acsicuib/YAFS/blob/master/src/trackanimation/utils.py
class TrackException(Exception):
    """
    Generic exception for TrackAnimation
    """

    def __init__(self, msg, original_exception):
        super(TrackException, self).__init__(msg + (": %s" % original_exception))
        self.original_exception = original_exception
# ----->8

def main():

    filename = r"projektopgave\data\activity_7403521010.gpx"
    points = read_gpx_file(filename)
    
    # https://requests.readthedocs.io/en/latest/user/quickstart/

    import requests

    # curl https://api.opentopodata.org/v1/eudem25m?locations=57.688709,11.976404 

    api_url = 'https://api.opentopodata.org/'
    endpoint = 'v1/eudem25m'

    for i, point in enumerate(points):

        params = {
            'locations' : f"{point['point.latitude']},{point['point.longitude']}" #57.688709,11.976404,
        }

        respons = requests.get(api_url+endpoint, params)

        # print(respons)
        # print("Response status:", respons.status_code)

        if respons.status_code == 200:
            # print(respons.json())
            rjson = respons.json()['results'][0]
            # print(f"elevation: {rjson['elevation']}")
            point['elevation(eudem25m)'] = rjson['elevation']
            print(f"\r{i}", end='')
        else:
            print('-')
            print("Response status:", respons.status_code)
 
    print(points[1].keys())

    for p in points:
        print(f"elevaton(garmin): {p['point.elevation']}, elevation(eudem25m): {p['elevation(eudem25m)']}," 
             + f" diff: {p['point.elevation'] - p['elevation(eudem25m)']}") 

if __name__ == '__main__':
    main()