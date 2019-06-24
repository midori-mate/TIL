UserAgentNote
===

## クライアント側で

```javascript
isSupportedBrowser: function () {
  const ua = window.navigator.userAgent.toLowerCase();
  if (ua.indexOf('msie') >= 0 || ua.indexOf('trident') >= 0) {
    return false;
  }
  if (   ua.indexOf('edge')    >= 0
      || ua.indexOf('chrome')  >= 0
      || ua.indexOf('safari')  >= 0
      || ua.indexOf('firefox') >= 0)
  {
    return true;
  }
  return false;
}
```


## Node で

```bash
$ npm install ua-parser-js --save-dev
```

```javascript
const parser = require('ua-parser-js');
const agent = parser(this.req.headers['user-agent']);
console.log(agent);
```

### Chrome でアクセスしてみた

```javascript
{ ua: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
  browser: { name: 'Chrome', version: '75.0.3770.100', major: '75' },
  engine: { name: 'Blink', version: undefined },
  os: { name: 'Mac OS', version: '10.14.5' },
  device: { vendor: undefined, model: undefined, type: undefined },
  cpu: { architecture: undefined } }
```

### Firefox でアクセスしてみた

```javascript
{ ua: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0',
  browser: { name: 'Firefox', version: '67.0', major: '67' },
  engine: { name: 'Gecko', version: '67.0' },
  os: { name: 'Mac OS', version: '10.14' },
  device: { vendor: undefined, model: undefined, type: undefined },
  cpu: { architecture: undefined } }
```

### Safari でアクセスしてみた

```javascript
{ ua: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
  browser: { name: 'Safari', version: '12.1.1', major: '12' },
  engine: { name: 'WebKit', version: '605.1.15' },
  os: { name: 'Mac OS', version: '10.14.5' },
  device: { vendor: undefined, model: undefined, type: undefined },
  cpu: { architecture: undefined } }
```

### Edge でアクセスしてみた

```javascript
{ ua: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
  browser: { name: 'Edge', version: '17.17134', major: '17' },
  engine: { name: 'EdgeHTML', version: '17.17134' },
  os: { name: 'Windows', version: '10' },
  device: { vendor: undefined, model: undefined, type: undefined },
  cpu: { architecture: 'amd64' } }
```

### IE11 でアクセスしてみた

```javascript
{ ua: 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
  browser: { name: 'IE', version: '11.0', major: '11' },
  engine: { name: 'Trident', version: '7.0' },
  os: { name: 'Windows', version: '10' },
  device: { vendor: undefined, model: undefined, type: undefined },
  cpu: { architecture: 'amd64' } }
```
