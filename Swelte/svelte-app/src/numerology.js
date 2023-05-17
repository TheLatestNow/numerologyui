function calculatePsychicNumber(day) {
    if ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30].includes(day)) {
      return undefined;
    }
  
    while (day >= 10) {
      day = [...String(day)].reduce((acc, digit) => acc + Number(digit), 0);
    }
    return day;
  }
  
  function calculateDestinyNumber(dateOfBirth) {
    const [day, month, year] = dateOfBirth.split('-').map(Number);
    let destinyNumber = day + month + year;
    while (destinyNumber >= 10) {
      destinyNumber = [...String(destinyNumber)].reduce((acc, digit) => acc + Number(digit), 0);
    }
    return destinyNumber;
  }
  
  function calculateKuaNumber(year, gender) {
    if (gender.toLowerCase() !== 'male' && gender.toLowerCase() !== 'female') {
      throw new Error('Gender must be "male" or "female"');
    }
    while (year >= 10) {
      year = [...String(year)].reduce((acc, digit) => acc + Number(digit), 0);
    }
    let kuaNumber = gender.toLowerCase() === 'male' ? 11 - year : year + 4;
    while (kuaNumber >= 10) {
      kuaNumber = [...String(kuaNumber)].reduce((acc, digit) => acc + Number(digit), 0);
    }
    return kuaNumber;
  }
  
  export { calculatePsychicNumber, calculateDestinyNumber, calculateKuaNumber };  