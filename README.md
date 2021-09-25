## 1.アプリ概要
東京ディズニーランドのアトラクションごとの隠れミッキーや裏話等共有するCRUDアプリです。
待ち時間で退屈な思いをする人を少しでも減らしたいという思いから開発しました。

主要機能
* エリアやアトラクション毎の記事絞り込み機能
* お気に入り記事、投稿記事の一覧化機能
* キーワード検索

サイトURL（PC、スマホ対応）：https://dss-tdr.com/

ポートフォリオ詳細説明：https://qiita.com/minari766/items/d67e009fe22bed619874

![スクリーンショット 2021-09-11 7.30.31.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/639072/5589137f-1064-d24f-cc0b-e886fc52d01d.png)

## 2.使用技術
* 開発環境
    * Visual Studio Code 1.59
    * mac OS Catalina 10.15.7
    * Adobe XD
    * Github
    
* バックエンド
    * Python 3.8.3
    * Django 2.2.16
    * SQLite 3.28.0 （9月25日時点　MySQL移行中）
学習当初、Webアプリと業務自動化ツールを開発したいと考えており、Pythonはどちらにも優れた言語と認識しておりますため最初の言語に選びました。

* フロントエンド
    * HTML/CSS
    * JavaScript 
    * jQuery 3.5.1
    * Bootstrap 4.5.0
基本的にはCSSでデザインを整えており、細かな部分やレスポンシブ化でBootstrapを使っています。
その他、ページネーションやお気に入りボタンでjQueryを、カテゴリボタンの色反転でJavaScriptを使用しています。

* インフラ
    * Nginx 1.12.2
    * Gunicorn
    * SQLlite　3.28.0 （9月25日時点　MySQL移行中）
    * VPS（Vultr）
    * Docker
    * AWS（学習中）
Djangoに初期導入されているSQLiteを使っていますが、9月25日現在、AWSの導入に伴い、MySQLへの移行中です。
当初実運用も視野に入れ維持費があまりかからないVPSにてデプロイしておりましたが、技術的に興味があったことからAWSへ移行中です。


## 3.開発過程
3-1. リーンキャンバス作成

![DSS_リーンキャンバス.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/639072/38dce75d-08dc-ca98-a376-b146dbae7c12.png)

3-2. ワイヤーフレーム作成

![スクリーンショット 2021-08-22 17.24.29.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/639072/99510ea5-c9d6-3eb9-a33f-047acb1444c4.png)

3-3. DB設計

![スクリーンショット 2021-09-25 18.18.57.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/639072/7b008462-fadd-100c-38e8-b4ae8bd66604.png)


## 4.機能一覧
|  | 　　　　 機能 |
|:-:|:-|
| 1| アカウント登録|
| 2| ログイン|
| 3| ゲストログイン|
| 4| 投稿記事絞り込み|
| 5| キーワード検索|
| 6| タグ検索|
| 7| 記事投稿（CRUD）|
| 8| 投稿記事確認(CRUD)|
| 9| 投稿記事編集（CRUD）|
| 10| 記事削除|
| 11|記事お気に入り（Ajax）|
| 12| ページネーション（Ajax）|
| 13| マイページ|
| 14| My投稿・Myお気に入り|
| 15| 投稿数・お気に入り獲得数表示|
| 16| お問い合わせ|


## 5.開発者
みなり：[Twitter](https://twitter.com/minari766)
