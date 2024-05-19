import streamlit as st
import locale
locale.setlocale(locale.LC_ALL, 'sv_SE') # Use '' for auto, or force e.g. to 'en_US.UTF-8'


def calcMaxPant(savings):
    houseYouCanAfford = (savings-1150)/0.182
    # round by first decimal and remove the decimal:
    if houseYouCanAfford < 0:
        houseYouCanAfford = 0
    return houseYouCanAfford


def calculate_costs(house_price: float, pant_brief: float):
    lagfart_max = house_price * 0.015 + 825
    pantbrev_max = (house_price * 0.85 - pant_brief) * 0.02 + 375
    kontantinsats_max = house_price * 0.15
    return lagfart_max, pantbrev_max, kontantinsats_max


def howMuchSavingsForHouse(pantSum, housePrice):
    savingsForHouse = 0.182*housePrice-0.02*pantSum+1150
    return savingsForHouse


def display_costs(house_price: float, pant_brief: float):
    lagfart_max, pantbrev_max, kontantinsats_max = calculate_costs(house_price, pant_brief)
    with st.expander("Vad går pengarna till?"):
        st.write("Lagfart: " + locale.format_string("%.0f", lagfart_max, grouping=True) + " kr")
        st.write("Pantbrev: " + locale.format_string("%.0f", pantbrev_max, grouping=True) + " kr")
        st.write("Kontantinsats: " + locale.format_string("%.0f", kontantinsats_max, grouping=True) + " kr")
        st.write("Summa 💰: " + locale.format_string("%.0f", lagfart_max+pantbrev_max+kontantinsats_max, grouping=True) + " kr")


st.title('Räknare för sparpengar och husköp')
st.write('Den här räknaren avser hus där du behöver betala lagfart och pantbrev utöver husets pris. Det finns två olika räknare.')
st.markdown('---')
st.header("1. Hur dyrt hus har jag råd med?")

# Create an input field
input_value = st.number_input("Hur mycket sparpengar kan du lägga på huset totalt, inklusive kontantinsats, pantbrev och lagfart?:", min_value=0, value=0)

# When the button is clicked, use the input value in the calc function
if st.button("Räkna ut pris på hus 💵"):
    result = calcMaxPant(input_value)
    output = "🏠 Du kan köpa ett hus för maximalt: " + locale.format_string("%.0f", result, grouping=True) + " kr."
    st.write(f"{output}")
    st.write("Detta inkluderar kontantinsats, pantbrev odh lagfart. Vi utgår från att huset inte har några pantbrev alls (dyrast möjliga situation) och att du vill betala 15 % i kontantinsats. Finns pantbrev kan huset bli något billigare och du kan ha råd med ett marginellt dyrare hus.")
    display_costs(result, 0)

st.markdown('---')
st.header("2. Hur mycket sparpengar behöver jag för ett specifikt hus?")

# Create an input field
house_price = st.number_input("Vad är husets uppskattade pris?", min_value=0, value=0)
pant_brief = st.number_input("Vad är värdet på husets pantbrev (t.ex. 120 000)", min_value=0, value=0)

# When the button is clicked, use the input value in the calc function
if st.button("Räkna ut sparpengar 💰"):
    result = howMuchSavingsForHouse(pant_brief, house_price)
    output = "🏠 För att köpa det här huset behöver du ha sparat ihop minst " + locale.format_string("%.0f", result, grouping=True) + " kr."
    st.write(f"{output}")
    display_costs(house_price, pant_brief)

