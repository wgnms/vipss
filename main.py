import StellarPlayer
class IwebdecodePlugin(StellarPlayer.IStellarPlayerPlugin):
    def __init__(self, player: StellarPlayer.IStellarPlayer):
        super().__init__(player)
        self.playurl = []
        self.url = ''

    def show(self):
        list_layout = [[{'type': 'label', 'name': 'video_profile'},
                        {'type': 'link', 'name': '播放', 'width': 60, '@click': 'onPlayClick'}]]
        controls = [
            {'type': 'space', 'height': 10},
            {'group':
                [
                    {'type': 'edit', 'name': 'url_edit', 'label': 'html页面地址'},
                    {'type': 'button', 'name': '解析', 'width': 60, '@click': 'parse_html'},
                    {'type': 'space', 'width': 10}
                ],
                'height': 30
            },
            {'type': 'space', 'height': 10},
            {'type': 'list', 'name': 'list', 'itemlayout': list_layout, 'separator': True, 'itemheight': 40}
        ]
        self.player.doModal('main', 500, 400, '', controls)

    def parse_html(self, *args):
        self.player.updateControlValue('main', 'list', [])
        self.playurl = []
        if hasattr(self.player, 'loadingAnimation'):
            self.player.loadingAnimation('main')
        # ----------------------------------------------
        #获取到输入框的地址
        search_url = self.player.getControlValue('main', 'url_edit')
        接口就写在这里
        urls = []        
        urls.append({'url': search_url, 'video_profile': '视频名称'})
        urls.append({'url': search_url, 'video_profile': '视频名称'})
        
        self.player.updateControlValue('main', 'list', urls)
        self.playurl = urls
        self.player.toast('main', '解析完成')
        #----------------------------------------------
        if hasattr(self.player, 'loadingAnimation'):
            self.player.loadingAnimation('main', stop=True)

    def onPlayClick(self, page, control, idx, *arg):
        if self.playurl:
            self.player.play(self.playurl[idx]['url'])

def newPlugin(player: StellarPlayer.IStellarPlayer, *arg):
    plugin = IwebdecodePlugin(player)
    return plugin


def destroyPlugin(plugin: StellarPlayer.IStellarPlayerPlugin):
    plugin.stop()
