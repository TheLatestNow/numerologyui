export const NumerologyCalculator = {

    calculatePsychicNumber(day) {
        while (day >= 10) {
            day = Array.from(String(day), Number).reduce((a, b) => a + b);
        }
        return day;
    },

    calculateDestinyNumber(dateOfBirth) {
        const [day, month, year] = dateOfBirth.split('-').map(Number);
        let destinyNumber = day + month + year;
        while (destinyNumber >= 10) {
            destinyNumber = Array.from(String(destinyNumber), Number).reduce((a, b) => a + b);
        }
        return destinyNumber;
    },

    calculateKuaNumber(year, gender) {
        if (gender.toLowerCase() !== "male" && gender.toLowerCase() !== "female") {
            throw new Error("Gender must be 'male' or 'female'");
        }
        while (year >= 10) {
            year = Array.from(String(year), Number).reduce((a, b) => a + b);
        }
        let kuaNumber = (gender.toLowerCase() === "male") ? 11 - year : year + 4;
        while (kuaNumber >= 10) {
            kuaNumber = Array.from(String(kuaNumber), Number).reduce((a, b) => a + b);
        }
        return kuaNumber;
    },

    createLoshuGrid(dob, gender) {
        let grid = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [] };
        const [year, month, day] = dob.split('-').map(Number);
        const psychicNumber = this.calculatePsychicNumber(day);
        const destinyNumber = this.calculateDestinyNumber(dob);
        const kuaNumber = this.calculateKuaNumber(year, gender);
        const dobDigits = Array.from(String(year) + String(month) + String(day), Number);
        if (![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30].includes(day)) {
            dobDigits.push(psychicNumber);
        }
        dobDigits.push(destinyNumber, kuaNumber);
        dobDigits.forEach(digit => {
            if (digit !== 0) {
                grid[digit].push(digit);
            }
        });
    
        const celestialBodies = {
            1: "Sun: King",
            2: "Moon: Queen",
            3: "Jupiter: Counselor",
            4: "Pluto: Mysterious",
            5: "Mercury: Prince",
            6: "Venus: Devil's Guru",
            7: "Neptune: Saint",
            8: "Saturn: Judge",
            9: "Mars: Commander"
        };
    
        const frequencyDescriptions = {
            0: "",
            1: "On",
            2: "Strong",
            3: "Weak"
        };
    
        const loshuGrid = [[4, 9, 2], [3, 5, 7], [8, 1, 6]];
        let finalGrid = [[], [], []];
    
        for (let i = 0; i < 3; i++) {
            finalGrid[i] = [];
            for (let j = 0; j < 3; j++) {
                let cell = loshuGrid[i][j];
                let cellContent = grid[cell];
                if (cellContent.length > 0) {
                    const celestialBody = celestialBodies[cell] || '';
                    const frequencyDescription = frequencyDescriptions[cellContent.length] || "Weaker";
                    finalGrid[i].push(`${cellContent.join('')}`);
                } else {
                    finalGrid[i].push('');
                }
            }
        }
    
        return finalGrid;
    },    

};  