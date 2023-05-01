from pyautocad import Autocad, APoint
from configparser import ConfigParser
from partition_gi import partition2,partition3,partition4,partition5,partition6,partition1
from GI import l
from GI import vchannel
from GI import thick
from GI import zchanneltb
from GI import zchannelside
from GI import width
from GI import hchannel
from GI import pz11
from GI import ppz7x
from GI import zleft
from GI import ztop
from GI import pz4
from GI import pz3
from GI import ppz2y
from GI import ppz3x
from GI import pz7
from GI import pz8
from GI import pz12
from GI import ppz1y
from GI import zbottom
from GI import zright
from GI import dclear
from GI import lenght


config = ConfigParser()
config.read('./INDOOR/gi_config_in.ini')

acad = Autocad()
 
dclearx = int(config["doors"]["door_clearence_X"])
dcleary = int(config["doors"]["door_clearence_Y"])
dclearmid = int(config["doors"]["door_clearence_MID"])

#start of codes

#FOR CUTOUTS IN TOP BOTTOM Z CHANNEL
cc1y = ppz2y - thick  # for top
cz1 = APoint(ppz3x,cc1y)

ccz6y = ppz2y - thick
cz6 = APoint(ppz7x,ccz6y)

linect1 = ztop.addline(pz3,cz1)
linect2 = ztop.addline(cz1,cz6)
linect7 = ztop.addline(cz6,pz7)

cczb1y = ppz1y + thick
czb1 = APoint(ppz3x,cczb1y)

cczb6y = ppz1y + thick
czb6 = APoint(ppz7x,cczb6y)

linecb1 = zbottom.addline(pz4,czb1)
linecb2 = zbottom.addline(czb1,czb6)
linecb7 = zbottom.addline(czb6,pz8)


#FOR PARTITION IN SECTION 2 (2 SECTION PANEL)
partition1_2 = config["section1_partition"]["partitons"]
if partition1_2 == "2":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition2(pz12,pz11,x1,x2,zleft,zright,"1","right")

elif partition1_2 == "3":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition3(pz12,pz11,x1,x2,zleft,zright,"1","right")

elif partition1_2 == "4":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition4(pz12,pz11,x1,x2,zleft,zright,"1","right")

elif partition1_2 == "5":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition5(pz12,pz11,x1,x2,zleft,zright,"1","right")

elif partition1_2 == "6":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition6(pz12,pz11,x1,x2,zleft,zright,"1","right")

elif partition1_2 == "1":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition1(pz12,pz11,x1,x2,zleft,zright,"1","right")

else:
        print("enter correct choice in partition")