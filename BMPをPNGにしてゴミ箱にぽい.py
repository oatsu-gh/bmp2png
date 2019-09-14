#!/usr/bin/python3
"""
.bmp → .png （子フォルダ孫フォルダも）
"""


import os.path
from time import time
from glob import glob
from PIL import Image
from send2trash import send2trash

test = False


def convert_bmp2png(d):
    """
    フォルダ内のbmpをpngに変換する関数
    """
    if test:
        print('  function : convert_bmp2png in', d)

    # BMP画像を収集する
    # pic_list = glob(d + "/*.bmp")
    pic_list = glob('**/*.bmp', recursive=True)
    if test:
        print('  pic_list =', pic_list)


    # 各画像を変換
    for pic in pic_list:
        filename = os.path.splitext(pic)
        # 対象ファイルを明示
        print('    ', pic)
        if test:
            print('    ', type(pic), pic)
            print('    ', type(filename), filename)
        # 画像を読み込んで変換
        with Image.open(pic) as f:
            f.save(filename[0] + '.png', 'PNG')
        # ごみ箱に送る
        send2trash(pic)


'''
def tour_directories():
    """
    子フォルダと孫フォルダをめぐって処理を実行する関数
    """
    if test:
        print('function : tour_directories')

    # 現在位置からディレクトリだけを抽出
    file_list = os.listdir(".", recursive=True)
    dir_list = [f for f in file_list if os.path.isdir(os.path.join(".", f))]

    print('dir_list =', dir_list)

    # 各ディレクトリ中の画像を変換
    for d in dir_list:
        print(d)
        # convert_bmp2png(d)
'''

def main():
    """
    まとめ
    """
    print('convert_bmp2png')
    convert_bmp2png('.')


# 実行（時間計測付き）
if __name__ == '__main__':
    start = time()

    main()

    elapsed_time = time() - start
    print("実行時間：{0:4f}".format(elapsed_time) + "[sec]")

    input('Press Enter to quit.')
