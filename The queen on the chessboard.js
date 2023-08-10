function availableMoves(position) {
    // Check if the input is a string
    if (typeof position !== 'string') {
        return [];
    }
    
    position = position.toUpperCase();
    
    // Check if the position is valid
    if (!/^[A-H][1-8]$/.test(position)) {
        return [];
    }
    
    const col = position.charCodeAt(0) - 'A'.charCodeAt(0);
    const row = parseInt(position[1]) - 1;
    
    const moves = [];
    
    // Vertical and horizontal moves
    for (let i = 0; i < 8; i++) {
        if (i !== row) {
            moves.push(position[0] + (i + 1));
        }
        if (i !== col) {
            moves.push(String.fromCharCode('A'.charCodeAt(0) + i) + position[1]);
        }
    }
    
    // Diagonal moves
    for (let i = 1; i < 8; i++) {
        if (col + i < 8 && row + i < 8) {
            moves.push(String.fromCharCode('A'.charCodeAt(0) + col + i) + (row + i + 1));
        }
        if (col - i >= 0 && row + i < 8) {
            moves.push(String.fromCharCode('A'.charCodeAt(0) + col - i) + (row + i + 1));
        }
        if (col + i < 8 && row - i >= 0) {
            moves.push(String.fromCharCode('A'.charCodeAt(0) + col + i) + (row - i + 1));
        }
        if (col - i >= 0 && row - i >= 0) {
            moves.push(String.fromCharCode('A'.charCodeAt(0) + col - i) + (row - i + 1));
        }
    }
    
    return moves.sort();
}

// Test cases
console.log(availableMoves("A1"));
