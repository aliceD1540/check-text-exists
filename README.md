# 概要

「特定ファイルのみを対象としてキーワードの存在を確認」する。
（Grepするには面倒くさいので・・・）

# 使用方法

1. target_file.txt にファイル一覧を記載
2. 起動
3. キーワードを入れて「Search」

# 必要なライブラリ

- PySimpleGUI

# ビルド

何かの都合で実行ファイルとして欲しいとき

> pyinstaller.exe .\main.py --hidden-import "PySimpleGUI.PySimpleGUI" --onefile --noconsole
