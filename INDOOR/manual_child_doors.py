from pyautocad import Autocad, APoint
from comtypes import COMError
from configparser import ConfigParser
from math import pi
import sys
sys.path.append('INDOOR')

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

import win32com.client
acad1 = win32com.client.Dispatch("AutoCAD.Application")
doc = acad1.ActiveDocument
acadmodel = acad1.activedocument.modelspace

config = ConfigParser()
config.read('./INDOOR/gi_config_in.ini')

print('Using file ' + acad.doc.Name)

inches = config["doors"]["inches"]
inchx = float(config["doors"]["inches_size_x"])
inchy = float(config["doors"]["inches_size_y"])
inchclear = int(config["doors"]["inches_clearence_y"])
needtext = config["doors"]["text_box"]
dclearx = int(config["doors"]["door_clearence_X"])
dcleary = int(config["doors"]["door_clearence_Y"])
dclearmid = int(config["doors"]["door_clearence_MID"])

block1 = acad.get_selection(text='Select objects')

for x in block1:
    block_name = x.name

def child_doors_Vv(a,b,c,d):


    block_name = a
    block = acad.doc.Blocks.Item(block_name)


    line_count = []
    for entity in block:
        if entity.EntityName == "AcDbLine":
            line_count.append(entity.length)


    #user inputs
    lenght = int(line_count[0])
    width = int(line_count[1])
    lx = int(config["shell"]["where_to_place"]) + int(config["shell"]["lenght"]) + b + lenght
    ly = c 
    fold = int(config["doors"]["folding_lenght"])
    thick = float(config["doors"]["door_thick"])
    fold1 = fold - thick
    off = thick*2
    len = lenght + fold1 + lx
    wid = width + fold1

    if inches == 'y':

        if width >= 650:
            pp1 = lx + fold1
            p1 = APoint(pp1, ly)

            pp2 = len - off
            p2 = APoint(pp2,ly)

            p3y = fold1 + ly
            p3 = APoint(pp2,p3y)

            pp4 = pp2 + fold1
            p4 = APoint(pp4,p3y)

            pp5 = wid - off +ly
            p5 = APoint(pp4,pp5)

            p6 = APoint(pp2,pp5)

            pp7 = pp5 + fold1
            p7 = APoint(pp2,pp7)

            p8 = APoint(pp1,pp7)

            p9 = APoint(pp1,pp5)

            p10 = APoint(lx,pp5)

            p11 = APoint(lx,p3y)

            p12 = APoint(pp1,p3y)

            #for inches 
            p13y = p3y + inchclear - thick 
            p13 = APoint(lx,p13y)

            p14x = lx + fold1 + inchx -thick
            p14 = APoint(p14x,p13y)

            p15y = inchy + p13y 
            p15 = APoint(p14x,p15y)

            p16 = APoint(lx,p15y)

            p17y = (width/2) - (inchy/2) +ly + fold1
            p17 = APoint(lx,p17y)

            p18y = p17y + inchy 
            p18 =APoint(lx,p18y)

            p19y = width - thick - inchclear - inchy +ly + fold1
            p19 = APoint(lx,p19y)

            p20y = p19y + inchy 
            p20 =APoint(lx,p20y)


            #for drawing rectangle
            line1 = acad.model.AddLine(p1, p2)
            line2 = acad.model.AddLine(p2, p3)
            line3 = acad.model.AddLine(p3, p4)
            line4 = acad.model.AddLine(p4, p5)
            line5 = acad.model.AddLine(p5, p6)
            line6 = acad.model.AddLine(p6, p7)
            line7 = acad.model.AddLine(p7, p8)
            line8 = acad.model.AddLine(p8, p9)
            line9 = acad.model.AddLine(p9, p10)
            #line10 = acad.model.AddLine(p10, p11)
            line11 = acad.model.AddLine(p11, p12)
            line12 = acad.model.AddLine(p12, p1)
            line17 = acad.model.AddLine(p11, p13)
            line18 = acad.model.AddLine(p13, p14)
            line19 = acad.model.AddLine(p14, p15)
            line20 = acad.model.AddLine(p15, p16)
            line21 = acad.model.AddLine(p16, p17)

            line22 = acad.model.AddLine(p13, p14);line22.move(p13,p17)
            line23 = acad.model.AddLine(p14, p15);line23.move(p13,p17)
            line24 = acad.model.AddLine(p15, p16);line24.move(p13,p17)
            line25 = acad.model.addline(p18,p19)
            line26 = acad.model.AddLine(p13, p14);line26.move(p13,p19)
            line27 = acad.model.AddLine(p14, p15);line27.move(p13,p19)
            line28 = acad.model.AddLine(p15, p16);line28.move(p13,p19)

            line29 = acad.model.addline(p20,p10)


            p21 = APoint(pp1,p13y)
            p22 = APoint(pp1,p15y)
            p23 = APoint(pp1,p17y)
            p24 = APoint(pp1,p18y)
            p25 = APoint(pp1,p19y)
            p26 = APoint(pp1,p20y)
            #for folding lines
            line13 = acad.model.AddLine(p12, p3);line13.color = 12
            line14 = acad.model.AddLine(p3, p6);line14.color = 12
            line15 = acad.model.AddLine(p6, p9);line15.color = 12
            #line16 = acad.model.AddLine(p9, p12);line16.color = 12
            line30 = acad.model.AddLine(p12, p21);line30.color = 12
            line31 = acad.model.AddLine(p22, p23);line31.color = 12
            line32 = acad.model.AddLine(p24, p25);line32.color = 12
            line33 = acad.model.AddLine(p26, p9);line33.color = 12
            
        elif width >= 200:
            pp1 = lx + fold1
            p1 = APoint(pp1, ly)

            pp2 = len - off
            p2 = APoint(pp2,ly)

            p3y = fold1 + ly
            p3 = APoint(pp2,p3y)

            pp4 = pp2 + fold1
            p4 = APoint(pp4,p3y)

            pp5 = wid - off +ly
            p5 = APoint(pp4,pp5)

            p6 = APoint(pp2,pp5)

            pp7 = pp5 + fold1
            p7 = APoint(pp2,pp7)

            p8 = APoint(pp1,pp7)

            p9 = APoint(pp1,pp5)

            p10 = APoint(lx,pp5)

            p11 = APoint(lx,p3y)

            p12 = APoint(pp1,p3y)

            #for inches 
            p13y = p3y + inchclear - thick 
            p13 = APoint(lx,p13y)

            p14x = lx + fold1 + inchx -thick
            p14 = APoint(p14x,p13y)

            p15y = inchy + p13y 
            p15 = APoint(p14x,p15y)

            p16 = APoint(lx,p15y)

            p17y = (width/2) - (inchy/2) +ly + fold1
            p17 = APoint(lx,p17y)

            p18y = p17y + inchy 
            p18 =APoint(lx,p18y)

            p19y = width - thick - inchclear - inchy +ly + fold1
            p19 = APoint(lx,p19y)

            p20y = p19y + inchy 
            p20 =APoint(lx,p20y)


            #for drawing rectangle
            line1 = acad.model.AddLine(p1, p2)
            line2 = acad.model.AddLine(p2, p3)
            line3 = acad.model.AddLine(p3, p4)
            line4 = acad.model.AddLine(p4, p5)
            line5 = acad.model.AddLine(p5, p6)
            line6 = acad.model.AddLine(p6, p7)
            line7 = acad.model.AddLine(p7, p8)
            line8 = acad.model.AddLine(p8, p9)
            line9 = acad.model.AddLine(p9, p10)
            #line10 = acad.model.AddLine(p10, p11)
            line11 = acad.model.AddLine(p11, p12)
            line12 = acad.model.AddLine(p12, p1)
            line17 = acad.model.AddLine(p11, p13)
            line18 = acad.model.AddLine(p13, p14)
            line19 = acad.model.AddLine(p14, p15)
            line20 = acad.model.AddLine(p15, p16)
            line21 = acad.model.AddLine(p16, p19)

            #line22 = acad.model.AddLine(p13, p14);line22.move(p13,p17)
            #line23 = acad.model.AddLine(p14, p15);line23.move(p13,p17)
            #line24 = acad.model.AddLine(p15, p16);line24.move(p13,p17)
            #line25 = acad.model.addline(p18,p19)
            line26 = acad.model.AddLine(p13, p14);line26.move(p13,p19)
            line27 = acad.model.AddLine(p14, p15);line27.move(p13,p19)
            line28 = acad.model.AddLine(p15, p16);line28.move(p13,p19)

            line29 = acad.model.addline(p20,p10)

            p21 = APoint(pp1,p13y)
            p22 = APoint(pp1,p15y)
            p23 = APoint(pp1,p17y)
            p24 = APoint(pp1,p18y)
            p25 = APoint(pp1,p19y)
            p26 = APoint(pp1,p20y)

            #for folding lines
            line13 = acad.model.AddLine(p12, p3);line13.color = 12
            line14 = acad.model.AddLine(p3, p6);line14.color = 12
            line15 = acad.model.AddLine(p6, p9);line15.color = 12
            #line16 = acad.model.AddLine(p9, p12);line16.color = 12
            line30 = acad.model.AddLine(p12, p21);line30.color = 12
            line31 = acad.model.AddLine(p22, p25);line31.color = 12
            #line32 = acad.model.AddLine(p24, p25);line32.color = 12
            line33 = acad.model.AddLine(p26, p9);line33.color = 12
        else:
            pp1 = lx + fold1
            p1 = APoint(pp1, ly)

            pp2 = len - off
            p2 = APoint(pp2,ly)

            p3y = fold1 + ly
            p3 = APoint(pp2,p3y)

            pp4 = pp2 + fold1
            p4 = APoint(pp4,p3y)

            pp5 = wid - off +ly
            p5 = APoint(pp4,pp5)

            p6 = APoint(pp2,pp5)

            pp7 = pp5 + fold1
            p7 = APoint(pp2,pp7)

            p8 = APoint(pp1,pp7)

            p9 = APoint(pp1,pp5)

            p10 = APoint(lx,pp5)

            p11 = APoint(lx,p3y)

            p12 = APoint(pp1,p3y)

            #for inches 
            p13y = p3y + inchclear - thick 
            p13 = APoint(lx,p13y)

            p14x = lx + fold1 + inchx -thick
            p14 = APoint(p14x,p13y)

            p15y = inchy + p13y 
            p15 = APoint(p14x,p15y)

            p16 = APoint(lx,p15y)

            p17y = (width/2) - (inchy/2) +ly + fold1
            p17 = APoint(lx,p17y)

            p18y = p17y + inchy 
            p18 =APoint(lx,p18y)

            p19y = width - thick - inchclear - inchy +ly + fold1
            p19 = APoint(lx,p19y)

            p20y = p19y + inchy 
            p20 =APoint(lx,p20y)


            #for drawing rectangle
            line1 = acad.model.AddLine(p1, p2)
            line2 = acad.model.AddLine(p2, p3)
            line3 = acad.model.AddLine(p3, p4)
            line4 = acad.model.AddLine(p4, p5)
            line5 = acad.model.AddLine(p5, p6)
            line6 = acad.model.AddLine(p6, p7)
            line7 = acad.model.AddLine(p7, p8)
            line8 = acad.model.AddLine(p8, p9)
            line9 = acad.model.AddLine(p9, p10)
            #line10 = acad.model.AddLine(p10, p11)
            line11 = acad.model.AddLine(p11, p12)
            line12 = acad.model.AddLine(p12, p1)
            #line17 = acad.model.AddLine(p11, p13)
            #line18 = acad.model.AddLine(p13, p14)
            #line19 = acad.model.AddLine(p14, p15)
            #line20 = acad.model.AddLine(p15, p16)
            #line21 = acad.model.AddLine(p16, p17)

            line22 = acad.model.AddLine(p13, p14);line22.move(p13,p17)
            line23 = acad.model.AddLine(p14, p15);line23.move(p13,p17)
            line24 = acad.model.AddLine(p15, p16);line24.move(p13,p17)
            line25 = acad.model.addline(p18,p10)
            #line26 = acad.model.AddLine(p13, p14);line26.move(p13,p19)
            #line27 = acad.model.AddLine(p14, p15);line27.move(p13,p19)
            #line28 = acad.model.AddLine(p15, p16);line28.move(p13,p19)

            line29 = acad.model.addline(p11,p17)


            p21 = APoint(pp1,p13y)
            p22 = APoint(pp1,p15y)
            p23 = APoint(pp1,p17y)
            p24 = APoint(pp1,p18y)
            p25 = APoint(pp1,p19y)
            p26 = APoint(pp1,p20y)

            #for folding lines
            line13 = acad.model.AddLine(p12, p3);line13.color = 12
            line14 = acad.model.AddLine(p3, p6);line14.color = 12
            line15 = acad.model.AddLine(p6, p9);line15.color = 12
            #line16 = acad.model.AddLine(p9, p12);line16.color = 12
            line30 = acad.model.AddLine(p12, p23);line30.color = 12
            #line31 = acad.model.AddLine(p22, p25);line31.color = 12
            #line32 = acad.model.AddLine(p24, p25);line32.color = 12
            line33 = acad.model.AddLine(p24, p9);line33.color = 12
        

    elif inches == 'n':
        pp1 = lx + fold1
        p1 = APoint(pp1, ly)

        pp2 = len - off
        p2 = APoint(pp2,ly)

        p3y = fold1 + ly
        p3 = APoint(pp2,p3y)

        pp4 = pp2 + fold1
        p4 = APoint(pp4,p3y)

        pp5 = wid - off +ly
        p5 = APoint(pp4,pp5)

        p6 = APoint(pp2,pp5)

        pp7 = pp5 + fold1
        p7 = APoint(pp2,pp7)

        p8 = APoint(pp1,pp7)

        p9 = APoint(pp1,pp5)

        p10 = APoint(lx,pp5)

        p11 = APoint(lx,p3y)

        p12 = APoint(pp1,p3y)

        #for drawing rectangle
        line1 = acad.model.AddLine(p1, p2)
        line2 = acad.model.AddLine(p2, p3)
        line3 = acad.model.AddLine(p3, p4)
        line4 = acad.model.AddLine(p4, p5)
        line5 = acad.model.AddLine(p5, p6)
        line6 = acad.model.AddLine(p6, p7)
        line7 = acad.model.AddLine(p7, p8)
        line8 = acad.model.AddLine(p8, p9)
        line9 = acad.model.AddLine(p9, p10)
        line10 = acad.model.AddLine(p10, p11)
        line11 = acad.model.AddLine(p11, p12)
        line12 = acad.model.AddLine(p12, p1)

        #for folding lines
        line13 = acad.model.AddLine(p12, p3)
        line14 = acad.model.AddLine(p3, p6)
        line15 = acad.model.AddLine(p6, p9)
        line16 = acad.model.AddLine(p9, p12)
        line13.color = 12
        line14.color = 12
        line15.color = 12
        line16.color = 12

    #For annotation
    anno = config["doors"]["annotation"]
    if anno == "y":
        dd1 = APoint(p4+40,0)
        dim1 = acad.model.AddDimAligned(p4, p5, dd1)
        dd2 = APoint(p2+fold1+65,0)
        dim2 = acad.model.AddDimAligned(p2, p7, dd2)
        dd3 = APoint(p7+30)
        dim3 = acad.model.AddDimAligned(p7, p8, dd3)
        dd4 = APoint(p10+fold1+55)
        dim4 = acad.model.AddDimAligned(p5, p10, dd4)
        dim5 = acad.model.adddimaligned(p5,p6,dd3)
    else:
            print("NO ANNOTATION")

    #For text box
    pp13 = lenght/2
    p100 = APoint((pp13+lx-90),(ly -30)) 
    thicktext = str(thick)
    if needtext == "y":
        ben = "DOWN"
        qty = "1"
        text = acad.model.addmtext(p100,210,"THICK "+thicktext +"MM    BEND "+ben + "       QTY "+ qty +" NOS" +"         "+block_name )
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")

    end = d
    if end == "y":
        p99x = p12.x + dclearx - thick - thick ;p99y = p12.y + dcleary - thick - thick
        p99 = APoint(p99x,p99y)
    elif end == "n":
        p99x = p12.x + dclearx - thick ;p99y = p12.y + dclearmid - thick
        p99 = APoint(p99x,p99y)
    else:
        print("choose correct choice")

    newblock = acad.model.InsertBlock(p99, block_name, 1, 1, 1, 0)
    try:
        newblock.explode()
    except KeyError:
        pass
    newblock.delete()
    


def child_doors_Hh(a,b,c,d):


    block_name = a
    block = acad.doc.Blocks.Item(block_name)


    line_count = []
    for entity in block:
        if entity.EntityName == "AcDbLine":
            line_count.append(entity.length)


    #user inputs
    lenght = int(line_count[1])
    width = int(line_count[0])
    lx = int(config["shell"]["where_to_place"]) + int(config["shell"]["lenght"]) + b + width
    ly = c 
    fold = int(config["doors"]["folding_lenght"])
    thick = float(config["doors"]["door_thick"])
    fold1 = fold - thick
    off = thick*2
    len = lenght + fold1 + lx
    wid = width + fold1

    if inches == 'y':

        if width >= 650:
            pp1 = lx + fold1
            p1 = APoint(pp1, ly)

            pp2 = len - off
            p2 = APoint(pp2,ly)

            p3y = fold1 + ly
            p3 = APoint(pp2,p3y)

            pp4 = pp2 + fold1
            p4 = APoint(pp4,p3y)

            pp5 = wid - off +ly
            p5 = APoint(pp4,pp5)

            p6 = APoint(pp2,pp5)

            pp7 = pp5 + fold1
            p7 = APoint(pp2,pp7)

            p8 = APoint(pp1,pp7)

            p9 = APoint(pp1,pp5)

            p10 = APoint(lx,pp5)

            p11 = APoint(lx,p3y)

            p12 = APoint(pp1,p3y)

            #for inches 
            p13y = p3y + inchclear - thick 
            p13 = APoint(lx,p13y)

            p14x = lx + fold1 + inchx -thick
            p14 = APoint(p14x,p13y)

            p15y = inchy + p13y 
            p15 = APoint(p14x,p15y)

            p16 = APoint(lx,p15y)

            p17y = (width/2) - (inchy/2) +ly + fold1
            p17 = APoint(lx,p17y)

            p18y = p17y + inchy 
            p18 =APoint(lx,p18y)

            p19y = width - thick - inchclear - inchy +ly + fold1
            p19 = APoint(lx,p19y)

            p20y = p19y + inchy 
            p20 =APoint(lx,p20y)


            #for drawing rectangle
            line1 = acad.model.AddLine(p1, p2)
            line2 = acad.model.AddLine(p2, p3)
            line3 = acad.model.AddLine(p3, p4)
            line4 = acad.model.AddLine(p4, p5)
            line5 = acad.model.AddLine(p5, p6)
            line6 = acad.model.AddLine(p6, p7)
            line7 = acad.model.AddLine(p7, p8)
            line8 = acad.model.AddLine(p8, p9)
            line9 = acad.model.AddLine(p9, p10)
            #line10 = acad.model.AddLine(p10, p11)
            line11 = acad.model.AddLine(p11, p12)
            line12 = acad.model.AddLine(p12, p1)
            line17 = acad.model.AddLine(p11, p13)
            line18 = acad.model.AddLine(p13, p14)
            line19 = acad.model.AddLine(p14, p15)
            line20 = acad.model.AddLine(p15, p16)
            line21 = acad.model.AddLine(p16, p17)

            line22 = acad.model.AddLine(p13, p14);line22.move(p13,p17)
            line23 = acad.model.AddLine(p14, p15);line23.move(p13,p17)
            line24 = acad.model.AddLine(p15, p16);line24.move(p13,p17)
            line25 = acad.model.addline(p18,p19)
            line26 = acad.model.AddLine(p13, p14);line26.move(p13,p19)
            line27 = acad.model.AddLine(p14, p15);line27.move(p13,p19)
            line28 = acad.model.AddLine(p15, p16);line28.move(p13,p19)

            line29 = acad.model.addline(p20,p10)


            p21 = APoint(pp1,p13y)
            p22 = APoint(pp1,p15y)
            p23 = APoint(pp1,p17y)
            p24 = APoint(pp1,p18y)
            p25 = APoint(pp1,p19y)
            p26 = APoint(pp1,p20y)
            #for folding lines
            line13 = acad.model.AddLine(p12, p3);line13.color = 12
            line14 = acad.model.AddLine(p3, p6);line14.color = 12
            line15 = acad.model.AddLine(p6, p9);line15.color = 12
            #line16 = acad.model.AddLine(p9, p12);line16.color = 12
            line30 = acad.model.AddLine(p12, p21);line30.color = 12
            line31 = acad.model.AddLine(p22, p23);line31.color = 12
            line32 = acad.model.AddLine(p24, p25);line32.color = 12
            line33 = acad.model.AddLine(p26, p9);line33.color = 12
            
        elif width >= 200:
            pp1 = lx + fold1
            p1 = APoint(pp1, ly)

            pp2 = len - off
            p2 = APoint(pp2,ly)

            p3y = fold1 + ly
            p3 = APoint(pp2,p3y)

            pp4 = pp2 + fold1
            p4 = APoint(pp4,p3y)

            pp5 = wid - off +ly
            p5 = APoint(pp4,pp5)

            p6 = APoint(pp2,pp5)

            pp7 = pp5 + fold1
            p7 = APoint(pp2,pp7)

            p8 = APoint(pp1,pp7)

            p9 = APoint(pp1,pp5)

            p10 = APoint(lx,pp5)

            p11 = APoint(lx,p3y)

            p12 = APoint(pp1,p3y)

            #for inches 
            p13y = p3y + inchclear - thick 
            p13 = APoint(lx,p13y)

            p14x = lx + fold1 + inchx -thick
            p14 = APoint(p14x,p13y)

            p15y = inchy + p13y 
            p15 = APoint(p14x,p15y)

            p16 = APoint(lx,p15y)

            p17y = (width/2) - (inchy/2) +ly + fold1
            p17 = APoint(lx,p17y)

            p18y = p17y + inchy 
            p18 =APoint(lx,p18y)

            p19y = width - thick - inchclear - inchy +ly + fold1
            p19 = APoint(lx,p19y)

            p20y = p19y + inchy 
            p20 =APoint(lx,p20y)


            #for drawing rectangle
            line1 = acad.model.AddLine(p1, p2)
            line2 = acad.model.AddLine(p2, p3)
            line3 = acad.model.AddLine(p3, p4)
            line4 = acad.model.AddLine(p4, p5)
            line5 = acad.model.AddLine(p5, p6)
            line6 = acad.model.AddLine(p6, p7)
            line7 = acad.model.AddLine(p7, p8)
            line8 = acad.model.AddLine(p8, p9)
            line9 = acad.model.AddLine(p9, p10)
            #line10 = acad.model.AddLine(p10, p11)
            line11 = acad.model.AddLine(p11, p12)
            line12 = acad.model.AddLine(p12, p1)
            line17 = acad.model.AddLine(p11, p13)
            line18 = acad.model.AddLine(p13, p14)
            line19 = acad.model.AddLine(p14, p15)
            line20 = acad.model.AddLine(p15, p16)
            line21 = acad.model.AddLine(p16, p19)

            #line22 = acad.model.AddLine(p13, p14);line22.move(p13,p17)
            #line23 = acad.model.AddLine(p14, p15);line23.move(p13,p17)
            #line24 = acad.model.AddLine(p15, p16);line24.move(p13,p17)
            #line25 = acad.model.addline(p18,p19)
            line26 = acad.model.AddLine(p13, p14);line26.move(p13,p19)
            line27 = acad.model.AddLine(p14, p15);line27.move(p13,p19)
            line28 = acad.model.AddLine(p15, p16);line28.move(p13,p19)

            line29 = acad.model.addline(p20,p10)

            p21 = APoint(pp1,p13y)
            p22 = APoint(pp1,p15y)
            p23 = APoint(pp1,p17y)
            p24 = APoint(pp1,p18y)
            p25 = APoint(pp1,p19y)
            p26 = APoint(pp1,p20y)

            #for folding lines
            line13 = acad.model.AddLine(p12, p3);line13.color = 12
            line14 = acad.model.AddLine(p3, p6);line14.color = 12
            line15 = acad.model.AddLine(p6, p9);line15.color = 12
            #line16 = acad.model.AddLine(p9, p12);line16.color = 12
            line30 = acad.model.AddLine(p12, p21);line30.color = 12
            line31 = acad.model.AddLine(p22, p25);line31.color = 12
            #line32 = acad.model.AddLine(p24, p25);line32.color = 12
            line33 = acad.model.AddLine(p26, p9);line33.color = 12
        else:
            pp1 = lx + fold1
            p1 = APoint(pp1, ly)

            pp2 = len - off
            p2 = APoint(pp2,ly)

            p3y = fold1 + ly
            p3 = APoint(pp2,p3y)

            pp4 = pp2 + fold1
            p4 = APoint(pp4,p3y)

            pp5 = wid - off +ly
            p5 = APoint(pp4,pp5)

            p6 = APoint(pp2,pp5)

            pp7 = pp5 + fold1
            p7 = APoint(pp2,pp7)

            p8 = APoint(pp1,pp7)

            p9 = APoint(pp1,pp5)

            p10 = APoint(lx,pp5)

            p11 = APoint(lx,p3y)

            p12 = APoint(pp1,p3y)

            #for inches 
            p13y = p3y + inchclear - thick 
            p13 = APoint(lx,p13y)

            p14x = lx + fold1 + inchx -thick
            p14 = APoint(p14x,p13y)

            p15y = inchy + p13y 
            p15 = APoint(p14x,p15y)

            p16 = APoint(lx,p15y)

            p17y = (width/2) - (inchy/2) +ly + fold1
            p17 = APoint(lx,p17y)

            p18y = p17y + inchy 
            p18 =APoint(lx,p18y)

            p19y = width - thick - inchclear - inchy +ly + fold1
            p19 = APoint(lx,p19y)

            p20y = p19y + inchy 
            p20 =APoint(lx,p20y)


            #for drawing rectangle
            line1 = acad.model.AddLine(p1, p2)
            line2 = acad.model.AddLine(p2, p3)
            line3 = acad.model.AddLine(p3, p4)
            line4 = acad.model.AddLine(p4, p5)
            line5 = acad.model.AddLine(p5, p6)
            line6 = acad.model.AddLine(p6, p7)
            line7 = acad.model.AddLine(p7, p8)
            line8 = acad.model.AddLine(p8, p9)
            line9 = acad.model.AddLine(p9, p10)
            #line10 = acad.model.AddLine(p10, p11)
            line11 = acad.model.AddLine(p11, p12)
            line12 = acad.model.AddLine(p12, p1)
            #line17 = acad.model.AddLine(p11, p13)
            #line18 = acad.model.AddLine(p13, p14)
            #line19 = acad.model.AddLine(p14, p15)
            #line20 = acad.model.AddLine(p15, p16)
            #line21 = acad.model.AddLine(p16, p17)

            line22 = acad.model.AddLine(p13, p14);line22.move(p13,p17)
            line23 = acad.model.AddLine(p14, p15);line23.move(p13,p17)
            line24 = acad.model.AddLine(p15, p16);line24.move(p13,p17)
            line25 = acad.model.addline(p18,p10)
            #line26 = acad.model.AddLine(p13, p14);line26.move(p13,p19)
            #line27 = acad.model.AddLine(p14, p15);line27.move(p13,p19)
            #line28 = acad.model.AddLine(p15, p16);line28.move(p13,p19)

            line29 = acad.model.addline(p11,p17)


            p21 = APoint(pp1,p13y)
            p22 = APoint(pp1,p15y)
            p23 = APoint(pp1,p17y)
            p24 = APoint(pp1,p18y)
            p25 = APoint(pp1,p19y)
            p26 = APoint(pp1,p20y)

            #for folding lines
            line13 = acad.model.AddLine(p12, p3);line13.color = 12
            line14 = acad.model.AddLine(p3, p6);line14.color = 12
            line15 = acad.model.AddLine(p6, p9);line15.color = 12
            #line16 = acad.model.AddLine(p9, p12);line16.color = 12
            line30 = acad.model.AddLine(p12, p23);line30.color = 12
            #line31 = acad.model.AddLine(p22, p25);line31.color = 12
            #line32 = acad.model.AddLine(p24, p25);line32.color = 12
            line33 = acad.model.AddLine(p24, p9);line33.color = 12
        

    elif inches == 'n':
        pp1 = lx + fold1
        p1 = APoint(pp1, ly)

        pp2 = len - off
        p2 = APoint(pp2,ly)

        p3y = fold1 + ly
        p3 = APoint(pp2,p3y)

        pp4 = pp2 + fold1
        p4 = APoint(pp4,p3y)

        pp5 = wid - off +ly
        p5 = APoint(pp4,pp5)

        p6 = APoint(pp2,pp5)

        pp7 = pp5 + fold1
        p7 = APoint(pp2,pp7)

        p8 = APoint(pp1,pp7)

        p9 = APoint(pp1,pp5)

        p10 = APoint(lx,pp5)

        p11 = APoint(lx,p3y)

        p12 = APoint(pp1,p3y)

        #for drawing rectangle
        line1 = acad.model.AddLine(p1, p2)
        line2 = acad.model.AddLine(p2, p3)
        line3 = acad.model.AddLine(p3, p4)
        line4 = acad.model.AddLine(p4, p5)
        line5 = acad.model.AddLine(p5, p6)
        line6 = acad.model.AddLine(p6, p7)
        line7 = acad.model.AddLine(p7, p8)
        line8 = acad.model.AddLine(p8, p9)
        line9 = acad.model.AddLine(p9, p10)
        line10 = acad.model.AddLine(p10, p11)
        line11 = acad.model.AddLine(p11, p12)
        line12 = acad.model.AddLine(p12, p1)

        #for folding lines
        line13 = acad.model.AddLine(p12, p3)
        line14 = acad.model.AddLine(p3, p6)
        line15 = acad.model.AddLine(p6, p9)
        line16 = acad.model.AddLine(p9, p12)
        line13.color = 12
        line14.color = 12
        line15.color = 12
        line16.color = 12

    #For annotation
    anno = config["doors"]["annotation"]
    if anno == "y":
        dd1 = APoint(p4+40,0)
        dim1 = acad.model.AddDimAligned(p4, p5, dd1)
        dd2 = APoint(p2+fold1+65,0)
        dim2 = acad.model.AddDimAligned(p2, p7, dd2)
        dd3 = APoint(p7+30)
        dim3 = acad.model.AddDimAligned(p7, p8, dd3)
        dd4 = APoint(p10+fold1+55)
        dim4 = acad.model.AddDimAligned(p5, p10, dd4)
        dim5 = acad.model.adddimaligned(p5,p6,dd3)
    else:
            print("NO ANNOTATION")

    #For text box
    pp13 = lenght/2
    p100 = APoint((pp13+lx-90),(ly -30)) 
    thicktext = str(thick)
    if needtext == "y":
        ben = "DOWN"
        qty = "1"
        text = acad.model.addmtext(p100,210,"THICK "+thicktext +"MM    BEND "+ben + "       QTY "+ qty +" NOS" +"         "+block_name )
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")

    end = d
    if end == "y":
        p99x = p9.x + dcleary -thick -thick ;p99y = p9.y - dclearx +thick +thick
        p99 = APoint(p99x,p99y)
    elif end == "n":
        p99x = p9.x + dclearmid -thick  ;p99y = p9.y - dclearx +thick 
        p99 = APoint(p99x,p99y)
    else:
        print("choose correct choice")

    newblock = acad.model.InsertBlock(p99, block_name, 1, 1, 1, pi*270/180)
    try:
        newblock.explode()
    except KeyError:
        pass
    newblock.delete()

type = config["shell"]["type_panel"]
if type == 'v':
    if block_name == 'door1_1':
        child_doors_Vv(block_name,500,0,'y')
    elif block_name == 'door2_1':
        child_doors_Vv(block_name,500,0,'y')
    elif block_name == 'door3_1':
        child_doors_Vv(block_name,500,0,'y')
    elif block_name == 'door4_1':
        child_doors_Vv(block_name,500,0,'y')
    elif block_name == 'door5_1':
        child_doors_Vv(block_name,500,0,'y')
    elif block_name == 'door6_1':
        child_doors_Vv(block_name,500,0,'y')
    else:
        child_doors_Vv(block_name,500,0,'n')

elif type == 'h':
    if block_name == 'door1_1':
        child_doors_Hh(block_name,500,0,'y')
    elif block_name == 'door2_1':
        child_doors_Hh(block_name,500,0,'y')
    elif block_name == 'door3_1':
        child_doors_Hh(block_name,500,0,'y')
    elif block_name == 'door4_1':
        child_doors_Hh(block_name,500,0,'y')
    elif block_name == 'door5_1':
        child_doors_Hh(block_name,500,0,'y')
    elif block_name == 'door6_1':
        child_doors_Hh(block_name,500,0,'y')
    else:
        child_doors_Hh(block_name,500,0,'n')


    
acad.app.zoomextents()

