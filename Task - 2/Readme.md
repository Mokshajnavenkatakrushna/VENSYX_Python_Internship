# Property Recommendation System

## Overview

This project is a Property Search and Recommendation System built using Python and Pandas.

The system searches properties based on user input and recommends properties using customer wishlist similarity.

Recommendation logic:

* 60% from search results
* 40% from similar customers wishlist

---

## Project Structure

project/

main.py
README.md

data/
    customer data.xlsx
    properties data.xlsx
    customer_wishlist_columns.xlsx

---

## Datasets Used

### customer data.xlsx

Contains customer information.

Required column:
customer_id

### properties data.xlsx

Contains property details.

Required columns:

Property_ID
City_Town
Property_Type
Bedrooms
Price_INR

### customer_wishlist_columns.xlsx

Contains wishlist in column format.

Example:

customer_id | wishlist1 | wishlist2 | wishlist3 | wishlist4

The program converts this into row format using Pandas melt().

---

## How the Program Works

### Step 1 — Load datasets

The program loads Excel files using pandas.

pd.read_excel()

### Step 2 — Convert wishlist to rows

wishlist.melt()

Result format:

customer_id | property_id

### Step 3 — Search properties

Filters using:

City
Property Type
Bedrooms
Max Price

### Step 4 — Find similar customers

Finds customers who added searched properties to wishlist.

### Step 5 — Get wishlist from similar customers

Gets other properties liked by those customers.

### Step 6 — Recommendation

Total recommendations = 10

40% from wishlist
60% from search result

---

## How to Run

Install requirements

pip install pandas openpyxl

Run program

python main.py

Enter input

Enter city: Hyderabad
Enter property type: Apartment
Enter BHK: 3bhk
Enter max price: 8000000

Output

Recommended Properties will be displayed.

---

## Functions Used

search_properties()

find_similar_customers()

get_wishlist_from_customers()

recommend()

---

## Technologies Used

Python
Pandas
Excel
Random Sampling

---

## Author

Internship Task 2
Property Recommendation System
