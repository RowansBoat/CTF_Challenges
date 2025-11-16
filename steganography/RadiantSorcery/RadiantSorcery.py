import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_depth_map(text, size=(800, 400)):
    img = Image.new('L', size, 0)  # Black background
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    draw.text(position, text, fill=255, font=font)
    return img

def create_stereogram(depth_map, separation=100, depth_scale=0.3):
    """
    Create a proper autostereogram using the classic SIRDS algorithm
    """
    width, height = depth_map.size
    depth_array = np.array(depth_map, dtype=float) / 255.0
    
    # Create output image with random pattern
    output = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Generate stereogram using proper algorithm
    for y in range(height):
        # Start with random pattern for leftmost strip
        same = np.arange(width)
        
        for x in range(separation, width):
            # Calculate the shift based on depth
            depth = depth_array[y, x]
            shift = int(separation - depth * depth_scale * separation)
            shift = max(separation // 2, min(shift, separation))
            
            # Link this pixel to the appropriate previous pixel
            left = x - shift
            if left >= 0:
                # Find the constraint
                while same[left] != left and same[left] < x:
                    left = same[left]
                    
                if same[left] == left:
                    same[x] = left
                else:
                    same[x] = same[left]
        
        # Second pass: assign colors based on constraints
        for x in range(width - 1, -1, -1):
            if same[x] != x and same[x] < x:
                output[y, x] = output[y, same[x]]
    
    return Image.fromarray(output)

# Alternative: Use a tiled pattern instead of pure random
def create_stereogram_with_pattern(depth_map, separation=100, depth_scale=0.3):
    """
    Creates a stereogram with a repeating pattern (easier to view)
    """
    width, height = depth_map.size
    depth_array = np.array(depth_map, dtype=float) / 255.0
    
    # Create a small repeating pattern
    pattern_size = 2
    pattern = np.random.randint(0, 256, (pattern_size, pattern_size, 3), dtype=np.uint8)
    
    # Tile the pattern across the image
    output = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            output[y, x] = pattern[y % pattern_size, x % pattern_size]
    
    # Apply depth mapping
    result = output.copy()
    for y in range(height):
        for x in range(separation, width):
            depth = depth_array[y, x]
            shift = int(depth * depth_scale * separation)
            source_x = x - separation + shift
            
            if 0 <= source_x < width:
                result[y, x] = result[y, source_x]
    
    return Image.fromarray(result)

# Generate challenge
print("Generating depth map...")
flag_text = "CTF{M4G1C_3Y3S}"
depth_map = create_depth_map(flag_text, size=(1000, 400))
depth_map.save("depth_map.png")

print("Generating stereogram (method 1 - SIRDS)...")
stereogram1 = create_stereogram(depth_map, separation=120, depth_scale=0.4)
stereogram1.save("challenge_sirds.png")