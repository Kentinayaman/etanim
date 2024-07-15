from PIL import Image

def check_alpha(image):
    if image.mode in ('RGBA', 'LA'):
        return image.mode, image.info.get('transparency', None)
    elif image.mode == 'P' and 'transparency' in image.info:
        return image.mode, image.info['transparency']
    else:
        return None, None

# Example usage:
img1 = Image.open('example1.png')
mode1, transparency1 = check_alpha(img1)
if mode1:
    print(f"Image 1 has alpha channel with mode {mode1} and transparency {transparency1}")
else:
    print("Image 1 does not have an alpha channel")

img2 = Image.open('example2.jpg')
mode2, transparency2 = check_alpha(img2)
if mode2:
    print(f"Image 2 has alpha channel with mode {mode2} and transparency {transparency2}")
else:
    print("Image 2 does not have an alpha channel")
