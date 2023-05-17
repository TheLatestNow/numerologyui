const EMPTY_GRID = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
  ];
  
  const POSITIONS = [
    [1, 0], [0, 1], [1, 2],
    [0, 0], [1, 1], [2, 1],
    [2, 0], [1, 2], [2, 2],
  ];
  
  export function generateLoshuGrid(day, month, year, psychicNumber, destinyNumber, kuaNumber) {
    const grid = JSON.parse(JSON.stringify(EMPTY_GRID));
  
    const numbers = [day, month, year, psychicNumber, destinyNumber, kuaNumber].filter(Boolean);
    for (let number of numbers) {
      const digits = String(number).split('');
      for (let digit of digits) {
        if (digit !== '0') { // Add this line
          const [i, j] = POSITIONS[digit - 1];
          grid[i][j] += digit;
        }
      }
    }
  
    return grid;
  }  