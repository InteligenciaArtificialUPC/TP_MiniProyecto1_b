import requests
from geopy.distance import geodesic
class ServiceClient:
    def compute_distance(latA,longA,latB,longB):
        res = requests.post(
            'https://maps.googleapis.com/maps/api/distancematrix/json?origins='+str(latA)+','+str(longA)+'&destinations='+str(latB)+','+str(longB)+'&mode=driving&language=es-ES&units=metric&key=AIzaSyAkSoqQ9v3nMJ9Tv60ZSwkZcgjoNkCGBsw')
        if res.ok:
            #print(res.json())
            r = res.json()
            return(r['rows'][0]['elements'][0]['distance']['value'])
        return 99999999
    def compute_heuristic_distance(latA,longA,latB,longB):
        return geodesic((latA,longA),(latB,longB)).meters




print(ServiceClient.compute_distance(-33.9196631120698,151.233391073654768,-33.908896455944124,151.2365632263835))
print(ServiceClient.compute_heuristic_distance(-33.9196631120698,151.233391073654768,-33.908896455944124,151.2365632263835))
