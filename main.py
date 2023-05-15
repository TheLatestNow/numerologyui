import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.table import Table


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


class LoshuGrid:

    def __init__(self, dob: str, gender: str):
        self.grid = {i: "" for i in range(1, 10)}
        self.populate_grid(dob, gender)

    def populate_grid(self, dob: str, gender: str):
        day, month, year = (int(part) for part in dob.split("-"))
        psychic_number = NumerologyCalculator.calculate_psychic_number(day)
        destiny_number = NumerologyCalculator.calculate_destiny_number(dob)
        kua_number = NumerologyCalculator.calculate_kua_number(year, gender)
        digits = list(map(int, list(dob.replace("-", ""))))
        if day not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]:
            digits.append(psychic_number)
        digits.append(destiny_number)
        digits.append(kua_number)
        for digit in digits:
            if digit != 0:
                self.grid[digit] += str(digit)


class LoshuGridPlot:

    @staticmethod
    def draw_loshu_grid(grid, ax=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(3, 3))

        table_data = [
            [grid[4], grid[9], grid[2]],
            [grid[3], grid[5], grid[7]],
            [grid[8], grid[1], grid[6]]
        ]

        celestial_bodies = {
            1: "Sun: King",
            2: "Moon: Queen",
            3: "Jupiter: Councellor",
            4: "Pluto: Myterious Robinhood",
            5: "Mercury: Prince",
            6: "Venus: Devil's Guru",
            7: "Neptune: Saint",
            8: "Saturn: Judge",
            9: "Mars: Commander"
        }

        row_labels = ['Mind Plane', 'Heart Plane', 'Rational Plane']
        col_labels = ['Vision Plane', 'Will Plane', 'Action Plane']

        table = Table(ax, bbox=[0, 0, 1, 1])

        for i in range(3):
            for j in range(3):
                cell_text = table_data[i][j]
                celestial_body = celestial_bodies.get(table_data[i][j], "")
                if celestial_body:
                    cell_text += f" ({celestial_body})"
                table.add_cell(i, j, 1, 1, text=cell_text,
                               loc='center', facecolor='white')

        # Add labels for rows
        for i, label in enumerate(row_labels):
            ax.text(-0.1, (2 - i) / 3 + 1/6, label,
                    ha='right', va='center', fontsize=5)

        # Add labels for columns
        for j, label in enumerate(col_labels):
            ax.text(j / 3 + 1/6, 1.1, label,
                    ha='center', va='bottom', fontsize=5)

        ax.add_table(table)
        ax.axis('off')

    @staticmethod
    def draw_loshu_celestial_grid(grid, ax=None):
        if ax is None:
            fig, ax = plt.subplots(figsize=(3, 3))

        table_data = [
            [grid[4], grid[9], grid[2]],
            [grid[3], grid[5], grid[7]],
            [grid[8], grid[1], grid[6]]
        ]

        celestial_bodies = {
            '1': "Sun: King",
            '2': "Moon: Queen",
            '3': "Jupiter: Councellor",
            '4': "Pluto: Myterious Robinhood",
            '5': "Mercury: Prince",
            '6': "Venus: Devil's Guru",
            '7': "Neptune: Saint",
            '8': "Saturn: Judge",
            '9': "Mars: Commander"
        }

        row_labels = ['Mind Plane', 'Heart Plane', 'Rational Plane']
        col_labels = ['Vision Plane', 'Will Plane', 'Action Plane']

        table = Table(ax, bbox=[0, 0, 1, 1])

        for i in range(3):
            for j in range(3):
                digits_in_cell = table_data[i][j]
                celestial_body_names = set(
                    celestial_bodies[digit] for digit in digits_in_cell if digit in celestial_bodies)
                frequency_description = {
                    0: "",
                    1: "On",
                    2: "Strong",
                    3: "Weak"
                }.get(len(digits_in_cell), "Weaker")
                cell_text = f'{digits_in_cell}\n{" ".join(celestial_body_names)}\n{frequency_description}'
                table.add_cell(i, j, 1, 1, text="", loc='center',
                               facecolor='white')  # add empty cell
                ax.text(j / 3 + 1/6, (2 - i) / 3 + 1/6, cell_text,
                        ha='center', va='center', fontsize=5)  # add text annotation

        # Add labels for rows
        for i, label in enumerate(row_labels):
            ax.text(-0.1, (2 - i) / 3 + 1/6, label,
                    ha='right', va='center', fontsize=5)

        # Add labels for columns
        for j, label in enumerate(col_labels):
            ax.text(j / 3 + 1/6, 1.1, label,
                    ha='center', va='bottom', fontsize=5)

        ax.add_table(table)
        ax.axis('off')


def main():
    st.title("Numerology Calculator")
    dob = st.date_input("Enter your date of birth", datetime(1990, 1, 28))
    gender = st.selectbox("Select your gender", ["Male", "Female"])

    if st.button("Calculate"):
        dob_str = dob.strftime("%d-%m-%Y")

        loshu_grid = LoshuGrid(dob_str, gender.lower()).grid

        fig, ax = plt.subplots(figsize=(3, 3))
        LoshuGridPlot.draw_loshu_grid(loshu_grid, ax=ax)
        st.pyplot(fig)

        fig, ax = plt.subplots(figsize=(3, 3))
        LoshuGridPlot.draw_loshu_celestial_grid(loshu_grid, ax=ax)
        st.pyplot(fig)


if __name__ == "__main__":
    main()
