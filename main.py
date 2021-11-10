# -*- coding: utf-8 -*- 
import StellarPlayer
class Plugin(StellarPlayer.IStellarPlayerPlugin): 
    def __init__(self, player:StellarPlayer.IStellarPlayer): 
        super().__init__(player) 
    
    def handleRequest(self, method, args): 
        if hasattr(self.simple, f"on_{method}"): 
            getattr(self.simple, f"on_{method}")(args) 
            
    def start(self): 
        super().stop() 
        print("插件启动") 
        
    def stop(self): 
        super().stop() 
        print("插件停止") 
        
    def newPlugin(player:StellarPlayer.IStellarPlayer,*arg): 
        print("插件初始化") 
        return Plugin(player) 
    
def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    plugin = Plugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

