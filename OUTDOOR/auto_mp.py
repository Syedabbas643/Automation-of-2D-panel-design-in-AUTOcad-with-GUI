from pyautocad import Autocad, APoint
from comtypes import COMError
from configparser import ConfigParser
from math import pi
import sys
sys.path.append('OUTDOOR')

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

config = ConfigParser()
config.read('./OUTDOOR/gi_config_out.ini')

acad.doc.purgeAll()

print('Using file ' + acad.doc.Name)

needtext = config["doors"]["text_box"]


def child_mp_v(a,b,c):
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
    fold = int(config["mounting_plate"]["mounting_plate_folding_lenght"])
    thick = float(config["mounting_plate"]["mounting_plate_thick"])
    fold1 = fold - thick
    
    mp1 = APoint(lx,ly)

    mp2x = lx + lenght
    mp2 = APoint(mp2x,ly)

    mp3y = width + fold1 + fold1 - thick - thick + ly
    mp3 = APoint(mp2x,mp3y)

    mp4 = APoint(mp1.x,mp3y)

    mp5y = ly + fold1
    mp5 = APoint(lx,mp5y)

    mp6 = APoint(mp2x,mp5y)

    mp7y = mp3y - fold1
    mp7 =APoint(lx,mp7y)

    mp8 = APoint(mp2x,mp7y)

    linemp1 = acad.model.addline(mp1,mp2)
    linemp2 = acad.model.addline(mp2,mp3)
    linemp3 = acad.model.addline(mp3,mp4)
    linemp4 = acad.model.addline(mp4,mp1)
    linemp5 = acad.model.addline(mp5,mp6);linemp5.color = 12
    linemp6 = acad.model.addline(mp7,mp8);linemp6.color = 12

    #For annotation
    anno = config["doors"]["annotation"]
    if anno == "y":
        dd1 = APoint(mp2+65,0)
        dim1 = acad.model.AddDimAligned(mp2, mp3, dd1)
        dd2 = APoint(mp2+40,0)
        dim2 = acad.model.AddDimAligned(mp6, mp8, dd2)
        dd3 = APoint(mp3+30)
        dim3 = acad.model.AddDimAligned(mp3, mp4, dd3)
        dim4 = acad.model.AddDimAligned(mp8, mp3, dd2)
        
    else:
            print("NO ANNOTATION")

    #For text box
    pp13 = lenght/2
    p100 = APoint((pp13+lx-90),(ly -30)) 
    thicktext = str(thick)
    if needtext == "y":
        ben = "UP"
        qty = "1"
        text = acad.model.addmtext(p100,210,"THICK "+thicktext +"MM    BEND "+ben + "       QTY "+ qty +" NOS" +"         "+block_name )
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")



    mp99y = mp5y - thick
    mp99 = APoint(lx,mp99y)

    newblock = acad.model.InsertBlock(mp99, block_name, 1, 1, 1, 0)
    try:
        newblock.explode()
    except KeyError:
        pass
    newblock.delete()

def child_mp_h(a,b,c):
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
    fold = int(config["mounting_plate"]["mounting_plate_folding_lenght"])
    thick = float(config["mounting_plate"]["mounting_plate_thick"])
    fold1 = fold - thick
    
    mp1 = APoint(lx,ly)

    mp2x = lx + lenght
    mp2 = APoint(mp2x,ly)

    mp3y = width + fold1 + fold1 - thick - thick + ly
    mp3 = APoint(mp2x,mp3y)

    mp4 = APoint(mp1.x,mp3y)

    mp5y = ly + fold1
    mp5 = APoint(lx,mp5y)

    mp6 = APoint(mp2x,mp5y)

    mp7y = mp3y - fold1
    mp7 =APoint(lx,mp7y)

    mp8 = APoint(mp2x,mp7y)

    linemp1 = acad.model.addline(mp1,mp2)
    linemp2 = acad.model.addline(mp2,mp3)
    linemp3 = acad.model.addline(mp3,mp4)
    linemp4 = acad.model.addline(mp4,mp1)
    linemp5 = acad.model.addline(mp5,mp6);linemp5.color = 12
    linemp6 = acad.model.addline(mp7,mp8);linemp6.color = 12

    #For annotation
    anno = config["doors"]["annotation"]
    if anno == "y":
        dd1 = APoint(mp2+65,0)
        dim1 = acad.model.AddDimAligned(mp2, mp3, dd1)
        dd2 = APoint(mp2+40,0)
        dim2 = acad.model.AddDimAligned(mp6, mp8, dd2)
        dd3 = APoint(mp3+30)
        dim3 = acad.model.AddDimAligned(mp3, mp4, dd3)
        dim4 = acad.model.AddDimAligned(mp8, mp3, dd2)
        
    else:
            print("NO ANNOTATION")

    #For text box
    pp13 = lenght/2
    p100 = APoint((pp13+lx-90),(ly -30)) 
    thicktext = str(thick)
    if needtext == "y":
        ben = "UP"
        qty = "1"
        text = acad.model.addmtext(p100,210,"THICK "+thicktext +"MM    BEND "+ben + "       QTY "+ qty +" NOS" +"         "+block_name )
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")



    mp99y = mp7y + thick
    mp99 = APoint(lx,mp99y)

    newblock = acad.model.InsertBlock(mp99, block_name, 1, 1, 1, pi*270/180)
    try:
        newblock.explode()
    except KeyError:
        pass
    newblock.delete()

type = config["shell"]["type_panel"]
if type == 'v':

    #for section 1
    try:
        child_mp_v('door1_1 MP',500,0)
    except COMError:
        pass
    try:
        child_mp_v('door1_2 MP',1200,0)
    except COMError:
        pass
    try:
        child_mp_v('door1_3 MP',1900,0)
    except COMError:
        pass
    try:
        child_mp_v('door1_4 MP',2600,0)
    except COMError:
        pass
    try:
        child_mp_v('door1_5 MP',3300,0)
    except COMError:
        pass
    try:
        child_mp_v('door1_6 MP',3900,0)
    except COMError:
        pass

    #for section 2
    try:
        child_mp_v('door2_1 MP',500,-900)
    except COMError:
        pass
    try:
        child_mp_v('door2_2 MP',1200,-900)
    except COMError:
        pass
    try:
        child_mp_v('door2_3 MP',1900,-900)
    except COMError:
        pass
    try:
        child_mp_v('door2_4 MP',2600,-900)
    except COMError:
        pass
    try:
        child_mp_v('door2_5 MP',3300,-900)
    except COMError:
        pass
    try:
        child_mp_v('door2_6 MP',3900,-900)
    except COMError:
        pass

    #for section 3
    try:
        child_mp_v('door3_1 MP',500,-1800)
    except COMError:
        pass
    try:
        child_mp_v('door3_2 MP',1200,-1800)
    except COMError:
        pass
    try:
        child_mp_v('door3_3 MP',1900,-1800)
    except COMError:
        pass
    try:
        child_mp_v('door3_4 MP',2600,-1800)
    except COMError:
        pass
    try:
        child_mp_v('door3_5 MP',3300,-1800)
    except COMError:
        pass
    try:
        child_mp_v('door3_6 MP',3900,-1800)
    except COMError:
        pass

    #for section 4
    try:
        child_mp_v('door4_1 MP',500,-2700)
    except COMError:
        pass
    try:
        child_mp_v('door4_2 MP',1200,-2700)
    except COMError:
        pass
    try:
        child_mp_v('door4_3 MP',1900,-2700)
    except COMError:
        pass
    try:
        child_mp_v('door4_4 MP',2600,-2700)
    except COMError:
        pass
    try:
        child_mp_v('door4_5 MP',3300,-2700)
    except COMError:
        pass
    try:
        child_mp_v('door4_6 MP',3900,-2700)
    except COMError:
        pass

    #for section 5
    try:
        child_mp_v('door5_1 MP',500,-3600)
    except COMError:
        pass
    try:
        child_mp_v('door5_2 MP',1200,-3600)
    except COMError:
        pass
    try:
        child_mp_v('door5_3 MP',1900,-3600)
    except COMError:
        pass
    try:
        child_mp_v('door5_4 MP',2600,-3600)
    except COMError:
        pass
    try:
        child_mp_v('door5_5 MP',3300,-3600)
    except COMError:
        pass
    try:
        child_mp_v('door5_6 MP',3900,-3600)
    except COMError:
        pass

    #for section 6
    try:
        child_mp_v('door6_1 MP',500,-4500)
    except COMError:
        pass
    try:
        child_mp_v('door6_2 MP',1200,-4500)
    except COMError:
        pass
    try:
        child_mp_v('door6_3 MP',1900,-4500)
    except COMError:
        pass
    try:
        child_mp_v('door6_4 MP',2600,-4500)
    except COMError:
        pass
    try:
        child_mp_v('door6_5 MP',3300,-4500)
    except COMError:
        pass
    try:
        child_mp_v('door6_6 MP',3900,-4500)
    except COMError:
        pass

elif type == 'h':
    #for section 1
    try:
        child_mp_h('door1_1 MP',500,0)
    except COMError:
        pass
    try:
        child_mp_h('door1_2 MP',1200,0)
    except COMError:
        pass
    try:
        child_mp_h('door1_3 MP',1900,0)
    except COMError:
        pass
    try:
        child_mp_h('door1_4 MP',2600,0)
    except COMError:
        pass
    try:
        child_mp_h('door1_5 MP',3300,0)
    except COMError:
        pass
    try:
        child_mp_h('door1_6 MP',3900,0)
    except COMError:
        pass

    #for section 2
    try:
        child_mp_h('door2_1 MP',500,-900)
    except COMError:
        pass
    try:
        child_mp_h('door2_2 MP',1200,-900)
    except COMError:
        pass
    try:
        child_mp_h('door2_3 MP',1900,-900)
    except COMError:
        pass
    try:
        child_mp_h('door2_4 MP',2600,-900)
    except COMError:
        pass
    try:
        child_mp_h('door2_5 MP',3300,-900)
    except COMError:
        pass
    try:
        child_mp_h('door2_6 MP',3900,-900)
    except COMError:
        pass

    #for section 3
    try:
        child_mp_h('door3_1 MP',500,-1800)
    except COMError:
        pass
    try:
        child_mp_h('door3_2 MP',1200,-1800)
    except COMError:
        pass
    try:
        child_mp_h('door3_3 MP',1900,-1800)
    except COMError:
        pass
    try:
        child_mp_h('door3_4 MP',2600,-1800)
    except COMError:
        pass
    try:
        child_mp_h('door3_5 MP',3300,-1800)
    except COMError:
        pass
    try:
        child_mp_h('door3_6 MP',3900,-1800)
    except COMError:
        pass

    #for section 4
    try:
        child_mp_h('door4_1 MP',500,-2700)
    except COMError:
        pass
    try:
        child_mp_h('door4_2 MP',1200,-2700)
    except COMError:
        pass
    try:
        child_mp_h('door4_3 MP',1900,-2700)
    except COMError:
        pass
    try:
        child_mp_h('door4_4 MP',2600,-2700)
    except COMError:
        pass
    try:
        child_mp_h('door4_5 MP',3300,-2700)
    except COMError:
        pass
    try:
        child_mp_h('door4_6 MP',3900,-2700)
    except COMError:
        pass

    #for section 5
    try:
        child_mp_h('door5_1 MP',500,-3600)
    except COMError:
        pass
    try:
        child_mp_h('door5_2 MP',1200,-3600)
    except COMError:
        pass
    try:
        child_mp_h('door5_3 MP',1900,-3600)
    except COMError:
        pass
    try:
        child_mp_h('door5_4 MP',2600,-3600)
    except COMError:
        pass
    try:
        child_mp_h('door5_5 MP',3300,-3600)
    except COMError:
        pass
    try:
        child_mp_h('door5_6 MP',3900,-3600)
    except COMError:
        pass

    #for section 6
    try:
        child_mp_h('door6_1 MP',500,-4500)
    except COMError:
        pass
    try:
        child_mp_h('door6_2 MP',1200,-4500)
    except COMError:
        pass
    try:
        child_mp_h('door6_3 MP',1900,-4500)
    except COMError:
        pass
    try:
        child_mp_h('door6_4 MP',2600,-4500)
    except COMError:
        pass
    try:
        child_mp_h('door6_5 MP',3300,-4500)
    except COMError:
        pass
    try:
        child_mp_h('door6_6 MP',3900,-4500)
    except COMError:
        pass

    acad.app.zoomextents()

