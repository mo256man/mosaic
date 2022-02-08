import cv2

filename = "pk2.png"

img = cv2.imread(filename)
img = img[2:, 7:]
ih, iw = img.shape[:2]
print(ih, iw)
ph, pw = 96, 96

for h in range(ih//ph-1):
#    cv2.line(img, (h*ph,0), (h*ph,iw-1), (0,0,255), 1)

    for w in range(iw//pw-1):
        #print(w,h)
        pic = img[h*ph:(h+1)*ph, w*pw:(w+1)*pw]
        cv2.imshow("", pic)
        cv2.imwrite(f"{w:02}_{h:02}.png", pic)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
#        cv2.line(img, (0,w*pw), (ih-1,w*pw), (0,0,255), 1)

cv2.imshow("", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

