# -*- coding: utf-8 -*- 
import StellarPlayer
class Plugin(StellarPlayer.IStellarPlayerPlugin): 
    def __init__(self, player:StellarPlayer.IStellarPlayer): 
        super().__init__(player) 
            
    def start(self): 
        return super().start() 
        print("插件启动") 
        
    def stop(self): 
        return super().stop() 
        print("插件停止") 
        
    def newPlugin(player:StellarPlayer.IStellarPlayer,*arg): 
        print("插件初始化") 
        return Plugin(player) 
    def makeLayout(self):
        controls = [ 
            [         
                {'type':'edit',    'name':'url','label':'html页面地址'},
                {'type':'button','name':'解析','@click':'search'}
            ] # 行为列表，包含两个控件对象，两个控件宽度各占行的一半空间
         ]
        return controls
    def search(self):
        return 
    def show(self):
        controls=self.makeLayout()
        self.doModal('main',800,600,'',controls)
def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    plugin = Plugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

