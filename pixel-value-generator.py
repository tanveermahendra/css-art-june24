from PIL import Image

def pixel_to_em(pixel, em_scale):
    return pixel * em_scale

def image_to_css_box_shadow(image_path, width_em, height_em):
    img = Image.open(image_path)
    img = img.convert('RGBA')
    width_px, height_px = img.size

    # Calculate em scaling factors based on provided width and height
    em_scale_x = width_em / width_px
    em_scale_y = height_em / height_px

    box_shadows = []

    for y in range(height_px):
        for x in range(width_px):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:  # If pixel is not transparent
                x_em = pixel_to_em(x, em_scale_x)
                y_em = pixel_to_em(y, em_scale_y)
                hex_color = f'#{r:02x}{g:02x}{b:02x}'
                box_shadows.append(f'{x_em}em {y_em}em {hex_color}')

    return ', '.join(box_shadows)

if __name__ == "__main__":
    image_path = 'trial-1.png'
    width_em = 100  # The width of the image in em units
    height_em = 200  # The height of the image in em units
    css_box_shadow = image_to_css_box_shadow(image_path, width_em, height_em)
    print(f'box-shadow: {css_box_shadow};')
