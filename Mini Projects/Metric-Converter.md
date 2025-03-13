# Metric & Currency Converter  

## Overview  
This Python program serves as a **Metric & Currency Converter**, allowing users to convert different measurement units, including **length, weight, and currency**. The program operates in a loop, enabling users to perform multiple conversions until they choose to exit.  

---

## How the Program Works  

### 1. Displaying the Welcome Message  
When the program starts, it prints a **welcome message** in a formatted style to introduce the converter. This makes it clear to the user what the program is about.  

### 2. Presenting the Conversion Menu  
The program provides a structured **conversion menu** listing eight different types of conversions. Users are prompted to select an option by entering a number from 1 to 8.  

### 3. Taking User Input & Performing the Conversion  
- Once the user selects a conversion type, they are prompted to enter a numerical value.  
- The program applies a **predefined mathematical formula** for conversion.  
- The result is displayed with proper formatting.  

#### Conversion Formulas:
- **Centimeters to Meters** → `value / 100`  
- **Meters to Kilometers** → `value / 1000`  
- **Meters to Feet** → `value * 3.28084`  
- **Grams to Kilograms** → `value / 1000`  
- **Kilograms to Tons** → `value / 1000`  
- **Kilograms to Pounds** → `value * 2.20462`  
- **Rupees to Dollars** → `value / 87.5425`  
- **Dollars to Rupees** → `value * 87.5425`  

For currency conversion, the program also displays an **exchange rate note** before accepting input.  

### 4. Continuing or Exiting the Program  
After completing a conversion, the user is given the option to continue or exit.  
- If they enter **1**, the program restarts, allowing them to perform another conversion.  
- If they enter **0**, the program exits.  
- If an invalid input is provided, the program prompts the user to enter a valid choice.  
