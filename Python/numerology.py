# numerology.py

class NumerologyCalculator:

    @staticmethod
    def calculate_psychic_number(day: int) -> int:
        while day >= 10:
            day = sum(int(digit) for digit in str(day))
        return day

    @staticmethod
    def calculate_destiny_number(date_of_birth: str) -> int:
        day, month, year = (int(part) for part in date_of_birth.split("-"))
        destiny_number = day + month + year
        while destiny_number >= 10:
            destiny_number = sum(int(digit) for digit in str(destiny_number))
        return destiny_number
    @staticmethod
    def calculate_kua_number(year: int, gender: str) -> int:
        if gender.lower() not in ["male", "female"]:
            raise ValueError("Gender must be 'male' or 'female'")
        while year >= 10:
            year = sum(int(digit) for digit in str(year))
        if gender.lower() == "male":
            kua_number = 11 - year
        else:  # female
            kua_number = year + 4
        while kua_number >= 10:
            kua_number = sum(int(digit) for digit in str(kua_number))
        return kua_number
    @staticmethod
    def calculate_numerology_values(inputs):
        dob_str = inputs.dob.strftime("%d-%m-%Y")
        day, month, year = (int(part) for part in dob_str.split("-"))
        psychic_number = NumerologyCalculator.calculate_psychic_number(day)
        destiny_number = NumerologyCalculator.calculate_destiny_number(dob_str)
        kua_number = NumerologyCalculator.calculate_kua_number(year, inputs.gender.lower())

        return psychic_number, destiny_number, kua_number, dob_str