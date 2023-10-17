from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class WashingtonBullets(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        props = WindowProperties() #creates window properties
        props.setTitle('Washington Bullets') #name of app running
        props.setSize(1280, 720) #sets display size
        props.setCursorHidden(True)

        base.win.requestProperties(props)


app = WashingtonBullets()
app.run()