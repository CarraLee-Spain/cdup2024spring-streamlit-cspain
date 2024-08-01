import streamlit as st

# This section draws a monogram circle

import hashlib
from PIL import Image, ImageDraw, ImageFont
import io

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

# This is my Citizen Development UpSkilling Spring 2024 Coding Challenge Page
# This is my sample Streamlit page

st.title('UpSkilling Spring 2024!')
st.subheader('This is my Coding Challenge Page')
st.write('')
st.write('')

# Here is a little bit about me and how to find me at Arcadis
st.write('I am Carra Lee Spain, from Arcadis US, and I am very excited about all I am learning!')
st.html('<sup> You can find me on our Collaboration hub at <a href="https://collaborationhub.arcadis.com/profile/b951f9f2-ccbc-4fe5-836c-162e84d7e583/contactdetails" target="_blank"></a></sup>')
st.write('')
st.write('')

# Here is a bit about my start at Arcadis
st.write('I have been with Arcadis since July 2015, and I have worked on some very interesting projects.')
st.write('My first project at Arcadis was a renovation and expansion of a waste to energy facility in York, Pennsylvania')
st.write('There were many great things about this project, but the best was the results.  After all was done,)
st.write('the facility was able to process 200 garbage trucks worth of waste and end up with only 2 trucks worth')
st.write('of material that was not converted to energy or recycled in some way.')
st.write('One of the exciting events was the excavation of the new Tipping Hall pit, which the general contractor')
st.write('"("' 'not Arcadis' '")"' 'ended up electing to use blasting for because of the density of rock.')
st.html('<sup> If you are interested, you can see a video a couple of seconds long at <a href="https://arcadiso365.sharepoint.com/:v:/r/teams/project-30001651/mediagallery/Blast%203-6-17%204PM.mp4?csf=1&web=1&e=jlSo40&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" target="_blank"></a></sup>')
st.write('After excavating this massive pit, the general contractor poured a concrete slab roughly equivalent to a')
st.write('football field in one pour, which required some unusal techniques.')
st.html('<sup> More photos can be seen here <a href="https://arcadiso365.sharepoint.com/teams/project-30001651/mediagallery/Forms/Thumbnails.aspx" target="_blank"></a></sup>')
st.write('The other exciting project I am proud to have been a part of on this site began in concurrence with this one,')
st.write('and was the first Ash Recycling Facility of its kind in the United States.  It takes ash from the waste to energy')
st.write('plant incinerator and harvests all the viable aggregates, metals, and sand, reducing the ash that must be managed at a landfill.')
st.write('')
st.write('')

*Here is a bit about my coding journey
st.write('Now for a bit about my coding journey!')
st.write('I began  when my older brother gave me a Commodore 64 when I was in elementary school.')
st.write('Everything I learned was trial and error and from the little booklet that came in the box.')
st.write('I progressed to BASIC and DOS, then Pascal and a jump to Unix.  I moved away from coding after')
st.write('that and only used what I needed in my other work, such as writing Excel macros and incidental')
st.write('code here and there in a command window.  When our Arcadis Skills Powered Organization program')
st.write('launched, I was part of the pilot program and decided I needed to be intentional about bringing')
st.write('my skills up to date.  I searched for an online, FREE, coding course and stumbled on a Stanford')
st.write('University course "Code in Place", which is equivalent to the first half of their freshman level')
st.write('Introduction to Coding course.  I took that early this spring, and finished it at the end of May,')
st.write('as we were starting this UpSkilling program.  I was really excited when I learned about this')
st.write('Citizen Development program, because it is perfect for my personal goals this year of updating my')
st.write('skills! Unfortunately, our SPO program has not been trained enough yet for it to be great at')
st.write('identifying and recommending courses to take, but I'm sure it will get better as we keep using it.')
st.write('Here is a link to a very basic Python program that I did as an early project in my "Code in Place"')
st.write('course through Stanford <a href="https://codeinplace.stanford.edu/cip4/share/h25pEezoWb0YAm7svm7y" target="_blank"></a></sup>')
st.write('It is a little arithmetic practice tool.')
st.write('')
st.write('')

#Ending of my little page
st.write('Thankts for visiting my page!!')
