from pyautocad import Autocad, APoint
from configparser import ConfigParser
from doors_gi import gidoores
from GI import l
from GI import vchannel
from GI import thick
from GI import zchanneltb
from GI import zchannelside
from GI import width
from GI import hchannel
from GI import ppz11x
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
config.read("gi_config_in.ini")

acad = Autocad()

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
partition2_1 = config["section1_partition"]["partitons"]
if partition2_1 == "2":
        part1 = int(config["section1_partition"]["part1"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ppz11x,hh1y)
        
        h2 =APoint(ss1x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss1x,hh3y)

        h4 = APoint(ppz11x,hh3y)

        h1_1 = acad.doc.Blocks.Add(APoint(0), "h1_1")
        lineh1 = h1_1.addline(h1,h2)
        lineh2 = h1_1.addline(h2,h3)
        lineh3 = h1_1.addline(h3,h4)
        lineh4 = h1_1.addline(h4,h1)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ppz11x,hh101y)

        h102 = APoint(ss1x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ppz11x,hh104y)

        h103 = APoint(ss1x,hh104y)

        lineh111 = h1_1.addline(h101,h102)
        lineh112 = h1_1.addline(h103,h104)

        acad.model.InsertBlock(APoint(0), "h1_1", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz11x + thick  #for left
        c1 = APoint(cc1x,hh1y)

        c2 = APoint(ppz11x,hh1y)
        
        cc3y = hh1y + hchannel
        c3 = APoint(ppz11x,cc3y)

        c4 = APoint(cc1x,cc3y)


        linec1 = zleft.addline(pz4,c1)
        linec2 = zleft.addline(c1,c2)
        linec3 = zleft.addline(c2,c3)
        linec4 = zleft.addline(c3,c4)
        linec5 = zleft.addline(c4,pz3)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss1x - thick
        cs1 = APoint(cs1x,ss1y)
        
        cs2 = APoint(cs1x,hh1y)
        
        cs3 = APoint(ss1x,hh1y)
        
        cs4y = hh1y + hchannel
        cs4 = APoint(ss1x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        linecs1 = u1.addline(s1,cs1)
        linecs2 = u1.addline(cs1,cs2)
        linecs3 = u1.addline(cs2,cs3)
        linecs4 = u1.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5)
        linecs6 = u1.addline(cs5,cs6)
        linecs7 = u1.addline(cs6,s2)

        #FOR DOORS
        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = pz12
        gidoores(a,b,c,d,"ddor1_1","sec1",zleft,u1,pz4,"bot")

        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = width - part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = c4
        gidoores(a,b,c,d,"ddor1_2","sec1",zleft,u1,c4,"top")

elif partition2_1 == "3":
        part1 = int(config["section1_partition"]["part1"])
        part2 = int(config["section1_partition"]["part2"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ppz11x,hh1y)
        
        h2 =APoint(ss1x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss1x,hh3y)

        h4 = APoint(ppz11x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ppz11x,hh5y)

        h1_1 = acad.doc.Blocks.Add(APoint(0), "h1_1")
        h1_2 = acad.doc.Blocks.Add(APoint(0), "h1_2")
        lineh1 = h1_1.addline(h1,h2)
        lineh2 = h1_1.addline(h2,h3)
        lineh3 = h1_1.addline(h3,h4)
        lineh4 = h1_1.addline(h4,h1)
        lineh5 = h1_2.addline(h1,h2);lineh5.move(h1,h5)
        lineh6 = h1_2.addline(h2,h3);lineh6.move(h1,h5)
        lineh7 = h1_2.addline(h3,h4);lineh7.move(h1,h5)
        lineh8 = h1_2.addline(h4,h1);lineh8.move(h1,h5)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ppz11x,hh101y)

        h102 = APoint(ss1x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ppz11x,hh104y)

        h103 = APoint(ss1x,hh104y)

        lineh111 = h1_1.addline(h101,h102)
        lineh112 = h1_1.addline(h103,h104)
        lineh113 = h1_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h1_2.addline(h103,h104);lineh114.move(h1,h5)

        acad.model.InsertBlock(APoint(0), "h1_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h1_2", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz11x + thick  #for left
        c1 = APoint(cc1x,hh1y)

        c2 = APoint(ppz11x,hh1y)
    
        cc3y = hh1y + hchannel
        c3 = APoint(ppz11x,cc3y)

        c4 = APoint(cc1x,cc3y)

        c5y = hh1y + part2
        c5 = APoint(cc1x,c5y)

        c6y = c5y + hchannel
        c6 = APoint(cc1x,c6y)


        linec1 = zleft.addline(pz4,c1)
        linec2 = zleft.addline(c1,c2)
        linec3 = zleft.addline(c2,c3)
        linec4 = zleft.addline(c3,c4)
        linec6 = zleft.addline(c1,c2);linec6.move(c1,c5)
        linec7 = zleft.addline(c2,c3);linec7.move(c1,c5)
        linec8 = zleft.addline(c3,c4);linec8.move(c1,c5)
        linec9 = zleft.addline(c4,c5)

        linec5 = zleft.addline(c6,pz3)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss1x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss1x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss1x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        linecs1 = u1.addline(s1,cs1)
        linecs2 = u1.addline(cs1,cs2)
        linecs3 = u1.addline(cs2,cs3)
        linecs4 = u1.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5)
        linecs8 = u1.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u1.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u1.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = u1.addline(cs8,cs6)

        linecs6 = u1.addline(cs5,cs7)
        linecs7 = u1.addline(cs6,s2)

        #FOR DOORS
        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = pz12
        gidoores(a,b,c,d,"ddor1_1","sec1",zleft,u1,pz4,"bot")

        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = part2 - dclear
        c = APoint(30,15)
        d = c4
        gidoores(a,b,c,d,"ddor1_2","sec1",zleft,u1,c4,"mid")

        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = width - part1 - part2 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = c6
        gidoores(a,b,c,d,"ddor1_3","sec1",zleft,u1,c6,"top")

elif partition2_1 == "4":
        part1 = int(config["section1_partition"]["part1"])
        part2 = int(config["section1_partition"]["part2"])
        part3 = int(config["section1_partition"]["part3"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ppz11x,hh1y)
        
        h2 =APoint(ss1x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss1x,hh3y)

        h4 = APoint(ppz11x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ppz11x,hh5y)

        hh6y = hh5y + part3
        h6 = APoint(ppz11x,hh6y)

        h1_1 = acad.doc.Blocks.Add(APoint(0), "h1_1")
        h1_2 = acad.doc.Blocks.Add(APoint(0), "h1_2")
        h1_3 = acad.doc.Blocks.Add(APoint(0), "h1_3")
        lineh1 = h1_1.addline(h1,h2)
        lineh2 = h1_1.addline(h2,h3)
        lineh3 = h1_1.addline(h3,h4)
        lineh4 = h1_1.addline(h4,h1)
        lineh5 = h1_2.addline(h1,h2);lineh5.move(h1,h5)
        lineh6 = h1_2.addline(h2,h3);lineh6.move(h1,h5)
        lineh7 = h1_2.addline(h3,h4);lineh7.move(h1,h5)
        lineh8 = h1_2.addline(h4,h1);lineh8.move(h1,h5)
        lineh9 = h1_3.addline(h1,h2);lineh9.move(h1,h6)
        lineh10 = h1_3.addline(h2,h3);lineh10.move(h1,h6)
        lineh11 = h1_3.addline(h3,h4);lineh11.move(h1,h6)
        lineh12 = h1_3.addline(h4,h1);lineh12.move(h1,h6)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ppz11x,hh101y)

        h102 = APoint(ss1x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ppz11x,hh104y)

        h103 = APoint(ss1x,hh104y)

        lineh111 = h1_1.addline(h101,h102)
        lineh112 = h1_1.addline(h103,h104)
        lineh113 = h1_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h1_2.addline(h103,h104);lineh114.move(h1,h5)
        lineh115 = h1_3.addline(h101,h102);lineh115.move(h1,h6)
        lineh116 = h1_3.addline(h103,h104);lineh116.move(h1,h6)

        acad.model.InsertBlock(APoint(0), "h1_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h1_2", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h1_3", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz11x + thick  #for left
        c1 = APoint(cc1x,hh1y)

        c2 = APoint(ppz11x,hh1y)
    
        cc3y = hh1y + hchannel
        c3 = APoint(ppz11x,cc3y)

        c4 = APoint(cc1x,cc3y)

        c5y = hh1y + part2
        c5 = APoint(cc1x,c5y)

        c6y = c5y + hchannel
        c6 = APoint(cc1x,c6y)

        c7y = c5y + part3
        c7 =APoint(cc1x,c7y)

        c8y = c7y + hchannel
        c8 =APoint(cc1x,c8y)


        linec1 = zleft.addline(pz4,c1)
        linec2 = zleft.addline(c1,c2)
        linec3 = zleft.addline(c2,c3)
        linec4 = zleft.addline(c3,c4)
        linec6 = zleft.addline(c1,c2);linec6.move(c1,c5)
        linec7 = zleft.addline(c2,c3);linec7.move(c1,c5)
        linec8 = zleft.addline(c3,c4);linec8.move(c1,c5)
        linec9 = zleft.addline(c4,c5)
        linec10 = zleft.addline(c1,c2);linec10.move(c1,c7)
        linec11 = zleft.addline(c2,c3);linec11.move(c1,c7)
        linec12 = zleft.addline(c3,c4);linec12.move(c1,c7)
        linec13 = zleft.addline(c6,c7)

        linec5 = zleft.addline(c8,pz3)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss1x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss1x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss1x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        cs9 = APoint(cs1x,c7y)

        cs10 = APoint(cs1x,c8y)

        linecs1 = u1.addline(s1,cs1)
        linecs2 = u1.addline(cs1,cs2)
        linecs3 = u1.addline(cs2,cs3)
        linecs4 = u1.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5)
        linecs8 = u1.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u1.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u1.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = u1.addline(cs8,cs9)
        linecs12 = u1.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = u1.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = u1.addline(cs4,cs5);linecs14.move(cs2,cs9)
        linecs15 = u1.addline(cs10,cs6)

        linecs6 = u1.addline(cs5,cs7)
        linecs7 = u1.addline(cs6,s2)

        #FOR DOORS
        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = pz12
        gidoores(a,b,c,d,"ddor1_1","sec1",zleft,u1,pz4,"bot")

        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = part2 - dclear
        c = APoint(30,15)
        d = c4
        gidoores(a,b,c,d,"ddor1_2","sec1",zleft,u1,c4,"mid")

        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = part3 - dclear
        c = APoint(30,15)
        d = c6
        gidoores(a,b,c,d,"ddor1_3","sec1",zleft,u1,c6,"mid")

        a = sec1 - (dclear/2) - (zchannelside-30) - thick
        b = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = c8
        gidoores(a,b,c,d,"ddor1_4","sec1",zleft,u1,c8,"top")

else:
        print("enter correct choice in partition")

#FOR PARTITION IN SECTION 2 (3 SECTION PANEL)
partition2_2 = config["section2_partition"]["partitons"]
if partition2_2 == "2":
        part1 = int(config["section2_partition"]["part1"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss3x,hh1y)
        
        h2 =APoint(ss5x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss5x,hh3y)

        h4 = APoint(ss3x,hh3y)

        h2_1 = acad.doc.Blocks.Add(APoint(0), "h2_1")
        lineh1 = h2_1.addline(h1,h2)
        lineh2 = h2_1.addline(h2,h3)
        lineh3 = h2_1.addline(h3,h4)
        lineh4 = h2_1.addline(h4,h1)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss3x,hh101y)

        h102 = APoint(ss5x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss3x,hh104y)

        h103 = APoint(ss5x,hh104y)

        lineh111 = h2_1.addline(h101,h102)
        lineh112 = h2_1.addline(h103,h104)

        acad.model.InsertBlock(APoint(0), "h2_1", 1, 1, 1, 0)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss3x + thick
        cs1v1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss3x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss3x,cs4y)

        cs5v1 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        linecs1 = u1.addline(s1,cs1v1)
        linecs2 = u1.addline(cs1v1,cs2)
        linecs3 = u1.addline(cs2,cs3)
        linecs4 = u1.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5v1)
        linecs6 = u1.addline(cs5v1,cs6)
        linecs7 = u1.addline(cs6,s2)

        #FOR CUTOUT IN V2 CHANNEL
        cs1x = ss5x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss5x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss5x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        linecs1 = u2.addline(s5,cs1)
        linecs2 = u2.addline(cs1,cs2)
        linecs3 = u2.addline(cs2,cs3)
        linecs4 = u2.addline(cs3,cs4)
        linecs5 = u2.addline(cs4,cs5)
        linecs6 = u2.addline(cs5,cs6)
        linecs7 = u2.addline(cs6,s6)

        #FOR DOORS
        a = sec2 - (dclear/2) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = s4
        gidoores(a,b,c,d,"ddor2_1","sec2",u1,u2,cs1v1,"bot")

        a = sec2 - (dclear/2) - thick
        b = width - part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = cs5v1
        gidoores(a,b,c,d,"ddor2_2","sec2",u1,u2,cs5v1,"top")

elif partition2_2 == "3":
        part1 = int(config["section2_partition"]["part1"])
        part2 = int(config["section2_partition"]["part2"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss3x,hh1y)
        
        h2 =APoint(ss5x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss5x,hh3y)

        h4 = APoint(ss3x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss3x,hh5y)

        h2_1 = acad.doc.Blocks.Add(APoint(0), "h2_1")
        h2_2 = acad.doc.Blocks.Add(APoint(0), "h2_2")
        lineh1 = h2_1.addline(h1,h2)
        lineh2 = h2_1.addline(h2,h3)
        lineh3 = h2_1.addline(h3,h4)
        lineh4 = h2_1.addline(h4,h1)
        lineh5 = h2_2.addline(h1,h2);lineh5.move(h1,h5)
        lineh6 = h2_2.addline(h2,h3);lineh6.move(h1,h5)
        lineh7 = h2_2.addline(h3,h4);lineh7.move(h1,h5)
        lineh8 = h2_2.addline(h4,h1);lineh8.move(h1,h5)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss3x,hh101y)

        h102 = APoint(ss5x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss3x,hh104y)

        h103 = APoint(ss5x,hh104y)

        lineh111 = h2_1.addline(h101,h102)
        lineh112 = h2_1.addline(h103,h104)
        lineh113 = h2_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h2_2.addline(h103,h104);lineh114.move(h1,h5)

        acad.model.InsertBlock(APoint(0), "h2_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h2_2", 1, 1, 1, 0)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss3x + thick
        cs1v1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss3x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss3x,cs4y)

        cs5v1 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)
        c5y = hh1y + part2
        cs7 =APoint(cs1x,c5y)
        c6y = c5y + hchannel
        cs8v1 = APoint(cs1x,c6y)

        linecs1 = u1.addline(s1,cs1v1)
        linecs2 = u1.addline(cs1v1,cs2)
        linecs3 = u1.addline(cs2,cs3)
        linecs4 = u1.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5v1)
        linecs8 = u1.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u1.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u1.addline(cs4,cs5v1);linecs10.move(cs2,cs7)
        linecs11 = u1.addline(cs8v1,cs6)
        linecs6 = u1.addline(cs5v1,cs7)
        linecs7 = u1.addline(cs6,s2)

        #FOR CUTOUT IN V2 CHANNEL
        cs1x = ss5x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss5x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss5x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)
        
        cs8 = APoint(cs1x,c6y)

        linecs1 = u2.addline(s5,cs1)
        linecs2 = u2.addline(cs1,cs2)
        linecs3 = u2.addline(cs2,cs3)
        linecs4 = u2.addline(cs3,cs4)
        linecs5 = u2.addline(cs4,cs5)
        linecs8 = u2.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u2.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u2.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = u2.addline(cs8,cs6)

        linecs6 = u2.addline(cs5,cs7)
        linecs7 = u2.addline(cs6,s6)

        #FOR DOORS
        a = sec2 - (dclear/2) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = s4
        gidoores(a,b,c,d,"ddor2_1","sec2",u1,u2,cs1v1,"bot")

        a = sec2 - (dclear/2) - thick
        b = part2 - dclear
        c = APoint(30,15)
        d = cs5v1
        gidoores(a,b,c,d,"ddor2_2","sec2",u1,u2,cs5v1,"mid")

        a = sec2 - (dclear/2) - thick
        b = width - part1 - part2 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = cs8v1
        gidoores(a,b,c,d,"ddor2_3","sec2",u1,u2,cs8v1,"top")

elif partition2_2 == "4":
        part1 = int(config["section2_partition"]["part1"])
        part2 = int(config["section2_partition"]["part2"])
        part3 = int(config["section2_partition"]["part3"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss3x,hh1y)
        
        h2 =APoint(ss5x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss5x,hh3y)

        h4 = APoint(ss3x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss3x,hh5y)

        hh6y = hh5y + part3
        h6 = APoint(ss3x,hh6y)

        h2_1 = acad.doc.Blocks.Add(APoint(0), "h2_1")
        h2_2 = acad.doc.Blocks.Add(APoint(0), "h2_2")
        h2_3 = acad.doc.Blocks.Add(APoint(0), "h2_3")
        lineh1 = h2_1.addline(h1,h2)
        lineh2 = h2_1.addline(h2,h3)
        lineh3 = h2_1.addline(h3,h4)
        lineh4 = h2_1.addline(h4,h1)
        lineh5 = h2_2.addline(h1,h2);lineh5.move(h1,h5)
        lineh6 = h2_2.addline(h2,h3);lineh6.move(h1,h5)
        lineh7 = h2_2.addline(h3,h4);lineh7.move(h1,h5)
        lineh8 = h2_2.addline(h4,h1);lineh8.move(h1,h5)
        lineh9 = h2_3.addline(h1,h2);lineh9.move(h1,h6)
        lineh10 = h2_3.addline(h2,h3);lineh10.move(h1,h6)
        lineh11 = h2_3.addline(h3,h4);lineh11.move(h1,h6)
        lineh12 = h2_3.addline(h4,h1);lineh12.move(h1,h6)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss3x,hh101y)

        h102 = APoint(ss5x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss3x,hh104y)

        h103 = APoint(ss5x,hh104y)

        lineh111 = h2_1.addline(h101,h102)
        lineh112 = h2_1.addline(h103,h104)
        lineh113 = h2_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h2_2.addline(h103,h104);lineh114.move(h1,h5)
        lineh115 = h2_3.addline(h101,h102);lineh115.move(h1,h6)
        lineh116 = h2_3.addline(h103,h104);lineh116.move(h1,h6)

        acad.model.InsertBlock(APoint(0), "h2_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h2_2", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h2_3", 1, 1, 1, 0)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss3x + thick
        cs1v1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss3x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss3x,cs4y)

        cs5v1 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        c5y = hh1y + part2
        cs7 =APoint(cs1x,c5y)
        c6y = c5y + hchannel
        cs8v1 = APoint(cs1x,c6y)
        c7y = c5y + part3
        cs9 = APoint(cs1x,c7y)
        c8y = c7y + hchannel
        cs10v1 = APoint(cs1x,c8y)

        linecs1 = u1.addline(s1,cs1v1)
        linecs2 = u1.addline(cs1v1,cs2)
        linecs3 = u1.addline(cs2,cs3)
        linecs4 = u1.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5v1)
        linecs8 = u1.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u1.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u1.addline(cs4,cs5v1);linecs10.move(cs2,cs7)
        linecs11 = u1.addline(cs8v1,cs9)
        linecs12 = u1.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = u1.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = u1.addline(cs4,cs5v1);linecs14.move(cs2,cs9)
        linecs15 = u1.addline(cs10v1,cs6)

        linecs6 = u1.addline(cs5v1,cs7)
        linecs7 = u1.addline(cs6,s2)

        #FOR CUTOUT IN V2 CHANNEL
        cs1x = ss5x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss5x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss5x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        cs9 = APoint(cs1x,c7y)

        cs10 = APoint(cs1x,c8y)

        linecs1 = u2.addline(s5,cs1)
        linecs2 = u2.addline(cs1,cs2)
        linecs3 = u2.addline(cs2,cs3)
        linecs4 = u2.addline(cs3,cs4)
        linecs5 = u1.addline(cs4,cs5)
        linecs8 = u2.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u2.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u2.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = u2.addline(cs8,cs9)
        linecs12 = u2.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = u2.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = u2.addline(cs4,cs5);linecs14.move(cs2,cs9)
        linecs15 = u2.addline(cs10,cs6)

        linecs6 = u2.addline(cs5,cs7)
        linecs7 = u2.addline(cs6,s6)

        #FOR DOORS
        a = sec2 - (dclear/2) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = s4
        gidoores(a,b,c,d,"ddor2_1","sec2",u1,u2,cs1v1,"bot")

        a = sec2 - (dclear/2) - thick
        b = part2 - dclear
        c = APoint(30,15)
        d = cs5v1
        gidoores(a,b,c,d,"ddor2_2","sec2",u1,u2,cs5v1,"mid")

        a = sec2 - (dclear/2) - thick
        b = part3 - dclear
        c = APoint(30,15)
        d = cs8v1
        gidoores(a,b,c,d,"ddor2_3","sec2",u1,u2,cs8v1,"mid")

        a = sec2 - (dclear/2) - thick
        b = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = cs10v1
        gidoores(a,b,c,d,"ddor2_4","sec2",u1,u2,cs10v1,"top")

else:
        print("enter correct choice in partition")

#FOR PARTITION IN SECTION 3  (3 SECTION PANEL)
partition2_3 = config["section3_partition"]["partitons"]
if partition2_3 == "2":
        part1 = int(config["section3_partition"]["part1"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss7x,hh1y)
        
        hh2x = ppz7x + thick
        h2 =APoint(hh2x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(hh2x,hh3y)

        h4 = APoint(ss7x,hh3y)

        h3_1 = acad.doc.Blocks.Add(APoint(0), "h3_1")
        lineh1 = h3_1.addline(h1,h2)
        lineh2 = h3_1.addline(h2,h3)
        lineh3 = h3_1.addline(h3,h4)
        lineh4 = h3_1.addline(h4,h1)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss7x,hh101y)

        h102 = APoint(hh2x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss7x,hh104y)

        h103 = APoint(hh2x,hh104y)

        lineh111 = h3_1.addline(h101,h102)
        lineh112 = h3_1.addline(h103,h104)

        acad.model.InsertBlock(APoint(0), "h3_1", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz7x   #for right
        c1 = APoint(cc1x,hh1y)

        c2x = ppz7x + thick
        c2 = APoint(c2x,hh1y)
    
        cc3y = hh1y + hchannel
        c3 = APoint(c2x,cc3y)

        c4 = APoint(cc1x,cc3y)


        linec1 = zright.addline(pz8,c1)
        linec2 = zright.addline(c1,c2)
        linec3 = zright.addline(c2,c3)
        linec4 = zright.addline(c3,c4)
        linec5 = zright.addline(c4,pz7)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss7x + thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss7x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss7x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        linecs1 = u2.addline(s8,cs1)
        linecs2 = u2.addline(cs1,cs2)
        linecs3 = u2.addline(cs2,cs3)
        linecs4 = u2.addline(cs3,cs4)
        linecs5 = u2.addline(cs4,cs5)
        linecs6 = u2.addline(cs5,cs6)
        linecs7 = u2.addline(cs6,s7)

        #FOR DOORS
        a = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-30) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = s8
        gidoores(a,b,c,d,"ddor3_1","sec3",u2,zright,cs1,"bot")

        a = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-30) - thick
        b = width - part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = cs5
        gidoores(a,b,c,d,"ddor3_2","sec3",u2,zright,cs5,"top")

elif partition2_3 == "3":
        part1 = int(config["section3_partition"]["part1"])
        part2 = int(config["section3_partition"]["part2"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss7x,hh1y)
        
        hh2x = ppz7x + thick
        h2 =APoint(hh2x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(hh2x,hh3y)

        h4 = APoint(ss7x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss7x,hh5y)

        h3_1 = acad.doc.Blocks.Add(APoint(0), "h3_1")
        h3_2 = acad.doc.Blocks.Add(APoint(0), "h3_2")
        lineh1 = h3_1.addline(h1,h2)
        lineh2 = h3_1.addline(h2,h3)
        lineh3 = h3_1.addline(h3,h4)
        lineh4 = h3_1.addline(h4,h1)
        lineh5 = h3_2.addline(h1,h2);lineh5.move(h1,h5)
        lineh6 = h3_2.addline(h2,h3);lineh6.move(h1,h5)
        lineh7 = h3_2.addline(h3,h4);lineh7.move(h1,h5)
        lineh8 = h3_2.addline(h4,h1);lineh8.move(h1,h5)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss7x,hh101y)

        h102 = APoint(hh2x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss7x,hh104y)

        h103 = APoint(hh2x,hh104y)

        lineh111 = h3_1.addline(h101,h102)
        lineh112 = h3_1.addline(h103,h104)
        lineh113 = h3_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h3_2.addline(h103,h104);lineh114.move(h1,h5)

        acad.model.InsertBlock(APoint(0), "h3_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h3_2", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz7x  #for right
        c1 = APoint(cc1x,hh1y)

        c2x = ppz7x + thick
        c2 = APoint(c2x,hh1y)
    
        cc3y = hh1y + hchannel
        c3 = APoint(c2x,cc3y)

        c4 = APoint(cc1x,cc3y)

        c5y = hh1y + part2
        c5 = APoint(cc1x,c5y)

        c6y = c5y + hchannel
        c6 = APoint(cc1x,c6y)


        linec1 = zright.addline(pz8,c1)
        linec2 = zright.addline(c1,c2)
        linec3 = zright.addline(c2,c3)
        linec4 = zright.addline(c3,c4)
        linec6 = zright.addline(c1,c2);linec6.move(c1,c5)
        linec7 = zright.addline(c2,c3);linec7.move(c1,c5)
        linec8 = zright.addline(c3,c4);linec8.move(c1,c5)
        linec9 = zright.addline(c4,c5)

        linec5 = zright.addline(c6,pz7)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss7x + thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss7x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss7x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        linecs1 = u2.addline(s8,cs1)
        linecs2 = u2.addline(cs1,cs2)
        linecs3 = u2.addline(cs2,cs3)
        linecs4 = u2.addline(cs3,cs4)
        linecs5 = u2.addline(cs4,cs5)
        linecs8 = u2.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u2.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u2.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = u2.addline(cs8,cs6)

        linecs6 = u2.addline(cs5,cs7)
        linecs7 = u2.addline(cs6,s7)

        #FOR DOORS
        a = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-30) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = s8
        gidoores(a,b,c,d,"ddor3_1","sec3",u2,zright,cs1,"bot")

        a = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-30) - thick
        b = part2 - dclear
        c = APoint(30,15)
        d = cs5
        gidoores(a,b,c,d,"ddor3_2","sec3",u2,zright,cs5,"mid")

        a = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-30) - thick
        b = width - part1 - part2 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = cs8
        gidoores(a,b,c,d,"ddor3_3","sec3",u2,zright,cs8,"top")

elif partition2_3 == "4":
        part1 = int(config["section3_partition"]["part1"])
        part2 = int(config["section3_partition"]["part2"])
        part3 = int(config["section3_partition"]["part3"])

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss7x,hh1y)
        
        hh2x = ppz7x + thick
        h2 =APoint(hh2x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(hh2x,hh3y)

        h4 = APoint(ss7x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss7x,hh5y)

        hh6y = hh5y + part3
        h6 = APoint(ss7x,hh6y)

        h3_1 = acad.doc.Blocks.Add(APoint(0), "h3_1")
        h3_2 = acad.doc.Blocks.Add(APoint(0), "h3_2")
        h3_3 = acad.doc.Blocks.Add(APoint(0), "h3_3")
        lineh1 = h3_1.addline(h1,h2)
        lineh2 = h3_1.addline(h2,h3)
        lineh3 = h3_1.addline(h3,h4)
        lineh4 = h3_1.addline(h4,h1)
        lineh5 = h3_2.addline(h1,h2);lineh5.move(h1,h5)
        lineh6 = h3_2.addline(h2,h3);lineh6.move(h1,h5)
        lineh7 = h3_2.addline(h3,h4);lineh7.move(h1,h5)
        lineh8 = h3_2.addline(h4,h1);lineh8.move(h1,h5)
        lineh9 = h3_3.addline(h1,h2);lineh9.move(h1,h6)
        lineh10 = h3_3.addline(h2,h3);lineh10.move(h1,h6)
        lineh11 = h3_3.addline(h3,h4);lineh11.move(h1,h6)
        lineh12 = h3_3.addline(h4,h1);lineh12.move(h1,h6)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss7x,hh101y)

        h102 = APoint(hh2x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss7x,hh104y)

        h103 = APoint(hh2x,hh104y)

        lineh111 = h3_1.addline(h101,h102)
        lineh112 = h3_1.addline(h103,h104)
        lineh113 = h3_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h3_2.addline(h103,h104);lineh114.move(h1,h5)
        lineh115 = h3_3.addline(h101,h102);lineh115.move(h1,h6)
        lineh116 = h3_3.addline(h103,h104);lineh116.move(h1,h6)

        acad.model.InsertBlock(APoint(0), "h3_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h3_2", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h3_3", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz7x  #for right
        c1 = APoint(cc1x,hh1y)

        c2x = ppz7x + thick
        c2 = APoint(c2x,hh1y)
    
        cc3y = hh1y + hchannel
        c3 = APoint(c2x,cc3y)

        c4 = APoint(cc1x,cc3y)

        c5y = hh1y + part2
        c5 = APoint(cc1x,c5y)

        c6y = c5y + hchannel
        c6 = APoint(cc1x,c6y)

        c7y = c5y + part3
        c7 =APoint(cc1x,c7y)

        c8y = c7y + hchannel
        c8 =APoint(cc1x,c8y)


        linec1 = zright.addline(pz8,c1)
        linec2 = zright.addline(c1,c2)
        linec3 = zright.addline(c2,c3)
        linec4 = zright.addline(c3,c4)
        linec6 = zright.addline(c1,c2);linec6.move(c1,c5)
        linec7 = zright.addline(c2,c3);linec7.move(c1,c5)
        linec8 = zright.addline(c3,c4);linec8.move(c1,c5)
        linec9 = zright.addline(c4,c5)
        linec10 = zright.addline(c1,c2);linec10.move(c1,c7)
        linec11 = zright.addline(c2,c3);linec11.move(c1,c7)
        linec12 = zright.addline(c3,c4);linec12.move(c1,c7)
        linec13 = zright.addline(c6,c7)

        linec5 = zright.addline(c8,pz7)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss7x + thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss7x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss7x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        cs9 = APoint(cs1x,c7y)

        cs10 = APoint(cs1x,c8y)

        linecs1 = u2.addline(s8,cs1)
        linecs2 = u2.addline(cs1,cs2)
        linecs3 = u2.addline(cs2,cs3)
        linecs4 = u2.addline(cs3,cs4)
        linecs5 = u2.addline(cs4,cs5)
        linecs8 = u2.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = u2.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = u2.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = u2.addline(cs8,cs9)
        linecs12 = u2.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = u2.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = u2.addline(cs4,cs5);linecs14.move(cs2,cs9)
        linecs15 = u2.addline(cs10,cs6)

        linecs6 = u2.addline(cs5,cs7)
        linecs7 = u2.addline(cs6,s7)

        #FOR DOORS
        a = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-30) - thick
        b = part1 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,25)
        c = c - thick
        d = s8
        gidoores(a,b,c,d,"ddor3_1","sec3",u2,zright,cs1,"bot")

        a = lenght - sec1- sec2 - (dclear/2) - (zchannelside-30) - thick
        b = part2 - dclear
        c = APoint(30,15)
        d = cs5
        gidoores(a,b,c,d,"ddor3_2","sec3",u2,zright,cs5,"mid")

        a = lenght - sec1- sec2 - (dclear/2) - (zchannelside-30) - thick
        b = part3 - dclear
        c = APoint(30,15)
        d = cs8
        gidoores(a,b,c,d,"ddor3_3","sec3",u2,zright,cs8,"mid")

        a = lenght - sec1- sec2 - (dclear/2) - (zchannelside-30) - thick
        b = width - part1 - part2 - part3 - (dclear/2) - (zchanneltb-25) - thick
        c = APoint(30,15)
        d = cs10
        gidoores(a,b,c,d,"ddor3_4","sec3",u2,zright,cs10,"top")

else:
        print("enter correct choice in partition")

acad.app.zoomextents()