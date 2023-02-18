# 確定申告に使う雑ツール集

動作保証はしません。自己責任でお使いください。

ライセンス: MIT-0

## 医療費情報変形ツール

### iryohijoho-to-json.py

マイナポータルの「わたしの情報」→「医療費通知情報」からダウンロードできるCSVを、JSON形式に変換します。

#### 使い方

標準入力からCSVファイルを入力すると、標準出力にJSONを出力します。

適宜リダイレクトしてファイルに保存してください。

```sh
python iryohijoho-to-json.py < private/iryohijoho/医療費情報_20230218164655617.csv
```

### iryohijoho-json-to-form.py

JSON形式の医療費情報を医療費集計フォーム（iryouhi_form_v3.xlsx）にコピーして入力できる形式に変換します。

出力はTSV形式なので、適宜フォームにダウンロードして使ってください。

#### 使い方

標準入力からJSONファイルを入力すると、標準出力にTSV形式のデータを出力します。

パイプを使って iryohijoho-to-json.py の出力をそのまま入力にできます。

適宜リダイレクトしてファイルに保存してください。

```sh
python iryohijoho-to-json.py < private/iryohijoho/医療費情報_20230218164655617.csv | python iryohijoho-json-to-form.py
```

#### バグ

区分の入力にはちゃんと対応していないので、convert_kubun関数を修正する必要があります。
