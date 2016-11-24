
: SJIS(Western Windows1252)で保存すること

: おまじない 
@echo off
cd /d %~dp0
setlocal enabledelayedexpansion

: for文
:     (オプションなし) ディレクトリ内を対象にとる
:     /d ディレクトリ名を対象にとる
:     /r ディレクトリ名およびそのサブディレクトリ内を対象にとる
:     /l 値を指定して代入
:     /f テキストファイル内の文章に対して

: dir
:     /a ファイルを表示する /adでディレクトリ、/ahで隠しファイル、-をつけるとその属性以外
:     /b ファイル名のみ表示
:     /o 表示順 n名前順 sサイズ順(小さい方から) e(拡張子順、アルファベット) d(古い方から) g(ディレクトリから) -つければ逆に /o-dこんな漢字


: find
:     /v 指定した文字列を含まない
:     /c 指定文字列を含む行数
:     /n 出力する行の前に行番号をつける
:     /i 小文字大文字を区別しない
find /v /c /n /i "検索文字列" ファイル名

: ディレクトリ内のディレクトリ数をCOUNTへ格納する
: http://capm-network.com/?tag=Windows%E3%83%90%E3%83%83%E3%83%81%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%AE%9F%E8%A1%8C%E7%B5%90%E6%9E%9C%E3%81%AE%E5%8F%96%E5%BE%97
for /f "usebackq" %%i in (`dir /ad /b "D:\01_Backup" ^| find /c /v ""`) do (
    set COUNT=%%i
)

: ディレクトリ内で一番古いディレクトリを取得する 新しいのがよかったら/o-dを/odにしてね
: delims=は配列(?)の区切りを決めてる。デフォルトではスペースが含まれるから、新しいフォルダ (1)で異常が出る
set OLDEST=
for /f "usebackq delims=" %%i in (`dir D:\01_Backup /ad /o-d /b`) do ( set OLDEST=%%i )
echo !OLDEST!

: ゼロ埋めした時刻を取得する
set T=%time: =0% (これがゼロ埋め)
echo %T:~0,2%.%T:~3,2%.%T:~6,2%.

: if文の比較演算子
: A equ B    ==
: A neq B    !=
: A gtr B    >
: A geq B    >=
: A lss B    <
: A leq B    <=

: スリープになるまでの時間をコントロールする
POWERCFG -x -standby-timeout-ac 0
POWERCFG -x -standby-timeout-dc 0
: 0ならスリープなし

: まあいろんな事情につき、変数の前後にはいっちゃった不要なスペースを取り除く方法
call :Foo !COUNT!
exit
:Foo
set COUNT=%*
: 最初COUNTが"2 "だったとしても"2"になる
: :Fooはexitより下に書くこと


endlocal
