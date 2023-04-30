from pyautocad import Autocad, APoint
from comtypes import COMError
from configparser import ConfigParser

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

import win32com.client
acad1 = win32com.client.Dispatch("AutoCAD.Application")
doc = acad1.ActiveDocument
acadmodel = acad1.activedocument.modelspace

config = ConfigParser()
config.read("gi_config_in.ini")

print('Using file ' + acad.doc.Name)

block1 = acad.get_selection(text='Select objects')

for x in block1:
    print(x.name)

block_name = x.name
block = acad.doc.Blocks.Item(block_name)


line_count = []
for entity in block:
    if entity.EntityName == "AcDbLine":
        line_count.append(entity.length)


#user inputs
l = int(config["shell"]["where_to_place"]) + 4000
lenght = int(line_count[0])
width = int(line_count[1])
fold = int(config["doors"]["folding_lenght"])
thick = float(config["doors"]["door_thick"])
fold1 = fold - thick
off = thick*2
len = lenght + fold1 + l
wid = width + fold1

pp1 = l + fold1
p1 = APoint(pp1, 0)

pp2 = len - off
p2 = APoint(pp2, 0)

p3 = APoint(pp2,fold1)

pp4 = pp2 + fold1
p4 = APoint(pp4,fold1)

pp5 = wid - off
p5 = APoint(pp4,pp5)

p6 = APoint(pp2,pp5)

pp7 = pp5 + fold1
p7 = APoint(pp2,pp7)

p8 = APoint(pp1,pp7)

p9 = APoint(pp1,pp5)

p10 = APoint(l,pp5)

p11 = APoint(l,fold1)

p12 = APoint(pp1,fold1)

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
line13.color = 10
line14.color = 10
line15.color = 10
line16.color = 10

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
p13 = APoint((pp13+l-90),-30) 
thicktext = str(thick)
needtext = "y"
if needtext == "y":
    b = "DOWN"
    qty = "1"
    text = acad.model.addmtext(p13,210,"THICK "+thicktext +"MM    BEND "+b + "       QTY "+ qty +" NOS")
    text.color = 80
    text.height = 23
    
else:
    print("NO text box")

end = input('IS IT END doors')
if end == "y":
    p99x = p12.x + 30 - thick - thick ;p99y = p12.y + 25 - thick - thick
    p99 = APoint(p99x,p99y)
elif end == "n":
    p99x = p12.x + 30 - thick ;p99y = p12.y + 15 - thick
    p99 = APoint(p99x,p99y)
else:
    print("choose correct choice")

newblock = acad.model.InsertBlock(p99, block_name, 1, 1, 1, 0)

acad.app.zoomextents()

