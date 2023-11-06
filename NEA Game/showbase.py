from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class WashingtonBullets(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        props = WindowProperties() #creates window properties
        props.setTitle('Washington Bullets') #name of app running
        props.setSize(1280, 720) #sets display size
        props.setCursorHidden(True) #hides cursor
        base.win.requestProperties(props)
        self.camera.setP(0) #sets the pitch (tilt) of camera

app = WashingtonBullets()
app.run()
