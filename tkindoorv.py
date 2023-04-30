
import customtkinter 
import configparser
import sys
import os

def top(a):

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme('dark-blue')

    a.title("GaMeR")
    a.geometry("680x500")
    a.resizable(False, False)
    a.attributes("-topmost", True)

    config = configparser.RawConfigParser()
    config.read('./INDOOR/V_section_panel/gi_config_in.ini')

    #for function place here

    def update(section, key, value):
        #Update config using section key and the value to change
        #call this when you want to update a value in configuation file
        # with some changes you can save many values in many sections
        config.set(section, key, value )
        with open('./INDOOR/V_section_panel/gi_config_in.ini', 'w') as output:
            config.write(output)

    def save():
        l = lenght.get()
        update('shell','lenght',l)
        w = width.get()
        update('shell','width',w)
        t = thick.get()
        update('shell','sheet_thickness',t)
        p = place.get()
        update('shell','where_to_place',p)
        s = var.get()
        update('section','Sections',s)
        d= dthick.get()
        update('doors','door_thick',d)
        dc = dclear.get()
        update('doors','door_to_door_clearence',dc)
        dx = dclearx.get()
        update('doors','door_clearence_x',dx)
        dy= dcleary.get()
        update('doors','door_clearence_y',dy)
        lx = lockx.get()
        update('doors','lock_clearence_x',lx)
        ly = locky.get()
        update('doors','lock_clearence_y',ly)
        dmc = dm.get()
        update('doors','door_clearence_mid',dmc)
        inch = varinch.get()
        update('doors','inches',inch)
        ix = inchx.get()
        update('doors','inches_size_x',ix)
        iy = inchy.get()
        update('doors','inches_size_y',iy)
        update('covers','cover_thick',cthick.get())
        update('covers','cover_clearence_x',cx.get())
        update('covers','cover_clearence_y',cy.get())
        update('mounting_plate','mounting_plate_clearence_x',mx.get())
        update('mounting_plate','mounting_plate_clearence_y',my.get())
        update('mounting_plate','mounting_plate_top_clearence',mt.get())
        update('mounting_plate','mounting_plate_bottom_clearence',mb.get())

        #for covers list

        cov = ['sec1','sec2','sec3','sec4','sec5','sec6']
        mp = ['sec1','sec2','sec3','sec4','sec5','sec6']

        
        # for section 1 updation
        update('section1_partition','partitons',sec1part.get())
        update('section','sec_1',sec1.get())
        update('section1_partition','part1',sec1part1.get())
        update('section1_partition','part2',sec1part2.get())
        update('section1_partition','part3',sec1part3.get())
        update('section1_partition','part4',sec1part4.get())
        update('section1_partition','part5',sec1part5.get())

        if csec1.get() == 'sec1':
            cov.append('sec1')
            update('covers','needcovers',cov)
        else:
            cov.remove('sec1')
            update('covers','needcovers',cov)

        if msec1.get() == 'sec1':
            mp.append('sec1')
            update('mounting_plate','need_mounting_plate',mp)
        else:
            mp.remove('sec1')
            update('mounting_plate','need_mounting_plate',mp)

        #for section 2 updation
        
        update('section2_partition','partitons',sec2part.get())
        update('section','sec_2',sec2.get())
        update('section2_partition','part1',sec2part1.get())
        update('section2_partition','part2',sec2part2.get())
        update('section2_partition','part3',sec2part3.get())
        update('section2_partition','part4',sec2part4.get())
        update('section2_partition','part5',sec2part5.get())

        if csec2.get() == 'sec2':
            cov.append('sec2')
            update('covers','needcovers',cov)
        else:
            cov.remove('sec2')
            update('covers','needcovers',cov)

        if msec2.get() == 'sec2':
            mp.append('sec2')
            update('mounting_plate','need_mounting_plate',mp)
        else:
            mp.remove('sec2')
            update('mounting_plate','need_mounting_plate',mp)

        #for section 3 updation
        
        update('section3_partition','partitons',sec3part.get())
        update('section','sec_3',sec3.get())
        update('section3_partition','part1',sec3part1.get())
        update('section3_partition','part2',sec3part2.get())
        update('section3_partition','part3',sec3part3.get())
        update('section3_partition','part4',sec3part4.get())
        update('section3_partition','part5',sec3part5.get())

        if csec3.get() == 'sec3':
            cov.append('sec3')
            update('covers','needcovers',cov)
        else:
            cov.remove('sec3')
            update('covers','needcovers',cov)

        if msec3.get() == 'sec3':
            mp.append('sec3')
            update('mounting_plate','need_mounting_plate',mp)
        else:
            mp.remove('sec3')
            update('mounting_plate','need_mounting_plate',mp)

        #for section 4 updation
        
        update('section4_partition','partitons',sec4part.get())
        update('section','sec_4',sec4.get())
        update('section4_partition','part1',sec4part1.get())
        update('section4_partition','part2',sec4part2.get())
        update('section4_partition','part3',sec4part3.get())
        update('section4_partition','part4',sec4part4.get())
        update('section4_partition','part5',sec4part5.get())

        if csec4.get() == 'sec4':
            cov.append('sec4')
            update('covers','needcovers',cov)
        else:
            cov.remove('sec4')
            update('covers','needcovers',cov)

        if msec4.get() == 'sec4':
            mp.append('sec4')
            update('mounting_plate','need_mounting_plate',mp)
        else:
            mp.remove('sec4')
            update('mounting_plate','need_mounting_plate',mp)

        #for section 5 updation
        
        update('section5_partition','partitons',sec5part.get())
        update('section','sec_5',sec5.get())
        update('section5_partition','part1',sec5part1.get())
        update('section5_partition','part2',sec5part2.get())
        update('section5_partition','part3',sec5part3.get())
        update('section5_partition','part4',sec5part4.get())
        update('section5_partition','part5',sec5part5.get())

        if csec5.get() == 'sec5':
            cov.append('sec5')
            update('covers','needcovers',cov)
        else:
            cov.remove('sec5')
            update('covers','needcovers',cov)

        if msec5.get() == 'sec5':
            mp.append('sec5')
            update('mounting_plate','need_mounting_plate',mp)
        else:
            mp.remove('sec5')
            update('mounting_plate','need_mounting_plate',mp)

        #for section 6 updation
        
        update('section6_partition','partitons',sec6part.get())
        update('section','sec_6',sec6.get())
        update('section6_partition','part1',sec6part1.get())
        update('section6_partition','part2',sec6part2.get())
        update('section6_partition','part3',sec6part3.get())
        update('section6_partition','part4',sec6part4.get())
        update('section6_partition','part5',sec6part5.get())

        if csec6.get() == 'sec6':
            cov.append('sec6')
            update('covers','needcovers',cov)
        else:
            cov.remove('sec6')
            update('covers','needcovers',cov)

        if msec6.get() == 'sec6':
            mp.append('sec6')
            update('mounting_plate','need_mounting_plate',mp)
        else:
            mp.remove('sec6')
            update('mounting_plate','need_mounting_plate',mp)

            

        os.system('python ./INDOOR/V_section_panel/GI.py')



    head = customtkinter.CTkLabel(a,text='INDOOR PANEL --- VERTICAL TYPE')
    head.grid(row=0,column=0,padx=20,pady=7)

    tabview = customtkinter.CTkTabview(a)
    tabview.grid(row=1,column=0,sticky=customtkinter.NSEW)

    tab_1 = tabview.add("SHELL")
    tab_2 = tabview.add("Doors")
    tab_3 = tabview.add("Covers & MP")
    tab_4 = tabview.add("Section1") 
    tab_5 = tabview.add("Section2") 
    tab_6 = tabview.add("Section3") 
    tab_7 = tabview.add("Section4")
    tab_8 = tabview.add("Section5")
    tab_9 = tabview.add("Section6")
    tabview.set("SHELL")  # set currently visible tab

    #for frame1

    frame1 = customtkinter.CTkFrame(tab_1)
    frame1.grid(row=0, column=0, padx=20, pady=20)

    label1= customtkinter.CTkLabel(frame1,text="Full Lenght :")
    label1.grid(row=1,column=0,padx=20,pady=5)

    lenght = customtkinter.CTkEntry(frame1,width=100)
    lenght1 = config.get('shell','lenght')
    lenght.insert(0,lenght1)
    lenght.grid(row=1,column=1,padx=15,pady=5)

    label2 = customtkinter.CTkLabel(frame1,text='Full Width :')
    label2.grid(row=1,column=2,padx=20,pady=5)

    width = customtkinter.CTkEntry(frame1,width=100)
    width1 = config.get('shell','width')
    width.insert(0,width1)
    width.grid(row=1,column=3,padx=15,pady=5)

    label3= customtkinter.CTkLabel(frame1,text="Thickness :")
    label3.grid(row=2,column=0,padx=20,pady=5)

    thick = customtkinter.CTkEntry(frame1,width=100)
    thick1 = config.get('shell','sheet_thickness')
    thick.insert(0,thick1)
    thick.grid(row=2,column=1,padx=15,pady=5)

    label4= customtkinter.CTkLabel(frame1,text=" Place :")
    label4.grid(row=2,column=2,padx=20,pady=5)

    place = customtkinter.CTkEntry(frame1,width=100)
    place1 = config.get('shell','where_to_place')
    place.insert(0,place1)
    place.grid(row=2,column=3,padx=15,pady=5)

    label5= customtkinter.CTkLabel(frame1,text="Top and Bottom shell size :")
    label5.grid(row=3,column=0,padx=10,pady=5)

    top = customtkinter.CTkEntry(frame1,width=100)
    top1 = config.get('shell','top_bottom_shell_size')
    top.insert(0,top1)
    top.grid(row=3,column=1,padx=15,pady=5)

    label6= customtkinter.CTkLabel(frame1,text=" Side shell size :")
    label6.grid(row=4,column=0,padx=20,pady=5)

    side = customtkinter.CTkEntry(frame1,width=100)
    side1 = config.get('shell','side_shell_size')
    side.insert(0,side1)
    side.grid(row=4,column=1,padx=15,pady=5)

    label7= customtkinter.CTkLabel(frame1,text="Vertical channel size :")
    label7.grid(row=3,column=2,padx=10,pady=5)

    v = customtkinter.CTkEntry(frame1,width=100)
    v1 = config.get('shell','vertical_channel_size')
    v.insert(0,v1)
    v.grid(row=3,column=3,padx=15,pady=5)

    label8= customtkinter.CTkLabel(frame1,text="Horizontal channel size :")
    label8.grid(row=4,column=2,padx=20,pady=5)

    h = customtkinter.CTkEntry(frame1,width=100)
    h1 = config.get('shell','horizontal_channel_size')
    h.insert(0,h1)
    h.grid(row=4,column=3,padx=15,pady=5)

        
    #for frame2

    frame2 = customtkinter.CTkFrame(tab_1)
    frame2.grid(row=1,column=0,padx=20,pady=20)

    var = customtkinter.IntVar()

    radiobutton_1 = customtkinter.CTkRadioButton(master=frame2, text="Section 1",value=1,variable=var)                                        
    radiobutton_2 = customtkinter.CTkRadioButton(master=frame2, text="Section 2",value=2,variable=var)
    radiobutton_3 = customtkinter.CTkRadioButton(master=frame2, text="Section 3",value=3,variable=var)
    radiobutton_4 = customtkinter.CTkRadioButton(master=frame2, text="Section 4",value=4,variable=var)
    radiobutton_5 = customtkinter.CTkRadioButton(master=frame2, text="Section 5",value=5,variable=var)
    radiobutton_6 = customtkinter.CTkRadioButton(master=frame2, text="Section 6",value=6,variable=var)

    radiobutton_1.grid(row=0,column=0,padx=3,pady=10)
    radiobutton_2.grid(row=0,column=1,padx=3,pady=10)
    radiobutton_3.grid(row=0,column=2,padx=3,pady=10)
    radiobutton_4.grid(row=0,column=3,padx=3,pady=10)
    radiobutton_5.grid(row=0,column=4,padx=3,pady=10)
    radiobutton_6.grid(row=0,column=5,padx=3,pady=10)

    s = config.get('section','sections')
    if s == "1":
        radiobutton_1.select()
    elif s == '2':
        radiobutton_2.select()
    elif s== '3':
        radiobutton_3.select()
    elif s== '4':
        radiobutton_4.select()
    elif s== '5':
        radiobutton_5.select()
    elif s== '6':
        radiobutton_6.select()
                                    
    button1 = customtkinter.CTkButton(tab_1,text="SAVE",command=save)
    button1.grid(row=2,column=0)

    #for doors tab (tab_2)

    tab2frame = customtkinter.CTkFrame(tab_2)
    tab2frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label1= customtkinter.CTkLabel(tab2frame,text="Door thick :")
    label1.grid(row=1,column=0,padx=30,pady=10)

    dthick = customtkinter.CTkEntry(tab2frame,width=100)
    dthick1 = config.get('doors','door_thick')
    dthick.insert(0,dthick1)
    dthick.grid(row=1,column=1,padx=15,pady=10)

    label2 = customtkinter.CTkLabel(tab2frame,text='Door to door CLearence :')
    label2.grid(row=1,column=2,padx=30,pady=10)

    dclear = customtkinter.CTkEntry(tab2frame,width=100)
    dclear1 = config.get('doors','door_to_door_clearence')
    dclear.insert(0,dclear1)
    dclear.grid(row=1,column=3,padx=15,pady=10)

    label3= customtkinter.CTkLabel(tab2frame,text="Door clearence X :")
    label3.grid(row=2,column=0,padx=30,pady=10)

    dclearx = customtkinter.CTkEntry(tab2frame,width=100)
    dclearx1 = config.get('doors','door_clearence_x')
    dclearx.insert(0,dclearx1)
    dclearx.grid(row=2,column=1,padx=15,pady=10)

    label4= customtkinter.CTkLabel(tab2frame,text="Door clearence Y :")
    label4.grid(row=2,column=2,padx=30,pady=10)

    dcleary = customtkinter.CTkEntry(tab2frame,width=100)
    dcleary1 = config.get('doors','door_clearence_y')
    dcleary.insert(0,dcleary1)
    dcleary.grid(row=2,column=3,padx=15,pady=10)

    label5= customtkinter.CTkLabel(tab2frame,text="Lock clearence X :")
    label5.grid(row=3,column=0,padx=30,pady=10)

    lockx = customtkinter.CTkEntry(tab2frame,width=100)
    lockx1 = config.get('doors','lock_clearence_x')
    lockx.insert(0,lockx1)
    lockx.grid(row=3,column=1,padx=15,pady=10)

    label6= customtkinter.CTkLabel(tab2frame,text="Lock clearence Y :")
    label6.grid(row=3,column=2,padx=30,pady=10)

    locky = customtkinter.CTkEntry(tab2frame,width=100)
    locky1 = config.get('doors','lock_clearence_y')
    locky.insert(0,locky1)
    locky.grid(row=3,column=3,padx=15,pady=10)

    label7= customtkinter.CTkLabel(tab2frame,text="Door Mid Clearence :")
    label7.grid(row=4,column=0,padx=30,pady=10)

    dm = customtkinter.CTkEntry(tab2frame,width=100)
    dm1 = config.get('doors','door_clearence_mid')
    dm.insert(0,dm1)
    dm.grid(row=4,column=1,padx=15,pady=10)

    label8= customtkinter.CTkLabel(tab2frame,text="Need INCHES :")
    label8.grid(row=4,column=2,padx=30,pady=10)

    inchframe = customtkinter.CTkFrame(tab2frame)
    inchframe.grid(row=4,column=3)

    varinch = customtkinter.StringVar()

    radioinch = customtkinter.CTkRadioButton(master=inchframe, text="YES",value='y',variable=varinch,width=4)                                        
    radioinch2 = customtkinter.CTkRadioButton(master=inchframe, text="NO",value='n',variable=varinch,width=4)
    radioinch.grid(row=0,column=0)
    radioinch2.grid(row=0,column=1)
    inc = config.get('doors','inches')
    if inc == 'y':
        radioinch.select()
    elif inc == 'n':
        radioinch2.select()

    label9= customtkinter.CTkLabel(tab2frame,text="Inch size X :")
    label9.grid(row=5,column=0,padx=30,pady=10)

    inchx = customtkinter.CTkEntry(tab2frame,width=100)
    inchx1 = config.get('doors','inches_size_x')
    inchx.insert(0,inchx1)
    inchx.grid(row=5,column=1,padx=15,pady=10)

    label10= customtkinter.CTkLabel(tab2frame,text="Inch size Y :")
    label10.grid(row=5,column=2,padx=30,pady=10)

    inchy = customtkinter.CTkEntry(tab2frame,width=100)
    inchy1 = config.get('doors','inches_size_y')
    inchy.insert(0,inchy1)
    inchy.grid(row=5,column=3,padx=15,pady=10)

    button1 = customtkinter.CTkButton(tab_2,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    #for section1 tab (tab_4)

    tab4frame = customtkinter.CTkFrame(tab_4)
    tab4frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label11= customtkinter.CTkLabel(tab4frame,text="Section 1 size :")
    label11.grid(row=0,column=0,padx=30,pady=10)

    sec1 = customtkinter.CTkEntry(tab4frame,width=100)
    sec11 = config.get('section','sec_1')
    sec1.insert(0,sec11)
    sec1.grid(row=0,column=1,padx=15,pady=10)

    label12= customtkinter.CTkLabel(tab4frame,text="Partitions in Section1:")
    label12.grid(row=1,column=0,padx=30,pady=10)

    sec1part = customtkinter.CTkOptionMenu(tab4frame,values=['1','2','3','4','5','6'])
    sec1p = config.get('section1_partition','partitons')
    sec1part.set(sec1p)
    sec1part.grid(row=1,column=1)

    button1 = customtkinter.CTkButton(tab_4,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    label13= customtkinter.CTkLabel(tab4frame,text="partition 1 size :")
    label13.grid(row=0,column=3,padx=30,pady=10)

    sec1part1 = customtkinter.CTkEntry(tab4frame,width=100)
    sec1part11 = config.get('section1_partition','part1')
    sec1part1.insert(0,sec1part11)
    sec1part1.grid(row=0,column=4,padx=15,pady=10)

    label14= customtkinter.CTkLabel(tab4frame,text="partition 2 size :")
    label14.grid(row=1,column=3,padx=30,pady=10)

    sec1part2 = customtkinter.CTkEntry(tab4frame,width=100)
    sec1part21 = config.get('section1_partition','part2')
    sec1part2.insert(0,sec1part21)
    sec1part2.grid(row=1,column=4,padx=15,pady=10)

    label15= customtkinter.CTkLabel(tab4frame,text="partition 3 size :")
    label15.grid(row=2,column=3,padx=30,pady=10)

    sec1part3 = customtkinter.CTkEntry(tab4frame,width=100)
    sec1part31 = config.get('section1_partition','part3')
    sec1part3.insert(0,sec1part31)
    sec1part3.grid(row=2,column=4,padx=15,pady=10)

    label16= customtkinter.CTkLabel(tab4frame,text="partition 4 size :")
    label16.grid(row=3,column=3,padx=30,pady=10)

    sec1part4 = customtkinter.CTkEntry(tab4frame,width=100)
    sec1part41 = config.get('section1_partition','part4')
    sec1part4.insert(0,sec1part41)
    sec1part4.grid(row=3,column=4,padx=15,pady=10)

    label17= customtkinter.CTkLabel(tab4frame,text="partition 5 size :")
    label17.grid(row=4,column=3,padx=30,pady=10)

    sec1part5 = customtkinter.CTkEntry(tab4frame,width=100)
    sec1part51 = config.get('section1_partition','part5')
    sec1part5.insert(0,sec1part51)
    sec1part5.grid(row=4,column=4,padx=15,pady=10)

    csec1 = customtkinter.CTkCheckBox(tab4frame,text="Need Covers in Section 1",onvalue='sec1',offvalue='')
    checkcov = config.get('covers','needcovers')
    if 'sec1' in checkcov:
        csec1.select()
    csec1.grid(row=2,column=0,rowspan=1,columnspan=2)

    msec1 = customtkinter.CTkCheckBox(tab4frame,text="Need M plate in Section 1",onvalue='sec1',offvalue='')
    checkmp = config.get('mounting_plate','need_mounting_plate')
    if 'sec1' in checkmp:
        msec1.select()
    msec1.grid(row=3,column=0,rowspan=1,columnspan=2)

    #for section 2 tab (tab_5)

    tab5frame = customtkinter.CTkFrame(tab_5)
    tab5frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label18= customtkinter.CTkLabel(tab5frame,text="Section 2 size :")
    label18.grid(row=0,column=0,padx=30,pady=10)

    sec2 = customtkinter.CTkEntry(tab5frame,width=100)
    sec21 = config.get('section','sec_2')
    sec2.insert(0,sec21)
    sec2.grid(row=0,column=1,padx=15,pady=10)

    label19= customtkinter.CTkLabel(tab5frame,text="Partitions in Section2:")
    label19.grid(row=1,column=0,padx=30,pady=10)

    sec2part = customtkinter.CTkOptionMenu(tab5frame,values=['1','2','3','4','5','6'])
    sec2p = config.get('section2_partition','partitons')
    sec2part.set(sec2p)
    sec2part.grid(row=1,column=1)

    button1 = customtkinter.CTkButton(tab_5,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    label20= customtkinter.CTkLabel(tab5frame,text="partition 1 size :")
    label20.grid(row=0,column=3,padx=30,pady=10)

    sec2part1 = customtkinter.CTkEntry(tab5frame,width=100)
    sec2part11 = config.get('section2_partition','part1')
    sec2part1.insert(0,sec2part11)
    sec2part1.grid(row=0,column=4,padx=15,pady=10)

    label21= customtkinter.CTkLabel(tab5frame,text="partition 2 size :")
    label21.grid(row=1,column=3,padx=30,pady=10)

    sec2part2 = customtkinter.CTkEntry(tab5frame,width=100)
    sec2part21 = config.get('section2_partition','part2')
    sec2part2.insert(0,sec2part21)
    sec2part2.grid(row=1,column=4,padx=15,pady=10)

    label22= customtkinter.CTkLabel(tab5frame,text="partition 3 size :")
    label22.grid(row=2,column=3,padx=30,pady=10)

    sec2part3 = customtkinter.CTkEntry(tab5frame,width=100)
    sec2part31 = config.get('section2_partition','part3')
    sec2part3.insert(0,sec2part31)
    sec2part3.grid(row=2,column=4,padx=15,pady=10)

    label23= customtkinter.CTkLabel(tab5frame,text="partition 4 size :")
    label23.grid(row=3,column=3,padx=30,pady=10)

    sec2part4 = customtkinter.CTkEntry(tab5frame,width=100)
    sec2part41 = config.get('section2_partition','part4')
    sec2part4.insert(0,sec2part41)
    sec2part4.grid(row=3,column=4,padx=15,pady=10)

    label24= customtkinter.CTkLabel(tab5frame,text="partition 5 size :")
    label24.grid(row=4,column=3,padx=30,pady=10)

    sec2part5 = customtkinter.CTkEntry(tab5frame,width=100)
    sec2part51 = config.get('section2_partition','part5')
    sec2part5.insert(0,sec2part51)
    sec2part5.grid(row=4,column=4,padx=15,pady=10)

    csec2 = customtkinter.CTkCheckBox(tab5frame,text="Need Covers in Section 2",onvalue='sec2',offvalue='')
    checkcov = config.get('covers','needcovers')
    if 'sec2' in checkcov:
        csec2.select()
    csec2.grid(row=2,column=0,rowspan=1,columnspan=2)

    msec2 = customtkinter.CTkCheckBox(tab5frame,text="Need M plate in Section 2",onvalue='sec2',offvalue='')
    checkmp = config.get('mounting_plate','need_mounting_plate')
    if 'sec2' in checkmp:
        msec2.select()
    msec2.grid(row=3,column=0,rowspan=1,columnspan=2)

    #for section3 tab (tab_6)

    tab6frame = customtkinter.CTkFrame(tab_6)
    tab6frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label25= customtkinter.CTkLabel(tab6frame,text="Section 3 size :")
    label25.grid(row=0,column=0,padx=30,pady=10)

    sec3 = customtkinter.CTkEntry(tab6frame,width=100)
    sec31 = config.get('section','sec_3')
    sec3.insert(0,sec31)
    sec3.grid(row=0,column=1,padx=15,pady=10)

    label26= customtkinter.CTkLabel(tab6frame,text="Partitions in Section3:")
    label26.grid(row=1,column=0,padx=30,pady=10)

    sec3part = customtkinter.CTkOptionMenu(tab6frame,values=['1','2','3','4','5','6'])
    sec3p = config.get('section3_partition','partitons')
    sec3part.set(sec3p)
    sec3part.grid(row=1,column=1)

    button1 = customtkinter.CTkButton(tab_6,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    label27= customtkinter.CTkLabel(tab6frame,text="partition 1 size :")
    label27.grid(row=0,column=3,padx=30,pady=10)

    sec3part1 = customtkinter.CTkEntry(tab6frame,width=100)
    sec3part11 = config.get('section3_partition','part1')
    sec3part1.insert(0,sec3part11)
    sec3part1.grid(row=0,column=4,padx=15,pady=10)

    label28= customtkinter.CTkLabel(tab6frame,text="partition 2 size :")
    label28.grid(row=1,column=3,padx=30,pady=10)

    sec3part2 = customtkinter.CTkEntry(tab6frame,width=100)
    sec3part21 = config.get('section3_partition','part2')
    sec3part2.insert(0,sec3part21)
    sec3part2.grid(row=1,column=4,padx=15,pady=10)

    label29= customtkinter.CTkLabel(tab6frame,text="partition 3 size :")
    label29.grid(row=2,column=3,padx=30,pady=10)

    sec3part3 = customtkinter.CTkEntry(tab6frame,width=100)
    sec3part31 = config.get('section3_partition','part3')
    sec3part3.insert(0,sec3part31)
    sec3part3.grid(row=2,column=4,padx=15,pady=10)

    label30= customtkinter.CTkLabel(tab6frame,text="partition 4 size :")
    label30.grid(row=3,column=3,padx=30,pady=10)

    sec3part4 = customtkinter.CTkEntry(tab6frame,width=100)
    sec3part41 = config.get('section3_partition','part4')
    sec3part4.insert(0,sec3part41)
    sec3part4.grid(row=3,column=4,padx=15,pady=10)

    label31= customtkinter.CTkLabel(tab6frame,text="partition 5 size :")
    label31.grid(row=4,column=3,padx=30,pady=10)

    sec3part5 = customtkinter.CTkEntry(tab6frame,width=100)
    sec3part51 = config.get('section3_partition','part5')
    sec3part5.insert(0,sec3part51)
    sec3part5.grid(row=4,column=4,padx=15,pady=10)

    csec3 = customtkinter.CTkCheckBox(tab6frame,text="Need Covers in Section 3",onvalue='sec3',offvalue='')
    checkcov = config.get('covers','needcovers')
    if 'sec3' in checkcov:
        csec3.select()
    csec3.grid(row=2,column=0,rowspan=1,columnspan=2)

    msec3 = customtkinter.CTkCheckBox(tab6frame,text="Need M plate in Section 3",onvalue='sec3',offvalue='')
    checkmp = config.get('mounting_plate','need_mounting_plate')
    if 'sec3' in checkmp:
        msec3.select()
    msec3.grid(row=3,column=0,rowspan=1,columnspan=2)

    #for section 4 tab (tab_7)

    tab7frame = customtkinter.CTkFrame(tab_7)
    tab7frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label32= customtkinter.CTkLabel(tab7frame,text="Section 4 size :")
    label32.grid(row=0,column=0,padx=30,pady=10)

    sec4 = customtkinter.CTkEntry(tab7frame,width=100)
    sec41 = config.get('section','sec_4')
    sec4.insert(0,sec31)
    sec4.grid(row=0,column=1,padx=15,pady=10)

    label33= customtkinter.CTkLabel(tab7frame,text="Partitions in Section4:")
    label33.grid(row=1,column=0,padx=30,pady=10)

    sec4part = customtkinter.CTkOptionMenu(tab7frame,values=['1','2','3','4','5','6'])
    sec4p = config.get('section4_partition','partitons')
    sec4part.set(sec3p)
    sec4part.grid(row=1,column=1)

    button1 = customtkinter.CTkButton(tab_7,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    label34= customtkinter.CTkLabel(tab7frame,text="partition 1 size :")
    label34.grid(row=0,column=3,padx=30,pady=10)

    sec4part1 = customtkinter.CTkEntry(tab7frame,width=100)
    sec4part11 = config.get('section4_partition','part1')
    sec4part1.insert(0,sec4part11)
    sec4part1.grid(row=0,column=4,padx=15,pady=10)

    label35= customtkinter.CTkLabel(tab7frame,text="partition 2 size :")
    label35.grid(row=1,column=3,padx=30,pady=10)

    sec4part2 = customtkinter.CTkEntry(tab7frame,width=100)
    sec4part21 = config.get('section4_partition','part2')
    sec4part2.insert(0,sec4part21)
    sec4part2.grid(row=1,column=4,padx=15,pady=10)

    label36= customtkinter.CTkLabel(tab7frame,text="partition 3 size :")
    label36.grid(row=2,column=3,padx=30,pady=10)

    sec4part3 = customtkinter.CTkEntry(tab7frame,width=100)
    sec4part31 = config.get('section4_partition','part3')
    sec4part3.insert(0,sec4part31)
    sec4part3.grid(row=2,column=4,padx=15,pady=10)

    label37= customtkinter.CTkLabel(tab7frame,text="partition 4 size :")
    label37.grid(row=3,column=3,padx=30,pady=10)

    sec4part4 = customtkinter.CTkEntry(tab7frame,width=100)
    sec4part41 = config.get('section4_partition','part4')
    sec4part4.insert(0,sec4part41)
    sec4part4.grid(row=3,column=4,padx=15,pady=10)

    label38= customtkinter.CTkLabel(tab7frame,text="partition 5 size :")
    label38.grid(row=4,column=3,padx=30,pady=10)

    sec4part5 = customtkinter.CTkEntry(tab7frame,width=100)
    sec4part51 = config.get('section4_partition','part5')
    sec4part5.insert(0,sec4part51)
    sec4part5.grid(row=4,column=4,padx=15,pady=10)

    csec4 = customtkinter.CTkCheckBox(tab7frame,text="Need Covers in Section 4",onvalue='sec4',offvalue='')
    checkcov = config.get('covers','needcovers')
    if 'sec4' in checkcov:
        csec4.select()
    csec4.grid(row=2,column=0,rowspan=1,columnspan=2)

    msec4 = customtkinter.CTkCheckBox(tab7frame,text="Need M plate in Section 4",onvalue='sec4',offvalue='')
    checkmp = config.get('mounting_plate','need_mounting_plate')
    if 'sec4' in checkmp:
        msec4.select()
    msec4.grid(row=3,column=0,rowspan=1,columnspan=2)

    #for section 5 tab (tab_8)

    tab8frame = customtkinter.CTkFrame(tab_8)
    tab8frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label39= customtkinter.CTkLabel(tab8frame,text="Section 5 size :")
    label39.grid(row=0,column=0,padx=30,pady=10)

    sec5 = customtkinter.CTkEntry(tab8frame,width=100)
    sec51 = config.get('section','sec_5')
    sec5.insert(0,sec51)
    sec5.grid(row=0,column=1,padx=15,pady=10)

    label40= customtkinter.CTkLabel(tab8frame,text="Partitions in Section5:")
    label40.grid(row=1,column=0,padx=30,pady=10)

    sec5part = customtkinter.CTkOptionMenu(tab8frame,values=['1','2','3','4','5','6'])
    sec5p = config.get('section5_partition','partitons')
    sec5part.set(sec5p)
    sec5part.grid(row=1,column=1)

    button1 = customtkinter.CTkButton(tab_8,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    label41= customtkinter.CTkLabel(tab8frame,text="partition 1 size :")
    label41.grid(row=0,column=3,padx=30,pady=10)

    sec5part1 = customtkinter.CTkEntry(tab8frame,width=100)
    sec5part11 = config.get('section5_partition','part1')
    sec5part1.insert(0,sec5part11)
    sec5part1.grid(row=0,column=4,padx=15,pady=10)

    label42= customtkinter.CTkLabel(tab8frame,text="partition 2 size :")
    label42.grid(row=1,column=3,padx=30,pady=10)

    sec5part2 = customtkinter.CTkEntry(tab8frame,width=100)
    sec5part21 = config.get('section5_partition','part2')
    sec5part2.insert(0,sec5part21)
    sec5part2.grid(row=1,column=4,padx=15,pady=10)

    label43= customtkinter.CTkLabel(tab8frame,text="partition 3 size :")
    label43.grid(row=2,column=3,padx=30,pady=10)

    sec5part3 = customtkinter.CTkEntry(tab8frame,width=100)
    sec5part31 = config.get('section5_partition','part3')
    sec5part3.insert(0,sec5part31)
    sec5part3.grid(row=2,column=4,padx=15,pady=10)

    label45= customtkinter.CTkLabel(tab8frame,text="partition 4 size :")
    label45.grid(row=3,column=3,padx=30,pady=10)

    sec5part4 = customtkinter.CTkEntry(tab8frame,width=100)
    sec5part41 = config.get('section5_partition','part4')
    sec5part4.insert(0,sec5part41)
    sec5part4.grid(row=3,column=4,padx=15,pady=10)

    label46= customtkinter.CTkLabel(tab8frame,text="partition 5 size :")
    label46.grid(row=4,column=3,padx=30,pady=10)

    sec5part5 = customtkinter.CTkEntry(tab8frame,width=100)
    sec5part51 = config.get('section5_partition','part5')
    sec5part5.insert(0,sec5part51)
    sec5part5.grid(row=4,column=4,padx=15,pady=10)

    csec5 = customtkinter.CTkCheckBox(tab8frame,text="Need Covers in Section 5",onvalue='sec5',offvalue='')
    checkcov = config.get('covers','needcovers')
    if 'sec5' in checkcov:
        csec5.select()
    csec5.grid(row=2,column=0,rowspan=1,columnspan=2)

    msec5 = customtkinter.CTkCheckBox(tab8frame,text="Need M plate in Section 5",onvalue='sec5',offvalue='')
    checkmp = config.get('mounting_plate','need_mounting_plate')
    if 'sec5' in checkmp:
        msec5.select()
    msec5.grid(row=3,column=0,rowspan=1,columnspan=2)

    #for section 6 tab (tab_9)

    tab9frame = customtkinter.CTkFrame(tab_9)
    tab9frame.grid(row=0,column=0,padx=25,pady=20,sticky= customtkinter.NSEW)

    label47= customtkinter.CTkLabel(tab9frame,text="Section 6 size :")
    label47.grid(row=0,column=0,padx=30,pady=10)

    sec6 = customtkinter.CTkEntry(tab9frame,width=100)
    sec6.grid(row=0,column=1,padx=15,pady=10)

    label48= customtkinter.CTkLabel(tab9frame,text="Partitions in Section6:")
    label48.grid(row=1,column=0,padx=30,pady=10)

    sec6part = customtkinter.CTkOptionMenu(tab9frame,values=['1','2','3','4','5','6'])
    sec6p = config.get('section6_partition','partitons')
    sec6part.set(sec6p)
    sec6part.grid(row=1,column=1)

    button1 = customtkinter.CTkButton(tab_9,text="SAVE",command=save)
    button1.grid(row=1,column=0,padx=20,pady=10)

    label49= customtkinter.CTkLabel(tab9frame,text="partition 1 size :")
    label49.grid(row=0,column=3,padx=30,pady=10)

    sec6part1 = customtkinter.CTkEntry(tab9frame,width=100)
    sec6part11 = config.get('section6_partition','part1')
    sec6part1.insert(0,sec6part11)
    sec6part1.grid(row=0,column=4,padx=15,pady=10)

    label50= customtkinter.CTkLabel(tab9frame,text="partition 2 size :")
    label50.grid(row=1,column=3,padx=30,pady=10)

    sec6part2 = customtkinter.CTkEntry(tab9frame,width=100)
    sec6part21 = config.get('section6_partition','part2')
    sec6part2.insert(0,sec6part21)
    sec6part2.grid(row=1,column=4,padx=15,pady=10)

    label51= customtkinter.CTkLabel(tab9frame,text="partition 3 size :")
    label51.grid(row=2,column=3,padx=30,pady=10)

    sec6part3 = customtkinter.CTkEntry(tab9frame,width=100)
    sec6part31 = config.get('section6_partition','part3')
    sec6part3.insert(0,sec6part31)
    sec6part3.grid(row=2,column=4,padx=15,pady=10)

    label51= customtkinter.CTkLabel(tab9frame,text="partition 4 size :")
    label51.grid(row=3,column=3,padx=30,pady=10)

    sec6part4 = customtkinter.CTkEntry(tab9frame,width=100)
    sec6part41 = config.get('section6_partition','part4')
    sec6part4.insert(0,sec6part41)
    sec6part4.grid(row=3,column=4,padx=15,pady=10)

    label52= customtkinter.CTkLabel(tab9frame,text="partition 5 size :")
    label52.grid(row=4,column=3,padx=30,pady=10)

    sec6part5 = customtkinter.CTkEntry(tab9frame,width=100)
    sec6part51 = config.get('section6_partition','part5')
    sec6part5.insert(0,sec6part51)
    sec6part5.grid(row=4,column=4,padx=15,pady=10)

    csec6 = customtkinter.CTkCheckBox(tab9frame,text="Need Covers in Section 6",onvalue='sec6',offvalue='')
    checkcov = config.get('covers','needcovers')
    if 'sec6' in checkcov:
        csec6.select()
    csec6.grid(row=2,column=0,rowspan=1,columnspan=2)

    msec6 = customtkinter.CTkCheckBox(tab9frame,text="Need M plate in Section 6",onvalue='sec6',offvalue='')
    checkmp = config.get('mounting_plate','need_mounting_plate')
    if 'sec6' in checkmp:
        msec6.select()
    msec6.grid(row=3,column=0,rowspan=1,columnspan=2)

    # for covers tab 

    cframe = customtkinter.CTkFrame(tab_3)
    cframe.grid(row=0,column=0,padx=20,pady=20)

    labelc = customtkinter.CTkLabel(cframe,text='Cover Thick :')
    labelc.grid(row=0,column=0,padx=30,pady=10)

    cthick = customtkinter.CTkEntry(cframe,width=100)
    cthick1= config.get('covers','cover_thick')
    cthick.insert(0,cthick1)
    cthick.grid(row=0,column=1,padx=15,pady=10)

    labelc1 = customtkinter.CTkLabel(cframe,text='Cover clearence X :')
    labelc1.grid(row=1,column=0,padx=30,pady=10)

    cx = customtkinter.CTkEntry(cframe,width=100)
    cx1= config.get('covers','cover_clearence_x')
    cx.insert(0,cx1)
    cx.grid(row=1,column=1,padx=15,pady=10)

    labelc2 = customtkinter.CTkLabel(cframe,text='Cover clearence Y:')
    labelc2.grid(row=1,column=2,padx=30,pady=10)

    cy = customtkinter.CTkEntry(cframe,width=100)
    cy1= config.get('covers','cover_clearence_y')
    cy.insert(0,cy1)
    cy.grid(row=1,column=3,padx=15,pady=10)

    labelc3 = customtkinter.CTkLabel(cframe,text='Mounting plate clearence X :')
    labelc3.grid(row=2,column=0,padx=10,pady=10)

    mx = customtkinter.CTkEntry(cframe,width=100)
    mx1= config.get('mounting_plate','mounting_plate_clearence_x')
    mx.insert(0,mx1)
    mx.grid(row=2,column=1,padx=15,pady=10)

    labelc4 = customtkinter.CTkLabel(cframe,text='Mounting plate clearence Y:')
    labelc4.grid(row=2,column=2,padx=10,pady=10)

    my = customtkinter.CTkEntry(cframe,width=100)
    my1= config.get('mounting_plate','mounting_plate_clearence_y')
    my.insert(0,my1)
    my.grid(row=2,column=3,padx=15,pady=10)

    labelc5 = customtkinter.CTkLabel(cframe,text='Mounting plate gap in top :')
    labelc5.grid(row=3,column=0,padx=10,pady=10)

    mt = customtkinter.CTkEntry(cframe,width=100)
    mt1= config.get('mounting_plate','mounting_plate_top_clearence')
    mt.insert(0,mt1)
    mt.grid(row=3,column=1,padx=15,pady=10)

    labelc6 = customtkinter.CTkLabel(cframe,text='Mounting plate gap in bottom:')
    labelc6.grid(row=3,column=2,padx=10,pady=10)

    mb = customtkinter.CTkEntry(cframe,width=100)
    mb1= config.get('mounting_plate','mounting_plate_bottom_clearence')
    mb.insert(0,mb1)
    mb.grid(row=3,column=3,padx=15,pady=10)

    buttonc = customtkinter.CTkButton(tab_3,text="SAVE",command=save)
    buttonc.grid(row=1,column=0,padx=20,pady=10)