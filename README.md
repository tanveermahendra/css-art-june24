_This is a submission for [Frontend Challenge v24.04.17](https://dev.to/challenges/frontend-2024-05-29), CSS Art: June._

## Inspiration
The idea for this project blossomed from a casual conversation with my friend [Ritul Choudhary](https://www.instagram.com/ritulchoudhary) over Discord. In search of inspiration, Ritul found several poems about June, and [this one by Annette Wynne](https://thedailygardener.org/june-was-made-for-happiness/) resonated deeply with him. Captivated by the poem's imagery, we decided to transform its essence into a visual representation.

To bring our vision to life, we enlisted the help of our talented artist friend [Niranjan Bharati](https://www.instagram.com/puntorturedartist/). He skillfully translated the poem's elements onto a 100px x 200px canvas, creating a beautiful piece of pixel art that encapsulates the poem's serene and joyful spirit.

The artwork depicts a tender moment between a mother and her daughter on a summer afternoon. They are seated in a lush grassland, surrounded by pink tulips and fluttering butterflies, while the mother reads a book to her daughter. The scene is set against a backdrop of majestic mountains and a sky dominated by a large, fluffy cloud, partially veiling the sun. This imagery perfectly captures the poem's celebration of June's simple pleasures and the happiness found in nature.

![Mother](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/bud1fialqrpdua7mrbiz.png)

## Demo 
https://codepen.io/tanveermahendra/pen/YzbQQwj

## The Art Process
Our journey began with a simple idea and evolved into a beautiful piece of digital art. Here are the steps we took to create our pixel art masterpiece:

1. **Initial Sketch:**
   
 ![Stage 1](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/trxx9gciiebnx3yj5c6t.png)

   We started with a basic sketch to outline the elements we wanted to include. This initial sketch helped us visualize the overall composition and placement of key elements like the mother, daughter, butterflies, and the surrounding nature.

2. **Defining Shapes and Colors:**
   
![Stage 2](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5vogpweimowc97tpnema.png)

   Next, we began defining the shapes and adding basic colors. This stage was crucial in establishing the structure and color palette of the artwork. We focused on ensuring the characters and elements were easily recognizable and aligned with the mood of the poem.

3. **Adding Details:**

![Stage 3](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/oiauiz59vgh1xgqon7gj.png)

   With the basic shapes and colors in place, we moved on to adding details. This included refining the characters, enhancing the background elements, and adding textures to make the scene more vibrant and lively.

4. **Final Touches:**
5. 
![Stage 4](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xeof8jpzu3u7azou3ojb.png)

   In the final stage, we added the finishing touches to the artwork. This involved adjusting colors, smoothing out lines, and ensuring all elements were cohesive. The result was a beautiful pixel art piece that captured the essence of Annette Wynne's poem.

## Journey and What I Learned

Why 100px x 200px, you might ask? Well, as this was my first CSS art project, I wanted to keep it simple and draw it in pixel-art form. I followed this [useful tutorial](https://www.youtube.com/watch?v=LjlHcmEclFE) to get started. Soon, I realized that creating a 100px by 200px image would require me to write 20,000 individual values to generate the art. The art size restriction we had set earlier wasn't small enough. But here we were, so I decided to automate the CSS pixel values generation.

```
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
    image_path = 'final-art.png'
    width_em = 100  # The width of the image in em units
    height_em = 200  # The height of the image in em units
    css_box_shadow = image_to_css_box_shadow(image_path, width_em, height_em)
    print(f'box-shadow: {css_box_shadow};')

```
The code above takes the constraint of 1em as a base unit in CSS and translates the pixel values into em counterparts. The logic is to iterate over the image, pick individual pixel values, and convert them into a CSS `box-shadow` property in the format: `'x'em 'y'em #xxxxxx`. Then, the script joins them with a comma separator. I ran the Python script and saved the output in a text file to later copy-paste into the `style.css` file.

This worked perfectly, and we were able to see the CSS code come to life! While discussing the results, we felt that the dimensions resembled a bookmark. Why not transform this into a digital bookmark? So, that's what we started looking into. I found this [amazing tutorial by w3schools](https://www.w3schools.com/howto/howto_css_flip_card.asp) and applied the learnings to our project.

The poem was the perfect candidate for the back side of the digital bookmark. I added a hover interaction on the parent `<div>` of the flip card to allow everyone to appreciate the inspiration behind the artwork. As a final touch, applied the [Noto Sans font by Google](https://fonts.google.com/noto/specimen/Noto+Sans) to the back side of the bookmark.
