import streamlit as st

st.markdown("<h1 style='text-align: center; color: red;'>CoWin Availability Status</h1>", unsafe_allow_html=True)
pin = st.text_input("PIN Code")
start_date = st.date_input("Lookup Start Date")
end_date = st.date_input("Lookup End Date")
fee = st.selectbox('Fee Type',('Paid', 'Free', 'both'))
age = st.selectbox('Age limit',('18-45', '45+'))

st.error(f'Cross origin resource sharing issue')
st.info("check out this [link](https://github.com/siddheshshankar/Covid-availability-check/blob/main/app.py) and try running it in your local machine")
