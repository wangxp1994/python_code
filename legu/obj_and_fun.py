
import os
import pymysql
import random
import copy
from time import sleep,time
from threading import Thread
from pprint import pprint


# 播放声音
class PlaySound(object):
    def __init__(self, method=2, path='sounds\msg.wav'):
        self.path = path
        self.method = method
        self.length = 10

    # 播放音乐的方法
    def method_fun(self):
        method_fun = {
            1 : self.one,
            2 : self.two,
            3 : self.three,
            4 : self.four,
        }

        return method_fun[self.method]

    # 音乐时长
    def music_len(self):
        type = self.path.split('.')[-1]
        type = type.lower()
        if type == 'mp3':
            from mutagen.mp3 import MP3
            audio = MP3(self.path)
            self.length = int(audio.info.length) + 5

    # 时间显示
    def play_show(self):
        self.music_len()
        for i in range(self.length,0,-1):
            sleep(1)

    # 时间进程开辟
    def show_thread(self):
        t = Thread(target=self.play_show())
        t.start()
        t.join()

    # 系统播放 - 会打开系统播放器
    def one(self):
        os.system(self.path)

    # playsound - 歌名只能是英文
    def two(self):
        from playsound import playsound

        playsound(self.path)

    # winsound - 只支持wav格式
    def three(self):
        import winsound

        winsound.PlaySound(self.path, winsound.SND_FILENAME)

    # pygame - 需要设置播放时间
    def four(self):
        from pygame import mixer

        mixer.init()
        mixer.music.load(self.path)
        mixer.music.play()

        self.show_thread()

        mixer.music.stop()

    def run(self):
        fx = self.method_fun()
        fx()


# 简单网页爬虫
class OneSpider(object):
    def __init__(self, surl=None, method='R', go=True, txt=True, bea=True):
        self.surl = surl

        spider_fun = {
            'R' : self.getHtmlByRequests,
            'S' : self.getHtmlBySelenium,
        }
        if method not in spider_fun:
            method = 'R'

        self.method = spider_fun[method]
        self.headers = None
        self.txt = txt
        self.bea = bea

        if go:
            self.work()

    # 爬取网页
    def work(self):
        self.method()

    # 获取网页
    def getHtmlByRequests(self, **kwargs):
        import requests
        from bs4 import BeautifulSoup

        if not self.headers:
            self.headers = {
                'User-Agent': "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
            }
        self.res = requests.get(self.surl, headers=self.headers, **kwargs)

        self.html = self.res.content
        if self.bea:
            self.html = BeautifulSoup(self.html).prettify()

        if self.txt:
            print('Requests已爬取网页')

    # 获取网页
    def getHtmlBySelenium(self):
        from selenium import webdriver
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        dr = webdriver.Chrome(options=option)
        dr.get(self.surl)
        self.html = dr.page_source
        dr.close()
        if self.txt:
            print('Selenium已爬取网页')

    # 使用xpath匹配
    def getElementByXpath(self, xpath_str):
        from lxml import etree
        html = etree.HTML(self.html)
        result = html.xpath(xpath_str)
        if self.txt:
            print('已使用xpath匹配{}'.format(xpath_str))
        return result

    # 使用正则匹配
    def getElementByRe(self, re_str):
        import re
        reslut = re.findall(re_str, self.html)
        if self.txt:
            print('已使用xpath匹配{}'.format(re_str))
        return  reslut

    # 保存网页
    def saveHtml(self,path='',name=''):
        if not name:
            from time import time
            name = str(int(time())) + '.html'
        with open(path+name, 'a', encoding='utf-8') as f:
            f.write(self.html)
        print('保存成功')


# 自制网易云听歌
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
        from bs4 import BeautifulSoup

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


# 连接我的mysql
class ConnectMysql(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host = '211.159.182.22',
            port = 3306,
            user = 'wang',
            password = 'wxp520++',
            database = 'my_db',
            charset='utf8'
        )
        self.cur = self.conn.cursor()
        print('数据库已连接')


    # 创建表
    def create(self, tbname, data):
        field_lst = []
        for k,v in data.items():
            field_str = str(k) + ' ' + str(v)
            field_lst.append(field_str)
        fields_str = ','.join(field_lst)
        create_str = 'create table {}({});'.format(tbname, fields_str)

        self.cur.execute(create_str)
        self.conn.commit()


    # 插入数据
    def insert(self, tbname, data):
        key_lst = []
        value_lst = []
        for k,v in data.items():
            v = '"{}"'.format(v)
            key_lst.append(str(k))
            value_lst.append(v)
        key_str = ','.join(key_lst)
        value_str = ','.join(value_lst)
        insert_str = 'insert into {}({}) values({});'.format(tbname, key_str, value_str)

        self.cur.execute(insert_str)
        self.conn.commit()

    # 更新数据
    def update(self, tbname, wstr, data):
        set_lst = []
        for k,v in data.items():
            set_str = '{}="{}"'.format(k,v)
            set_lst.append(set_str)
        sets_str = ','.join(set_lst)
        update_str = 'update {} set {} where {};'.format(tbname, sets_str, wstr)

        self.cur.execute(update_str)
        self.conn.commit()

    # 删除数据
    def delete(self, tbname, wstr):
        delete_str = 'delete  from {} where {};'.format(tbname, wstr)

        self.cur.execute(delete_str)
        self.conn.commit()

    # 查询语句 - 所有
    def find_all(self, tbname, show='*'):
        find_str = 'select {} from {};'.format(show, tbname)

        self.cur.execute(find_str)
        return self.cur.fetchall()

    # 查询语句 - 指定条件
    def find(self, tbname, wstr, show='*'):
        find_str = 'select {} from {} where {};'.format(show, tbname, wstr)

        self.cur.execute(find_str)
        return self.cur.fetchall()


    # 关闭数据库
    def __del__(self):
        self.cur.close()
        self.conn.close()
        print('数据库已关闭')


# 随机数字,且数字不在指定列表内
# 参数 最小数,最大数,不可重复数列表,随机出来列表数量
def rand(minNum,maxNum,lst=[],num=1):
    lst = copy.deepcopy(lst)
    lst.append(minNum)
    lst.append(maxNum)
    lst = sorted(lst)
    # 随机出来的数字列表
    randlst = []
    for i in range(num):
        newLst = []
        for n,i in enumerate(lst[:-1]):
            if lst[n+1] - i != 1:
                newLst.append((i+1, lst[n+1]-1))

        randTuple = random.choice(newLst)
        randNum = random.randint(*randTuple)
        lst.append(randNum)
        randlst.append(randNum)
        lst = sorted(lst)

    return sorted(randlst)