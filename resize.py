# for local uplaods
from PIL import Image
import glob

# for url uploads
import requests
from io import BytesIO

# taking user input here
url = input('\nEnter image url (ends in .jpg, .png, etc): ')
print(f'{"--" * 10}')

# gets content from url, and creates Image object from content
response = requests.get(url)
web_image_01 = Image.open(BytesIO(response.content))
print(f'{web_image_01.format = }')
print(f'{web_image_01.size = }')
print(f'{web_image_01.mode = }')
print(f'{"--" * 10}')

# set scale for new image here, and calculate new pixel dimensions
scale = input("Choose scale to reduce by (0.0 - 1.0): ")
scale = float(scale)

# TODO - while loop for input validation
assert isinstance(scale, float), input("Choose scale to reduce by (0.0 - 1.0): ")
assert 0 < scale < 1, input("Choose scale to reduce by (0.0 - 1.0): ")

new_size = (int(web_image_01.size[0] * scale), int(web_image_01.size[1] * scale))

print(f'{"--" * 10}')
print(f'{new_size = }')
print(f'{"--" * 10}')
print('Save photo before closing otherwise it will be lost.')

web_image_01 = web_image_01.resize(new_size)
web_image_01.show()
