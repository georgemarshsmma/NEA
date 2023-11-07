from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class WashingtonBullets(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.properties()
        self.enviroment1()

    def properties(self):
        props = WindowProperties() #creates window properties
        props.setTitle('Alaska Bullets') #name of app running
        props.setSize(1280, 720) #sets display size
        props.setCursorHidden(True) #hides cursor
        base.win.requestProperties(props)

    def enviroment1(self):
        self.scene = self.loader.loadModel('enviroment/maps/bedroom_awesome.glb')
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(0, -59, 0)




        



        


app = WashingtonBullets()
app.run()