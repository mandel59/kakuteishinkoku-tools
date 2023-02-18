# SPDX-FileCopyrightText: Copyright 2023 Ryusei Yamaguchi
# SPDX-License-Identifier: MIT-0

import csv
import json
import sys


def check_equals(expected, actual):
    if not expected == actual:
        raise ValueError(f'{expected} expected')


def parse_iryohijoho(rowiter):
    """医療費情報CSVファイルをパース"""
    check_equals(['わたしの情報'], next(rowiter))
    check_equals(['医療費通知情報'], next(rowiter))
    check_equals([], next(rowiter))
    check_equals(['項目名', '内容'], next(rowiter))
    data = dict()
    pointer = data
    group_key = None
    first_key_of_group = None
    for row in rowiter:
        k = row[0]
        if len(row) == 1:
            pointer = dict()
            data[k] = [pointer]
            group_key = k
            row = next(rowiter)
            k = row[0]
            v = row[1]
            pointer[k] = v
            first_key_of_group = k
            continue
        if k == first_key_of_group:
            pointer = dict()
            data[group_key].append(pointer)
        v = row[1]
        pointer[k] = v
    return data


def main():
    reader = csv.reader(sys.stdin)
    rowiter = iter(reader)
    iryohijoho = parse_iryohijoho(rowiter)
    json.dump(iryohijoho, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
