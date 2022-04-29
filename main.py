import os
import sys
import PySimpleGUI as sg

header = ('File Path', 'Exists')
path_list = []

# main.pyのあるディレクトリに移動しておく
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# 与えられたファイル一覧に指定ワードが含まれているかチェック
def isExistWord(path_list: list, word: str):
    ans_list = []
    for path in path_list:
        try:
            file_path = path[0]
            with open(file_path, encoding="utf-8", errors='ignore') as f:
                # for line in f.readlines():
                #     if word in line:
                #         ans_list.append([file_path, 'True'])
                #         break
                if word in f.read():
                    ans_list.append([file_path, 'True'])
                else:
                    ans_list.append([file_path, 'False'])
        except FileNotFoundError:
            ans_list.append([file_path, 'File Not Found!!'])
    return ans_list


# 確認対象ファイル一覧を読み込む
with open("target_file.txt") as f:
    target_list = f.readlines()
    for target_path in target_list:
        path_list.append([target_path.strip(), ''])

sg.theme('DarkAmber')

# ウィンドウに配置するコンポーネント
layout = [[sg.Text('Search Word'), sg.InputText(), sg.Button('Search')],
          [sg.Table(path_list, headings=header, auto_size_columns=False, col_widths=[100, 15], justification='left', key='list')]]

# ウィンドウの生成
window = sg.Window('Check Text Exists', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Search':
        #print('あなたが入力した値： ', values[0])
        path_list = isExistWord(path_list, values[0])
        window['list'].update(values=path_list)

window.close()
