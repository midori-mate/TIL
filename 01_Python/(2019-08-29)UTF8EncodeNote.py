
"""UTF8EncodeNote

UTF8 のエンコード方式を調べた。 Python で再現してみようと思った。

Unicode 文字 -> UTF-8 の変換手順

- 文字のコードポイントを取得。
- コードポイントの値によって4パターンに分岐
    1. 7f まで
        0xxxxxxx に7桁2進数化したコードポイントを当てはめる。
    2. 7ff まで
        110xxxxx 10xxxxxx に11桁2進数化したコードポイントを当てはめる。
    3. ffff まで
        1110xxxx 10xxxxxx 10xxxxxx に16桁2進数化したコードポイントを当てはめる。
    4. 10ffff まで
        11110xxx 10xxxxxx 10xxxxxx 10xxxxxx に21桁2進数化したコードポイントを当てはめる。
- 各2進数(8桁ずつなのでバイト列)を16進数化する。
"""

"""'あ' の場合
"""

# 文字のコードポイントを取得します。
codepoint = ord('あ')  # 12354

# 12354 だと「ffff まで」の分類になるので
# 1110xxxx 10xxxxxx 10xxxxxx に16桁2進数化したコードポイントを当てはめます。

# コードポイントを16桁の2進数にします。
codepoint_bin = '{:016b}'.format(codepoint)  # 0011000001000010

# x に2進数を当てはめます。
bytes_bin = [
    '1110' + codepoint_bin[  : 4],  # 11100011
    '10'   + codepoint_bin[ 4:10],  # 10000001
    '10'   + codepoint_bin[10:  ],  # 10000010
]

# 各バイト列を16進数に変換します。
def hex_(b):
    return '{:02x}'.format(int(b, 2))
bytes_hex = map( hex_, bytes_bin )  # e3, 81, 82

# くっつけます。
bytes_ = ''.join(bytes_hex)  # e38182

# bytes 型にします。
bytes_ = bytes.fromhex(bytes_)  # b'\xe3\x81\x82'

# 本当に UTF-8 になっているのか? デコードして確認してみよう。
print( bytes_.decode('UTF-8') )  # あ

"""'あ' の場合 ここまで
"""


def manual_encode_UTF8(char):
    """char.encode('UTF-8') で出来ることをがんばって再現してみる。"""

    # 文字のコードポイントを取得します。
    codepoint = ord(char)

    # コードポイントの値によって、 UTF-8 バイト列の作成方法が分岐します。
    def calc(i):
        if i <= int('7f', 16):
            return _get_bytes1
        if i <= int('7ff', 16):
            return _get_bytes2
        if i <= int('ffff', 16):
            return _get_bytes3
        if i <= int('10ffff', 16):
            return _get_bytes4
    get_bytes_function = calc(codepoint)

    # UTF-8 バイト列を取得します。
    return get_bytes_function(codepoint)


def _get_bytes1(codepoint):
    """バイトが1個のときの UTF-8 バイト列作成。
    0xxxxxxx に2進数を当てはめます。
    """

    # コードポイントを x の数ぶんの2進数にします。
    codepoint_bin = '{:07b}'.format(codepoint)

    # x に2進数を当てはめます。
    bytes_bin = [
        '0' + codepoint_bin,
    ]

    # 各2進数を16進数に変換します。
    bytes_hex = map( lambda b: '{:02x}'.format(int(b, 2)), bytes_bin )

    # くっつけてバイト列にします。これが UTF-8 のバイト列です。
    return bytes.fromhex(''.join(bytes_hex))


def _get_bytes2(codepoint):
    """バイトが2個のときの UTF-8 バイト列作成。
    110xxxxx 10xxxxxx に2進数を当てはめます。
    """

    codepoint_bin = '{:011b}'.format(codepoint)
    bytes_bin = [
        '110' + codepoint_bin[ :5],
        '10'  + codepoint_bin[5: ],
    ]
    return bytes.fromhex( ''.join( map( lambda b: '{:02x}'.format(int(b, 2)), bytes_bin ) ) )


def _get_bytes3(codepoint):
    """バイトが3個のときの UTF-8 バイト列作成。
    1110xxxx 10xxxxxx 10xxxxxx に2進数を当てはめます。
    """

    codepoint_bin = '{:016b}'.format(codepoint)
    bytes_bin = [
        '1110' + codepoint_bin[  : 4],
        '10'   + codepoint_bin[ 4:10],
        '10'   + codepoint_bin[10:  ],
    ]
    return bytes.fromhex( ''.join( map( lambda b: '{:02x}'.format(int(b, 2)), bytes_bin ) ) )


def _get_bytes4(codepoint):
    """バイトが4個のときの UTF-8 バイト列作成。
    11110xxx 10xxxxxx 10xxxxxx 10xxxxxx に2進数を当てはめます。
    """

    codepoint_bin = '{:021b}'.format(codepoint)
    bytes_bin = [
        '11110' + codepoint_bin[  : 3],
        '10'    + codepoint_bin[ 3: 9],
        '10'    + codepoint_bin[ 9:15],
        '10'    + codepoint_bin[15:  ],
    ]
    return bytes.fromhex( ''.join( map( lambda b: '{:02x}'.format(int(b, 2)), bytes_bin ) ) )


#  UTF-8 エンコードが出来る全文字でテストします。
unicode_chars = ( chr(i) for i in range(int('10ffff', 16)+1) )
for char in unicode_chars:
    try:
        assert manual_encode_UTF8(char) == char.encode('UTF-8'), f'失敗したよ: {char}'
    except UnicodeEncodeError:
        pass
