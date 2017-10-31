#!/usr/bin/env python
# coding: utf-8

'''
実行
    $ nosetests -v -s --with-coverage

目次
    ■ とりあえずpipしとけ
        $ pip install nose
        $ pip install coverage
        $ pip install mock
        $ pip install parameterized

    ■ テスト命名規則
        FILE NAME  : test_か_testのついた名前
        TEST METHOD: 同上

    ■ テスト作成手順
        コンソールから
            $ nosetests -v(テスト名やdocの表示) -s(標準出力)
        スクリプト内から
            nose.main(argv=['-v', '--with-afterlog'], addplugins=[Foo()])
            ただしコレで実行するとカバレッジがうまくとれないよ。

    ■ カバレッジのとりかた
        $ nosetests --with-coverage
        $ coverage report -m コンソール上でカバレッジ表示
        $ coverage html      カバレッジhtml作成

    ■ 最初に書いたほうがいいimport
        ↓これ
'''
from nose.tools import ok_, eq_, with_setup
from mock import Mock
from parameterized import parameterized

import foo  # これはテストするモジュール。


# ■ 実例1: 普通のテスト。
def test_1():

    # Input.
    x = 1
    y = 2

    # Expected.
    expected = 3

    # Verify.
    actual = foo.Foo.static_method(x, y)
    eq_(expected, actual)


# ■ 実例2: ひたすらたくさんの入力値、期待値パターンを書く。ぶっちゃけ全部コレでいいだろ。
@parameterized([
    (1, 2, 3),
    (3, 4, 7),
    (6, 3, 9),
])
def test_2(x, y, expected):

    # Verify.
    actual = foo.Foo.static_method(x, y)
    eq_(expected, actual)


# ■ 実例3: 例外を出すテスト。
@parameterized([
    (True, TypeError),
    (False, ValueError),
])
def test_3(x, expectedException):

    try:
        foo.Foo.exception_method(x)
    except Exception as e:
        ok_(isinstance(e, expectedException))
        return
    ok_(True is False, 'Exception must be thrown.')


# ■ 実例4: parametarizedに例外を含む。実例2,3の合成。
@parameterized([
    (True, True, TypeError),
    (False, True, ValueError),
    (1, False, 1),
    ('a', False, None),
])
def test_4(x, expectException, expected):

    # 通常の返り値期待。
    if not expectException:
        actual = foo.Foo.exception_method(x)
        eq_(expected, actual)
        return

    # 例外期待。
    try:
        foo.Foo.exception_method(x)
    except Exception as e:
        ok_(isinstance(e, expected))
        return
    ok_(True is False, 'Exception must be thrown.')


# ■ 実例5: メソッドをすげ替える(モックする)。
def test_5():

    # 対象メソッド内の Bar.static_method をモックします。
    # フツーに実行したら 1 が返ってくるけど、そこを 5 にすげ替える。
    foo.Bar.static_method = Mock(return_value=5)

    # Expected.
    expected = 5

    # Verify.
    actual = foo.Foo.use_other_class_method()
    eq_(expected, actual)


# ■ 実例6: モジュールの前後に関数を実行させる。
def setup():
    '''setupって名前で作れば自動で実行。'''
    print('実例6: setup')
def teardown():
    '''teardownって名前で作れば自動で実行。'''
    print('実例6: teardown')


# ■ 実例7: 関数の前後に関数を実行させる。
def setup2():
    foo.Bar.X = 5
def teardown2():
    foo.Bar.X = 1


@with_setup(setup2, teardown2)
def test_7():
    eq_(5, foo.Bar.class_method())
