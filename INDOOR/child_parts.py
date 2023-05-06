from pyautocad import Autocad, APoint
from comtypes import COMError
from configparser import ConfigParser
from math import pi
import sys
sys.path.append('INDOOR')

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

config = ConfigParser()
config.read('./INDOOR/gi_config_in.ini')

vchannel = int(config["shell"]["Vertical_channel_size"])
hchannel = int(config["shell"]["Horizontal_channel_size"])
thick = float(config["shell"]["sheet_thickness"])
needtext = config["doors"]["text_box"]

import win32com.client
acad1 = win32com.client.Dispatch("AutoCAD.Application")
doc = acad1.ActiveDocument
acadmodel = acad1.activedocument.modelspace

print('Using file ' + acad.doc.Name)

def hchannelf(a,b):

    block_name = a

    block = acad.doc.Blocks.Item(block_name)

    newblock = acad.model.InsertBlock(APoint(b,0), block_name, 1, 1, 1, 0)

    for obj in acad.iter_objects(block=block):
        if obj.length == hchannel:
            p = obj.startpoint
            break

    #for side and top view

    pnew = p + APoint(b,0)
    
    p1x = pnew.x + 80
    p1 = APoint(p1x,pnew.y)
    p2y = pnew.y + hchannel
    p2 = APoint(p1x,p2y)
    p3x = p1x + 20
    p3 = APoint(p3x,p2y)
    p4 = APoint(p3x,pnew.y)
    p5 = APoint(p3x,(pnew.y+thick))
    p6 = APoint(p1x+thick,p5.y)
    p7 = APoint(p6.x,p2y-thick)
    p8 = APoint(p3x,p7.y)

    line1 = acad.model.addline(p1,p2)
    line2 = acad.model.addline(p2,p3)
    line3 = acad.model.addline(p1,p4)
    line4 = acad.model.addline(p4,p5)
    line5 = acad.model.addline(p5,p6)
    line6 = acad.model.addline(p6,p7)
    line7 = acad.model.addline(p7,p8)
    line8 = acad.model.addline(p8,p3)

    #For annotation
    anno = config["doors"]["annotation"]
    if anno == "y":
        dd1 = APoint(p1-25,0)
        dim1 = acad.model.AddDimAligned(p1, p2, dd1)
        dd3 = APoint(p2+25)
        dim3 = acad.model.AddDimAligned(p2, p3, dd3)
        
        
    else:
            print("NO ANNOTATION")

    #For text box
    p100 = APoint((pnew.x-300),(pnew.y -30)) 
    thicktext = str(thick)
    if needtext == "y":
        ben = "DOWN"
        if a == 'h1_1':
            qty = int(config["section1_partition"]["partitons"]) -1
            qty1 = str(qty)
        elif a == 'h2_1':
            qty = int(config["section2_partition"]["partitons"]) -1
            qty1 = str(qty)
        elif a == 'h3_1':
            qty = int(config["section3_partition"]["partitons"])-1
            qty1 = str(qty)
        elif a== 'h4_1':
            qty = int(config["section4_partition"]["partitons"])-1
            qty1 = str(qty)
        elif a == 'h5_1':
            qty = int(config["section5_partition"]["partitons"])-1
            qty1 = str(qty)
        elif a == 'h6_1':
            qty = int(config["section6_partition"]["partitons"])-1
            qty1 = str(qty)
        text = acad.model.addmtext(p100,210,"THICK "+thicktext +"MM    BEND "+ben + "       QTY "+ qty1 +" NOS" +"         "+block_name )
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")


    
    try:
        newblock.explode()
    except KeyError:
        pass

    newblock.delete()

def vchannelf(a,b):
    block_name = a

    block = acad.doc.Blocks.Item(block_name)

    newblock = acad.model.InsertBlock(APoint(b+200,0), block_name, 1, 1, 1, 0)

    for obj in acad.iter_objects(block=block):
        if obj.length == (vchannel-thick-thick):
            p = obj.startpoint
            break
    
    #for side and top view

    pnew = p + APoint(b+200,0)
    
    p1y = pnew.y + 80
    p1 = APoint(pnew.x,p1y)
    p2x = pnew.x + vchannel
    p2 = APoint(p2x,p1y)
    p3y = p1y + 20
    p3 = APoint(p2x,p3y)
    p4 = APoint(pnew.x,p3y)
    p5 = APoint((pnew.x+thick),p3y)
    p6 = APoint(p5.x,(p1.y+thick))
    p7 = APoint(p2x-thick,p6.y)
    p8 = APoint(p7.x,p3y)

    line1 = acad.model.addline(p1,p2)
    line2 = acad.model.addline(p2,p3)
    line3 = acad.model.addline(p1,p4)
    line4 = acad.model.addline(p4,p5)
    line5 = acad.model.addline(p5,p6)
    line6 = acad.model.addline(p6,p7)
    line7 = acad.model.addline(p7,p8)
    line8 = acad.model.addline(p8,p3)

    #For annotation
    anno = config["doors"]["annotation"]
    if anno == "y":
        dd1 = APoint(p1-25)
        dim1 = acad.model.AddDimAligned(p1, p2, dd1)
        dd3 = APoint(p2+25)
        dim3 = acad.model.AddDimAligned(p2, p3, dd3)
        
        
    else:
            print("NO ANNOTATION")

    #For text box
    p100 = APoint((pnew.x-60)) 
    thicktext = str(thick)
    if needtext == "y":
        ben = "DOWN"
        qty1 = '1'
        text = acad.model.addmtext(p100,210,"THICK "+thicktext +"MM    BEND "+ben + "       QTY "+ qty1 +" NOS" +"         "+block_name )
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")


    
    try:
        newblock.explode()
    except KeyError:
        pass

    newblock.delete()


try:
    hchannelf('h1_1',3000)
except COMError:
    pass
try:
    hchannelf('h2_1',3500)
except COMError:
    pass
try:
    hchannelf('h3_1',4000)
except COMError:
    pass
try:
    hchannelf('h4_1',4500)
except COMError:
    pass
try:
    hchannelf('h5_1',5000)
except COMError:
    pass

try:
    vchannelf('u1',3000)
except COMError:
    pass
try:
    vchannelf('u2',3500)
except COMError:
    pass
try:
    vchannelf('u3',4000)
except COMError:
    pass
try:
    vchannelf('u4',4500)
except COMError:
    pass
try:
    vchannelf('u5',5000)
except COMError:
    pass

acad.app.zoomextents()