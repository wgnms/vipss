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
    def search(self):
        return 
    def show(self):
        list_layout = [[{'type':'label','name':'video_profile'},{'type':'link','name':'播放','width':60,'@click':'onPlayClick'}]]
        controls = [
            {'type':'space','height':10},
            {'group':
                [
                    {'type':'edit','name':'url_edit','label':'html页面地址'},
                    {'type':'button','name':'解析','width':60,'@click':'parse_html'},
                    {'type':'space','width':10}
                ],
                'height':30
            },
            {'type':'space','height':10},
            {'type':'list','name':'list','itemlayout':list_layout,'separator':True,'itemheight':40}
        ]
        self.player.doModal('main',500,400,'',controls)
def newPlugin(player:StellarPlayer.IStellarPlayer,*arg):
    plugin = Plugin(player)
    return plugin

def destroyPlugin(plugin:StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()

