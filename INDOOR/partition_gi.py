from pyautocad import Autocad, APoint
from configparser import ConfigParser
from doors_gi import gidoores

config = ConfigParser()
config.read('./INDDOOR/gi_config_in.ini')

acad = Autocad()

dclearx = int(config["doors"]["door_clearence_X"])
dcleary = int(config["doors"]["door_clearence_Y"])
dclearmid = int(config["doors"]["door_clearence_MID"])
sec1 = int(config["section"]["Sec_1"])
sec2 = int(config["section"]["Sec_2"])
sec3 = int(config["section"]["Sec_3"])
sec4 = int(config["section"]["Sec_4"]) 
thick = float(config["shell"]["sheet_thickness"])
width = int(config["shell"]["width"])
dclear = int(config["doors"]["door_to_door_clearence"])
hchannel = int(config["shell"]["Horizontal_channel_size"])
zchanneltb = int(config["shell"]["Top_bottom_shell_size"])- thick
zchannelside = int(config["shell"]["side_shell_size"])- thick
lenght = int(config["shell"]["lenght"])

def partition1(a,b,c,d,e,f,g,h):

        ss1x = c.x
        ss1y = c.y
        ss2y = d.y
        #FOR CUTOUT IN Z CHANNEL

        c100x = a.x + thick
        c100 = APoint(c100x,a.y) 

        c101 = APoint(c100x,b.y)

        linec1 = e.addline(c100,c101)
        linec6 = e.addline(a,c100)
        linec7 = e.addline(b,c101)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss1x - thick
        cs1 = APoint(cs1x,ss1y)
        
        cs2 = APoint(cs1x,ss2y)

        linecs1 = f.addline(c,cs1)
        linecs2 = f.addline(cs1,cs2)
        linecs7 = f.addline(cs2,d)

        if h =="left":
                #FOR DOORS
                sec1 = int(config["section"]["Sec_"+g])
                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

        elif h == 'mid':
                #FOR DOORS
                sec1 = int(config["section"]["Sec_"+g])
                a1 = sec1 - dclear
                b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)
        elif h == "right":
                if g == '1':
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - (zchannelside-dclearx)-(zchannelside-dclearx) - thick - thick
                        b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)
                elif g == "2":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                elif g == "3":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                elif g == '4':
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                elif g =='5':
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 -sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)
                elif g == "6":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])  
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 -sec4 -sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width- (zchanneltb-dcleary) - (zchanneltb-dcleary) - thick - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)



def partition2(a,b,c,d,e,f,g,h):
        part1 = int(config["section"+g+"_partition"]["part1"])

        ppz11x = a.x
        ss1x = c.x
        ss1y = c.y
        ss2y = d.y

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ppz11x,hh1y)
        
        h2 =APoint(ss1x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss1x,hh3y)

        h4 = APoint(ppz11x,hh3y)

        h1_1 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_1")
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

        acad.model.InsertBlock(APoint(0), "h"+g+"_1", 1, 1, 1, 0)

        #FOR CUTOUT IN Z CHANNEL
        cc1x = ppz11x + thick  #for left
        c1 = APoint(cc1x,hh1y)

        c2 = APoint(ppz11x,hh1y)
        
        cc3y = hh1y + hchannel
        c3 = APoint(ppz11x,cc3y)

        c4 = APoint(cc1x,cc3y)

        c100x = a.x + thick
        c100 = APoint(c100x,a.y) 

        c101 = APoint(c100x,b.y)

        linec1 = e.addline(c100,c1)
        linec2 = e.addline(c1,c2)
        linec3 = e.addline(c2,c3)
        linec4 = e.addline(c3,c4)
        linec5 = e.addline(c4,c101)
        linec6 = e.addline(a,c100)
        linec7 = e.addline(b,c101)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss1x - thick
        cs1 = APoint(cs1x,ss1y)
        
        cs2 = APoint(cs1x,hh1y)
        
        cs3 = APoint(ss1x,hh1y)
        
        cs4y = hh1y + hchannel
        cs4 = APoint(ss1x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        linecs1 = f.addline(c,cs1)
        linecs2 = f.addline(cs1,cs2)
        linecs3 = f.addline(cs2,cs3)
        linecs4 = f.addline(cs3,cs4)
        linecs5 = f.addline(cs4,cs5)
        linecs6 = f.addline(cs5,cs6)
        linecs7 = f.addline(cs6,d)

        

        if h == "left":
                #FOR DOORS
                sec1 = int(config["section"]["Sec_"+g])
                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = c4
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)

                
        elif h == 'mid':
                #FOR DOORS
                sec1 = int(config["section"]["Sec_"+g])
                a1 = sec1 - dclear
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                a1 = sec1 - dclear
                b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = c4
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)
        elif h == 'right':
                if g == "1":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = c4
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)
                elif g == "2":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = c4
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)
                elif g == "3":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = c4
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)
                elif g == "4":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                        a1 = lenght - sec1 - sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = c4
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)
                elif g == "5":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 -sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                        a1 = lenght - sec1 - sec2 -sec3 -sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = c4
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)
                elif g == "6":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])  
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 -sec4 -sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,c100,"bot",h)

                        a1 = lenght - sec1 - sec2 -sec3 -sec4 -sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = c4
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,c4,"top",h)

def partition3(a,b,c,d,e,f,g,h):
        part1 = int(config["section"+g+"_partition"]["part1"])
        part2 = int(config["section"+g+"_partition"]["part2"])

        ss3x = a.x
        ss5x = c.x
        ss1y = a.y
        ss2y = b.y

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss3x,hh1y)
        
        h2 =APoint(ss5x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss5x,hh3y)

        h4 = APoint(ss3x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss3x,hh5y)

        h2_1 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_1")
        h2_2 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_2")
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

        acad.model.InsertBlock(APoint(0), "h"+g+"_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_2", 1, 1, 1, 0)

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

        linecs1 = e.addline(a,cs1v1)
        linecs2 = e.addline(cs1v1,cs2)
        linecs3 = e.addline(cs2,cs3)
        linecs4 = e.addline(cs3,cs4)
        linecs5 = e.addline(cs4,cs5v1)
        linecs8 = e.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = e.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = e.addline(cs4,cs5v1);linecs10.move(cs2,cs7)
        linecs11 = e.addline(cs8v1,cs6)

        linecs6 = e.addline(cs5v1,cs7)
        linecs7 = e.addline(cs6,b)

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

        linecs1 = f.addline(c,cs1)
        linecs2 = f.addline(cs1,cs2)
        linecs3 = f.addline(cs2,cs3)
        linecs4 = f.addline(cs3,cs4)
        linecs5 = f.addline(cs4,cs5)
        linecs8 = f.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = f.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = f.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = f.addline(cs8,cs6)

        linecs6 = f.addline(cs5,cs7)
        linecs7 = f.addline(cs6,d)

        

        if h == "left":
                #FOR DOORS
                sec1 = int(config["section"]["Sec_"+g])
                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)

                

        elif h == 'mid':

                #FOR DOORS
                sec1 = int(config["section"]["Sec_"+g])
                a1 = sec1 - dclear
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - dclear
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - dclear
                b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)

        elif h == "right":
                if g == "1":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"]) 
                        #FOR DOORS
                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)
                elif g =="2":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"]) 
                        #FOR DOORS
                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)

                elif g == "3":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"]) 
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)

                elif g == "4":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"]) 
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1 - sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1 - sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)
                elif g == "5":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"]) 
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - sec3 -sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1 - sec2 - sec3- sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1 - sec2 - sec3- sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)

                elif g == "6":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"]) 
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - sec3 - sec4 - sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1 - sec2 - sec3 - sec4 - sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1 - sec2 - sec3 - sec4 - sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width - part1 - part2 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"top",h)


def partition4(a,b,c,d,e,f,g,h):

        part1 = int(config["section"+g+"_partition"]["part1"])
        part2 = int(config["section"+g+"_partition"]["part2"])
        part3 = int(config["section"+g+"_partition"]["part3"])

        ss7x = a.x
        ss9x = c.x
        ss1y = a.y
        ss2y = b.y

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss7x,hh1y)
        
        h2 =APoint(ss9x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss9x,hh3y)

        h4 = APoint(ss7x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss7x,hh5y)

        hh6y = hh5y + part3
        h6 = APoint(ss7x,hh6y)

        h3_1 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_1")
        h3_2 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_2")
        h3_3 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_3")
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

        h102 = APoint(ss9x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss7x,hh104y)

        h103 = APoint(ss9x,hh104y)

        lineh111 = h3_1.addline(h101,h102)
        lineh112 = h3_1.addline(h103,h104)
        lineh113 = h3_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h3_2.addline(h103,h104);lineh114.move(h1,h5)
        lineh115 = h3_3.addline(h101,h102);lineh115.move(h1,h6)
        lineh116 = h3_3.addline(h103,h104);lineh116.move(h1,h6)

        acad.model.InsertBlock(APoint(0), "h"+g+"_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_2", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_3", 1, 1, 1, 0)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss7x + thick
        cs1v1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss7x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss7x,cs4y)

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

        linecs1 = e.addline(a,cs1v1)
        linecs2 = e.addline(cs1v1,cs2)
        linecs3 = e.addline(cs2,cs3)
        linecs4 = e.addline(cs3,cs4)
        linecs5 = e.addline(cs4,cs5v1)
        linecs8 = e.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = e.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = e.addline(cs4,cs5v1);linecs10.move(cs2,cs7)
        linecs11 = e.addline(cs8v1,cs9)
        linecs12 = e.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = e.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = e.addline(cs4,cs5v1);linecs14.move(cs2,cs9)
        linecs15 = e.addline(cs10v1,cs6)

        linecs6 = e.addline(cs5v1,cs7)
        linecs7 = e.addline(cs6,b)

        #FOR CUTOUT IN V2 CHANNEL
        cs1x = ss9x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss9x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss9x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        cs9 = APoint(cs1x,c7y)

        cs10 = APoint(cs1x,c8y)

        linecs1 = f.addline(c,cs1)
        linecs2 = f.addline(cs1,cs2)
        linecs3 = f.addline(cs2,cs3)
        linecs4 = f.addline(cs3,cs4)
        linecs5 = f.addline(cs4,cs5)
        linecs8 = f.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = f.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = f.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = f.addline(cs8,cs9)
        linecs12 = f.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = f.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = f.addline(cs4,cs5);linecs14.move(cs2,cs9)
        linecs15 = f.addline(cs10,cs6)

        linecs6 = f.addline(cs5,cs7)
        linecs7 = f.addline(cs6,d)

        

        if h == "left":
                sec1 = int(config["section"]["Sec_"+g])
                #FOR DOORS
                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part3 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs10v1
                gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)

        elif h == "mid":
                sec1 = int(config["section"]["Sec_"+g])
                #FOR DOORS
                a1 = sec1 - dclear
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - dclear
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - dclear
                b1 = part3 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                a1 = sec1 - dclear
                b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs10v1
                gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)
        elif h == "right":
                if g == "1":
                        #FOR DOORS
                        a1 = lenght - (zchannelside-dclearx) - thick- (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - (zchannelside-dclearx) - thick- (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick- (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick- (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)
                elif g == "2":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)

                elif g == "3":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)

                elif g == "4":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)

                elif g == "5":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)

                elif g == "6":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3-sec4-sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3-sec4-sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4-sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3-sec4 -sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"top",h)


def partition5(a,b,c,d,e,f,g,h):

        part1 = int(config["section"+g+"_partition"]["part1"])
        part2 = int(config["section"+g+"_partition"]["part2"])
        part3 = int(config["section"+g+"_partition"]["part3"])
        part4 = int(config["section"+g+"_partition"]["part4"])

        ss7x = a.x
        ss9x = c.x
        ss1y = a.y
        ss2y = b.y

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss7x,hh1y)
        
        h2 =APoint(ss9x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss9x,hh3y)

        h4 = APoint(ss7x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss7x,hh5y)

        hh6y = hh5y + part3
        h6 = APoint(ss7x,hh6y)

        hh7y = hh6y + part4
        h7 = APoint(ss7x,hh7y)

        h3_1 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_1")
        h3_2 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_2")
        h3_3 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_3")
        h3_4 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_4")
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
        lineh13 = h3_4.addline(h1,h2);lineh13.move(h1,h7)
        lineh14 = h3_4.addline(h2,h3);lineh14.move(h1,h7)
        lineh15 = h3_4.addline(h3,h4);lineh15.move(h1,h7)
        lineh16 = h3_4.addline(h4,h1);lineh16.move(h1,h7)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss7x,hh101y)

        h102 = APoint(ss9x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss7x,hh104y)

        h103 = APoint(ss9x,hh104y)

        lineh111 = h3_1.addline(h101,h102)
        lineh112 = h3_1.addline(h103,h104)
        lineh113 = h3_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h3_2.addline(h103,h104);lineh114.move(h1,h5)
        lineh115 = h3_3.addline(h101,h102);lineh115.move(h1,h6)
        lineh116 = h3_3.addline(h103,h104);lineh116.move(h1,h6)
        lineh117 = h3_4.addline(h101,h102);lineh117.move(h1,h7)
        lineh118 = h3_4.addline(h103,h104);lineh118.move(h1,h7)

        acad.model.InsertBlock(APoint(0), "h"+g+"_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_2", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_3", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_4", 1, 1, 1, 0)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss7x + thick
        cs1v1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss7x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss7x,cs4y)

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
        cs11y = c7y + part4
        cs11 = APoint(cs1x,cs11y)
        cs12y = cs11y +hchannel
        cs12v1 = APoint(cs1x,cs12y)

        linecs1 = e.addline(a,cs1v1)
        linecs2 = e.addline(cs1v1,cs2)
        linecs3 = e.addline(cs2,cs3)
        linecs4 = e.addline(cs3,cs4)
        linecs5 = e.addline(cs4,cs5v1)
        linecs6 = e.addline(cs5v1,cs7)
        linecs8 = e.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = e.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = e.addline(cs4,cs5v1);linecs10.move(cs2,cs7)
        linecs11 = e.addline(cs8v1,cs9)
        linecs12 = e.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = e.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = e.addline(cs4,cs5v1);linecs14.move(cs2,cs9)
        linecs15 = e.addline(cs10v1,cs11)

        linecs16 = e.addline(cs2,cs3);linecs16.move(cs2,cs11)
        linecs17 = e.addline(cs3,cs4);linecs17.move(cs2,cs11)
        linecs18 = e.addline(cs4,cs5v1);linecs18.move(cs2,cs11)
        linecs19 = e.addline(cs12v1,cs6)
        linecs7 = e.addline(cs6,b)

        #FOR CUTOUT IN V2 CHANNEL
        cs1x = ss9x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss9x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss9x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        cs9 = APoint(cs1x,c7y)

        cs10 = APoint(cs1x,c8y)

        cs11 = APoint(cs1x,cs11y)

        cs12 = APoint(cs1x,cs12y)

        linecs1 = f.addline(c,cs1)
        linecs2 = f.addline(cs1,cs2)
        linecs3 = f.addline(cs2,cs3)
        linecs4 = f.addline(cs3,cs4)
        linecs5 = f.addline(cs4,cs5)
        linecs8 = f.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = f.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = f.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = f.addline(cs8,cs9)
        linecs12 = f.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = f.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = f.addline(cs4,cs5);linecs14.move(cs2,cs9)
        linecs15 = f.addline(cs10,cs11)

        linecs6 = f.addline(cs5,cs7)
        linecs7 = f.addline(cs6,d)
        linecs16 = f.addline(cs2,cs3);linecs16.move(cs2,cs11)
        linecs17 = f.addline(cs3,cs4);linecs17.move(cs2,cs11)
        linecs18 = f.addline(cs4,cs5);linecs18.move(cs2,cs11)
        linecs19 = f.addline(cs12,cs6)

        

        if h == "left":
                sec1 = int(config["section"]["Sec_"+g])
                #FOR DOORS
                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part3 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part4 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs10v1
                gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = width -part1 - part2 - part3- part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs12v1
                gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)

        elif h == "mid":
                sec1 = int(config["section"]["Sec_"+g])
                #FOR DOORS
                a1 = sec1 - dclear
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - dclear
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - dclear
                b1 = part3 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                a1 = sec1 - dclear
                b1 = part4 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs10v1
                gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                a1 = sec1 - dclear
                b1 = width -part1 - part2 - part3 - part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs12v1
                gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)
        elif h == "right":
                if g == "1":
                        #FOR DOORS
                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)
                elif g == "2":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)

                elif g == "3":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3-part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)

                elif g == "4":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)

                elif g == "5":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3-part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)

                elif g == "6":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3-sec4-sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3-sec4-sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4-sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4-sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3-sec4 -sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"top",h)



def partition6(a,b,c,d,e,f,g,h):

        part1 = int(config["section"+g+"_partition"]["part1"])
        part2 = int(config["section"+g+"_partition"]["part2"])
        part3 = int(config["section"+g+"_partition"]["part3"])
        part4 = int(config["section"+g+"_partition"]["part4"])
        part5 = int(config["section"+g+"_partition"]["part5"])

        ss7x = a.x
        ss9x = c.x
        ss1y = a.y
        ss2y = b.y

        hh1y = part1 -(hchannel/2)
        h1 = APoint(ss7x,hh1y)
        
        h2 =APoint(ss9x,hh1y)

        hh3y = hh1y + hchannel
        h3 = APoint(ss9x,hh3y)

        h4 = APoint(ss7x,hh3y)

        hh5y = hh1y + part2
        h5 = APoint(ss7x,hh5y)

        hh6y = hh5y + part3
        h6 = APoint(ss7x,hh6y)

        hh7y = hh6y + part4
        h7 = APoint(ss7x,hh7y)

        hh8y = hh7y + part5
        h8 = APoint(ss7x,hh8y)

        h3_1 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_1")
        h3_2 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_2")
        h3_3 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_3")
        h3_4 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_4")
        h3_5 = acad.doc.Blocks.Add(APoint(0), "h"+g+"_5")
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
        lineh13 = h3_4.addline(h1,h2);lineh13.move(h1,h7)
        lineh14 = h3_4.addline(h2,h3);lineh14.move(h1,h7)
        lineh15 = h3_4.addline(h3,h4);lineh15.move(h1,h7)
        lineh16 = h3_4.addline(h4,h1);lineh16.move(h1,h7)
        lineh17 = h3_5.addline(h1,h2);lineh17.move(h1,h8)
        lineh18 = h3_5.addline(h2,h3);lineh18.move(h1,h8)
        lineh19 = h3_5.addline(h3,h4);lineh19.move(h1,h8)
        lineh20 = h3_5.addline(h4,h1);lineh20.move(h1,h8)

        #for hchannel thickness
        hh101y = hh1y + thick
        h101 = APoint(ss7x,hh101y)

        h102 = APoint(ss9x,hh101y)

        hh104y = hh3y - thick
        h104 = APoint(ss7x,hh104y)

        h103 = APoint(ss9x,hh104y)

        lineh111 = h3_1.addline(h101,h102)
        lineh112 = h3_1.addline(h103,h104)
        lineh113 = h3_2.addline(h101,h102);lineh113.move(h1,h5)
        lineh114 = h3_2.addline(h103,h104);lineh114.move(h1,h5)
        lineh115 = h3_3.addline(h101,h102);lineh115.move(h1,h6)
        lineh116 = h3_3.addline(h103,h104);lineh116.move(h1,h6)
        lineh117 = h3_4.addline(h101,h102);lineh117.move(h1,h7)
        lineh118 = h3_4.addline(h103,h104);lineh118.move(h1,h7)
        lineh119 = h3_5.addline(h101,h102);lineh119.move(h1,h8)
        lineh120 = h3_5.addline(h103,h104);lineh120.move(h1,h8)

        acad.model.InsertBlock(APoint(0), "h"+g+"_1", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_2", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_3", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_4", 1, 1, 1, 0)
        acad.model.InsertBlock(APoint(0), "h"+g+"_5", 1, 1, 1, 0)

        #FOR CUTOUT IN V CHANNEL
        cs1x = ss7x + thick
        cs1v1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss7x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss7x,cs4y)

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
        cs11y = c7y + part4
        cs11 = APoint(cs1x,cs11y)
        cs12y = cs11y +hchannel
        cs12v1 = APoint(cs1x,cs12y)

        cs13y = cs11y + part5
        cs13 = APoint(cs1x,cs13y)
        cs14y = cs13y + hchannel
        cs14v1 = APoint(cs1x,cs14y)

        linecs1 = e.addline(a,cs1v1)
        linecs2 = e.addline(cs1v1,cs2)
        linecs3 = e.addline(cs2,cs3)
        linecs4 = e.addline(cs3,cs4)
        linecs5 = e.addline(cs4,cs5v1)
        linecs6 = e.addline(cs5v1,cs7)
        linecs8 = e.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = e.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = e.addline(cs4,cs5v1);linecs10.move(cs2,cs7)
        linecs11 = e.addline(cs8v1,cs9)
        linecs12 = e.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = e.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = e.addline(cs4,cs5v1);linecs14.move(cs2,cs9)
        linecs15 = e.addline(cs10v1,cs11)

        linecs16 = e.addline(cs2,cs3);linecs16.move(cs2,cs11)
        linecs17 = e.addline(cs3,cs4);linecs17.move(cs2,cs11)
        linecs18 = e.addline(cs4,cs5v1);linecs18.move(cs2,cs11)
        linecs19 = e.addline(cs12v1,cs13)
        linecs7 = e.addline(cs6,b)

        linecs20 = e.addline(cs2,cs3);linecs20.move(cs2,cs13)
        linecs21 = e.addline(cs3,cs4);linecs21.move(cs2,cs13)
        linecs22 = e.addline(cs4,cs5v1);linecs22.move(cs2,cs13)
        linecs23 = e.addline(cs14v1,cs6)

        #FOR CUTOUT IN V2 CHANNEL
        cs1x = ss9x - thick
        cs1 = APoint(cs1x,ss1y)
    
        cs2 = APoint(cs1x,hh1y)
     
        cs3 = APoint(ss9x,hh1y)
    
        cs4y = hh1y + hchannel
        cs4 = APoint(ss9x,cs4y)

        cs5 = APoint(cs1x,cs4y)

        cs6 = APoint(cs1x,ss2y)

        cs7 =APoint(cs1x,c5y)

        cs8 = APoint(cs1x,c6y)

        cs9 = APoint(cs1x,c7y)

        cs10 = APoint(cs1x,c8y)

        cs11 = APoint(cs1x,cs11y)

        cs12 = APoint(cs1x,cs12y)

        cs13 = APoint(cs1x,cs13y)

        cs14 = APoint(cs1x,cs14y)

        linecs1 = f.addline(c,cs1)
        linecs2 = f.addline(cs1,cs2)
        linecs3 = f.addline(cs2,cs3)
        linecs4 = f.addline(cs3,cs4)
        linecs5 = f.addline(cs4,cs5)
        linecs8 = f.addline(cs2,cs3);linecs8.move(cs2,cs7)
        linecs9 = f.addline(cs3,cs4);linecs9.move(cs2,cs7)
        linecs10 = f.addline(cs4,cs5);linecs10.move(cs2,cs7)
        linecs11 = f.addline(cs8,cs9)
        linecs12 = f.addline(cs2,cs3);linecs12.move(cs2,cs9)
        linecs13 = f.addline(cs3,cs4);linecs13.move(cs2,cs9)
        linecs14 = f.addline(cs4,cs5);linecs14.move(cs2,cs9)
        linecs15 = f.addline(cs10,cs11)

        linecs6 = f.addline(cs5,cs7)
        linecs7 = f.addline(cs6,d)
        linecs16 = f.addline(cs2,cs3);linecs16.move(cs2,cs11)
        linecs17 = f.addline(cs3,cs4);linecs17.move(cs2,cs11)
        linecs18 = f.addline(cs4,cs5);linecs18.move(cs2,cs11)
        linecs19 = f.addline(cs12,cs13)

        linecs20 = f.addline(cs2,cs3);linecs20.move(cs2,cs13)
        linecs21 = f.addline(cs3,cs4);linecs21.move(cs2,cs13)
        linecs22 = f.addline(cs4,cs5);linecs22.move(cs2,cs13)
        linecs23 = f.addline(cs14,cs6)

        

        if h == "left":
                sec1 = int(config["section"]["Sec_"+g])
                #FOR DOORS
                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part3 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part4 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs10v1
                gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = part5 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs12v1
                gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                a1 = sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                b1 = width -part1 - part2 - part3- part4-part5 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs14v1
                gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)

        elif h == "mid":
                sec1 = int(config["section"]["Sec_"+g])
                #FOR DOORS
                a1 = sec1 - dclear
                b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                c0 = APoint(dclearx,dcleary)
                c1 = c0 - thick
                d1 = a
                gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                a1 = sec1 - dclear
                b1 = part2 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs5v1
                gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                a1 = sec1 - dclear
                b1 = part3 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs8v1
                gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                a1 = sec1 - dclear
                b1 = part4 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs10v1
                gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                a1 = sec1 - dclear
                b1 = part5 - dclear
                c1 = APoint(dclearx,dclearmid)
                d1 = cs12v1
                gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                a1 = sec1 - dclear
                b1 = width -part1 - part2 - part3 - part4-part5 - (dclear/2) - (zchanneltb-dcleary) - thick
                c1 = APoint(dclearx,dclearmid)
                d1 = cs14v1
                gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)
        elif h == "right":
                if g == "1":
                        #FOR DOORS
                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = part5 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                        a1 = lenght - (zchannelside-dclearx) - thick - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 -part5- (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs14v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)
                elif g == "2":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part5 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                        a1 = lenght - sec1- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 -part5- (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs14v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)

                elif g == "3":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part5 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                        a1 = lenght - sec1- sec2 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3-part4-part5 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs14v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)

                elif g == "4":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part5 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4-part5 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs14v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)

                elif g == "5":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part5 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3-sec4 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3-part4-part5 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs14v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)

                elif g == "6":
                        sec1 = int(config["section"]["Sec_1"])
                        sec2 = int(config["section"]["Sec_2"])
                        sec3 = int(config["section"]["Sec_3"])
                        sec4 = int(config["section"]["Sec_4"])
                        sec5 = int(config["section"]["Sec_5"])
                        #FOR DOORS
                        a1 = lenght - sec1 - sec2 -sec3-sec4-sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part1 - (dclear/2) - (zchanneltb-dcleary) - thick
                        c0 = APoint(dclearx,dcleary)
                        c1 = c0 - thick
                        d1 = a
                        gidoores(a1,b1,c1,d1,"door"+g+"_1","sec"+g,e,f,cs1v1,"bot",h)

                        a1 = lenght - sec1- sec2- sec3-sec4-sec5 - (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part2 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs5v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_2","sec"+g,e,f,cs5v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4-sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part3 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs8v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_3","sec"+g,e,f,cs8v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4-sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part4 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs10v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_4","sec"+g,e,f,cs10v1,"mid",h)

                        a1 = lenght - sec1- sec2 -sec3-sec4-sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = part5 - dclear
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs12v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_5","sec"+g,e,f,cs12v1,"mid",h)

                        a1 = lenght - sec1- sec2 - sec3-sec4 -sec5- (dclear/2) - (zchannelside-dclearx) - thick
                        b1 = width -part1 - part2 - part3 - part4 -part5- (dclear/2) - (zchanneltb-dcleary) - thick
                        c1 = APoint(dclearx,dclearmid)
                        d1 = cs14v1
                        gidoores(a1,b1,c1,d1,"door"+g+"_6","sec"+g,e,f,cs14v1,"top",h)