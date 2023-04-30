from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

print('Using file ' + acad.doc.Name)

#user inputs
l = int(input("Where to place: "))
channel = input("L or U or Z CHANNEL (L/U/Z): ")
lenght = int(input('Enter lenght: '))
width = int(input('Enter width: '))
fold = int(input("Enter folding lenght: "))
thick = float(input("Sheet Thickness: "))

if channel == "l":
    off = thick *2
    len = lenght + fold - off

    pl1 = APoint(l,0)

    ppl2 = l + len
    pl2 = APoint(ppl2,0)

    pl3 = APoint(ppl2,width)

    pl4 = APoint(l,width)

    ppl8 = l + fold - thick
    pl8 = APoint(ppl8,0)

    pl9 = APoint(ppl8,width)

    #for drawing rectangle
    line1 = acad.model.AddLine(pl1, pl2)
    line2 = acad.model.AddLine(pl2, pl3)
    line3 = acad.model.AddLine(pl3, pl4)
    line4 = acad.model.AddLine(pl4, pl1)
    line7 = acad.model.addline(pl8,pl9)
    line7.color = 10

    #for top view
    ppl5 = width + 120
    pl5 = APoint(ppl2,ppl5)

    ppl6 = ppl2 - lenght
    pl6 = APoint(ppl6,ppl5)

    ppl7 = width + fold + 120
    pl7 = APoint(ppl6,ppl7)

    line5 = acad.model.AddLine(pl5, pl6)
    line6 = acad.model.AddLine(pl6, pl7)

    #For annotation
    anno = input("NEED ANNOTATION (Y/N): ")
    if anno == "y":
        ddl1 = APoint(pl3+25)
        dim1 = acad.model.AddDimAligned(pl3, pl4, ddl1)
        ddl2 = APoint(pl1-30)
        dim2 = acad.model.adddimaligned(pl1,pl4,ddl2)
        ddl3 = APoint(pl5-30)
        dim3 = acad.model.adddimaligned(pl5,pl6,ddl3)
        ddl4 = APoint(pl6-30)
        dim4 = acad.model.adddimaligned(pl6,pl7,ddl4)
        
       
    else:
        print("NO ANNOTATION")

    #For text box
    ppl10 = len/2
    pl10 = APoint((ppl10+l-90),-45) 
    thicktext = str(thick)
    needtext = input("Need TEXT BOX (Y/N): ")
    if needtext == "y":
        bend = input("BEND UP OR DOWN (U/D): ")
        qty = input("QUANTITY: ")
        if bend == "u":
            b = "UP"
        elif bend == "d":
            b = "DOWN"
        else:
            print("enter correct answer")
        text = acad.model.addmtext(pl10,210,"THICK "+thicktext +"MM    BEND "+b + "       QTY "+ qty +" NOS")
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")

    acad.app.zoomextents()      
    
elif channel == "u":
    off = thick*4
    len = lenght + fold + fold - off

    pu1 = APoint(l,0)

    ppu2 = l + len
    pu2 = APoint(ppu2,0)

    pu3 = APoint(ppu2,width)

    pu4 = APoint(l,width)

    ppu5 = l+ fold - thick
    pu5 = APoint(ppu5,width)

    pu6 = APoint(ppu5,0)

    ppu7 = l+ len - fold + thick
    pu7 = APoint(ppu7,0)

    pu8 = APoint(ppu7,width)

    #for drawing rectangle
    line1 = acad.model.AddLine(pu1, pu2)
    line2 = acad.model.AddLine(pu2, pu3)
    line3 = acad.model.AddLine(pu3, pu4)
    line4 = acad.model.AddLine(pu4, pu1)
    line5 = acad.model.addline(pu5,pu6)
    line6 = acad.model.addline(pu7,pu8)
    line5.color = 10
    line6.color = 10

    #for top view
    ppu9 = width + fold + 120
    pu9 = APoint(ppu7,ppu9)

    ppu10 = ppu9 - fold 
    pu10 = APoint(ppu7,ppu10)

    ppu11 = ppu7 - lenght
    pu11 = APoint(ppu11,ppu10)

    ppu12 = ppu10 + fold
    pu12 = APoint(ppu11,ppu12)

    line7 = acad.model.addline(pu9,pu10)
    line8 = acad.model.addline(pu10,pu11)
    line9 = acad.model.addline(pu11,pu12)


    

    #For annotation
    anno = input("NEED ANNOTATION (Y/N): ")
    if anno == "y":
        ddl1 = APoint(pu3+25)
        dim1 = acad.model.AddDimAligned(pu3, pu4, ddl1)
        ddl2 = APoint(pu1-30)
        dim2 = acad.model.adddimaligned(pu1,pu4,ddl2)
        ddl3 = APoint(pu10-30)
        dim3 = acad.model.adddimaligned(pu10,pu11,ddl3)
        ddl4 = APoint(pu12-30)
        dim4 = acad.model.adddimaligned(pu11,pu12,ddl4)
        
       
    else:
        print("NO ANNOTATION")

    #For text box
    ppu13 = len/2
    pu13 = APoint((ppu13+l-90),-45) 
    thicktext = str(thick)
    needtext = input("Need TEXT BOX (Y/N): ")
    if needtext == "y":
        bend = input("BEND UP OR DOWN (U/D): ")
        qty = input("QUANTITY: ")
        if bend == "u":
            b = "UP"
        elif bend == "d":
            b = "DOWN"
        else:
            print("enter correct answer")
        text = acad.model.addmtext(pu13,210,"THICK "+thicktext +"MM    BEND "+b + "       QTY "+ qty +" NOS")
        text.color = 80
        text.height = 23
        
    else:
        print("NO text box")    

    acad.app.zoomextents()

else:
    print("enter correct choice!")


