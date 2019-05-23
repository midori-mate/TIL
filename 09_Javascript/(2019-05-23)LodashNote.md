LodashNote
===

lodash.js ライブラリをまとめる。まとめることで JS 書いてるときに「これ lodash にあった気がする」って思いつけるように。


## 配列

```javascript
// foreach 的なやつ。
_.each(array, (a) => {
    console.log(a);
});
```


## 高階関数

```javascript
// map
var newArray = _.map(array, (a) => {
    return `_${a}_`;
});

// オブジェクトを値で map 
var newObj = _.mapValues(obj, (value) => {
    return `_${value}_`;
}); 

// オブジェクトをキーで map
var newObj = _.mapKeys(obj, (key) => {
    return key;
});

// filter
var newArray = _.filter(array, (a) => {
    return _.includes(a, 'u');
});

// オブジェクトを値で filter
var newObj = _.pickBy(obj, (value) => {
    return _.includes(value, 'u');
});
```


## 集合

```javascript
// Python でいうところの set()
var newArray = _.union(array);

// 和集合
var newArray = _.union(array, array2);

// 積集合
var newArray = _.intersection(array, array2);

// 差集合
var newArray = _.difference(array, array2);
```


## ソート

```javascript
// 文字列でソート
var newArray = _.orderBy(array, String, 'desc');
console.log(newArray);

// 数値でソート
var newArray = _.orderBy(array, Number, 'asc');
console.log(newArray);

// オブジェクトをソート
var newArray = _.orderBy(array, ['name', 'create_at'], ['asc', 'desc']);

// ソート条件を関数で指定
var newArray = _.orderBy(array, (a) => {
    return a.name.length;
}, 'desc');
```


## ランダム

```javascript
// なにこれこんなのなかなかないよね? シャッフル。
var newArray = _.shuffle(array);

// ランダムにいっこ取り出し。
var a = _.sample(array);
```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

```javascript

```

