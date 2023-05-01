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
config.read('./INDDOOR/gi_config_in.ini')

acad = Autocad()

dclearx = int(config["doors"]["door_clearence_X"])
dcleary = int(config["doors"]["door_clearence_Y"])
dclearmid = int(config["doors"]["door_clearence_MID"])
#start of codes
sec1 = int(config["section"]["Sec_1"])
sec2 = int(config["section"]["Sec_2"])

ss1x = l + sec1 -(vchannel/2) +thick ; ss1y = zchanneltb 
s1 = APoint(ss1x,ss1y)

ss2y = width - zchanneltb 
s2 = APoint(ss1x,ss2y)

ss3x = ss1x + vchannel -(thick*2)
s3 = APoint(ss3x,ss2y)

s4 = APoint(ss3x,ss1y)

ss5x = l + sec1 + sec2 -(vchannel/2) + thick
s5 = APoint(ss5x,ss1y)

s6 = APoint(ss5x,ss2y)

ss7x = ss5x + vchannel -(thick*2)
s7 = APoint(ss7x,ss2y)

s8 = APoint(ss7x,ss1y)

u1 = acad.doc.Blocks.Add(APoint(0), "u1")
u2 = acad.doc.Blocks.Add(APoint(0), "u2")
lines1 = u1.AddLine(s1, s2)
lines2 = u1.AddLine(s2, s3)
lines3 = u1.AddLine(s3, s4)
lines4 = u1.AddLine(s4, s1)
lines5 = u2.AddLine(s5, s6)
lines6 = u2.AddLine(s6, s7)
lines7 = u2.AddLine(s7, s8)
lines8 = u2.AddLine(s8, s5)

acad.model.InsertBlock(APoint(0), "u1", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "u2", 1, 1, 1, 0)

#FOR CUTOUTS IN TOP BOTTOM Z CHANNEL
cc1y = ppz2y - thick  # FOR TOP
cz1 = APoint(ppz3x,cc1y)

cc2x = ss1x - thick
cz2 = APoint(cc2x,cc1y)

cz3 = APoint(cc2x,ss2y)

cc4x = cc2x + vchannel
cz4 = APoint(cc4x,ss2y)

cz5 = APoint(cc4x,cc1y)

ccz6y = ppz2y - thick
cz6 = APoint(ppz7x,ccz6y)

ccz7x = cc2x + sec2
cz7 = APoint(ccz7x,cc1y)

ccz8x = ccz7x + vchannel
cz8 = APoint(ccz8x,cc1y)

linect1 = ztop.addline(pz3,cz1)
linect2 = ztop.addline(cz1,cz2)
linect3 = ztop.addline(cz2,cz3)
linect4 = ztop.addline(cz3,cz4)
linect5 = ztop.addline(cz4,cz5)
linect6 = ztop.addline(cz5,cz7)
linect7 = ztop.addline(cz6,pz7)
linect8 = ztop.addline(cz2,cz3);linect8.move(cz2,cz7)
linect9 = ztop.addline(cz3,cz4);linect9.move(cz2,cz7)
linect10 = ztop.addline(cz4,cz5);linect10.move(cz2,cz7)
linect11 = ztop.addline(cz8,cz6)

cczb1y = ppz1y + thick  #FOR BOTTOM
czb1 = APoint(ppz3x,cczb1y)

cczb2x = ss1x - thick
czb2 = APoint(cczb2x,cczb1y)

czb3 = APoint(cczb2x,ppz1y)

cczb4x = cczb2x + vchannel
czb4 = APoint(cczb4x,ppz1y)

czb5 = APoint(cczb4x,cczb1y)

cczb6y = ppz1y + thick
czb6 = APoint(ppz7x,cczb6y)

czb7 = APoint(ccz7x,cczb1y)

czb8 = APoint(ccz8x,cczb1y)

linecb1 = zbottom.addline(pz4,czb1)
linecb2 = zbottom.addline(czb1,czb2)
linecb3 = zbottom.addline(czb2,czb3)
linecb4 = zbottom.addline(czb3,czb4)
linecb5 = zbottom.addline(czb4,czb5)
linecb6 = zbottom.addline(czb5,czb7)
linecb7 = zbottom.addline(czb8,czb6)
linecb8 = zbottom.addline(czb6,pz8)
linecb9 = zbottom.addline(czb2,czb3);linecb9.move(czb2,czb7)
linecb10 = zbottom.addline(czb3,czb4);linecb10.move(czb2,czb7)
linecb11 = zbottom.addline(czb4,czb5);linecb11.move(czb2,czb7)

#FOR PARTITION IN SECTION 1 (3 SECTION PANEL)
partition3_1 = config["section1_partition"]["partitons"]
if partition3_1 == "2":
        partition2(pz12,pz11,s1,s2,zleft,u1,"1","left")

elif partition3_1 == "3":
        partition3(pz12,pz11,s1,s2,zleft,u1,"1","left")

elif partition3_1 == "4":
        partition4(pz12,pz11,s1,s2,zleft,u1,"1","left")

elif partition3_1 == "5":
        partition5(pz12,pz11,s1,s2,zleft,u1,"1","left")

elif partition3_1 == "6":
        partition6(pz12,pz11,s1,s2,zleft,u1,"1","left")

elif partition3_1 == "1":
        partition1(pz12,pz11,s1,s2,zleft,u1,"1","left")

else:
        print("enter correct choice in partition")

#FOR PARTITION IN SECTION 2 (3 SECTION PANEL)
partition3_2 = config["section2_partition"]["partitons"]
if partition3_2 == "2":
        partition2(s4,s3,s5,s6,u1,u2,"2","mid")

elif partition3_2 == "3":
        partition3(s4,s3,s5,s6,u1,u2,"2","mid")

elif partition3_2 == "4":
        partition4(s4,s3,s5,s6,u1,u2,"2","mid")

elif partition3_2 == "5":
        partition5(s4,s3,s5,s6,u1,u2,"2","mid")

elif partition3_2 == "6":
        partition6(s4,s3,s5,s6,u1,u2,"2","mid")

elif partition3_2 == "1":
        partition1(s4,s3,s5,s6,u1,u2,"2","mid")

else:
        print("enter correct choice in partition")

#FOR PARTITION IN SECTION 3  (3 SECTION PANEL)
partition2_3 = config["section3_partition"]["partitons"]
if partition2_3 == "2":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition2(s8,s7,x1,x2,u2,zright,"3","right")

elif partition2_3 == "3":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition3(s8,s7,x1,x2,u2,zright,"3","right")

elif partition2_3 == "4":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition4(s8,s7,x1,x2,u2,zright,"3","right")

elif partition2_3 == "5":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition5(s8,s7,x1,x2,u2,zright,"3","right")

elif partition2_3 == "6":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition6(s8,s7,x1,x2,u2,zright,"3","right")

elif partition2_3 == "1":
        x1 = APoint(pz8.x + thick,pz8.y)
        x2 = APoint(pz7.x + thick,pz7.y)
        partition1(s8,s7,x1,x2,u2,zright,"3","right")

else:
        print("enter correct choice in partition")

acad.app.zoomextents()