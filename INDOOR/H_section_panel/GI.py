from pyautocad import Autocad, APoint
from configparser import ConfigParser

import win32com.client
acad1 = win32com.client.Dispatch("AutoCAD.Application")
acad1.visible = True
acadmodel = acad1.activedocument.modelspace

config = ConfigParser()
config.read("gi_config_in.ini")

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR")

print('Using file ' + acad.doc.Name)

#FOR FRESH DOCUMENT(DELETE AFTER CODE COMPLETE)
acad.doc.sendcommand("erase all  ")
acad.doc.purgeAll()

#USER INPUTS
l = int(config["shell"]["where_to_place"])
lenght = int(config["shell"]["lenght"])
width = int(config["shell"]["width"])
thick = float(config["shell"]["sheet_thickness"])
tops = int(config["shell"]["Top_bottom_shell_size"]) - thick
sides = int(config["shell"]["side_shell_size"])- thick
zchanneltb = int(config["shell"]["Top_bottom_shell_size"])- thick
zchannelside = int(config["shell"]["side_shell_size"])- thick
vchannel = int(config["shell"]["Vertical_channel_size"])
hchannel = int(config["shell"]["Horizontal_channel_size"])
dclear = int(config["doors"]["door_clearence"])

#SHELL APOINTS
ps1 = APoint(l,0)

pps2 = l + lenght
ps2 = APoint(pps2,0)

ps3 = APoint(pps2,width)

ps4 = APoint(l,width)

pps5x = ps1.x + sides ; pps5y = ps1.y + tops
ps5 = APoint(pps5x,pps5y)

pps6x = ps2.x - sides
ps6 = APoint(pps6x,pps5y)

pps7y = ps3.y - tops
ps7 = APoint(pps6x,pps7y)

ps8 = APoint(pps5x,pps7y)


# FOR Z CHANNEL
ppz1x = l + thick ; ppz1y = zchanneltb
pz1 = APoint(ppz1x,ppz1y)  #for left 

ppz2y = width - zchanneltb
pz2 = APoint(ppz1x,ppz2y)

ppz3x = ppz1x + zchannelside
pz3 = APoint(ppz3x,ppz2y)

pz4 = APoint(ppz3x,ppz1y)

ppz5x = l + lenght - thick
pz5 = APoint(ppz5x,ppz1y)    #for right

ppz6y = width - zchanneltb
pz6 = APoint(ppz5x,ppz6y)

ppz7x = ppz5x - zchannelside
pz7 = APoint(ppz7x,ppz6y)

pz8 = APoint(ppz7x,ppz1y)

ppz9x = ppz1x + thick     
pz9 = APoint(ppz9x,ppz1y)

pz10 = APoint(ppz9x,ppz2y)

ppz11x = ppz3x - thick
pz11 = APoint(ppz11x,ppz2y)

pz12 = APoint(ppz11x,ppz1y)

ppz13y = ppz2y + zchanneltb - thick
pz13 = APoint(ppz1x,ppz13y)

ppz14x = l - thick + lenght
pz14 = APoint(ppz14x,ppz13y)

zleft = acad.doc.Blocks.Add(APoint(0), "zleft")
zright = acad.doc.Blocks.Add(APoint(0), "zright")
ztop = acad.doc.Blocks.Add(APoint(0), "ztop")
zbottom = acad.doc.Blocks.Add(APoint(0), "zbottom")

#linez1 = zleft.addline(pz1,pz2);linez1.color = 6
linez2 = zleft.addline(pz11,pz3);linez2.color = 6
linez3 = zright.addline(pz11,pz3);linez2.color = 6;linez3.move(pz12,pz8)
#linez3 = zleft.addline(pz3,pz4);linez3.color = 6
#linez4 = zleft.addline(pz4,pz1);linez4.color = 6
#linez5 = zright.addline(pz5,pz6);linez5.color = 6
#linez6 = zright.addline(pz6,pz7);linez6.color = 6
#linez7 = zright.addline(pz7,pz8);linez7.color = 6
#linez8 = zright.addline(pz8,pz5);linez8.color = 6
linez9 = zleft.addline(pz12,pz4);linez9.color = 6
linez10 = zleft.addline(pz11,pz12);linez10.color = 6
linez11 = zright.addline(pz9,pz10); linez11.move(pz1,pz8);linez11.color = 6
#linez12 = zright.addline(pz11,pz12); linez12.move(pz4,pz5);linez12.color = 6
#linez13 = ztop.addline(pz2,pz13);linez13.color = 6
#linez14 = ztop.addline(pz13,pz14);linez14.color = 6
#linez15 = ztop.addline(pz14,pz6);linez15.color = 6
linez16 = ztop.addline(pz3,pz7);linez16.color = 6
#linez17 = zbottom.addline(pz2,pz13);linez17.color = 6;linez17.move(pz13,pz1)
#linez18 = zbottom.addline(pz13,pz14);linez18.color = 6;linez18.move(pz13,pz1)
#linez19 = zbottom.addline(pz14,pz6);linez19.color = 6;linez19.move(pz13,pz1)
#linez20 = zbottom.addline(pz6,pz2);linez20.color = 6;linez20.move(pz13,pz1)

acad.model.InsertBlock(APoint(0), "ztop", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zbottom", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zleft", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zright", 1, 1, 1, 0)

#FOR DRAWING SHELL
shellleft = acad.doc.Blocks.Add(APoint(0), "shellleft")
shellright = acad.doc.Blocks.Add(APoint(0), "shellright")
shelltop = acad.doc.Blocks.Add(APoint(0), "shelltop")
shellbottom = acad.doc.Blocks.Add(APoint(0), "shellbottom")
linep1 = zbottom.AddLine(ps1, ps2);linep1.color = 6
linep2 = zright.AddLine(ps2, ps3);linep2.color = 6
linep3 = ztop.AddLine(ps3, ps4);linep3.color = 6
linep4 = zleft.AddLine(ps4, ps1);linep4.color = 6
linep5 = zbottom.AddLine(ps5, ps6);linep5.color = 6
#linep6 = shellright.AddLine(ps6, ps7)
#linep7 = shelltop.AddLine(ps7, ps8)
#linep8 = shellleft.AddLine(ps8, ps5)
linep9 = zbottom.AddLine(ps1, ps5);linep9.color = 6
linep10 = ztop.AddLine(ps4, ps8);linep10.color = 6
linep11 = ztop.AddLine(ps7, ps3);linep11.color = 6
linep12 = zbottom.AddLine(ps2, ps6);linep12.color = 6

linep13 = zleft.AddLine(ps1, ps5);linep13.color = 6
linep14 = zleft.AddLine(ps4, ps8);linep14.color = 6
linep15 = zright.AddLine(ps7, ps3);linep15.color = 6
linep16 = zright.AddLine(ps2, ps6);linep16.color = 6

acad.model.InsertBlock(APoint(0), "shellleft", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "shellright", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "shelltop", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "shellbottom", 1, 1, 1, 0)


#FOR VERTICAL SECTIONS
section = config["section"]["Sections"]
if section == "2":         #FOR 2 SECTIONS
    import section2


elif section =="3":      #FOR 3 SECTIONS
   import section3


elif section == "4":       #FOR 4 SECTIONS
    import section4
    
else:
    print("enter correct choice in section")

