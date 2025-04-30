# pip install pyowm

from pyowm import OWM
from pprint import pprint

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()


obs = mgr.weather_at_place('Minsk')
w = obs.to_dict()


pprint(w)
