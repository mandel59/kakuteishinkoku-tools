# SPDX-FileCopyrightText: Copyright 2023 Ryusei Yamaguchi
# SPDX-License-Identifier: MIT-0

"""
医療費情報のJSONを、医療費


https://www.nta.go.jp/taxes/shiraberu/shinkoku/tokushu/iryouhi-download.htm
"""

import csv
import json
import sys


def gaito_suru(b: bool):
    return '該当する' if b else ''

def convert_kubun(kubun: str):
    sinryo_chiryo = kubun.endswith('外来')
    iyakuhin_konyu = kubun == '調剤'
    kaigo = False
    sonota = False
    return list(map(gaito_suru, [sinryo_chiryo, iyakuhin_konyu, kaigo, sonota]))

def iryohijoho_details(data):
    name = data['資格情報'][0]['氏名']
    details = data['医療費情報明細']
    for record in details:
        yield [
            name,
            record['医療機関等名称'],
            *convert_kubun(record['診療区分']),
            record['窓口相当負担額（円）'],
            '',
            record['診療年月'],
        ]


def main():
    data = json.load(sys.stdin)
    writer = csv.writer(sys.stdout, delimiter='\t')
    writer.writerows(iryohijoho_details(data))


if __name__ == '__main__':
    main()
