SequelizeNote
===

これをゴチャゴチャ調べることで orm と migration がわかったように思う。


## orm と migration

object-relational mapping ってのはアレだ DB をオブジェクト指向っぽく扱う方式のことだ。オブジェクト指向っぽくと言うのは……

- テーブルが model クラスになってる
- データ取り出すときは sql じゃなくてメソッドチェーンとかリフレクションでとってこれる

ぼくが**「モデルからメソッドチェーンでデータとるやつよ!」**とかこれまで言ってたやつには orm って名前がついてたってわけね。

migration ってのはプログラムが migration file をもとにして DB の構造を変更してくれるやつよ。

ぼくは一番最初に django に触れたから、「migration == モデルクラスがあってラクにデータとれて、モデルを自動で migration file にしてくれて、それを DB に反映してくれる方式のこと」だと思いこんでいたのだ。だけどこれは orm と migration の組み合わせだったわけだ。


## 上の知識を前提にして「Sequelize って何?」

orm と migration をどっちも担当できるモジュール。 migration を担当できるのは sequelize-cli っていうさらに他のモジュール。だからこれについて調べるときは orm のほうか migration のほうの話か意識しないとダメ。

このノートを書いているとき(2019-07-01)には migration 機能だけを使いたいのでそっちに重点をおいている。


## 役に立つページ

Sequelize のドキュメントはブラウザのページタイトルが変わらないのがクソ。見づらい。

- [モデルの定義](http://docs.sequelizejs.com/manual/models-definition.html)
- [DataType の種類](http://docs.sequelizejs.com/manual/data-types.html)
- [QueryInterface のメソッド](http://docs.sequelizejs.com/class/lib/query-interface.js~QueryInterface.html)


## コマンド

```bash
# インストール
$ npm install --save-dev sequelize sequelize-cli

# 確認(もしグローバルにインストールするなら sequelize だけで動くけどね)
$ node_modules/.bin/sequelize

# DB の情報を書く config.json 生成。
$ node_modules/.bin/sequelize init:config

# DB 作成。 schema 用の migration file とかはなくて config.json の設定が使われる。
$ node_modules/.bin/sequelize db:create

# DB 削除。
$ node_modules/.bin/sequelize db:drop

# model, migration 同時作成。
$ node_modules/.bin/sequelize model:generate --name ModelName --attributes Field1:string,Field2:integer

# migration だけ作成。 attributes はこっちにはない。
# ここの name はモデル名じゃなくて migration file 名になるから create- とかつけるといいかも。
$ node_modules/.bin/sequelize migration:generate --name create-ModelName

# migration file を使って migrate
$ node_modules/.bin/sequelize db:migrate
# migration file 指定。これは「このファイルまで」だよ。時刻がこれより前のやつは全部実行される。
$ node_modules/.bin/sequelize db:migrate --to 20190628070134-create-ModelName.js

# migration file が間違ってたから戻したいわ。
# いっこ戻す。
$ node_modules/.bin/sequelize db:migrate:undo
# 全部戻す。
$ node_modules/.bin/sequelize db:migrate:undo:all
# 「このファイルまで」戻す。
$ node_modules/.bin/sequelize db:migrate:undo:all --to 20190628070134-create-ModelName.js
# 裏技
# DB の SequelizeMeta を直接編集。

# ちっとオプションをつけたコマンド。
# --env config.json のキー名を指定する。
# --url config.json に
$ node_modules/.bin/sequelize db:migrate --env XXX --url 'mysql://user:pw@host/dbname'
```


## config.json

```json
{
  "local": {
    "username": "",
    "password": "",
    "database": "",
    "host": "mysqldb",
    "dialect": "mysql",
    "dialectOptions": {
      "charset": "utf8"
    }
  },
  // json ファイルにパスワードとか書きたくないなら --url オプションで補ってね。
  "production": {
    "dialectOptions": {
      "charset": "utf8"
    }
  },
}
```


## MySQL の型と Sequelize の type の対応

基本的には[ここ](http://docs.sequelizejs.com/manual/data-types.html)を見れば OK。

```javascript
// varchar(255) はどうすんの?
type: Sequelize.STRING,

// varchar(16) はどうすんの?
type: Sequelize.STRING(16),

// NOT NULL はどうすんの?
allowNull: false,

// longtext
type: Sequelize.TEXT('long'),

// tinyint(1)
type: Sequelize.BOOLEAN,
```


## migration file

多分だけど up と down には以下のようなことを書く……

- up: `db:migrate` のときの処理。
- down: `db:migrate:undo` のときの処理。

```javascript
'use strict';

const tableName = 'table';

module.exports = {
  up: (queryInterface, Sequelize) => {

    // createTable こんな感じ。
    return queryInterface.createTable(tableName, {
      createdAt: {
        type: Sequelize.STRING,
      },
      updatedAt: {
        type: Sequelize.STRING,
      },
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        unique: true,
        type: Sequelize.INTEGER,
      },
    });

    // addColumn こんな感じ。
    return Promise.all([
      queryInterface.addColumn(tableName, 'newColumn', {
        type: Sequelize.STRING,
        after: 'existingColumn',
      }),
    ]);


    // bulkInsert こんな感じ。
    const currentUtcIsoString = (new Date()).toISOString();
    const insertParams = timezones.map((t) => {
      return {
        createdAt: currentUtcIsoString,
        updatedAt: currentUtcIsoString,
        timezoneName: t,
      };
    });
    return queryInterface.bulkInsert(tableName, insertParams);
  },

  down: (queryInterface, Sequelize) => {

    // up が createTable のとき。
    return queryInterface.dropTable(tableName);

    // up が addColumn のとき。
    return Promise.all([
      queryInterface.removeColumn(tableName, 'title'),
    ]);

    // up が bulkInsert のとき。
    const deleteParams = timezones.map((t) => {
      return { timezoneName: t };
    });
    return queryInterface.bulkDelete(tableName, {
      [Sequelize.Op.or]: deleteParams,
    });
  },
};
```
