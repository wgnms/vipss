# -*- coding: utf-8 -*- 
import StellarPlayer

class Plugin(StellarPlayer.IStellarPlayerPlugin): 
    def __init__(self, player:StellarPlayer.IStellarPlayer): 
        super().__init__(player) 
    
    def handleRequest(self, method, args): 
        if hasattr(self.simple, f"on_{method}"): 
            getattr(self.simple, f"on_{method}")(args) 
    def makeLayout(self):
        nav_labels = []
        for cat in self.categories:
            nav_labels.append({'type': 'link', 'name': cat['title'], '@click': 'onCategoryClick'})

        grid_layout = {'group':
            [
                {'type': 'image', 'name': 'img', 'width': 120, 'height': 150, '@click': 'onMovieImageClick'},
                {'type': 'label', 'name': 'title', 'hAlign': 'center'},
            ],
            'dir': 'vertical'
        }
        controls = [
            {'group': nav_labels, 'height': 30},
            {'type': 'space', 'height': 10},
            {'group':
                [
                    {'type': 'edit', 'name': 'search_edit', 'label': '搜索'},
                    {'type': 'button', 'name': '搜电影', '@click': 'onSearch'}
                ]
                , 'height': 30
            },
            {'type': 'space', 'height': 10},
            {'type': 'grid', 'name': 'list', 'itemlayout': grid_layout, 'value': self.movies, 'marginSize': 5,
             'itemheight': 180, 'itemwidth': 120},
            {'group':
                [
                    {'type': 'space'},
                    {'group':
                        [
                            {'type': 'label', 'name': 'cur_page', ':value': 'cur_page'},
                            {'type': 'link', 'name': '上一页', '@click': 'onClickFormerPage'},
                            {'type': 'link', 'name': '下一页', '@click': 'onClickNextPage'},
                            {'type': 'link', 'name': '首页', '@click': 'onClickFirstPage'},
                            {'type': 'link', 'name': '末页', '@click': 'onClickLastPage'},
                            {'type': 'label', 'name': 'num_page', ':value': 'num_page'},
                        ]
                        , 'width': 0.45
                        , 'hAlign': 'center'
                    },
                    {'type': 'space'}
                ]
                , 'height': 30
            },
            {'type': 'space', 'height': 5}
        ]
        return controls
    def show(self):
        controls=
        self.doModal('main', 800, 600, '', controls)           
    def start(self): 
        self.show()
        print("插件启动") 
        
    def stop(self): 
        super().stop() 
        print("插件停止") 
        
    def newPlugin(player:StellarPlayer.IStellarPlayer,*arg): 
        print("插件初始化") 
        return Plugin(player) 
