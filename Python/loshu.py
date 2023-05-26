# loshu.py
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.table import Table
from numerology import NumerologyCalculator

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
        for digit in digits:
            if digit != 0:
                self.grid[digit] += str(digit)


class LoshuGridPlot:

    @staticmethod
    def draw_loshu_grid(grid, celestial=False, labels=False, ax=None):
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
            '4': "Pluto: Myterious",
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
                if celestial:
                    digits_in_cell = table_data[i][j]
                    celestial_body_names = set(
                        celestial_bodies[digit] for digit in digits_in_cell if digit in celestial_bodies)
                    frequency_description = {
                        0: "",
                        1: "Effects",
                        2: "Strong Effects",
                        3: "Weak"
                    }.get(len(digits_in_cell), "Weaker")
                    cell_text = f'{digits_in_cell}\n{" ".join(celestial_body_names)}\n{frequency_description}'
                    table.add_cell(i, j, 1, 1, text="", loc='center',facecolor='white')  # add empty cell
                    ax.text(j / 3 + 1/6, (2 - i) / 3 + 1/6, cell_text,
                        ha='center', va='center', fontsize=5, color='red')
                else:
                    cell_text = table_data[i][j]
                    table.add_cell(i, j, 1, 1, text=cell_text, loc='center', facecolor='white')


        if labels:
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

def draw_loshu_grids(loshu_grid, labels):
    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots(figsize=(3, 3))
        LoshuGridPlot.draw_loshu_grid(loshu_grid, celestial=False, labels=labels, ax=ax)
        st.pyplot(fig)
    with col2:
        fig, ax = plt.subplots(figsize=(3, 3))
        LoshuGridPlot.draw_loshu_grid(loshu_grid, celestial=True, labels=labels, ax=ax)
        st.pyplot(fig)