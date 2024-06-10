from PIL import Image, ImageDraw, ImageFont

def create_logo(output_path):
    # Define logo dimensions and background color
    width, height = 400, 200
    background_color = (255, 255, 255)  # White

    # Create a new image with a white background
    image = Image.new('RGBA', (width, height), background_color)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the color and thickness of the shapes
    shape_color = (0, 0, 0)  # Black
    shape_thickness = 5

    # Draw a rectangle
    rectangle_coords = [(50, 50), (350, 150)]
    draw.rectangle(rectangle_coords, outline=shape_color, width=shape_thickness)

    # Draw a circle
    circle_coords = [(170, 70), (230, 130)]
    draw.ellipse(circle_coords, outline=shape_color, width=shape_thickness)

    # Add text
    text = "My Logo"
    text_color = (0, 0, 0)  # Black
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = ((width - text_width) / 2, (height - text_height) / 2)
    draw.text(text_position, text, fill=text_color, font=font)

    # Save the image
    image.save(output_path, 'PNG')

# Usage
create_logo('my_logo.png')
