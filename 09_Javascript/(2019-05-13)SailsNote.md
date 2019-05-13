SailsNote
===



## Problems


#### layout.ejs 問題

- ページごとに違う layout を使いたい。
- ページごとに違う css を使いたい。

```javascript
// routes.js
'GET /login' :  { action: 'view-login',
                  locals: {
                    layout: 'layouts/layout-login',
                  },
                },
```

```html
// layout-login.ejs

↓ これは消す。勝手に assets の中のファイルが記述されちゃうから。
<!--STYLES-->
<!--STYLES END-->

↓ こうして別途書く。
<link rel="stylesheet" href="/styles/pages/login.css">
```
