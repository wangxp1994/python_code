
import warnings
import os
from obj_and_fun import OneSpider, PlaySound
from bs4 import BeautifulSoup

warnings.filterwarnings('ignore')

class Music163(object):
    def __init__(self):
        self.start_url = 'https://music.163.com/discover/playlist'  # 歌单列表起始页
        self.cat = ''           # 歌曲类别
        self.catlst = []        # 歌曲类别清单
        self.cats = ['']
        self.songlst = {}       # 歌单列表
        self.songlst_num = 0    # 歌单列表 - 选择数字
        self.songs = {}         # 歌单里所有歌曲
        self.songs_num = 0      # 歌单里所有歌曲 - 选择数字
        self.song_name = ''     # 歌名
        self.song_href = ''     # 歌曲地址
        self.path = 'songs/'
        self.get_cat()

    # 获取类别
    def get_cat(self):
        sp = OneSpider(self.start_url,'R', txt=False)

        cat_lst = sp.getElementByXpath('//div[@class="bd"]//dl')
        self.catlst = []
        self.cats = ['']
        for dl in cat_lst:
            cat_dict = {}
            style = dl.xpath('dt/text()')[1].strip()
            lst =  dl.xpath('dd/a/text()')
            lst = [i.strip() for i in lst]

            cat_dict['name'] = style
            cat_dict['lst'] = lst
            self.cats.extend(lst)
            self.catlst.append(cat_dict)
        print('已获取类别')

    # 显示类别
    def show_cat(self):
        if not self.catlst:
            self.get_cat()
        for style in self.catlst:
            name = style['name']
            lst = style['lst']
            print('------------{}------------'.format(name))
            n = 1
            for cat in lst:
                if n % 5 == 0:
                    print()
                print(cat, end=' ')
                n+= 1
            print()

    # 获取歌单列表
    def get_songlst(self):
        if self.cat:
            url = 'https://music.163.com/discover/playlist/?cat={}'.format(self.cat)
        else:
            url = self.start_url
        self.songlst = {}
        sp = OneSpider(url, 'R', txt=False)
        song_lst = sp.getElementByXpath('//p[@class="dec"]/a')
        for n,ss in enumerate(song_lst):
            song_dict = {}
            song_dict['title'] = ss.xpath('@title')[0]
            song_dict['href'] =  'https://music.163.com' + ss.xpath('@href')[0]
            self.songlst[n] = song_dict
        print('已获歌单列表')

    # 显示歌单列表
    def show_songlst(self):
        if not self.songlst:
            self.get_songlst()
        for k,v in self.songlst.items():
            print('{} {}'.format(k,v['title']))

    # 获取歌单里歌曲
    def get_songs(self):
        info = self.songlst[self.songlst_num]
        title = info['title']
        url = info['href']
        self.songs = {}
        sp = OneSpider(url, 'R', txt=False)
        s = BeautifulSoup(sp.html, 'lxml')
        main = s.find('ul', {'class': 'f-hide'})
        for n,music in enumerate(main.find_all('a')):
            href = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
            name = music.text.strip()
            self.songs[n] = {'name':name,'href':href}
        print('已获取歌单歌曲列表')

    # 显示歌单里歌曲
    def show_songs(self):
        if not self.songs:
            self.get_songs()
        for k,v in self.songs.items():
            print('{} {}'.format(k, v['name']))

    # 获取歌曲
    def get_song(self):
        info = self.songs[self.songs_num]
        self.song_href = info['href']
        self.song_name = info['name'] + '.mp3'

        dirlst = os.listdir(self.path)
        if self.song_name in dirlst:
            return

        sp = OneSpider(self.song_href, 'R', txt=False, bea=False)
        with open(self.path+self.song_name, 'wb') as f:
            f.write(sp.html)
        print('已获取歌曲')

    # 播放歌曲
    def play_song(self):
        song = PlaySound(4, self.path+self.song_name)
        try:
            song.run()
        except:
            return

    # 选择 - 播放歌曲
    def sel_one(self):
        self.show_songs()
        try:
            self.songs_num = int(input('\n>>>请输入选择-歌曲>>>'))
            self.get_song()
        except:
            print('--选择失败--')
            return 0
        self.play_song()
        return 1

    # 选择 - 选择歌单
    def sel_two(self):
        self.show_songlst()
        try:
            self.songlst_num = int(input('\n>>>请输入选择-歌单>>>'))
        except:
            print('--选择失败--')
            return 0
        self.get_songs()
        return 1

    # 选择 - 选择类别
    def sel_three(self):
        self.show_cat()
        cat = input('\n>>>请输入选择-类别>>>')
        cat = cat.strip()
        if cat not in self.cats:
            print('--选择失败--')
            return 0
        self.cat = cat
        self.get_songlst()
        return 1

    # 选择 - 重新播放
    def sel_four(self):
        self.play_song()

    # 选择界面
    def sel_main(self):
        show = '''
        1  -  选择歌曲 
        2  -  选择歌单
        3  -  选择类别 
        4  -  重新播放       
        '''
        print(show)

    # 操作
    def work(self):
        self.sel_three()
        self.sel_two()
        self.sel_one()
        while True:
            self.sel_main()
            try:
                sel = int(input('\n>>>请输入选择-操作>>>'))
            except:
                print('--选择失败--')
                continue
            if sel == 1:
                self.sel_one()
            elif sel == 2:
                self.sel_two()
                self.sel_one()
            elif sel == 3:
                self.sel_three()
                self.sel_two()
                self.sel_one()
            elif sel == 4:
                self.sel_four()



if __name__ == "__main__":
    m = Music163()
    m.work()
