import requests as rq
from matplotlib import pyplot as plt
from PIL import Image
r1 = rq.get('https://www.yaklass.ru/testwork?from=menu')
print(r1.text)
payload = {'key1': 'value1', 'key2': 'value2'}
r = rq.get('https://httpbin.org/get', params=payload)
print(r.url)



"""fig, ax = plt.subplots()
ax.plot([5, 0, 0, 5, 10, 15, 15, 10, 5, 5, 10, 5, 10, 10], [5, 10, 15, 20, 20, 15, 10, 5, 5, 20, 5, 5, 20, 5])
plt.show()"""



"""image = Image.open('tower.jpg')
image.show()
cropped = image.crop((50, 50, 200, 400))
cropped.show()
rotated_tower = image.rotate(180)
rotated_tower.show()
black_white = image.convert("L")
black_white.show()"""


