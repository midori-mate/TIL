
GitNote
===

2015 年のエンジニアに Git は欠かせない。

## 設定編

### インストール
    $ brew doctor
    $ brew install git
    $ git --version

### config
    $ git config --global user.name ****
    $ git config --global user.email ****@****.com
    $ git config --global ui.color auto
    $ git config --global push.default current    「カレントブランチと同名のリモートブランチがあればそこへpushする」
    $ git config -l --global                      確認

### テキスト入力をSublimeで行う
    1. sublコマンドを有効化(sublのシンボリックリンクを作る)
        $ ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
    2. gitのエディタをsublにする
        $ git config --global core.editor "subl -w"

### エイリアス(.gitconfigに書く) 以下、ノートはこのエイリアスありきで書く。
    [alias]
        graph = log --graph --date=short --pretty='format:%C(yellow)%h %C(green)%cd %C(blue)%an%C(red)%d %C(reset)%s' --all
        graph5 = log --graph --date=short --pretty='format:%C(yellow)%h %C(green)%cd %C(blue)%an%C(red)%d %C(reset)%s' --all -n 5
        graph10 = log --graph --date=short --pretty='format:%C(yellow)%h %C(green)%cd %C(blue)%an%C(red)%d %C(reset)%s' --all -n 10
        stt = status -uno
        diffno = diff --name-only
        diffwd = diff --word-diff
        co = checkout
        br = branch
        inicom = commit --allow-empty -m 'Initial Commit.'
        adda = add --all

***

## ネーミングルール

### ブランチ
    master          つねにHEADはリリースできる状態。
    develop         開発中のメインブランチ。完了したら master にマージ。
    feature/NAME    各個人が機能ごとに切るブランチ。NAMEは機能名。完了したら develop にマージ。
    hotfix/NAME     緊急に master から切るブランチ。完了後は master と develop にマージ。

### タグ
    よくわからんけど yyyy-mm-dd とかでいいんじゃね?

### コミットのコメント
    {ブランチ名} {作業内容}
        例: feature/users ■ユーザ一覧を作成

### リモートリポジトリ
    origin

***

## シチュエーション別コマンドセット

### 01. ローカルで自分だけで遊ぼーっと
    $ git init                     リポジトリ作成。
    $ git inicom                   空コミット作成。
    $ git adda                     ステージング。
    $ git stt                      現在の状態。
    $ git commit -m "COMMENT"      コミット。
    $ git commit --amend           最新のコミットを修正。コメントを変更したり、ファイルを追加したり。じつは --ame だけで有効。マジかよ。
    $ git reset --mixed HEAD       最新コミット取り消し。HEADをREVISION名にすればそこまで取り消す。
    $ git graph                    コミット履歴。
    $ git graph5                   
    $ git graph10                  
    $ git reset --hard REVISION    昔の状態にリセットする。REVISIONにはコミット履歴で見れるハッシュ文字列を書く。

### 02. ブランチ切って遊ぼーっと
    $ git branch BRANCHNAME           ブランチ作成。
    $ git branch -m ORIGINAL NEW      名前変更。
    $ git co BRANCHNAME               ブランチ移動。
    $ git merge --no-ff BRANCHNAME    現在のブランチへ、BRANCHNAMEをマージする。
                                      --no-ffはfast-forwardの関係であってもマージコミットを作る。
    $ git branch -d BRANCHNAME        ブランチ削除。

### 03. リモートリポジトリを準備する
    $ git init --bare --shared=true    リモートにするディレクトリで。

### 04. リモートから落としたり上げたり
    $ git remote add origin URL              リモートリポジトリのURLを登録。
    $ git remote -v                          登録されてるリモートを確認。
    $ git remote rm origin                   リモートの登録解除。
    $ git push REMOTENAMEorURL BRANCHNAME    リモートに上げる。
    $ git clone URL                          (初回)リモートから落とす。
    $ git fetch                              リモートの状態を落とす(ワーキングツリーには影響なし)。

### 05. てかブランチを切るの切るって何?
    英語で Start a branch って出たので思いついた。この「切る」は「スタートを切る」の切ると同じだろう。
    そしてスタートを切るの切るは、「堰を切る」が語源っぽい。堰(ダム)を留めている綱を切り落とすように勢い良く物事が始まること。
    納得できた。

### 06. 開発ブランチに develop を反映したい
    $ git co develop
    $ git pull origin develop
    $ git co feature/***
    $ git merge --no-ff develop

### 07. rebase について
    なんかー、 github desktop 使いながら実際に運用してたらー、結局あんまり使わないー。
    ぶっちゃけマージでよくない? って感じ。いちおうコマンドは下に書いとくけど……。

### 08. rebase を使って develop の内容を開発ブランチに反映させたい
    develop を最新にする。
    開発ブランチに移動。
    $ git rebase develop --whitespace=nowarn (trailing whitespaceのエラーを無視)
    コンフリクトを解消する。
    $ git adda
    $ git rebase --continue
    $ git rebase --abort      rebase をやっぱヤメ。

### 09. 開発ブランチに develop を反映したいんだけどワーキングツリーが中途半端。一時コミットもしたくない
    $ git stash
    $ git stash pop

    ● 詳しく。
    $ git stash                   コミットしていない変更を保存
    $ git stash save "mes"        メッセージありstash
    $ git stash list              stashのリスト
    $ git stash show -p           最新stashの内容
    $ git diffno HEAD..stash@{n}  stashの内容確認(ファイル名のみ)
    $ git stash show -p stash@{0} もっと詳しい内容
    $ git stash pop               最新のstashを適用(stashは消える)
    $ git stash pop stash@{n}     n番目のstashを適用(stashは消える)
    $ git stash apply pop         適用(stash残す)
    $ git stash drop              消す

### 10. gitignore はとりあえずこれだけ書いとけ
    *~
    .DS_Store

    # これは最後に書かないとダメ。
    !.gitkeep

### 11. gitignore が反映されないんだけど
    $ git reset --mixed HEAD            github desktop 使ってるときは勝手にaddられてる可能性あるので解除。
    $ git rm -r --cached .
    $ git adda
    $ git commit -m "develop Update gitignore."

### 12. プロジェクト内にもっておきたいが commit に含めたくない gitignore にも書きたくないファイル
    .git/info/exclude に記述する。
    書き方はignoreと同じ。

### 13. ファイルを無視したい(exclude との違いはしらん)
    $ git update-index --skip-worktree スキップしたいファイル名
    解除するには
    $ git update-index --no-skip-worktree スキップしてたファイル名
    現在無視しているファイルを見るには
    $ git ls-files -v | grep ^S

### 14. タグをつけたい
    $ git tag TAGNAME REVISION          タグ作成
    $ git push REMOTENAME --tags        タグをリモートに反映
    $ git tag -d TAGNAME                タグ削除
    $ git push -d REMOTENAME TAGNAME    リモートのタグ削除
    $ git tag                           タグ一覧
    $ git graph | grep tag:             タグとハッシュを同時に確認

### 15. リセットいろいろ
    $ git reset --hard REVISION         全部そこに戻る。作業中データも失せる。
    $ git reset --mixed REVISION        コミットとステージングが戻る。
    $ git reset --soft REVISION         コミットが戻る。あっ、今のコミットなしで……ってとき。
    $ git co REVISION -- FILEPATH       ファイル単位でのリセット。

### 16. リセットでしくじったら
    $ git reset --hard ORIG_HEAD    リポジトリにおける最新状態に戻る
    $ git reflog                    HEADの履歴を見る。これで戻りたいところを指定できる。

### 17. PatchMaker 使ってサーバにパッチを上げるときの手順 
    $ git graph | grep tag          前回のタグのハッシュを確認
    $ git diffno REVISION           前回と変わったファイルを取得
    ・PatchMakerに貼って実行。
    ・パッチファイルをサーバに移動。
    ・動作が問題なければタグをつけてpush。

### 18. やべ、ブランチ消しちゃった
    $ git reflog
    $ git branch ブランチ名 消しちゃったブランチのREVISION名

### 19. ディレクトリが add できず submodule なんちゃらって出る
    $ git rm -rf --cached 対象ディレクトリ
    $ git add 対象ディレクトリ
    ・ディレクトリがファイルとして認識されてるのが原因らしい。ひとまず消して、まだ足せばOK。

### 20. Commit の日付を変更したい
    ・ 直前のやつしか今のとこできない。
    $ git rebase -i HEAD~1
    $ git commit --amend --date="Wed Feb 07 00:00:00 2018 +0900"  # 日付は適当に作って。
    $ git rebase --continue
    $ git rebase HEAD~1 --committer-date-is-author-date
    $ git log --pretty=fuller  # 変わっていること確認したいとき。

### 21. windows10 cmdで日本語が文字化けする
    $ git config --global core.pager "LESSCHARSET=utf-8 less"

    ・ .gitconfigではこんな感じになる。
        [core]
            pager = LESSCHARSET=utf-8 less

### 22. git をビルトインではなくて brew 版にする
    $ brew doctor
    $ brew update
    $ brew install git
    これだけだとまだMacデフォルトのやつ /usr/bin/git が呼び出されちゃう。
    だから .bash_profile に追加
        export PATH=/usr/local/bin:$PATH


***

## Gitbucket ノート

### ローカルのリポジトリをBucketへアップ
    リポジトリ作って、readme.mdは作らない
    そうするとQuick setupが出る
    git remote add origin <表示されたURL>
    git push -u origin master

### Bucket上でマージしたい
    feature/A を feature/B にマージ
    プロジェクトトップの左サイドバー > Pull requests > New pull requests > 左にBのブランチ、右にAのブランチ

### Gitbucketとslackの連携
    Slack側
        Customize slack > Configure Apps > Githubを選択 > Add Configuration > Post Channelを選択 > switch to unauthed modeリンク
        Customize Nameをgitbucketに変更
        Customize Iconをhttps://raw.githubusercontent.com/takezoe/gitbucket/master/src/main/webapp/assets/common/images/gitbucket.png から拝借してUpload.
        Webhook URLをコピー
    Gitbucket側
        setting > Service Hooks > URL貼り付け > 適当に、通知の設定して完了

### 他人のリポジトリに pull request する
    そもそもリポジトリ側で pull request を許可
        リポジトリ > Settings > Issues and Pull request
        All users can view, create and comment on issues and pull requests にチェックつける。
    Fork する
        対象のリポジトリ > Forks > Forkボタン押す
        自分のとこに対象リポジトリのコピーみたいなもんができる。
    更新する
        ふつーにブランチ切って push
    PRする
        ふつーに bucket 上でPRする。

***

## Gitlab ノート

### ほかの人をグループ許可
    https://gitlab.com/groups/groupname/-/group_members
    グループのページ > 左サイドバーMembers > Add new memberのところで追加。

### merge request を投げるまで
    $ git clone https://gitlab.com/groupname/GitNote.git    とりあえずクローン。自分の Gitlab 情報を打ち込む必要あるかも。
    あとはリポジトリを github desktop に読ませていつもどおりブランチ切って push して
    https://gitlab.com/groupname/GitNote/branches
    ここから merge request すればよい。
    Developer 以下の権限だと自分でマージができない。

### Slackと連携
    Slack側
        1. https://slack.com/apps/A0F7XDUAZ--web-
        2. Add Configuration
    Gitlab側
        対象プロジェクト > Settings > Integrations > Slack notifications
        Active にチェック入れる。
        Webhookにさっきのコピーをペースト。

***

## これを書いてる頃にはもう出会わないんだけど昔のエラーノート
    ● 出たエラー
        Please enter the commit message for your changes.
            -mオプションの入れ忘れによるもの。vimで入力することになる。
            vimは :q! で脱出。
        remote HEAD refers to nonexistent ref, unable to checkout.
            リモートリポジトリでブランチが設定されてないのが原因。
            リモートリポジトリに入ってブランチ移動すればいい。
            ただしcheckoutじゃなくてsymbolic-refを使う。checkoutはローカルでのみ。
                checkoutだと fatal: This operation must be run in a work tree 言われる。
            $ git symbolic-ref HEAD refs/heads/<BRANCH NAME>
        (rebase中に) error: could not apply
            rebase中にCONFLICTしてる。
            ファイルの <<<<<<< HEAD とかを整理したら
                $ git rebase --continue
            やっぱやめるなら
                $ git rebase --abort
        エラーじゃないが、 detached HEAD というブランチに来てしまった。
            * (HEAD detached from refs/heads/way2) こんな感じ。
            あわてずgitちゃんの親切なメッセージを読めばよろしい。
        Untracked files でコミットができない。
            新しくファイルが増えたときは -a -m "..." ができないっぽい。まずは add --all してから。
        error: failed to push some refs to 'ins.git'
            rebase -i でコミットをまとめたあとにpushしたら出た。
            方法1. git pullする
                したらマージが始まって、履歴がもちゃっとして、それでもpushができるようにはなった。
            しかし、マージで履歴のグラフがすげーことになっちまってる。一本にしたいんだけど。
            てかrebase -iがもとに戻っちゃってるし。
    問題:リモートリポジトリの履歴を整理したい
        上の「git pull --rebase を理解するまでのノート」で整理しながら理解
            リモートリポジトリは履歴を整理するものじゃねえ。
    問題:HEAD detached from 7d096fc
        コミットしても.DS_Storeが修正されてるって出てる。
        えっとねえ…よくわからんうちに解決した。よくわからんなりにやったことを書いとくよ。
            1. $ git co -- .DS_Store (こうしろってgitに言われた。意味はしらん)
            2. $ git co master       (こうしたらすっげえ前のバージョンに戻っちゃった。ちょっと焦ったが、もちろん…)
            3. $ git reflog
            4. $ git reset --hard HEAD@{1} (もちろんこうする。)
        以上のことをやったら、なんかdetachedじゃなくなってた。ちゃんとmaster上になってた。
        解決?
    問題:Windows でgitコマンド叩くと、日本語が文字化けする
        $ git config --global core.quotepath false
        $ git config --global gui.encoding utf-8
        $ SETX LANG ja_JP.UTF-8
        これ全部打ってPowerShell開き直したら日本語出た。ゴメン、次やるときは一個ずつやって、どれが効果あるのか見て下さい。

***

## コミットログ例文集

オプションやフラグ、メニューを追加した

    Add -enable-experimental-nested-generic-types frontend flag
    Add --main-process flag to run specs in the main process
    Add Throws flag and ThrowsLoc to AbstractFunctionDecl
    Add "event" parameter for "click" handler of MenuItem
    Add File > Exit menu on Windows

ファイルを追加した

    Add npm start script
    Add build script
    Add SkUserConfig.h with blank SkDebugf macro

メソッドや機能を追加した

    Add TypeLowering::hasFixedSize()
    Add overflow scrolling
    Add convenience API for demangling
    Add a typealias to avoid a build ordering dependency between projects
    Add a helper method mayHaveOpenedArchetypeOperands to SILInstruction

実装を別のものへ切り替えた

    Use args.resourcePath instead of args.devResourcePath
    Use arrays instead of while loops
    Use auto instead of repeating explicit class names
    Use weak pointer instead of manual bookkeeping
    Change all uses of 'CInt' to 'Int32' in the SDK overlay
    Change Integer#year to return a Fixnum instead of a Float to improve consistency

新しく何かに対応した/機能上の制約を取り払った

    Add support for closure contexts to readMetadataFromInstance()
    Add support for activating and deactivating package-specific keymaps
    Add support for launching HTML files directly
    Add support for allocators that require tensors with zero
    Make it possible to call reflect multiple times
    Make it possible to set a data type for variables that come out of constants
    Allow atom-pane to be shrunk independently of its contents' width
    Allow null TextEditorComponent::domNode during visibility check

何かを使うようにした

    Use const for util require
    Use FoldingSetNode for ProtocolType
    Use unique text editor title in window and tab titles
    Use an empty object if metadata is ~null
    Use target_link_libraries for fat executable dependencies
    Use existing flatMapToOptionalTests dataset

より好ましい実装に改良した

    Make the clone function more generic
    Make IO faster for v8 compile cache
    Make model constructor argument to addViewProvider optional
    Make Browser::Quit more robust
    Make Menu.getApplicationMenu() public
    Improve incompatible native module error message
    Improve readability of multi-line command
    Improve folds behavior when duplicating lines
    Improve deprecated message on webPreferences options

何かを出来ない/しないようにした

    Don't bail reading a metadata instance if swift_isaMask isn't available
    Don't exit until the parent asks for an instance
    Don't include Parent pointer in Nominal/BoundGeneric TypeRef uniquing
    Don't use MatchesExtension for matching filters
    Don't use ES6 class for AutoUpdater windows class
    Don't use MatchesExtension for matching filters
    Avoid distinct if a subquery has already materialized
    Avoid infinite recursion when bad values are passed to tz aware fields

オブジェクトの内容や挙動を確認しやすくした

    Emit capture descriptors in their own section
    Emit field metadata for @objc classes
    Emit reflection info for protocols

Assertを追加した

    Add assert for role with app name in label
    Add assertions for no available bookmark
    Add asserts for properties

不要なコードを除去した

    Remove some dead code
    Remove some unused enum declaration
    Remove unused variable
    Remove unnecessary line feeds
    Remove trailing whitespace
    Remove debug statement
    Remove redundant mapType{Into,OutOf}Context() calls

コードを移動した

    Move function signature analysis to a Util
    Move markInvalidGenericSignature() to a method on TypeChecker
    Move diagnostic for stored properties in protocols from type checking to validation
    Move Doxygen converter into a proper MarkupASTNode visitor
    Move Module require to top

名前を修正した

    Rename environment -> environmentHelpers
    Rename watchProjectPath to watchProjectPaths
    Rename generic arguments
    s/grammarName/grammar
    fullVersion -> writeFullVersion

小さなバグやタイポを修正した, 警告を潰した

    Fix typos
    Fix a typo
    Fix a test
    Fix typo in DevTools Extensions tutorial
    Fix DownloadingState typo
    Fix includes order
    Fix mistake in tvOS availability
    Fix cpplint warnings
    Fix wrong markdown
    Add missing return
    Add missing period in comment

バグや好ましくない挙動を修正した

    Fix a memory leak in FSO
    Fix lifetime issues in ManagedBuffer.value
    Fix mangling for nested generic types
    Fix memory corruption in another circularity check
    Fix thread-unsafety in Process.Argument initialization
    Fix "Object has been destroyed" error in "page-title-updated" event
    Make Error.prepareStackTrace read-only (again)
    Make string slicing tests standalone
    Make sure showing success dialogs works correctly
    Make sure to emit closure bodies only once
    Make sure all native resources get freed on exit
    Make sure temp file will be cleaned up when base::Move fails

テスト、コメント、ドキュメントを追加した

    Add tests for pending pane items
    Add validation test for projecting existentials
    Add a basic test for opening an editor in largeFileMode if >= 2MB
    Add specs for moveSelectionLeft()
    Add failing spec for Menu.buildFromTemplate
    Add comment about map key/values
    Add TODO about blinkFeatures -> enableBlinkFeatures
    Add a design-decisions section to the CONTRIBUTING guide
    Add style.less examples
    Add docs for app.getLocale()
    Add documentation for --proxy-bypass-list

テストを削除した

    Remove a redundant test
    Remove an empty test

テスト、コメントを修正した

    Fix comment
    Fix outdated comment
    Fix failing specs on Windows
    Fix PersistentVector test for powerpc64{le}
    Update specs for deferred activation hooks
    Update successor/predecessor in validation tests
    Update some tests to use LifetimeTracked instead of hand-rolled canaries

ドキュメントを修正した

    Update README.md
    Update docs for marker callback
    Update link to solarized-dark-syntax
    Improve documentation of ses.cookies.set()
    Improve readability in CSRF section of guide
    Improve spec description
