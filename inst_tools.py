from inst_scrappers import *

# testing
ECO_DELIVERY = 'https://www.instagram.com/eco_delivery_'
KOZAK = 'https://www.instagram.com/tima.kozak'
ARCHAKOV = 'https://www.instagram.com/seva_archakov'
MELANIUK = 'https://www.instagram.com/melaniuk_'
GINGER = 'https://www.instagram.com/ginger_with_tea'
KRYVYI = 'https://www.instagram.com/nikolaykrivoy'


def save_insta_image_to_file(inst):
    """
    Save insta image to file in format:
    profile_image_insta_tag.jpg
    """
    tag = scrap_insta_tag(inst)
    image = scrap_insta_image(inst)

    if not os.path.exists(f'images/{tag}'):
        os.mkdir(f'images/{tag}')

    urllib.request.urlretrieve(image, f"images/{tag}/profile_image_{tag}.jpg")


def save_insta_products_to_file(inst):
    """
    Save insta products to file in format:
    product_insta_tag_???.jpg
    """
    tag = scrap_insta_tag(inst)
    images = scrap_insta_product(inst)[::-1]

    if not os.path.exists(f'images/{tag}'):
        os.mkdir(f'images/{tag}')

    if not os.path.exists(f'images/{tag}/products'):
        os.mkdir(f'images/{tag}/products')

    # for idx in range(len(images)-1, -1, -1):
    for idx, image in enumerate(images):
        if not os.path.exists(f'images/{tag}/products/product_{tag}_{idx}.jpg'):
            urllib.request.urlretrieve(
                image, f"images/{tag}/products/product_{tag}_{idx}.jpg")


if __name__ == "__main__":
    tag = input("@")

    instagram = get_html(f'https://www.instagram.com/{tag}')
    print(instagram)
    save_insta_products_to_file(instagram)
    save_insta_image_to_file(instagram)
