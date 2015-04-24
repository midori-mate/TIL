# coding: utf-8
# Python のクラスシステム <https://www.shido.info/py/python7.html> より


class Workers:
    """ This is a class of workers working in the company."""
    
    def __init__(self, name, position, email, age, salary):
        self.name = name
        self.position = position
        self.email = email
        self.age = age
        self.salary = salary
# Workers のインスタンスは、初期化されるときインスタンス変数として名前とか色々保持する。

class ITWorkers(Workers): # Workers のサブクラスであることを示す。
    """ This is a class of IT engineers. """
    
    OS = 'WinNT'
    
    def __init__(self, language, *av): # *av でレストパラメータにまとめる。
        Workers.__init__(self, *av)
        self.language=language

    def work(self, n): # n は働いた時間。
        """ IT engineers should work."""
        # 職種に応じて、何を何時間したか表示するだけ。
        if self.position == 'web creator':
            w = 'makes web site'
        elif self.position == 'server administrator':
            w = 'checks the trafic'
        elif self.position == 'programmer':
            w = 'writes programs'

        print '%s %s for %d, hours using %s on %s' % (self.name, w, n, self.language, self.OS)

midoriiro = Founders()
##------------------------------------------------------------------------------------------------
henley = ITWorkers('PHP', 'Henley', 'web creator', 'henley@livegate.com', 32, 700)
thomas = ITWorkers('Python', 'Thomas', 'server administrator', 'thomas@livegate.com', 37, 900)
gates  = ITWorkers('C', 'Gates', 'programmer', 'gates@livegate.com', 42, 1200)

henley.OS = 'Mac' # ふたりの名前空間に OS というエントリーを加える。
thomas.OS = 'Linux' # gates の名前空間には OS というエントリーがないので ITWorkers まで探しに行く。

if __name__ == '__main__':

    henley.work(8)
    thomas.work(7)
    gates.work(10) # 3人は今日それぞれ8, 7, 10時間働いた。