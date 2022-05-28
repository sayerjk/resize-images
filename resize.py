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



#  ============================================================

# # for local upload
# # gather image characteristics into image objects
# # testing here with single image
# img_path = r"images\39530001.JPG"
# im = Image.open(img_path)

# print(f'{im.format = }')
# print(f'{im.size = }')
# print(f'{im.mode = }')
# im.show()

# Make function to get pixel dimensions halved from im.size tuple

# half_size = [int(j * .33) for i,j in enumerate(web_image_01.size)]
# half_size = tuple(half_size)
# half_size

# image_list = []
# resized_image = []

# for filename in glob.glob('images/*.JPG'):
#     print(f'Current {filename = }')
#     img = Image.open(filename)
#     image_list.append(img)

# for image in image_list:
#     image = image.resize(half_size)
#     resized_image.append(image)

# for i,new in enumerate(resized_image):
#     new.save(f'images/rescaled_images/rs_{i+1}.JPG')