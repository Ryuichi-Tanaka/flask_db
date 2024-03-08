# Name
flask_db

https://github.com/Ryuichi-Tanaka/flask_db/assets/87804267/f6876c18-496f-43ba-b5ba-a548f6219518

## Overview
赤ちゃん育児記録簿
## Requirement
Flask 3.0.2

sqlite3

## Usage
「きろくをする」ボタンを押下後、人物やミルクの量などを設定し記録簿へ書込みを行う

「きろくを表示」ボタンを押下後、データベースに保存しているデータを表示

## Description

「きろくをする」ボタン押下後、人物やミルク、便の色、備考等を記載、「さくせい」ボタンを押下するとデータベースへ反映

「きろくを表示」ボタン押下後、全てのデータ一覧が表示されるが検索フォームを作成しているため、特定文言での検索も可能

データ一覧の右端にはCSVファイルへの書込みもできるよう機能を作成

## Obsessed Points

UXにこだわりを持ち、入力工程が少なくなるようできるだけワンタップで処理ができるようにしました。

## Test Case

1. きろく画面でのアイコンのデザイン崩れ等が発生していないか

2. ラジオボタンやチェックボックス、備考等が正しくデータに反映されているか

3. 検索フォームから検索を行った際、正しく文字列のフィルターがかかっているか

4. csvをダウンロードした際、出力されたデータが正しく表示されているか

## Future Issues

・Login、Logoutの実装（セキュリティの観点からGoogle、LINEでの実装を検討しています）

・画面のレスポンシブ対応

・デザイン性の質の向上（ターゲット層を考え、現在はパステルカラーでのデザインで統一しています）

・共有機能（LINE等にデータを送信できるように考えています）

・検索フォームの刷新（文字を打ち込んで検索をかけるのではなく、検索対象をボタンワンタップでサーチできるよう考えています）

・ファイルダウンロード時、ExcelやPDFへもダウンロードを可能にする

・データベースの変更（現在はsqlite3を使って実装していますが、今後は学習も兼ねてFireBaseなどのクラウドサービスを使っての運用も考えています）

・Pythonanywereでのエラー対応（Pythonanywereを使用してWeb公開を行っていますが、データベースとの接続部分でエラーがでており、現在調査と検証を行っています）
公開URL⇒https://ryu.pythonanywhere.com/
