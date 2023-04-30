from pyautocad import Autocad, APoint
from configparser import ConfigParser

config = ConfigParser()
config.read('./OUTDOOR/gi_config_out.ini')

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
tops = int(config["shell"]["Top_bottom_shell_size"])
sides = int(config["shell"]["side_shell_size"])
zchanneltb = int(config["shell"]["Z_channel_top_bottom_size"])
zchannelside = int(config["shell"]["Z_channel_side_size"])
vchannel = int(config["shell"]["Vertical_channel_size"])
hchannel = int(config["shell"]["Horizontal_channel_size"])
dclear = int(config["doors"]["door_to_door_clearence"])
dclearx = int(config["doors"]["door_clearence_X"])
dcleary = int(config["doors"]["door_clearence_Y"])
dclearmid = int(config["doors"]["door_clearence_MID"])

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

#FOR DRAWING SHELL
shellleft = acad.doc.Blocks.Add(APoint(0), "shellleft")
shellright = acad.doc.Blocks.Add(APoint(0), "shellright")
shelltop = acad.doc.Blocks.Add(APoint(0), "shelltop")
shellbottom = acad.doc.Blocks.Add(APoint(0), "shellbottom")
linep1 = shellbottom.AddLine(ps1, ps2)
linep2 = shellright.AddLine(ps2, ps3)
try:
    linep18 = linep2.offset(thick)
except KeyError:
    pass

linep3 = shelltop.AddLine(ps3, ps4)
linep4 = shellleft.AddLine(ps4, ps1)
try:
    linep17 = linep4.offset(thick)
except KeyError:
    pass

linep5 = shellbottom.AddLine(ps5, ps6)
try:
    linep19 = linep5.offset(-thick)
    
except KeyError:
    pass

linep6 = shellright.AddLine(ps6, ps7)
linep7 = shelltop.AddLine(ps7, ps8)
try:
    linep21 = linep7.offset(-thick)
except KeyError:
    pass
linep8 = shellleft.AddLine(ps8, ps5)

linep23 = shellbottom.addline(ps5,APoint(ps5.x,(ps5.y - thick)))
linep24 = shellbottom.addline(ps6,APoint(ps6.x,(ps6.y - thick)))
linep25 = shelltop.addline(ps7,APoint(ps7.x,(ps7.y + thick)))
linep26 = shelltop.addline(ps8,APoint(ps8.x,(ps8.y + thick)))
linep27 = shellright.addline(APoint(ps6.x+thick,ps6.y-thick),APoint(ps7.x+thick,ps7.y+thick))
linep28 = shellright.addline(APoint(linep27.endpoint),APoint(linep25.endpoint))
linep29 = shellright.addline(APoint(linep27.startpoint),APoint(linep24.endpoint))
linep30 = shellleft.addline(APoint(ps5.x-thick,ps5.y-thick),APoint(ps8.x-thick,ps8.y+thick))
linep31 = shellleft.addline(APoint(linep30.startpoint),APoint(linep23.endpoint))
linep31 = shellleft.addline(APoint(linep30.endpoint),APoint(linep26.endpoint))


acad.model.InsertBlock(APoint(0), "shellleft", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "shellright", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "shelltop", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "shellbottom", 1, 1, 1, 0)

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

linep14 = shellleft.AddLine(APoint(linep30.endpoint), pz13)
linep10 = shelltop.AddLine(APoint(linep30.endpoint), pz13)
linep9 = shellleft.AddLine(APoint(linep30.startpoint), ps1)
linep11 = shellbottom.AddLine(APoint(linep30.startpoint), ps1)
linep12 = shellright.AddLine(APoint(linep27.startpoint), ps2)
linep13 = shellbottom.AddLine(APoint(linep27.startpoint), ps2)
linep14 = shellright.AddLine(APoint(linep27.endpoint), ps3)
linep15 = shelltop.AddLine(APoint(linep27.endpoint), ps3)

zleft = acad.doc.Blocks.Add(APoint(0), "zleft")
zright = acad.doc.Blocks.Add(APoint(0), "zright")
ztop = acad.doc.Blocks.Add(APoint(0), "ztop")
zbottom = acad.doc.Blocks.Add(APoint(0), "zbottom")

linez1 = zleft.addline(pz1,pz2);linez1.color = 6
linez2 = zleft.addline(pz2,pz3);linez2.color = 6
#linez3 = zleft.addline(pz3,pz4);linez3.color = 6
linez4 = zleft.addline(pz4,pz1);linez4.color = 6
linez5 = zright.addline(pz5,pz6);linez5.color = 6
linez6 = zright.addline(pz6,pz7);linez6.color = 6
#linez7 = zright.addline(pz7,pz8);linez7.color = 6
linez8 = zright.addline(pz8,pz5);linez8.color = 6
linez9 = zleft.addline(pz9,pz10);linez9.color = 6
linez10 = zleft.addline(pz11,pz12);linez10.color = 6
linez11 = zright.addline(pz9,pz10); linez11.move(pz1,pz8);linez11.color = 6
linez12 = zright.addline(pz11,pz12); linez12.move(pz4,pz5);linez12.color = 6
linez13 = ztop.addline(pz2,pz13);linez13.color = 6
linez14 = ztop.addline(pz13,pz14);linez14.color = 6
linez15 = ztop.addline(pz14,pz6);linez15.color = 6
linez16 = ztop.addline(pz6,pz2);linez16.color = 6
linez17 = zbottom.addline(pz2,pz13);linez17.color = 6;linez17.move(pz13,pz1)
linez18 = zbottom.addline(pz13,pz14);linez18.color = 6;linez18.move(pz13,pz1)
linez19 = zbottom.addline(pz14,pz6);linez19.color = 6;linez19.move(pz13,pz1)
linez20 = zbottom.addline(pz6,pz2);linez20.color = 6;linez20.move(pz13,pz1)

acad.model.InsertBlock(APoint(0), "ztop", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zbottom", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zleft", 1, 1, 1, 0)
acad.model.InsertBlock(APoint(0), "zright", 1, 1, 1, 0)


#FOR VERTICAL SECTIONS
section = config["section"]["Sections"]
if section == "2":         #FOR 2 SECTIONS
    import section2

elif section =="3":      #FOR 3 SECTIONS
   import section3

elif section == "4":       #FOR 4 SECTIONS
    import section4
    
elif section == "5":
    import section5

elif section == "6":
    import section6

else:
    print("enter correct choice in section")
