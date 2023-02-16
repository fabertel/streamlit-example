import streamlit as st


Title


st.title('Compound Interest Calculator')


Header/Subheader


st.header('Calculate your compound interest')

st.subheader('Input your values below')


Get user inputs


principal = st.number_input('Principal amount ($)', min_value=0)

rate = st.number_input('Annual rate of interest (%)', min_value=0)

compounding_periods = st.number_input('Number of compounding periods (per year)', min_value=0)

time = st.number_input('Time (years)', min_value=0)


Calculate compound interest


compound_interest = principal * (1 + (rate / compounding_periods)) ** (compounding_periods * time)


Show outputif st.button('Calculate'):

st.success(f'Compound interest is ${compound_interest:,.2f}')
