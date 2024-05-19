#  🏠 House Purchase Cost Calculator

Welcome to the House Purchase Cost Calculator! This Streamlit app, written in Python, helps you calculate the amount of savings needed for buying a house in Sweden. The app includes calculations for 'lagfart', 'pantbrev', and 'kontantinsats'. You can also use it to calculate the amount of savings needed to buy a particular house.💰

## Demo 🚀

Check out the live demo of the app [here](https://housesavingscalculator.streamlit.app/). 


## How to Use

1. **Install Dependencies**: Ensure you have Python and Streamlit installed. If not, you can install Streamlit using pip:
    ```bash
    pip install streamlit
    ```

2. **Run the App**: Clone this repository and run the app using Streamlit:
    ```bash
    streamlit run app.py
    ```

3. **Enter the Details**: 
    - Enter the house price.
    - Enter the existing pant brief (if any).
    - Click on the "Calculate" button.

4. **View the Results**: The app will display the calculated 'lagfart', 'pantbrev', 'kontantinsats', and the total savings needed to buy the house.

## Example Calculations

### Lagfart Calculation
- **Formula**: `lagfart_max = house_price * 0.015 + 825`
- **Description**: This fee is typically 1.5% of the house price plus a fixed amount of 825 SEK.

### Pantbrev Calculation
- **Formula**: `pantbrev_max = (house_price * 0.85 - pant_brief) * 0.02 + 325`
- **Description**: This cost is for registering a mortgage deed, calculated as 2% of the mortgage amount plus a fixed fee of 325 SEK.

### Kontantinsats Calculation
- **Formula**: `kontantinsats_max = house_price * 0.15`
- **Description**: The down payment required is 15% of the house price.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please feel free to reach out.

---

Thank you for using the House Purchase Cost Calculator! We hope it helps you in planning your house purchase in Sweden.
