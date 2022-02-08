import cv2

filename = "pk2.png"

img = cv2.imread(filename)
img = img[8:-8, 4:-8]
ih, iw = img.shape[:2]
print(ih, iw)
ph, pw = 96, 96

for h in range(iw//pw-1):
    for w in range(ih//ph-1):
        #print(w,h)
        pic = img[h*ph:(h+1)*ph, w*pw:(w+1)*pw]
        cv2.imshow("", pic)
        cv2.imwrite(f"{w}_{h}.png", pic)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break

cv2.destroyAllWindows()

