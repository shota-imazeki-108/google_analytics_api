# APIで取得してきたGoogle AnalyticsやSearch Consoleから取得してきた辞書型データを整形して、DataFrameにする。
## これは何か
APIから取得してくるデータは辞書型でネストされているため扱いづらい。こちらのコードは、このネストされた辞書型データをDataFrameに整形するコードである。
なお、Search Consoleは作成途中である。

## 使用方法
具体的な使用方法は `tutorial_*.ipynb` を確認してください。
`tutorial_*.ipynb` を使用する際に、書き換える必要のあるファイルについて。
- src/config/config.pyファイル
    - key_file_location: Googleサービスアカウントの秘密鍵のパス
        - 秘密鍵は[こちら](https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py)の `1. API を有効にする`を参考に。
    - view_id: GAの管理画面から、ビュー→ビューの設定→ビューIDの値