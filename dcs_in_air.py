from dcs import Mission, Point
from dcs.planes import F_15C
from dcs.terrain import Caucasus
from dcs.unitgroup import FlyingGroup
from dcs.lua import loads
from dcs.mission import StartType
from dcs.unit import Skill
import datetime

# 1. 创建任务：高加索地图
mission = Mission(Caucasus())

# 2. 任务时间：傍晚 18:00（你可以改成 21 点深夜）
#mission.start_time = datetime.time(10,0,0)
mission.day = 1
mission.month = 1
mission.year = 2025
mission.hour = 18
mission.minute = 0
print("set time")


# 3. 天气：晴天、能见度拉满、微风
weather = mission.weather
weather.atmosphere_type = 0

weather.enable_fog= True
weather.fog_visibility= 2000
weather.fog_thickness = 100

print("set weather")

# 西风 2m/s

# 4. 选机场：Vaziani 机场（坐标稳定）
terrain = Caucasus()
ap=terrain.airports['Batumi']

print("set airport")

pos = Point(
    ap.position.x+5000,
    ap.position.y,
    terrain=mission.terrain
)

blue = mission.coalition["blue"]

flight = mission.flight_group(
    country=mission.country("USA"),
    #airport=ap,
    name="Player_F15",
    aircraft_type=F_15C,   # 这个才是正确参数名！
    position=pos,
    altitude=1500,
    speed=250 / 3.6,
    airport=None,
    #pitch = 2.0,
    #throttle = 0.9,
    
    #start_type=StartType.IN_AIR,
   
)

#flight.airport = None

flight.pitch = 2.0
flight.hrottle = 0.9

flight.spawn_in_air = True

# 无限燃油
for unit in flight.units:
    unit.skill = Skill.Player
    unit.fuel = 9999

# 进近航路点
flight.add_waypoint(
    pos=ap.position,
    altitude=500,
    speed=250 / 3.6
)

# ==============================
# 4. 保存任务
# ==============================
mission.save("F15C_Land_play7.miz")
print("生成成功：F15C_Land_play7.miz")