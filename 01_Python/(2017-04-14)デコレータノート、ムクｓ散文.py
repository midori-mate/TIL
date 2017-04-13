#!/usr/bin/env python
# coding: utf-8

'''
Component         :xとyだけもつ
ConcreteComponent :xとyだけもつ
Decorator         :
ConcreteDecoratorA:ConcreteComponentインスタンスのそれぞれを二倍して出力するように
ConcreteDecoratorB:ConcreteComponentインスタンスのそれぞれを1/2して出力するように
'''


class Component:
    '''責任を動的に追加できるようになっている
    オブジェクトのためのインタフェースを定義します。
    '''
    def __init__(self, x, y):
        # 値を定義しちゃってるけどそれはpythonにはインタフェースがないため。
        self.x = x
        self.y = y

    def show(self):
        pass

    def mul(self, dx, dy):
        pass

class ConcreteComponent(Component):
    '''責任を追加できるようになっているオブジェクト(component)を定義します。'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f'x={self.x}でy={self.y}ですよ。'

    def mul(self, dx, dy):
        self.x *= dx
        self.y *= dy


class Decorator(Component):
    '''componentまたはdecoratorへの参照を保持し、
    またComponentクラスのインタフェースと一致したインタフェースを定義します。'''
    def __init__(self, component):
        self.component = component

    def show(self):
        return self.component.show()

    def mul(self, dx, dy):
        return self.component.mul(dx, dy)


class ConcreteDecoratorA(Decorator):
    '''componentに責任を追加するオブジェクト(decorator)を定義します。'''
    def __init__(self, component):
        super().__init__(component)

    def show(self):
        self.nibai()
        return super().show() + 'にばーい'

    def nibai(self):
        self.mul(2, 2)


class ConcreteDecoratorB(Decorator):
    '''同上'''
    def __init__(self, component):
        super().__init__(component)

    def show(self):
        self.nibun()
        return super().show() + 'にぶーん'

    def nibun(self):
        self.mul(1/3, 1/3)


component1 = ConcreteComponent(100, 200)
print(component1.show())
component2 = ConcreteDecoratorA(component1)
print(component2.show())
component3 = ConcreteDecoratorB(component2)
print(component3.show())
