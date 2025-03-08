import cv2
from PIL import Image

image_path = 'wait im serious.jpg'
cat_face_cascade = cv2.CascadeClassifier \
    ('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
    glasses = glasses.resize((w, int(h / 3)))
    cat.paste(glasses, (x + 5, int(y + h / 3)), glasses)
    cat.save("cat_with_glasses.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()
cv2.imshow("Cat", image)
cv2.waitKey()
