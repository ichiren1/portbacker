# portbacker

## 必要なもの

### Python
* version 2.7

### mongoDB
* version 2.4.3
* 参照→ http://nigohiroki.hatenablog.com/entry/2013/01/05/234631

### sudo easy_install pymongo
* version 2.5.2

## portfolioシステムの起動の仕方
* portbackerのディレクトリに移動
* python portfolio.py
  * もし起動しない場合は上記のインストールに不備がある
* ブラウザでlocalhost:5000に接続

## データ構造
* とりあえず去年のものを参照だが一応

### ポートフォリオ 

collection名 portfolios

```javascript
{"public":boolean,"owner"="string","text"="string"}
```

### ゴール
collection名 goals

```javascript
{"owner"="string","goal"="string"}
```


