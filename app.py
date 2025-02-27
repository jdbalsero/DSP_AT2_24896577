import streamlit as st
import datetime

from frankfurter import get_currencies_list, get_latest_rates, get_historical_rate
from currency import reverse_rate, round_rate, format_output

# Display Streamlit App Title
st.title('FX Converter')

# Get the list of available currencies from Frankfurter
currencies_list = get_currencies_list()

# If the list of available currencies is None, display an error message in Streamlit App
if currencies_list == None:
    st.error('Cannot get the currencies list. Please contact the app administrator')

# Add input fields for capturing amount, from and to currencies
amount = st.number_input('Enter the amount to be converted', format='%.2f', step=0.50, min_value=00.00, value=50.00)

from_currency = st.selectbox('From Currency:', currencies_list)
to_currency = st.selectbox('To Currency:', currencies_list)

# Add a button to get and display the latest rate for selected currencies and amount
if st.button('Get Latest Rate'):
    st.header('Latest Conversion Rate')
    latest_rate, date = get_latest_rates(from_currency, to_currency, amount)
    st.write(format_output(date, from_currency, to_currency, latest_rate, amount))

# Add a date selector (calendar)
hist_date = st.date_input('Select a date for historical rates:', max_value=datetime.date.today())

# Add a button to get and display the historical rate for selected date, currencies and amount
if st.button('Conversion Rate'):
    st.header('Historical Conversion Rate')
    historical_rate = get_historical_rate(from_currency, to_currency, hist_date, amount)
    st.write(format_output(hist_date, from_currency, to_currency, historical_rate, amount))
