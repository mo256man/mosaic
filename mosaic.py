import os
import glob
import cv2
from PIL import Image
import numpy as np
import random

def gray2color(img, color1, color2):
    """
    輝度0～255をcolor1～color2間に凝縮？する
    """
    b1, g1, r1 = color1                         # 色要素
    b2, g2, r2 = color2                         # 色要素
    b = np.array(img[:, :, 0], np.float)        # B要素のグレースケール画像 をuint8→floatにしたもの
    g = np.array(img[:, :, 1], np.float)        # G要素のグレースケール画像 をuint8→floatにしたもの
    r = np.array(img[:, :, 2], np.float)        # R要素のグレースケール画像 をuint8→floatにしたもの
    b3 = np.array((b2-b1)*b/255+b1, np.uint8)   # B要素の輝度を凝縮したグレースケール画像
    g3 = np.array((g2-g1)*g/255+g1, np.uint8)   # G要素の輝度を凝縮したグレースケール画像
    r3 = np.array((r2-r1)*r/255+r1, np.uint8)   # R要素の輝度を凝縮したグレースケール画像
    img = cv2.merge((b3, g3, r3))               # 色要素を凝縮したBGR画像
    return img


def calc_color(c):
    """
    明るい部分を暗くする、暗い部分を明るくする
    """
    sign = 1 if c<128 else -1
    r = random.randint(15, 40)
    return c + sign * r


def main(filename):
    base = cv2.imread(filename, 1)
    big = base.copy()
    bH, bW = base.shape[:2]                     # ベース画像のサイズ

    mH, mW = 96, 96                             # モザイクのサイズ　前提として全画像共通なので
    #os.chdir("./imgs/")
    file_list = glob.glob("./imgs/*")

    imgH, imgW = bH*mH, bW*mW
    canvas = np.full((imgH, imgW, 3), (255,255,255), np.uint8)
    big = cv2.resize(big, (bW*mW, bH*mH), interpolation=cv2.INTER_NEAREST)
    #cv2.imwrite("big_"+filename, big)
    cnt = 1
    for w in range(bW):
        for h in range(bH):
            color1 = base[h, w]                 # ドットの色
            b1, g1, r1  = color1

            if b1>240 and g1>240 and r1>240:
                b1 -= random.randint(0,30)
                g1 -= random.randint(0,30)
                r1 -= random.randint(0,30)
                color1 = (b1, g1, r1)

            color2 = (calc_color(b1), calc_color(g1), calc_color(r1))

            file = random.choice(file_list)
            img = cv2.imread(file, 1)
            img = gray2color(img, color1, color2)
            canvas[mH*h:mH*(h+1), mW*w:mW*(w+1)] = img
            cnt += 1

    cv2.imshow("", canvas)
    cv2.waitKey(0)
    cv2.imwrite("misaic_" + filename, canvas)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    filename = "origin.png"
    main(filename)