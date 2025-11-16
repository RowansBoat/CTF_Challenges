import hashlib

def create_gesture_key(pattern, filename='gesture.key'):
    """
    Create an Android gesture.key file from a pattern sequence.
    
    Pattern grid:
    +---+---+---+
    | 0 | 1 | 2 |
    +---+---+---+
    | 3 | 4 | 5 |
    +---+---+---+
    | 6 | 7 | 8 |
    +---+---+---+
    
    Args:
        pattern: list of integers [0-8] representing the unlock pattern
        filename: output filename for the gesture.key file
    """
    # Convert pattern to bytes
    pattern_bytes = bytes(pattern)
    
    # Android uses SHA-1 hash of the pattern
    sha1_hash = hashlib.sha1(pattern_bytes).digest()
    
    # Write to file
    with open(filename, 'wb') as f:
        f.write(sha1_hash)
    
    print(f"✓ Created {filename}")
    print(f"  Pattern: {' → '.join(map(str, pattern))}")
    print(f"  SHA-1 hash: {sha1_hash.hex()}")
    
    # Visualize the pattern on the grid
    print("\n  Visual representation:")
    print("  +---+---+---+")
    for row in range(3):
        line = "  |"
        for col in range(3):
            pos = row * 3 + col
            if pos in pattern:
                idx = pattern.index(pos)
                line += f" {idx} |"
            else:
                line += "   |"
        print(line)
        print("  +---+---+---+")

# Create gesture file with custom pattern
# Pattern: 6 → 3 → 0 → 4 → 2 → 5 → 8
custom_pattern = [6, 3, 0, 4, 2, 5, 8]

create_gesture_key(custom_pattern, 'gesture.key')

print("\n" + "="*50)
print("To decode this file, use:")
print("java -jar DecodeAndroidGesture.jar gesture.key")
print("="*50)