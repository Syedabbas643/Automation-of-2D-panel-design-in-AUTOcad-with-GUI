from pyautocad import Autocad, APoint,aDouble
from configparser import ConfigParser
from math import pi

config = ConfigParser()
config.read('./INDOOR/gi_config_in.ini')

acad = Autocad()

acad.doc.purgeAll()

sthick = float(config["shell"]["sheet_thickness"])
clear = int(config["doors"]["door_to_door_clearence"])
thick = int(config["doors"]["door_thick"])
locknutclearx = int(config["doors"]["lock_clearence_X"])
locknutclear = int(config["doors"]["lock_clearence_Y"])
coverclearx = int(config["covers"]["cover_clearence_X"])
coverclear = int(config["covers"]["cover_clearence_Y"])
cthick = int(config["covers"]["cover_thick"])
inchclear = int(config["doors"]["Inches_clearence_Y"])
inchlen = float(config["doors"]["Inches_size_X"])
inchwid = float(config["doors"]["Inches_size_Y"])
vchannel = int(config["shell"]["Vertical_channel_size"])
hchannel = int(config["shell"]["Horizontal_channel_size"])
mpclearx = int(config["mounting_plate"]["mounting_plate_clearence_X"])
mpcleary = int(config["mounting_plate"]["mounting_plate_clearence_Y"])
mpclearbot = int(config["mounting_plate"]["mounting_plate_bottom_clearence"]) + sthick
mpcleartop = int(config["mounting_plate"]["mounting_plate_top_clearence"]) + sthick
zchanneltb = int(config["shell"]["Top_bottom_shell_size"])
zchannelside = int(config["shell"]["side_shell_size"])
dclearx = int(config["doors"]["door_clearence_X"])
dcleary = int(config["doors"]["door_clearence_Y"])
dclearmid = int(config["doors"]["door_clearence_MID"])
type =  config["shell"]["type_panel"]

def gidoores(a,b,c,d,e,f,g,h,i,j,l):
    sec = f
    dlenght = a 
    dwidth = b 
    check = config["covers"]["needcovers"]
    if sec in check:
        if dwidth >= 600:
            #FOR DOOR APOINTS
            dc = c

            dp = d

            d1 = APoint(0,0)

            d2 = APoint(dlenght)

            d3 = APoint(dlenght,dwidth)

            d4 = APoint(0,dwidth)
            #FOR DOOR THICKNESS

            d5 = d1 + cthick

            d6 = APoint((dlenght-thick),cthick)

            d7 = d3 - cthick

            d8 = APoint(cthick,(dwidth-cthick))

            string = e

            e = acad.doc.Blocks.Add(APoint(dc),string)

            cov1y = coverclear
            cov1 = APoint(coverclearx,cov1y)
            cov2y = dwidth - coverclear
            cov2 = APoint(coverclearx,cov2y)
            cov3x = dlenght - coverclearx
            cov3 = APoint(cov3x,cov2y)
            cov4 = APoint(cov3x,cov1y)
            cov5y = dwidth/2
            cov5 = APoint(coverclearx,cov5y)
            cov6 = APoint(cov3x,cov5y)

            cir1 = e.addcircle(d1,4);cir1.move(d1,cov1);cir1.color = 50
            cir2 = e.addcircle(d1,4);cir2.move(d1,cov2);cir2.color = 50
            cir3 = e.addcircle(d1,4);cir3.move(d1,cov3);cir3.color = 50
            cir4 = e.addcircle(d1,4);cir4.move(d1,cov4);cir4.color = 50
            cir5 = e.addcircle(d1,4);cir5.move(d1,cov5);cir5.color = 50
            cir6 = e.addcircle(d1,4);cir6.move(d1,cov6);cir6.color = 50

            #FOR cutout in left and right channel

            rec = aDouble(-4.5,-4.5,0,4.5,-4.5,0,4.5,4.5,0,-4.5,4.5,0,-4.5,-4.5,0)
            rec1 = g.addpolyline(rec);rec1.move(d1,cov1);rec1.move(dc,dp)
            rec2 = g.addpolyline(rec);rec2.move(d1,cov2);rec2.move(dc,dp)
            rec3 = h.addpolyline(rec);rec3.move(d1,cov3);rec3.move(dc,dp)
            rec4 = h.addpolyline(rec);rec4.move(d1,cov4);rec4.move(dc,dp)
            rec5 = g.addpolyline(rec);rec5.move(d1,cov5);rec5.move(dc,dp)
            rec6 = h.addpolyline(rec);rec6.move(d1,cov6);rec6.move(dc,dp)

            lined1 = e.addline(d1,d2);lined1.color = 10
            lined2 = e.addline(d2,d3);lined2.color = 10
            lined3 = e.addline(d3,d4);lined3.color = 10
            lined4 = e.addline(d4,d1);lined4.color = 10
            lined5 = e.addline(d5,d6);lined5.color = 10
            lined6 = e.addline(d6,d7);lined6.color = 10
            lined7 = e.addline(d7,d8);lined7.color = 10
            lined8 = e.addline(d8,d5);lined8.color = 10

            acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)


        elif dwidth >= 250:
            #FOR DOOR APOINTS
            dc = c

            dp = d

            d1 = APoint(0,0)

            d2 = APoint(dlenght)

            d3 = APoint(dlenght,dwidth)

            d4 = APoint(0,dwidth)
            #FOR DOOR THICKNESS

            d5 = d1 + cthick

            d6 = APoint((dlenght-cthick),cthick)

            d7 = d3 - cthick

            d8 = APoint(cthick,(dwidth-cthick))

            string = e

            e = acad.doc.Blocks.Add(APoint(dc),string)

            cov1y = coverclear
            cov1 = APoint(coverclearx,cov1y)
            cov2y = dwidth - coverclear
            cov2 = APoint(coverclearx,cov2y)
            cov3x = dlenght - coverclearx
            cov3 = APoint(cov3x,cov2y)
            cov4 = APoint(cov3x,cov1y)

            cir1 = e.addcircle(d1,4);cir1.move(d1,cov1);cir1.color = 50
            cir2 = e.addcircle(d1,4);cir2.move(d1,cov2);cir2.color = 50
            cir3 = e.addcircle(d1,4);cir3.move(d1,cov3);cir3.color = 50
            cir4 = e.addcircle(d1,4);cir4.move(d1,cov4);cir4.color = 50

            #FOR cutout in left and right channel

            rec = aDouble(-4.5,-4.5,0,4.5,-4.5,0,4.5,4.5,0,-4.5,4.5,0,-4.5,-4.5,0)
            rec1 = g.addpolyline(rec);rec1.move(d1,cov1);rec1.move(dc,dp)
            rec2 = g.addpolyline(rec);rec2.move(d1,cov2);rec2.move(dc,dp)
            rec3 = h.addpolyline(rec);rec3.move(d1,cov3);rec3.move(dc,dp)
            rec4 = h.addpolyline(rec);rec4.move(d1,cov4);rec4.move(dc,dp)
            

            lined1 = e.addline(d1,d2);lined1.color = 10
            lined2 = e.addline(d2,d3);lined2.color = 10
            lined3 = e.addline(d3,d4);lined3.color = 10
            lined4 = e.addline(d4,d1);lined4.color = 10
            lined5 = e.addline(d5,d6);lined5.color = 10
            lined6 = e.addline(d6,d7);lined6.color = 10
            lined7 = e.addline(d7,d8);lined7.color = 10
            lined8 = e.addline(d8,d5);lined8.color = 10

            acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

        else:
            #FOR DOOR APOINTS

            dc = c

            dp = d

            d1 = APoint(0,0)

            d2 = APoint(dlenght)

            d3 = APoint(dlenght,dwidth)

            d4 = APoint(0,dwidth)
            #FOR DOOR THICKNESS

            d5 = d1 + cthick

            d6 = APoint((dlenght-cthick),cthick)

            d7 = d3 - cthick

            d8 = APoint(cthick,(dwidth-cthick))

            string = e

            e = acad.doc.Blocks.Add(APoint(dc),string)

            cov1y = coverclear
            cov1 = APoint(coverclearx,cov1y)
            cov2y = dwidth - coverclear
            cov2 = APoint(coverclearx,cov2y)
            cov3x = dlenght - coverclearx
            cov3 = APoint(cov3x,cov2y)
            cov4 = APoint(cov3x,cov1y)

            cir1 = e.addcircle(d1,4);cir1.move(d1,cov1);cir1.color = 50
            cir2 = e.addcircle(d1,4);cir2.move(d1,cov2);cir2.color = 50
            cir3 = e.addcircle(d1,4);cir3.move(d1,cov3);cir3.color = 50
            cir4 = e.addcircle(d1,4);cir4.move(d1,cov4);cir4.color = 50

            #FOR cutout in left and right channel

            rec = aDouble(-4.5,-4.5,0,4.5,-4.5,0,4.5,4.5,0,-4.5,4.5,0,-4.5,-4.5,0)
            rec1 = g.addpolyline(rec);rec1.move(d1,cov1);rec1.move(dc,dp)
            rec2 = g.addpolyline(rec);rec2.move(d1,cov2);rec2.move(dc,dp)
            rec3 = h.addpolyline(rec);rec3.move(d1,cov3);rec3.move(dc,dp)
            rec4 = h.addpolyline(rec);rec4.move(d1,cov4);rec4.move(dc,dp)

            lined1 = e.addline(d1,d2);lined1.color = 10
            lined2 = e.addline(d2,d3);lined2.color = 10
            lined3 = e.addline(d3,d4);lined3.color = 10
            lined4 = e.addline(d4,d1);lined4.color = 10
            lined5 = e.addline(d5,d6);lined5.color = 10
            lined6 = e.addline(d6,d7);lined6.color = 10
            lined7 = e.addline(d7,d8);lined7.color = 10
            lined8 = e.addline(d8,d5);lined8.color = 10

            acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)


    else:                                      # FOR H TYPE PANEL
        if type == "h":
            inch = config["doors"]["inches"]
            if inch == "y":
                if dlenght >= 600:
                    #FOR DOOR APOINTS
                    dc = c

                    dp = d

                    d1 = APoint(0,0)

                    d2 = APoint(dlenght)

                    d3 = APoint(dlenght,dwidth)

                    d4 = APoint(0,dwidth)
                    #FOR DOOR THICKNESS

                    d5 = d1 + thick

                    d6 = APoint((dlenght-thick),thick)

                    d7 = d3 - thick

                    d8 = APoint(thick,(dwidth-thick))

                    string = e

                    e = acad.doc.Blocks.Add(APoint(dc),string)


                    lined1 = e.addline(d4,d3);lined1.color = 10
                    lined2 = e.addline(d2,d3);lined2.color = 10
                    lined3 = e.addline(d1,d4);lined3.color = 10
                    #lined4 = e.addline(d4,d1);lined4.color = 10
                    #lined5 = e.addline(d5,d6);lined5.color = 10
                    lined6 = e.addline(d6,d7);lined6.color = 10
                    lined7 = e.addline(d7,d8);lined7.color = 10
                    lined8 = e.addline(d8,d5);lined8.color = 10

                    #FOR LOCK NUT
                    p1 = APoint(-4,-4)
                    p2 =APoint(4,-4)
                    p3 =APoint(4,4)
                    p4 =APoint(-4,4)
                    p5 = APoint(4,-10)
                    p6 = APoint(-4,-10)
                    p7=APoint(10,-4)
                    p8 = APoint(10,4)
                    p9 = APoint(4,10)
                    p10=APoint(-4,10)
                    p11=APoint(-10,4)
                    p12=APoint(-10,-4)

                    lock1x = locknutclear
                    lock1y = dwidth - locknutclearx
                    lock1 = APoint(lock1x,lock1y)
                    lock2x = dlenght - locknutclear
                    lock2 = APoint(lock2x,lock1y)
                    lock3x = dlenght/2
                    lock3 = APoint(lock3x,lock1y)

                    cut1 = e.addline(p5,p6);cut1.color = 50
                    cut2 = e.addline(p7,p8);cut2.color = 50
                    cut3 = e.addline(p9,p10);cut3.color = 50
                    cut4 = e.addline(p11,p12);cut4.color = 50
                    cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                    cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                    cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                    cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50

                    cut9 = cut1.copy();cut9.move(d1,lock2)
                    cut10 = cut2.copy();cut10.move(d1,lock2)
                    cut11 = cut3.copy();cut11.move(d1,lock2)
                    cut12 = cut4.copy();cut12.move(d1,lock2)
                    cut13 = cut5.copy();cut13.move(d1,lock2)
                    cut14 = cut6.copy();cut14.move(d1,lock2)
                    cut15 = cut7.copy();cut15.move(d1,lock2)
                    cut16 = cut8.copy();cut16.move(d1,lock2)

                    cut17 = cut1.copy();cut17.move(d1,lock3)
                    cut18 = cut2.copy();cut18.move(d1,lock3)
                    cut19 = cut3.copy();cut19.move(d1,lock3)
                    cut20 = cut4.copy();cut20.move(d1,lock3)
                    cut21 = cut5.copy();cut21.move(d1,lock3)
                    cut22 = cut6.copy();cut22.move(d1,lock3)
                    cut23 = cut7.copy();cut23.move(d1,lock3)
                    cut24 = cut8.copy();cut24.move(d1,lock3)

                    cut1.move(d1,lock1)
                    cut2.move(d1,lock1)
                    cut3.move(d1,lock1)
                    cut4.move(d1,lock1)
                    cut5.move(d1,lock1)
                    cut6.move(d1,lock1)
                    cut7.move(d1,lock1)
                    cut8.move(d1,lock1)

                    acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                    #FOR INCHES
                    d9x = inchclear
                    d9 = APoint(d9x,0)
                    d10y = inchlen
                    d10 =APoint(d9x,d10y)
                    d11x = d9x + inchwid
                    d11 = APoint(d11x,d10y)
                    d12 = APoint(d11x,0)
                    d13x = dlenght - inchclear - inchwid
                    d13 = APoint(d13x,0)
                    d14x = dlenght - inchclear
                    d14 = APoint(d14x,0)

                    d15y = thick
                    d15 = APoint(d9x,d15y)
                    d16 = APoint(d11x,d15y)
                    d17 = APoint(d13x,d15y)
                    d18 = APoint(d14x,d15y)
                    

                    lined8 = e.addline(d1,d9);lined8.color = 10
                    lined9 = e.addline(d9,d10);lined9.color = 10
                    lined10 = e.addline(d10,d11);lined10.color = 10
                    lined11 = e.addline(d11,d12);lined11.color = 10
                    lined12 = e.addline(d12,d13);lined12.color = 10
                    lined13 = e.addline(d14,d2);lined13.color = 10
                    lined14 = e.addline(d1,d9);lined14.color = 10

                    lined15 = e.addline(d9,d10);lined15.move(d9,d13);lined15.color = 10
                    lined16 = e.addline(d10,d11);lined16.move(d9,d13);lined16.color = 10
                    lined17 = e.addline(d11,d12);lined17.move(d9,d13);lined17.color = 10
                    lined18 = e.addline(d5,d15);lined18.color = 10
                    lined19 = e.addline(d16,d17);lined19.color = 10
                    lined20 = e.addline(d18,d6);lined20.color = 10

                    #for holes in other channels
                    #holep = APoint(5.5,inchwid/2)
                    #hole1 = g.addcircle(holep,3.5);hole1.move(d1,d9);hole1.move(dc,dp)
                    #hole2 = g.addcircle(holep,3.5);hole2.move(d1,d13);hole2.move(dc,dp)


                elif dlenght >= 250:
                    #FOR DOOR APOINTS
                    dc = c

                    dp = d

                    d1 = APoint(0,0)

                    d2 = APoint(dlenght)

                    d3 = APoint(dlenght,dwidth)

                    d4 = APoint(0,dwidth)
                    #FOR DOOR THICKNESS

                    d5 = d1 + thick

                    d6 = APoint((dlenght-thick),thick)

                    d7 = d3 - thick

                    d8 = APoint(thick,(dwidth-thick))

                    string = e

                    e = acad.doc.Blocks.Add(APoint(dc),string)


                    lined1 = e.addline(d4,d3);lined1.color = 10
                    lined2 = e.addline(d2,d3);lined2.color = 10
                    lined3 = e.addline(d1,d4);lined3.color = 10
                    #lined4 = e.addline(d4,d1);lined4.color = 10
                    #lined5 = e.addline(d5,d6);lined5.color = 10
                    lined6 = e.addline(d6,d7);lined6.color = 10
                    lined7 = e.addline(d7,d8);lined7.color = 10
                    lined8 = e.addline(d8,d5);lined8.color = 10

                    #FOR LOCK NUT
                    p1 = APoint(-4,-4)
                    p2 =APoint(4,-4)
                    p3 =APoint(4,4)
                    p4 =APoint(-4,4)
                    p5 = APoint(4,-10)
                    p6 = APoint(-4,-10)
                    p7=APoint(10,-4)
                    p8 = APoint(10,4)
                    p9 = APoint(4,10)
                    p10=APoint(-4,10)
                    p11=APoint(-10,4)
                    p12=APoint(-10,-4)

                    lock1x = locknutclear
                    lock1y = dwidth - locknutclearx
                    lock1 = APoint(lock1x,lock1y)
                    lock2x = dlenght - locknutclear
                    lock2 = APoint(lock2x,lock1y)

                    cut1 = e.addline(p5,p6);cut1.color = 50
                    cut2 = e.addline(p7,p8);cut2.color = 50
                    cut3 = e.addline(p9,p10);cut3.color = 50
                    cut4 = e.addline(p11,p12);cut4.color = 50
                    cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                    cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                    cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                    cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                    cut9 = cut1.copy();cut9.move(d1,lock2)
                    cut10 = cut2.copy();cut10.move(d1,lock2)
                    cut11 = cut3.copy();cut11.move(d1,lock2)
                    cut12 = cut4.copy();cut12.move(d1,lock2)
                    cut13 = cut5.copy();cut13.move(d1,lock2)
                    cut14 = cut6.copy();cut14.move(d1,lock2)
                    cut15 = cut7.copy();cut15.move(d1,lock2)
                    cut16 = cut8.copy();cut16.move(d1,lock2)
                    cut1.move(d1,lock1)
                    cut2.move(d1,lock1)
                    cut3.move(d1,lock1)
                    cut4.move(d1,lock1)
                    cut5.move(d1,lock1)
                    cut6.move(d1,lock1)
                    cut7.move(d1,lock1)
                    cut8.move(d1,lock1)


                    acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                    #FOR INCHES
                    d9x = inchclear
                    d9 = APoint(d9x,0)
                    d10y = inchlen
                    d10 =APoint(d9x,d10y)
                    d11x = d9x + inchwid
                    d11 = APoint(d11x,d10y)
                    d12 = APoint(d11x,0)
                    d13x = dlenght - inchclear - inchwid
                    d13 = APoint(d13x,0)
                    d14x = dlenght - inchclear
                    d14 = APoint(d14x,0)

                    d15y = thick
                    d15 = APoint(d9x,d15y)
                    d16 = APoint(d11x,d15y)
                    d17 = APoint(d13x,d15y)
                    d18 = APoint(d14x,d15y)
                    

                    lined8 = e.addline(d1,d9);lined8.color = 10
                    lined9 = e.addline(d9,d10);lined9.color = 10
                    lined10 = e.addline(d10,d11);lined10.color = 10
                    lined11 = e.addline(d11,d12);lined11.color = 10
                    lined12 = e.addline(d12,d13);lined12.color = 10
                    lined13 = e.addline(d14,d2);lined13.color = 10
                    lined14 = e.addline(d1,d9);lined14.color = 10

                    lined15 = e.addline(d9,d10);lined15.move(d9,d13);lined15.color = 10
                    lined16 = e.addline(d10,d11);lined16.move(d9,d13);lined16.color = 10
                    lined17 = e.addline(d11,d12);lined17.move(d9,d13);lined17.color = 10
                    lined18 = e.addline(d5,d15);lined18.color = 10
                    lined19 = e.addline(d16,d17);lined19.color = 10
                    lined20 = e.addline(d18,d6);lined20.color = 10

                    #for holes in other channels
                    #holep = APoint(5.5,inchwid/2)
                    #hole1 = g.addcircle(holep,3.5);hole1.move(d1,d9);hole1.move(dc,dp)
                    #hole2 = g.addcircle(holep,3.5);hole2.move(d1,d13);hole2.move(dc,dp)

                else:
                    #FOR DOOR APOINTS

                    dc = c

                    dp = d

                    d1 = APoint(0,0)

                    d2 = APoint(dlenght)

                    d3 = APoint(dlenght,dwidth)

                    d4 = APoint(0,dwidth)
                    #FOR DOOR THICKNESS

                    d5 = d1 + thick

                    d6 = APoint((dlenght-thick),thick)

                    d7 = d3 - thick

                    d8 = APoint(thick,(dwidth-thick))

                    string = e

                    e = acad.doc.Blocks.Add(APoint(dc),string)

                    lined1 = e.addline(d4,d3);lined1.color = 10
                    lined2 = e.addline(d2,d3);lined2.color = 10
                    lined3 = e.addline(d1,d4);lined3.color = 10
                    #lined4 = e.addline(d4,d1);lined4.color = 10
                    #lined5 = e.addline(d5,d6);lined5.color = 10
                    lined6 = e.addline(d6,d7);lined6.color = 10
                    lined7 = e.addline(d7,d8);lined7.color = 10
                    lined8 = e.addline(d8,d5);lined8.color = 10

                    #FOR LOCK NUT
                    p1 = APoint(-4,-4)
                    p2 =APoint(4,-4)
                    p3 =APoint(4,4)
                    p4 =APoint(-4,4)
                    p5 = APoint(4,-10)
                    p6 = APoint(-4,-10)
                    p7=APoint(10,-4)
                    p8 = APoint(10,4)
                    p9 = APoint(4,10)
                    p10=APoint(-4,10)
                    p11=APoint(-10,4)
                    p12=APoint(-10,-4)

                    lock1x = dlenght/2
                    lock1y = dwidth - locknutclearx
                    lock1 = APoint(lock1x,lock1y)

                    cut1 = e.addline(p5,p6);cut1.color = 50
                    cut2 = e.addline(p7,p8);cut2.color = 50
                    cut3 = e.addline(p9,p10);cut3.color = 50
                    cut4 = e.addline(p11,p12);cut4.color = 50
                    cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                    cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                    cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                    cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                    cut1.move(d1,lock1)
                    cut2.move(d1,lock1)
                    cut3.move(d1,lock1)
                    cut4.move(d1,lock1)
                    cut5.move(d1,lock1)
                    cut6.move(d1,lock1)
                    cut7.move(d1,lock1)
                    cut8.move(d1,lock1)

                    acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                    #FOR INCHES
                    d9x = inchclear
                    d9 = APoint(d9x,0)
                    d10y = inchlen
                    d10 =APoint(d9x,d10y)
                    d11x = d9x + inchwid
                    d11 = APoint(d11x,d10y)
                    d12 = APoint(d11x,0)
                    d13x = dlenght - inchclear - inchwid
                    d13 = APoint(d13x,0)
                    d14x = dlenght - inchclear
                    d14 = APoint(d14x,0)

                    d15y = thick
                    d15 = APoint(d9x,d15y)
                    d16 = APoint(d11x,d15y)
                    d17 = APoint(d13x,d15y)
                    d18 = APoint(d14x,d15y)
                    
                    lined8 = e.addline(d1,d9);lined8.color = 10
                    lined9 = e.addline(d9,d10);lined9.color = 10
                    lined10 = e.addline(d10,d11);lined10.color = 10
                    lined11 = e.addline(d11,d12);lined11.color = 10
                    lined12 = e.addline(d12,d13);lined12.color = 10
                    lined13 = e.addline(d14,d2);lined13.color = 10
                    lined14 = e.addline(d1,d9);lined14.color = 10

                    lined15 = e.addline(d9,d10);lined15.move(d9,d13);lined15.color = 10
                    lined16 = e.addline(d10,d11);lined16.move(d9,d13);lined16.color = 10
                    lined17 = e.addline(d11,d12);lined17.move(d9,d13);lined17.color = 10
                    lined18 = e.addline(d5,d15);lined18.color = 10
                    lined19 = e.addline(d16,d17);lined19.color = 10
                    lined20 = e.addline(d18,d6);lined20.color = 10

                    #for holes in other channels
                    #holep = APoint(5.5,inchwid/2)
                    #hole1 = g.addcircle(holep,3.5);hole1.move(d1,d9);hole1.move(dc,dp)
                    #hole2 = g.addcircle(holep,3.5);hole2.move(d1,d13);hole2.move(dc,dp)

            else:
                    if dlenght >= 600:
                        #FOR DOOR APOINTS
                        dc = c

                        dp = d

                        d1 = APoint(0,0)

                        d2 = APoint(dlenght)

                        d3 = APoint(dlenght,dwidth)

                        d4 = APoint(0,dwidth)
                        #FOR DOOR THICKNESS

                        d5 = d1 + thick

                        d6 = APoint((dlenght-thick),thick)

                        d7 = d3 - thick

                        d8 = APoint(thick,(dwidth-thick))

                        string = e

                        e = acad.doc.Blocks.Add(APoint(dc),string)


                        lined1 = e.addline(d1,d2);lined1.color = 10
                        lined2 = e.addline(d2,d3);lined2.color = 10
                        lined3 = e.addline(d3,d4);lined3.color = 10
                        lined4 = e.addline(d4,d1);lined4.color = 10
                        lined5 = e.addline(d5,d6);lined5.color = 10
                        lined6 = e.addline(d6,d7);lined6.color = 10
                        lined7 = e.addline(d7,d8);lined7.color = 10
                        lined8 = e.addline(d8,d5);lined8.color = 10

                        #FOR LOCK NUT
                        p1 = APoint(-4,-4)
                        p2 =APoint(4,-4)
                        p3 =APoint(4,4)
                        p4 =APoint(-4,4)
                        p5 = APoint(4,-10)
                        p6 = APoint(-4,-10)
                        p7=APoint(10,-4)
                        p8 = APoint(10,4)
                        p9 = APoint(4,10)
                        p10=APoint(-4,10)
                        p11=APoint(-10,4)
                        p12=APoint(-10,-4)

                        lock1x = locknutclear
                        lock1y = dwidth - locknutclearx
                        lock1 = APoint(lock1x,lock1y)
                        lock2x = dlenght - locknutclear
                        lock2 = APoint(lock2x,lock1y)
                        lock3x = dlenght/2
                        lock3 = APoint(lock3x,lock1y)

                        cut1 = e.addline(p5,p6);cut1.color = 50
                        cut2 = e.addline(p7,p8);cut2.color = 50
                        cut3 = e.addline(p9,p10);cut3.color = 50
                        cut4 = e.addline(p11,p12);cut4.color = 50
                        cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                        cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                        cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                        cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50

                        cut9 = cut1.copy();cut9.move(d1,lock2)
                        cut10 = cut2.copy();cut10.move(d1,lock2)
                        cut11 = cut3.copy();cut11.move(d1,lock2)
                        cut12 = cut4.copy();cut12.move(d1,lock2)
                        cut13 = cut5.copy();cut13.move(d1,lock2)
                        cut14 = cut6.copy();cut14.move(d1,lock2)
                        cut15 = cut7.copy();cut15.move(d1,lock2)
                        cut16 = cut8.copy();cut16.move(d1,lock2)

                        cut17 = cut1.copy();cut17.move(d1,lock3)
                        cut18 = cut2.copy();cut18.move(d1,lock3)
                        cut19 = cut3.copy();cut19.move(d1,lock3)
                        cut20 = cut4.copy();cut20.move(d1,lock3)
                        cut21 = cut5.copy();cut21.move(d1,lock3)
                        cut22 = cut6.copy();cut22.move(d1,lock3)
                        cut23 = cut7.copy();cut23.move(d1,lock3)
                        cut24 = cut8.copy();cut24.move(d1,lock3)

                        cut1.move(d1,lock1)
                        cut2.move(d1,lock1)
                        cut3.move(d1,lock1)
                        cut4.move(d1,lock1)
                        cut5.move(d1,lock1)
                        cut6.move(d1,lock1)
                        cut7.move(d1,lock1)
                        cut8.move(d1,lock1)

                        acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                        

                    elif dlenght >= 250:
                        #FOR DOOR APOINTS
                        dc = c

                        dp = d

                        d1 = APoint(0,0)

                        d2 = APoint(dlenght)

                        d3 = APoint(dlenght,dwidth)

                        d4 = APoint(0,dwidth)
                        #FOR DOOR THICKNESS

                        d5 = d1 + thick

                        d6 = APoint((dlenght-thick),thick)

                        d7 = d3 - thick

                        d8 = APoint(thick,(dwidth-thick))

                        string = e

                        e = acad.doc.Blocks.Add(APoint(dc),string)


                        lined1 = e.addline(d1,d2);lined1.color = 10
                        lined2 = e.addline(d2,d3);lined2.color = 10
                        lined3 = e.addline(d3,d4);lined3.color = 10
                        lined4 = e.addline(d4,d1);lined4.color = 10
                        lined5 = e.addline(d5,d6);lined5.color = 10
                        lined6 = e.addline(d6,d7);lined6.color = 10
                        lined7 = e.addline(d7,d8);lined7.color = 10
                        lined8 = e.addline(d8,d5);lined8.color = 10

                        #FOR LOCK NUT
                        p1 = APoint(-4,-4)
                        p2 =APoint(4,-4)
                        p3 =APoint(4,4)
                        p4 =APoint(-4,4)
                        p5 = APoint(4,-10)
                        p6 = APoint(-4,-10)
                        p7=APoint(10,-4)
                        p8 = APoint(10,4)
                        p9 = APoint(4,10)
                        p10=APoint(-4,10)
                        p11=APoint(-10,4)
                        p12=APoint(-10,-4)

                        lock1x = locknutclear
                        lock1y = dwidth - locknutclearx
                        lock1 = APoint(lock1x,lock1y)
                        lock2x = dlenght - locknutclear
                        lock2 = APoint(lock2x,lock1y)

                        cut1 = e.addline(p5,p6);cut1.color = 50
                        cut2 = e.addline(p7,p8);cut2.color = 50
                        cut3 = e.addline(p9,p10);cut3.color = 50
                        cut4 = e.addline(p11,p12);cut4.color = 50
                        cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                        cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                        cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                        cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                        cut9 = cut1.copy();cut9.move(d1,lock2)
                        cut10 = cut2.copy();cut10.move(d1,lock2)
                        cut11 = cut3.copy();cut11.move(d1,lock2)
                        cut12 = cut4.copy();cut12.move(d1,lock2)
                        cut13 = cut5.copy();cut13.move(d1,lock2)
                        cut14 = cut6.copy();cut14.move(d1,lock2)
                        cut15 = cut7.copy();cut15.move(d1,lock2)
                        cut16 = cut8.copy();cut16.move(d1,lock2)
                        cut1.move(d1,lock1)
                        cut2.move(d1,lock1)
                        cut3.move(d1,lock1)
                        cut4.move(d1,lock1)
                        cut5.move(d1,lock1)
                        cut6.move(d1,lock1)
                        cut7.move(d1,lock1)
                        cut8.move(d1,lock1)


                        acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                        

                    else:
                        #FOR DOOR APOINTS

                        dc = c

                        dp = d

                        d1 = APoint(0,0)

                        d2 = APoint(dlenght)

                        d3 = APoint(dlenght,dwidth)

                        d4 = APoint(0,dwidth)
                        #FOR DOOR THICKNESS

                        d5 = d1 + thick

                        d6 = APoint((dlenght-thick),thick)

                        d7 = d3 - thick

                        d8 = APoint(thick,(dwidth-thick))

                        string = e

                        e = acad.doc.Blocks.Add(APoint(dc),string)

                        lined1 = e.addline(d1,d2);lined1.color = 10
                        lined2 = e.addline(d2,d3);lined2.color = 10
                        lined3 = e.addline(d3,d4);lined3.color = 10
                        lined4 = e.addline(d4,d1);lined4.color = 10
                        lined5 = e.addline(d5,d6);lined5.color = 10
                        lined6 = e.addline(d6,d7);lined6.color = 10
                        lined7 = e.addline(d7,d8);lined7.color = 10
                        lined8 = e.addline(d8,d5);lined8.color = 10

                        #FOR LOCK NUT
                        p1 = APoint(-4,-4)
                        p2 =APoint(4,-4)
                        p3 =APoint(4,4)
                        p4 =APoint(-4,4)
                        p5 = APoint(4,-10)
                        p6 = APoint(-4,-10)
                        p7=APoint(10,-4)
                        p8 = APoint(10,4)
                        p9 = APoint(4,10)
                        p10=APoint(-4,10)
                        p11=APoint(-10,4)
                        p12=APoint(-10,-4)

                        lock1x = dlenght/2
                        lock1y = dwidth - locknutclearx
                        lock1 = APoint(lock1x,lock1y)

                        cut1 = e.addline(p5,p6);cut1.color = 50
                        cut2 = e.addline(p7,p8);cut2.color = 50
                        cut3 = e.addline(p9,p10);cut3.color = 50
                        cut4 = e.addline(p11,p12);cut4.color = 50
                        cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                        cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                        cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                        cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                        cut1.move(d1,lock1)
                        cut2.move(d1,lock1)
                        cut3.move(d1,lock1)
                        cut4.move(d1,lock1)
                        cut5.move(d1,lock1)
                        cut6.move(d1,lock1)
                        cut7.move(d1,lock1)
                        cut8.move(d1,lock1)

                        acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)
        elif type == 'v':
            inch = config["doors"]["inches"]
            if inch == "y":
                if dwidth >= 600:
                    #FOR DOOR APOINTS
                    dc = c

                    dp = d

                    d1 = APoint(0,0)

                    d2 = APoint(dlenght)

                    d3 = APoint(dlenght,dwidth)

                    d4 = APoint(0,dwidth)
                    #FOR DOOR THICKNESS

                    d5 = d1 + thick

                    d6 = APoint((dlenght-thick),thick)

                    d7 = d3 - thick

                    d8 = APoint(thick,(dwidth-thick))

                    string = e

                    e = acad.doc.Blocks.Add(APoint(dc),string)


                    lined1 = e.addline(d1,d2);lined1.color = 10
                    lined2 = e.addline(d2,d3);lined2.color = 10
                    lined3 = e.addline(d3,d4);lined3.color = 10
                    #lined4 = e.addline(d4,d1);lined4.color = 10
                    lined5 = e.addline(d5,d6);lined5.color = 10
                    lined6 = e.addline(d6,d7);lined6.color = 10
                    lined7 = e.addline(d7,d8);lined7.color = 10
                    #lined8 = e.addline(d8,d5);lined8.color = 10

                    #FOR LOCK NUT
                    p1 = APoint(-4,-4)
                    p2 =APoint(4,-4)
                    p3 =APoint(4,4)
                    p4 =APoint(-4,4)
                    p5 = APoint(4,-10)
                    p6 = APoint(-4,-10)
                    p7=APoint(10,-4)
                    p8 = APoint(10,4)
                    p9 = APoint(4,10)
                    p10=APoint(-4,10)
                    p11=APoint(-10,4)
                    p12=APoint(-10,-4)

                    lock1x = dlenght - locknutclearx
                    lock1y = dwidth - locknutclear
                    lock1 = APoint(lock1x,lock1y)
                    lock2y = locknutclear
                    lock2 = APoint(lock1x,lock2y)
                    lock3y = dwidth/2
                    lock3 = APoint(lock1x,lock3y)

                    cut1 = e.addline(p5,p6);cut1.color = 50
                    cut2 = e.addline(p7,p8);cut2.color = 50
                    cut3 = e.addline(p9,p10);cut3.color = 50
                    cut4 = e.addline(p11,p12);cut4.color = 50
                    cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                    cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                    cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                    cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50

                    cut9 = cut1.copy();cut9.move(d1,lock2)
                    cut10 = cut2.copy();cut10.move(d1,lock2)
                    cut11 = cut3.copy();cut11.move(d1,lock2)
                    cut12 = cut4.copy();cut12.move(d1,lock2)
                    cut13 = cut5.copy();cut13.move(d1,lock2)
                    cut14 = cut6.copy();cut14.move(d1,lock2)
                    cut15 = cut7.copy();cut15.move(d1,lock2)
                    cut16 = cut8.copy();cut16.move(d1,lock2)

                    cut17 = cut1.copy();cut17.move(d1,lock3)
                    cut18 = cut2.copy();cut18.move(d1,lock3)
                    cut19 = cut3.copy();cut19.move(d1,lock3)
                    cut20 = cut4.copy();cut20.move(d1,lock3)
                    cut21 = cut5.copy();cut21.move(d1,lock3)
                    cut22 = cut6.copy();cut22.move(d1,lock3)
                    cut23 = cut7.copy();cut23.move(d1,lock3)
                    cut24 = cut8.copy();cut24.move(d1,lock3)

                    cut1.move(d1,lock1)
                    cut2.move(d1,lock1)
                    cut3.move(d1,lock1)
                    cut4.move(d1,lock1)
                    cut5.move(d1,lock1)
                    cut6.move(d1,lock1)
                    cut7.move(d1,lock1)
                    cut8.move(d1,lock1)

                    acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                    #FOR INCHES
                    d9y = inchclear
                    d9 = APoint(0,d9y)
                    d10x = inchlen
                    d10 =APoint(d10x,d9y)
                    d11y = d9y + inchwid
                    d11 = APoint(d10x,d11y)
                    d12 = APoint(0,d11y)
                    d13y = dwidth - inchclear - inchwid
                    d13 = APoint(0,d13y)
                    d14y = dwidth - inchclear
                    d14 = APoint(0,d14y)

                    d15x = thick
                    d15 = APoint(d15x,d9y)
                    d16 = APoint(d15x,d11y)
                    d17 = APoint(d15x,d13y)
                    d18 = APoint(d15x,d14y)
                    

                    lined8 = e.addline(d1,d9);lined8.color = 10
                    lined9 = e.addline(d9,d10);lined9.color = 10
                    lined10 = e.addline(d10,d11);lined10.color = 10
                    lined11 = e.addline(d11,d12);lined11.color = 10
                    lined12 = e.addline(d12,d13);lined12.color = 10
                    lined13 = e.addline(d14,d4);lined13.color = 10
                    lined14 = e.addline(d1,d9);lined14.color = 10

                    lined15 = e.addline(d9,d10);lined15.move(d9,d13);lined15.color = 10
                    lined16 = e.addline(d10,d11);lined16.move(d9,d13);lined16.color = 10
                    lined17 = e.addline(d11,d12);lined17.move(d9,d13);lined17.color = 10
                    lined18 = e.addline(d5,d15);lined18.color = 10
                    lined19 = e.addline(d16,d17);lined19.color = 10
                    lined20 = e.addline(d18,d8);lined20.color = 10

                    #for holes in other channels
                    holep = APoint(5.5,inchwid/2)
                    hole1 = g.addcircle(holep,3.5);hole1.move(d1,d9);hole1.move(dc,dp)
                    hole2 = g.addcircle(holep,3.5);hole2.move(d1,d13);hole2.move(dc,dp)


                elif dwidth >= 250:
                    #FOR DOOR APOINTS
                    dc = c

                    dp = d

                    d1 = APoint(0,0)

                    d2 = APoint(dlenght)

                    d3 = APoint(dlenght,dwidth)

                    d4 = APoint(0,dwidth)
                    #FOR DOOR THICKNESS

                    d5 = d1 + thick

                    d6 = APoint((dlenght-thick),thick)

                    d7 = d3 - thick

                    d8 = APoint(thick,(dwidth-thick))

                    string = e

                    e = acad.doc.Blocks.Add(APoint(dc),string)


                    lined1 = e.addline(d1,d2);lined1.color = 10
                    lined2 = e.addline(d2,d3);lined2.color = 10
                    lined3 = e.addline(d3,d4);lined3.color = 10
                    #lined4 = e.addline(d4,d1);lined4.color = 10
                    lined5 = e.addline(d5,d6);lined5.color = 10
                    lined6 = e.addline(d6,d7);lined6.color = 10
                    lined7 = e.addline(d7,d8);lined7.color = 10
                    #lined8 = e.addline(d8,d5);lined8.color = 10

                    #FOR LOCK NUT
                    p1 = APoint(-4,-4)
                    p2 =APoint(4,-4)
                    p3 =APoint(4,4)
                    p4 =APoint(-4,4)
                    p5 = APoint(4,-10)
                    p6 = APoint(-4,-10)
                    p7=APoint(10,-4)
                    p8 = APoint(10,4)
                    p9 = APoint(4,10)
                    p10=APoint(-4,10)
                    p11=APoint(-10,4)
                    p12=APoint(-10,-4)

                    lock1x = dlenght - locknutclearx
                    lock1y = dwidth- locknutclear
                    lock1 = APoint(lock1x,lock1y)
                    lock2y = locknutclear
                    lock2 = APoint(lock1x,lock2y)

                    cut1 = e.addline(p5,p6);cut1.color = 50
                    cut2 = e.addline(p7,p8);cut2.color = 50
                    cut3 = e.addline(p9,p10);cut3.color = 50
                    cut4 = e.addline(p11,p12);cut4.color = 50
                    cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                    cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                    cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                    cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                    cut9 = cut1.copy();cut9.move(d1,lock2)
                    cut10 = cut2.copy();cut10.move(d1,lock2)
                    cut11 = cut3.copy();cut11.move(d1,lock2)
                    cut12 = cut4.copy();cut12.move(d1,lock2)
                    cut13 = cut5.copy();cut13.move(d1,lock2)
                    cut14 = cut6.copy();cut14.move(d1,lock2)
                    cut15 = cut7.copy();cut15.move(d1,lock2)
                    cut16 = cut8.copy();cut16.move(d1,lock2)
                    cut1.move(d1,lock1)
                    cut2.move(d1,lock1)
                    cut3.move(d1,lock1)
                    cut4.move(d1,lock1)
                    cut5.move(d1,lock1)
                    cut6.move(d1,lock1)
                    cut7.move(d1,lock1)
                    cut8.move(d1,lock1)


                    acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                    #FOR INCHES
                    d9y = inchclear
                    d9 = APoint(0,d9y)
                    d10x = inchlen
                    d10 =APoint(d10x,d9y)
                    d11y = d9y + inchwid
                    d11 = APoint(d10x,d11y)
                    d12 = APoint(0,d11y)
                    d13y = dwidth - inchclear - inchwid
                    d13 = APoint(0,d13y)
                    d14y = dwidth - inchclear
                    d14 = APoint(0,d14y)

                    d15x = thick
                    d15 = APoint(d15x,d9y)
                    d16 = APoint(d15x,d11y)
                    d17 = APoint(d15x,d13y)
                    d18 = APoint(d15x,d14y)
                    

                    lined8 = e.addline(d1,d9);lined8.color = 10
                    lined9 = e.addline(d9,d10);lined9.color = 10
                    lined10 = e.addline(d10,d11);lined10.color = 10
                    lined11 = e.addline(d11,d12);lined11.color = 10
                    lined12 = e.addline(d12,d13);lined12.color = 10
                    lined13 = e.addline(d14,d4);lined13.color = 10
                    lined14 = e.addline(d1,d9);lined14.color = 10

                    lined15 = e.addline(d9,d10);lined15.move(d9,d13);lined15.color = 10
                    lined16 = e.addline(d10,d11);lined16.move(d9,d13);lined16.color = 10
                    lined17 = e.addline(d11,d12);lined17.move(d9,d13);lined17.color = 10
                    lined18 = e.addline(d5,d15);lined18.color = 10
                    lined19 = e.addline(d16,d17);lined19.color = 10
                    lined20 = e.addline(d18,d8);lined20.color = 10

                    #for holes in other channels
                    holep = APoint(5.5,inchwid/2)
                    hole1 = g.addcircle(holep,3.5);hole1.move(d1,d9);hole1.move(dc,dp)
                    hole2 = g.addcircle(holep,3.5);hole2.move(d1,d13);hole2.move(dc,dp)

                else:
                    #FOR DOOR APOINTS

                    dc = c

                    dp = d

                    d1 = APoint(0,0)

                    d2 = APoint(dlenght)

                    d3 = APoint(dlenght,dwidth)

                    d4 = APoint(0,dwidth)
                    #FOR DOOR THICKNESS

                    d5 = d1 + thick

                    d6 = APoint((dlenght-thick),thick)

                    d7 = d3 - thick

                    d8 = APoint(thick,(dwidth-thick))

                    string = e

                    e = acad.doc.Blocks.Add(APoint(dc),string)

                    lined1 = e.addline(d1,d2);lined1.color = 10
                    lined2 = e.addline(d2,d3);lined2.color = 10
                    lined3 = e.addline(d3,d4);lined3.color = 10
                    #lined4 = e.addline(d4,d1);lined4.color = 10
                    lined5 = e.addline(d5,d6);lined5.color = 10
                    lined6 = e.addline(d6,d7);lined6.color = 10
                    lined7 = e.addline(d7,d8);lined7.color = 10
                    #lined8 = e.addline(d8,d5);lined8.color = 10

                    #FOR LOCK NUT
                    p1 = APoint(-4,-4)
                    p2 =APoint(4,-4)
                    p3 =APoint(4,4)
                    p4 =APoint(-4,4)
                    p5 = APoint(4,-10)
                    p6 = APoint(-4,-10)
                    p7=APoint(10,-4)
                    p8 = APoint(10,4)
                    p9 = APoint(4,10)
                    p10=APoint(-4,10)
                    p11=APoint(-10,4)
                    p12=APoint(-10,-4)

                    lock1x = dlenght - locknutclearx
                    lock1y = dwidth/2
                    lock1 = APoint(lock1x,lock1y)

                    cut1 = e.addline(p5,p6);cut1.color = 50
                    cut2 = e.addline(p7,p8);cut2.color = 50
                    cut3 = e.addline(p9,p10);cut3.color = 50
                    cut4 = e.addline(p11,p12);cut4.color = 50
                    cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                    cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                    cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                    cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                    cut1.move(d1,lock1)
                    cut2.move(d1,lock1)
                    cut3.move(d1,lock1)
                    cut4.move(d1,lock1)
                    cut5.move(d1,lock1)
                    cut6.move(d1,lock1)
                    cut7.move(d1,lock1)
                    cut8.move(d1,lock1)

                    acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                    #FOR INCHES
                    d9y = inchclear
                    d9 = APoint(0,d9y)
                    d10x = inchlen
                    d10 =APoint(d10x,d9y)
                    d11y = d9y + inchwid
                    d11 = APoint(d10x,d11y)
                    d12 = APoint(0,d11y)
                    d13y = dwidth - inchclear - inchwid
                    d13 = APoint(0,d13y)
                    d14y = dwidth - inchclear
                    d14 = APoint(0,d14y)

                    d15x = thick
                    d15 = APoint(d15x,d9y)
                    d16 = APoint(d15x,d11y)
                    d17 = APoint(d15x,d13y)
                    d18 = APoint(d15x,d14y)
                    
                    lined8 = e.addline(d1,d9);lined8.color = 10
                    lined9 = e.addline(d9,d10);lined9.color = 10
                    lined10 = e.addline(d10,d11);lined10.color = 10
                    lined11 = e.addline(d11,d12);lined11.color = 10
                    lined12 = e.addline(d12,d13);lined12.color = 10
                    lined13 = e.addline(d14,d4);lined13.color = 10
                    lined14 = e.addline(d1,d9);lined14.color = 10

                    lined15 = e.addline(d9,d10);lined15.move(d9,d13);lined15.color = 10
                    lined16 = e.addline(d10,d11);lined16.move(d9,d13);lined16.color = 10
                    lined17 = e.addline(d11,d12);lined17.move(d9,d13);lined17.color = 10
                    lined18 = e.addline(d5,d15);lined18.color = 10
                    lined19 = e.addline(d16,d17);lined19.color = 10
                    lined20 = e.addline(d18,d8);lined20.color = 10

                    #for holes in other channels
                    holep = APoint(5.5,inchwid/2)
                    hole1 = g.addcircle(holep,3.5);hole1.move(d1,d9);hole1.move(dc,dp)
                    hole2 = g.addcircle(holep,3.5);hole2.move(d1,d13);hole2.move(dc,dp)

            else:
                    if dwidth >= 600:
                        #FOR DOOR APOINTS
                        dc = c

                        dp = d

                        d1 = APoint(0,0)

                        d2 = APoint(dlenght)

                        d3 = APoint(dlenght,dwidth)

                        d4 = APoint(0,dwidth)
                        #FOR DOOR THICKNESS

                        d5 = d1 + thick

                        d6 = APoint((dlenght-thick),thick)

                        d7 = d3 - thick

                        d8 = APoint(thick,(dwidth-thick))

                        string = e

                        e = acad.doc.Blocks.Add(APoint(dc),string)


                        lined1 = e.addline(d1,d2);lined1.color = 10
                        lined2 = e.addline(d2,d3);lined2.color = 10
                        lined3 = e.addline(d3,d4);lined3.color = 10
                        lined4 = e.addline(d4,d1);lined4.color = 10
                        lined5 = e.addline(d5,d6);lined5.color = 10
                        lined6 = e.addline(d6,d7);lined6.color = 10
                        lined7 = e.addline(d7,d8);lined7.color = 10
                        lined8 = e.addline(d8,d5);lined8.color = 10

                        #FOR LOCK NUT
                        p1 = APoint(-4,-4)
                        p2 =APoint(4,-4)
                        p3 =APoint(4,4)
                        p4 =APoint(-4,4)
                        p5 = APoint(4,-10)
                        p6 = APoint(-4,-10)
                        p7=APoint(10,-4)
                        p8 = APoint(10,4)
                        p9 = APoint(4,10)
                        p10=APoint(-4,10)
                        p11=APoint(-10,4)
                        p12=APoint(-10,-4)

                        lock1x = dlenght - locknutclearx
                        lock1y = dwidth - locknutclear
                        lock1 = APoint(lock1x,lock1y)
                        lock2y = locknutclear
                        lock2 = APoint(lock1x,lock2y)
                        lock3y = dwidth/2
                        lock3 = APoint(lock1x,lock3y)

                        cut1 = e.addline(p5,p6);cut1.color = 50
                        cut2 = e.addline(p7,p8);cut2.color = 50
                        cut3 = e.addline(p9,p10);cut3.color = 50
                        cut4 = e.addline(p11,p12);cut4.color = 50
                        cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                        cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                        cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                        cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50

                        cut9 = cut1.copy();cut9.move(d1,lock2)
                        cut10 = cut2.copy();cut10.move(d1,lock2)
                        cut11 = cut3.copy();cut11.move(d1,lock2)
                        cut12 = cut4.copy();cut12.move(d1,lock2)
                        cut13 = cut5.copy();cut13.move(d1,lock2)
                        cut14 = cut6.copy();cut14.move(d1,lock2)
                        cut15 = cut7.copy();cut15.move(d1,lock2)
                        cut16 = cut8.copy();cut16.move(d1,lock2)

                        cut17 = cut1.copy();cut17.move(d1,lock3)
                        cut18 = cut2.copy();cut18.move(d1,lock3)
                        cut19 = cut3.copy();cut19.move(d1,lock3)
                        cut20 = cut4.copy();cut20.move(d1,lock3)
                        cut21 = cut5.copy();cut21.move(d1,lock3)
                        cut22 = cut6.copy();cut22.move(d1,lock3)
                        cut23 = cut7.copy();cut23.move(d1,lock3)
                        cut24 = cut8.copy();cut24.move(d1,lock3)

                        cut1.move(d1,lock1)
                        cut2.move(d1,lock1)
                        cut3.move(d1,lock1)
                        cut4.move(d1,lock1)
                        cut5.move(d1,lock1)
                        cut6.move(d1,lock1)
                        cut7.move(d1,lock1)
                        cut8.move(d1,lock1)

                        acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                        

                    elif dwidth >= 250:
                        #FOR DOOR APOINTS
                        dc = c

                        dp = d

                        d1 = APoint(0,0)

                        d2 = APoint(dlenght)

                        d3 = APoint(dlenght,dwidth)

                        d4 = APoint(0,dwidth)
                        #FOR DOOR THICKNESS

                        d5 = d1 + thick

                        d6 = APoint((dlenght-thick),thick)

                        d7 = d3 - thick

                        d8 = APoint(thick,(dwidth-thick))

                        string = e

                        e = acad.doc.Blocks.Add(APoint(dc),string)


                        lined1 = e.addline(d1,d2);lined1.color = 10
                        lined2 = e.addline(d2,d3);lined2.color = 10
                        lined3 = e.addline(d3,d4);lined3.color = 10
                        lined4 = e.addline(d4,d1);lined4.color = 10
                        lined5 = e.addline(d5,d6);lined5.color = 10
                        lined6 = e.addline(d6,d7);lined6.color = 10
                        lined7 = e.addline(d7,d8);lined7.color = 10
                        lined8 = e.addline(d8,d5);lined8.color = 10

                        #FOR LOCK NUT
                        p1 = APoint(-4,-4)
                        p2 =APoint(4,-4)
                        p3 =APoint(4,4)
                        p4 =APoint(-4,4)
                        p5 = APoint(4,-10)
                        p6 = APoint(-4,-10)
                        p7=APoint(10,-4)
                        p8 = APoint(10,4)
                        p9 = APoint(4,10)
                        p10=APoint(-4,10)
                        p11=APoint(-10,4)
                        p12=APoint(-10,-4)

                        lock1x = dlenght - locknutclearx
                        lock1y = dwidth- locknutclear
                        lock1 = APoint(lock1x,lock1y)
                        lock2y = locknutclear
                        lock2 = APoint(lock1x,lock2y)

                        cut1 = e.addline(p5,p6);cut1.color = 50
                        cut2 = e.addline(p7,p8);cut2.color = 50
                        cut3 = e.addline(p9,p10);cut3.color = 50
                        cut4 = e.addline(p11,p12);cut4.color = 50
                        cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                        cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                        cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                        cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                        cut9 = cut1.copy();cut9.move(d1,lock2)
                        cut10 = cut2.copy();cut10.move(d1,lock2)
                        cut11 = cut3.copy();cut11.move(d1,lock2)
                        cut12 = cut4.copy();cut12.move(d1,lock2)
                        cut13 = cut5.copy();cut13.move(d1,lock2)
                        cut14 = cut6.copy();cut14.move(d1,lock2)
                        cut15 = cut7.copy();cut15.move(d1,lock2)
                        cut16 = cut8.copy();cut16.move(d1,lock2)
                        cut1.move(d1,lock1)
                        cut2.move(d1,lock1)
                        cut3.move(d1,lock1)
                        cut4.move(d1,lock1)
                        cut5.move(d1,lock1)
                        cut6.move(d1,lock1)
                        cut7.move(d1,lock1)
                        cut8.move(d1,lock1)


                        acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

                        

                    else:
                        #FOR DOOR APOINTS

                        dc = c

                        dp = d

                        d1 = APoint(0,0)

                        d2 = APoint(dlenght)

                        d3 = APoint(dlenght,dwidth)

                        d4 = APoint(0,dwidth)
                        #FOR DOOR THICKNESS

                        d5 = d1 + thick

                        d6 = APoint((dlenght-thick),thick)

                        d7 = d3 - thick

                        d8 = APoint(thick,(dwidth-thick))

                        string = e

                        e = acad.doc.Blocks.Add(APoint(dc),string)

                        lined1 = e.addline(d1,d2);lined1.color = 10
                        lined2 = e.addline(d2,d3);lined2.color = 10
                        lined3 = e.addline(d3,d4);lined3.color = 10
                        lined4 = e.addline(d4,d1);lined4.color = 10
                        lined5 = e.addline(d5,d6);lined5.color = 10
                        lined6 = e.addline(d6,d7);lined6.color = 10
                        lined7 = e.addline(d7,d8);lined7.color = 10
                        lined8 = e.addline(d8,d5);lined8.color = 10

                        #FOR LOCK NUT
                        p1 = APoint(-4,-4)
                        p2 =APoint(4,-4)
                        p3 =APoint(4,4)
                        p4 =APoint(-4,4)
                        p5 = APoint(4,-10)
                        p6 = APoint(-4,-10)
                        p7=APoint(10,-4)
                        p8 = APoint(10,4)
                        p9 = APoint(4,10)
                        p10=APoint(-4,10)
                        p11=APoint(-10,4)
                        p12=APoint(-10,-4)

                        lock1x = dlenght - locknutclearx
                        lock1y = dwidth/2
                        lock1 = APoint(lock1x,lock1y)

                        cut1 = e.addline(p5,p6);cut1.color = 50
                        cut2 = e.addline(p7,p8);cut2.color = 50
                        cut3 = e.addline(p9,p10);cut3.color = 50
                        cut4 = e.addline(p11,p12);cut4.color = 50
                        cut5 = e.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
                        cut6 = e.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
                        cut7 = e.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
                        cut8 = e.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50
                        cut1.move(d1,lock1)
                        cut2.move(d1,lock1)
                        cut3.move(d1,lock1)
                        cut4.move(d1,lock1)
                        cut5.move(d1,lock1)
                        cut6.move(d1,lock1)
                        cut7.move(d1,lock1)
                        cut8.move(d1,lock1)

                        acad.model.InsertBlock(APoint(dp),string, 1, 1, 1, 0)

        mountpos = j
        hmount = l
        mountcheck = config["mounting_plate"]["need_mounting_plate"]
        if sec in mountcheck:
            if type == 'h':
                if hmount == 'mid':
                    if mountpos == "mid":
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght 
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dclearmid - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = (vchannel/2) +mpcleary - 10 ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - (vchannel/2) - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x -(vchannel/2) +10 ; mppy = i.y + thick + 0.5
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                        
                    elif mountpos == 'bot':
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght 
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dcleary - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = (vchannel/2) +mpcleary - 10 ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - (vchannel/2) - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x -(vchannel/2) +10 ; mppy = i.y + thick + 0.5 + thick
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                        
                    elif mountpos == 'top':
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght 
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dcleary - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = (vchannel/2) +mpcleary - 10 ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - (vchannel/2) - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x -(vchannel/2) +10 ; mppy = i.y + thick + 0.5
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                        

                elif hmount == 'left':
                    if mountpos == "mid":
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght - dclearx + zchannelside - mpcleartop + (clear/2)
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dclearmid - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = zchannelside -mpcleartop +mpcleary ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - (vchannel/2) - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x - zchannelside + mpcleartop ; mppy = i.y + thick + 0.5
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                        
                    elif mountpos == 'bot':
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght - dclearx + zchannelside - mpcleartop + (clear/2)
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dcleary - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = zchannelside -mpcleartop +mpcleary ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - (vchannel/2) - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x - zchannelside + mpcleartop ; mppy = i.y + thick + 0.5 + thick
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                    elif mountpos == 'top':
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght - dclearx + zchannelside - mpcleartop + (clear/2)
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dcleary - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = zchannelside -mpcleartop +mpcleary ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - (vchannel/2) - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x - zchannelside + mpcleartop ; mppy = i.y + thick + 0.5
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                        
                        

                elif hmount == "right":
                    if mountpos == "mid":
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght - dclearx + zchannelside - mpclearbot + (clear/2) - 10
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dclearmid - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = (vchannel/2) +mpcleary - 10 ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - zchannelside + mpcleartop - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x -(vchannel/2) +10  ; mppy = i.y + thick + 0.5
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                    elif mountpos == 'bot':
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght - dclearx + zchannelside - mpclearbot + (clear/2) - 10
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dcleary - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = (vchannel/2) +mpcleary - 10 ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - zchannelside + mpcleartop - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x -(vchannel/2) +10  ; mppy = i.y + thick + 0.5 + thick
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                    elif mountpos == 'top':
                        #FOR MOUNTING PLATE MIDDLE
                        mp1 = APoint(0)

                        mp2x = dlenght - dclearx + zchannelside - mpclearbot + (clear/2) - 10
                        mp2 = APoint(mp2x,0)

                        mp3y = dwidth - dcleary - dclearmid - 1 - thick - thick
                        mp3 = APoint(mp2x,mp3y)

                        mp4 = APoint(0,mp3y)

                        blockname = string + " MP"

                        k = acad.doc.Blocks.Add(APoint(0),blockname)

                        linem1 = k.addline(mp1,mp2);linem1.color = 50
                        linem2 = k.addline(mp2,mp3);linem2.color = 50
                        linem3 = k.addline(mp3,mp4);linem3.color = 50
                        linem4 = k.addline(mp4,mp1);linem4.color = 50
                        try:
                            linem5 = linem2.offset(thick);linem5.color = 10
                        except KeyError:
                            pass
                        try:
                            linem6 = linem4.offset(thick);linem6.color = 10
                        except KeyError:
                            pass
                        

                        ab1 = APoint(-4.5,-2.5)
                        ab4 = APoint(4.5,-2.5)
                        ab3 = APoint(4.5,2.5)
                        ab2 = APoint(-4.5,2.5)
                        ab5 = APoint(0,2.5)
                        ab6 = APoint(0,-2.5)

                        

                        ap1x = (vchannel/2) +mpcleary - 10 ; ap1y = mpclearx
                        ap1 = APoint(ap1x,ap1y)
                        ap2x = mp2x - zchannelside + mpcleartop - mpcleary
                        ap2 = APoint(ap2x,ap1y)
                        ap3y = mp3y -  mpclearx
                        ap3 = APoint(ap1x,ap3y)
                        ap4 = APoint(ap2x,ap3y)
                        

                        lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                        lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                        lineab3 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                        lineab4 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                        lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                        lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                        lineab7 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                        lineab8 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                        lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                        lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                        lineab11 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                        lineab12 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                        lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                        lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                        lineab15 = k.addarc(ab5,4.5,0*pi/180,180*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                        lineab16 = k.addarc(ab6,4.5,180*pi/180,360*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                        mppx = i.x -(vchannel/2) +10  ; mppy = i.y + thick + 0.5 
                        mpp = APoint(mppx,mppy) 

                        acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)
                        

            elif type == "v":
                if mountpos == 'mid':
                    #FOR MOUNTING PLATE MIDDLE
                    mp1 = APoint(0)

                    mp2x = dlenght - dclearx - dclearx - 1 - thick - thick
                    mp2 = APoint(mp2x,0)

                    mp3y = dwidth
                    mp3 = APoint(mp2x,mp3y)

                    mp4 = APoint(0,mp3y)

                    blockname = string + " MP"

                    k = acad.doc.Blocks.Add(APoint(0),blockname)

                    linem1 = k.addline(mp1,mp2);linem1.color = 50
                    linem2 = k.addline(mp2,mp3);linem2.color = 50
                    linem3 = k.addline(mp3,mp4);linem3.color = 50
                    linem4 = k.addline(mp4,mp1);linem4.color = 50
                    try:
                        linem5 = linem1.offset(thick);linem5.color = 10
                    except KeyError:
                        pass
                    try:
                        linem6 = linem3.offset(thick);linem6.color = 10
                    except KeyError:
                        pass
                    

                    ab1 = APoint(-2.5,-4.5)
                    ab2 = APoint(2.5,-4.5)
                    ab3 = APoint(2.5,4.5)
                    ab4 = APoint(-2.5,4.5)
                    ab5 = APoint(-2.5)
                    ab6 = APoint(2.5)

                    ap1x = mpclearx; ap1y = (hchannel/2) + mpcleary
                    ap1 = APoint(ap1x,ap1y)
                    ap2x = mp2x - mpclearx
                    ap2 = APoint(ap2x,ap1y)
                    ap3y = mp3y - (hchannel/2)  + 10 - mpcleary
                    ap3 = APoint(ap1x,ap3y)
                    ap4 = APoint(ap2x,ap3y)
                    

                    lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                    lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                    lineab3 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                    lineab4 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                    lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                    lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                    lineab7 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                    lineab8 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                    lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                    lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                    lineab11 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                    lineab12 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                    lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                    lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                    lineab15 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                    lineab16 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                    mppx = i.x + thick + 0.5; mppy = i.y - (hchannel/2)
                    mpp = APoint(mppx,mppy) 

                    acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)

                elif mountpos == 'bot':
                    #FOR MOUNTING PLATE BOTTOM
                    mp1 = APoint(0)

                    mp2x = dlenght - dclearx - dclearx - 1 - thick - thick
                    mp2 = APoint(mp2x,0)

                    mp3y = dwidth - dcleary + zchanneltb - mpclearbot - 5
                    mp3 = APoint(mp2x,mp3y)

                    mp4 = APoint(0,mp3y)

                    blockname = string + " MP"

                    k = acad.doc.Blocks.Add(APoint(0),blockname)

                    linem1 = k.addline(mp1,mp2);linem1.color = 50
                    linem2 = k.addline(mp2,mp3);linem2.color = 50
                    linem3 = k.addline(mp3,mp4);linem3.color = 50
                    linem4 = k.addline(mp4,mp1);linem4.color = 50
                    try:
                        linem5 = linem1.offset(thick);linem5.color = 10
                    except KeyError:
                        pass
                    try:
                        linem6 = linem3.offset(thick);linem6.color = 10
                    except KeyError:
                        pass
                    

                    ab1 = APoint(-2.5,-4.5)
                    ab2 = APoint(2.5,-4.5)
                    ab3 = APoint(2.5,4.5)
                    ab4 = APoint(-2.5,4.5)
                    ab5 = APoint(-2.5)
                    ab6 = APoint(2.5)

                    ap1x = mpclearx; ap1y = zchanneltb - mpclearbot + mpcleary
                    ap1 = APoint(ap1x,ap1y)
                    ap2x = mp2x - mpclearx
                    ap2 = APoint(ap2x,ap1y)
                    ap3y = mp3y - (hchannel/2) + 10 - mpcleary
                    ap3 = APoint(ap1x,ap3y)
                    ap4 = APoint(ap2x,ap3y)
                    

                    lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                    lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                    lineab3 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                    lineab4 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                    lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                    lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                    lineab7 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                    lineab8 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                    lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                    lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                    lineab11 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                    lineab12 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                    lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                    lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                    lineab15 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                    lineab16 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                    mppx = i.x + thick + 0.5; mppy = i.y + thick - zchanneltb + mpclearbot
                    mpp = APoint(mppx,mppy) 

                    acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)

                elif mountpos == "top":
                    #FOR MOUNTING PLATE TOP
                    mp1 = APoint(0)

                    mp2x = dlenght - dclearx - dclearx - 1 - thick - thick
                    mp2 = APoint(mp2x,0)

                    mp3y = dwidth - dcleary + zchanneltb - mpcleartop + (clear/2)
                    mp3 = APoint(mp2x,mp3y)

                    mp4 = APoint(0,mp3y)

                    blockname = string + " MP"

                    k = acad.doc.Blocks.Add(APoint(0),blockname)

                    linem1 = k.addline(mp1,mp2);linem1.color = 50
                    linem2 = k.addline(mp2,mp3);linem2.color = 50
                    linem3 = k.addline(mp3,mp4);linem3.color = 50
                    linem4 = k.addline(mp4,mp1);linem4.color = 50
                    try:
                        linem5 = linem1.offset(thick);linem5.color = 10
                    except KeyError:
                        pass
                    try:
                        linem6 = linem3.offset(thick);linem6.color = 10
                    except KeyError:
                        pass
                    

                    ab1 = APoint(-2.5,-4.5)
                    ab2 = APoint(2.5,-4.5)
                    ab3 = APoint(2.5,4.5)
                    ab4 = APoint(-2.5,4.5)
                    ab5 = APoint(-2.5)
                    ab6 = APoint(2.5)

                    ap1x = mpclearx; ap1y = (hchannel/2) + mpcleary
                    ap1 = APoint(ap1x,ap1y)
                    ap2x = mp2x - mpclearx
                    ap2 = APoint(ap2x,ap1y)
                    ap3y = mp3y - zchanneltb + mpcleartop - mpcleary 
                    ap3 = APoint(ap1x,ap3y)
                    ap4 = APoint(ap2x,ap3y)
                    

                    lineab1 = k.addline(ab1,ab2);lineab1.color = 50;lineab1.move(d1,ap1)
                    lineab2 = k.addline(ab3,ab4);lineab2.color = 50;lineab2.move(d1,ap1)
                    lineab3 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab3.color = 50;lineab3.move(d1,ap1)
                    lineab4 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab4.color = 50;lineab4.move(d1,ap1)
                    lineab5 = k.addline(ab1,ab2);lineab5.color = 50;lineab5.move(d1,ap2)
                    lineab6 = k.addline(ab3,ab4);lineab6.color = 50;lineab6.move(d1,ap2)
                    lineab7 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab7.color = 50;lineab7.move(d1,ap2)
                    lineab8 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab8.color = 50;lineab8.move(d1,ap2)
                    lineab9 = k.addline(ab1,ab2);lineab9.color = 50;lineab9.move(d1,ap3)
                    lineab10 = k.addline(ab3,ab4);lineab10.color = 50;lineab10.move(d1,ap3)
                    lineab11 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab11.color = 50;lineab11.move(d1,ap3)
                    lineab12 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab12.color = 50;lineab12.move(d1,ap3)
                    lineab13 = k.addline(ab1,ab2);lineab13.color = 50;lineab13.move(d1,ap4)
                    lineab14 = k.addline(ab3,ab4);lineab14.color = 50;lineab14.move(d1,ap4)
                    lineab15 = k.addarc(ab5,4.5,90*pi/180,270*pi/180);lineab15.color = 50;lineab15.move(d1,ap4)
                    lineab16 = k.addarc(ab6,4.5,270*pi/180,90*pi/180);lineab16.color = 50;lineab16.move(d1,ap4)

                    mppx = i.x + thick + 0.5; mppy = i.y - (hchannel/2)
                    mpp = APoint(mppx,mppy) 

                    acad.model.InsertBlock(mpp,blockname, 1, 1, 1, 0)


                





