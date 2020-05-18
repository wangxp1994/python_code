
import os
from time import sleep,time
from threading import Thread


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
            self.length = int(audio.info.length)

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


if __name__ == '__main__':
    n = 4
    # p = PlaySound(n,'sounds\卡农.wav')
    p = PlaySound(n, 'sounds\qingtian.mp3')
    # p = PlaySound(n)
    p.run()