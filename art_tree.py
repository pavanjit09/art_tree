def draw_tree(height, width):
    if height == 0:
        return
    
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    
    # Draw the trunk
    trunk_width = 3
    trunk_height = 2
    trunk_spaces = ' ' * (height - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + '*' * trunk_width)

# Draw a tree of height 5
draw_tree(5, 5)
