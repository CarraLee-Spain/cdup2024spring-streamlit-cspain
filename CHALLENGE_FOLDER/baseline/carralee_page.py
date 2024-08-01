import streamlit as st
import hashlib
from PIL import Image, ImageDraw, ImageFont
import io

# This page draws my monogram circle

name_var = "CarraLee"

def string_to_color_code(input_string:str):
    # Use hashlib to generate a hash of the input string
    hash_obj = hashlib.sha256(input_string.encode())
    # Convert the hash to a hexadecimal string
    hex_hash = hash_obj.hexdigest()
    # Take the first 6 characters to use as a color code
    color_code = '#' + hex_hash[:6]
    return color_code

def create_image(text_input:str, color_code:str):
    words = text_input.split()
    first_letters = ''.join(word[0].upper() for word in words if word)[:4]
    
    # Create an image with a solid background color
    img_size = (1000, 1000)
    background_color = (0, 0, 0, 0)     
    image = Image.new('RGBA', img_size, color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Draw a circle in the middle of the image
    circle_radius = 400  
    left_up_point = (img_size[0] / 2 - circle_radius, img_size[1] / 2 - circle_radius)
    right_down_point = (img_size[0] / 2 + circle_radius, img_size[1] / 2 + circle_radius)
    draw.ellipse([left_up_point, right_down_point], fill=color_code)
    
    # Use ImageFont.truetype to specify the font and size
    font_path = "baseline/arial.ttf"  
    font_size = 240  
    font = ImageFont.truetype(font_path, font_size)
    
    text_size = draw.textlength(first_letters, font=font)
    # Draw text in the middle of the circle
    text_x = (img_size[0] - text_size) / 2
    text_y = (img_size[1] - font_size) / 2  
    draw.text((text_x, text_y), text=first_letters, fill="white", font=font)

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    image = Image.open(buffer)
    image_resized = image.resize((150, 150))  
    buffer_resized = io.BytesIO()
    image_resized.save(buffer_resized, format='PNG') 
    buffer_resized.seek(0)
    return buffer_resized
    
if name_var:
    # Generate a color code from the name
    color_code = string_to_color_code(name_var)
    # Display the color code
    st.write(f"Your color code is: {color_code}")
    # Assuming name_var and color_code are defined
    buffer_resized = create_image(name_var, color_code)
    # Display the resized image
    st.image(buffer_resized)
    img_bytes = buffer_resized.getvalue()
