from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)
acad.prompt("Hello, Autocad from GaMeR\n")

print('Using file ' + acad.doc.Name)

#user inputs
l = int(input("Where to place: "))
lenght = int(input('Enter lenght: '))
width = int(input('Enter width: '))
fold = int(input("Enter folding lenght: "))
thick = float(input("Sheet Thickness: "))
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
anno = input("NEED ANNOTATION: ")
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
    text = acad.model.addmtext(p13,210,"THICK "+thicktext +"MM    BEND "+b + "       QTY "+ qty +" NOS")
    text.color = 80
    text.height = 23
    
else:
    print("NO text box")

acad.app.zoomextents()