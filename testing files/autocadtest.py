from pyautocad import Autocad, APoint
from math import pi
import pythoncom
from comtypes import COMError

import win32com.client
acad = win32com.client.Dispatch("AutoCAD.Application")
acad.visible = True
acadmodel = acad.activedocument.modelspace

def APoint2(x, y = 0, z = 0):
     return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

print('Using file ' + acad.doc.Name)

#FOR FRESH DOCUMENT(DELETE AFTER CODE COMPLETE)
acad.doc.sendcommand("erase all  ")
acad.doc.purgeAll()

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

zleft = acad.doc.Blocks.Add(APoint(0), "zleft")
zright = acad.doc.Blocks.Add(APoint(0), "zright")

cut1 = zleft.addline(p5,p6);cut1.color = 50
cut2 = zleft.addline(p7,p8);cut2.color = 50
cut3 = zleft.addline(p9,p10);cut3.color = 50
cut4 = zleft.addline(p11,p12);cut4.color = 50
cut5 = zright.addarc(p3,6,0*pi/180,90*pi/180);cut5.color = 50
cut6 = zright.addarc(p2,6,270*pi/180,0*pi/180);cut6.color = 50
cut7 = zright.addarc(p1,6,180*pi/180,270*pi/180);cut7.color = 50
cut8 = zright.addarc(p4,6,90*pi/180,180*pi/180);cut8.color = 50


acad.model.InsertBlock(APoint(0), "zleft", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zright", 1, 1, 1, 0)


acad.app.zoomextents()