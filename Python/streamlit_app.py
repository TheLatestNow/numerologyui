# streamlit_app.py
import streamlit as st
import matplotlib.pyplot as plt

from loshu import LoshuGrid, LoshuGridPlot
from user_inputs import UserInputs
from numerology_table import NumerologyTable
from numerology import NumerologyCalculator

def get_psychic_description(psychic_number: int) -> str:
    with open(f"psychic{psychic_number}.md", "r") as f:
        return f.read()

def display_numerology_values(psychic_number, destiny_number, kua_number, inputs):
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown(f"<h5 style='text-align: center; color: green;'>{inputs.fname} {inputs.lname}</h5>", unsafe_allow_html=True)
    col2.markdown(f"<h5 style='text-align: center; color: green;'>Psychic Number: {psychic_number}</h5>", unsafe_allow_html=True)
    col3.markdown(f"<h5 style='text-align: center; color: green;'>Destiny Number: {destiny_number}</h5>", unsafe_allow_html=True)
    # col4.markdown(f"<h5 style='text-align: center; color: green;'>Kua Number: {kua_number}</h5>", unsafe_allow_html=True)


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

def main():

    st.markdown("""
        <style>
        .header {
            padding: 10px;
            text-align: center;
            background: #11998e;  /* fallback for old browsers */
            background: -webkit-linear-gradient(to right, #38ef7d, #11998e);  /* Chrome 10-25, Safari 5.1-6 */
            background: linear-gradient(to right, #38ef7d, #11998e); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
            color: white;
            font-size: 25px;
        }
        </style>
        <div class="header">
            Loshu Creator App
        </div>
        """, unsafe_allow_html=True)
    
    inputs = UserInputs()

    if st.button("Calculate"):
        if inputs.is_valid():

            psychic_number, destiny_number, kua_number, dob_str = NumerologyCalculator.calculate_numerology_values(inputs)

            display_numerology_values(psychic_number, destiny_number, kua_number, inputs)

            loshu_grid = LoshuGrid(dob_str, inputs.gender.lower()).grid

            draw_loshu_grids(loshu_grid, inputs.labels)

            # st.image("https://github.com/TheLatestNow/numerologyui/blob/main/Python/knumberchart.jpg", caption = kua_number)

            NumerologyTable.create_record(inputs.fname, inputs.lname, inputs.dob, inputs.gender, psychic_number, destiny_number, kua_number, loshu_grid)

            # Get psychic description and display it
            # description = get_psychic_description(psychic_number)
            # st.markdown(description, unsafe_allow_html=True)

            pass
        else:
            st.error('Please fill in all the fields before proceeding.')

    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #11998e;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to right, #38ef7d, #11998e);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to right, #38ef7d, #11998e); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
    Made by Sameer Goel | Student of Astro Arun Pandit | Please email to sameer.neu@gmail.com for bugs/suggestions.
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()