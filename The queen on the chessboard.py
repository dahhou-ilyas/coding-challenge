def availableMoves(position):
    # Convert the position to uppercase string if it's not already
    if not isinstance(position, str):
        return []
    
    position = position.upper()
    
    # Check if the position is valid
    if len(position) != 2 or position[0] not in 'ABCDEFGH' or position[1] not in '12345678':
        return []
    
    col, row = ord(position[0]) - ord('A'), int(position[1]) - 1
    
    # generer les mouvement possible
    moves = []
    
    # Vertical et horizontal mouvenment
    for i in range(8):
        if i != row:
            moves.append(position[0] + str(i + 1))
        if i != col:
            moves.append(chr(i + ord('A')) + position[1])
    
    # Diagonal moves
    for i in range(1, 8):
        if 0 <= col + i < 8 and 0 <= row + i < 8:
            moves.append(chr(col + i + ord('A')) + str(row + i + 1))
        if 0 <= col - i < 8 and 0 <= row + i < 8:
            moves.append(chr(col - i + ord('A')) + str(row + i + 1))
        if 0 <= col + i < 8 and 0 <= row - i < 8:
            moves.append(chr(col + i + ord('A')) + str(row - i + 1))
        if 0 <= col - i < 8 and 0 <= row - i < 8:
            moves.append(chr(col - i + ord('A')) + str(row - i + 1))
    
    return sorted(moves)

# Test cases
print(availableMoves("A1"))
