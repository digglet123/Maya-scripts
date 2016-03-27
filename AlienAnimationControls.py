import maya.cmds as mc

########### UI for Alien Animation Controls ###########


#create new window and set layout 
appWindow = mc.window(title ="Alien Control UI", wh = (500,500))
mc.columnLayout(adj = True, rs = 10, cat = ["both",10])
imagePath = "C:\Users\mikko\Desktop\Alien\sourceimages\AnimationControlsIcon.png" 
mc.image(image = imagePath)

#sliders for controlling back bones
mc.text("Back controls")
mc.separator()
backBendSlider = mc.floatSliderGrp(l = "Bend:", min = -30, max  = 30, value = 0, step = 1, dc = "backBend()", cc = "backBend()" , field = True, cw3 = [60,40,300], cal = [1,"left"])
backSwingSlider = mc.floatSliderGrp(l = "Swing:", min = -30, max  = 30, value = 0, step = 1, dc = "backSwing()", cc = "backSwing()" , field = True, cw3 = [60,40,300], cal = [1,"left"])
backTwistSlider = mc.floatSliderGrp(l = "Twist:", min = -30, max  = 30, value = 0, step = 1, dc = "backTwist()", cc = "backTwist()" , field = True, cw3 = [60,40,300], cal = [1,"left"])

#sliders for controlling hips
mc.text("Hip Controls")
mc.separator()
hipSwingSlider = mc.floatSliderGrp(l = "Swing:", min = -30, max  = 30, value = 0, step = 1, dc = "hipSwing()", cc = "hipSwing()" , field = True, cw3 = [60,40,300], cal = [1,"left"])
hipTwistSlider = mc.floatSliderGrp(l = "Twist:", min = -30, max  = 30, value = 0, step = 1, dc = "hipTwist()", cc = "hipTwist()" , field = True, cw3 = [60,40,300], cal = [1,"left"])


#sliders for controlling toes.
mc.text("Toe controls")
mc.separator()
toeBendLeftSlider = mc.floatSliderGrp(l = "Bend L:", min = -30, max  = 30, value = 0, step = 1, dc = "toeBendLeft()", cc = "toeBendLeft()" , field = True, cw3 = [60,40,300], cal = [1,"left"])
toeBendRightSlider = mc.floatSliderGrp(l = "Bend R:", min = -30, max  = 30, value = 0, step = 1, dc = "toeBendRight()", cc = "toeBendRight()" , field = True, cw3 = [60,40,300], cal = [1,"left"])

#checkbox
mc.separator()
headCompensation = mc.checkBox(label = "Compensate head movement")
resetbutton = mc.button(label = "Reset tool", command = "reset()")

#show appWindow
mc.showWindow(appWindow)

    
    
########### UI for Alien Animation Controls ###########


    
#function for selecting and rotating back in forward-backward direction.
def backBend():
    mc.select("BACK_1","BACK_2","BACK_3","HEAD")
    selList = mc.ls(sl=True)
    rotateAmount = mc.floatSliderGrp(backBendSlider, q = True, value = True)
    for bone in selList:
        mc.setAttr(bone + ".rotateX", rotateAmount)
    
    checkState = mc.checkBox(headCompensation, q = True, value = True)
    if checkState == True:
        mc.setAttr("HEAD.rotateX", 3* -rotateAmount)
        
#function for selecting and rotating back in sideways direction.
def backSwing():
    mc.select("BACK_1","BACK_2","BACK_3","HEAD")
    selList = mc.ls(sl=True)
    rotateAmount = mc.floatSliderGrp(backSwingSlider, q = True, value = True)
    for bone in selList:
        mc.setAttr(bone + ".rotateZ", rotateAmount)
    
    checkState = mc.checkBox(headCompensation, q = True, value = True)
    if checkState == True:
        mc.setAttr("HEAD.rotateZ", 3* -rotateAmount)

             
#function for selecting and twisting back. 
def backTwist():
    mc.select("BACK_1","BACK_2","BACK_3","HEAD")
    selList = mc.ls(sl=True)
    rotateAmount = mc.floatSliderGrp(backTwistSlider, q = True, value = True)
    for bone in selList:
        mc.setAttr(bone + ".rotateY", rotateAmount)
     
    checkState = mc.checkBox(headCompensation, q = True, value = True)
    if checkState == True:
        mc.setAttr("HEAD.rotateY", 3* -rotateAmount)


#function for selecting and swinging hips.        
def hipSwing():
    mc.select("BACK_1","BACK_2","BACK_3","HEAD")
    selList = mc.ls(sl=True)
    rotateAmount = mc.floatSliderGrp(hipSwingSlider, q = True, value = True)
    mc.setAttr("HIPS_CONTROL.rotateZ", rotateAmount)
    for bone in selList:
        mc.setAttr(bone + ".rotateZ", -rotateAmount / 2 )
    
    checkState = mc.checkBox(headCompensation, q = True, value = True)
    if checkState == True:
        mc.setAttr("HEAD.rotateZ", rotateAmount / 2) 
 
       
#function for selecting twisting hips.        
def hipTwist():
    mc.select("BACK_1","BACK_2","BACK_3","HEAD")
    selList = mc.ls(sl=True)
    rotateAmount = mc.floatSliderGrp(hipTwistSlider, q = True, value = True)
    mc.setAttr("HIPS_CONTROL.rotateY", rotateAmount)
    for bone in selList:
        mc.setAttr(bone + ".rotateY", -rotateAmount / 2)
    
    checkState = mc.checkBox(headCompensation, q = True, value = True)
    if checkState == True:
        mc.setAttr("HEAD.rotateY", rotateAmount / 3)         
        
#function for selecting and bending left foot toes.
def toeBendLeft():
    mc.select("TOEF_1_L","TOEF_2_L","TOEB_1_L", "TOEB_2_L")
    rotateAmount = mc.floatSliderGrp(toeBendLeftSlider, q = True, value = True)    
   
    mc.setAttr("TOEF_1_L.rotateX", rotateAmount)
    mc.setAttr("TOEF_2_L.rotateX", rotateAmount*2)
    mc.setAttr("TOEB_1_L.rotateX", -rotateAmount)
    mc.setAttr("TOEB_2_L.rotateX", -rotateAmount*2)
    
#function for selecting and bending right foot toes.
def toeBendRight():
    mc.select("TOEF_1_R","TOEF_2_R","TOEB_1_R", "TOEB_2_R")
    rotateAmount = mc.floatSliderGrp(toeBendRightSlider, q = True, value = True)    
   
    mc.setAttr("TOEF_1_R.rotateX", rotateAmount)
    mc.setAttr("TOEF_2_R.rotateX", rotateAmount*2)
    mc.setAttr("TOEB_1_R.rotateX", -rotateAmount)
    mc.setAttr("TOEB_2_R.rotateX", -rotateAmount*2)

#function for resetting tool
def reset():
    mc.floatSliderGrp(backBendSlider, e = True, value = 0)
    backBend()
    mc.floatSliderGrp(backSwingSlider, e = True, value = 0)
    backSwing()
    mc.floatSliderGrp(backTwistSlider, e = True, value = 0)
    backTwist()
    mc.floatSliderGrp(hipSwingSlider, e = True, value = 0)
    hipSwing()
    mc.floatSliderGrp(hipTwistSlider, e = True, value = 0)
    hipTwist()
    mc.floatSliderGrp(toeBendLeftSlider, e = True, value = 0)
    toeBendLeft()
    mc.floatSliderGrp(toeBendRightSlider, e = True, value = 0)
    toeBendRight()
