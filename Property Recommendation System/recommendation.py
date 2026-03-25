import pandas as pd
import random


# -------------------------
# Load datasets
# -------------------------

customers = pd.read_excel("/Users/NANI/iCloud Drive (Archive)/Desktop/Desktop/Internship/task2/data/customer data.xlsx")
properties = pd.read_excel("/Users/NANI/iCloud Drive (Archive)/Desktop/Desktop/Internship/task2/data/properties data.xlsx")
wishlist = pd.read_excel("/Users/NANI/iCloud Drive (Archive)/Desktop/Desktop/Internship/task2/data/customer_wishlist_columns.xlsx")


# -------------------------
# Convert wishlist to rows
# -------------------------

wishlist_long = wishlist.melt(
    id_vars=["customer_id"],
    var_name="property_col",
    value_name="property_id"
)

wishlist_long = wishlist_long.dropna()


# -------------------------
# Search properties (STRICT)
# -------------------------

def search_properties(city, ptype, bhk, max_price):

    result = properties[
        (properties["City_Town"].str.lower() == city.lower()) &
        (properties["Property_Type"].str.lower() == ptype.lower()) &
        (properties["Bedrooms"] == bhk) &
        (properties["Price_INR"] <= max_price)
    ]

    return result


# -------------------------
# Find customers with similar interest
# -------------------------

def find_similar_customers(property_ids):

    data = wishlist_long[
        wishlist_long["property_id"].isin(property_ids)
    ]

    return data["customer_id"].unique()


# -------------------------
# Get wishlist from those customers
# -------------------------

def get_wishlist_from_customers(customer_ids):

    data = wishlist_long[
        wishlist_long["customer_id"].isin(customer_ids)
    ]

    return data["property_id"].unique()


# -------------------------
# Recommendation logic
# -------------------------

def recommend(city, ptype, bhk, max_price):

    # Step 1 — search
    search_result = search_properties(
        city, ptype, bhk, max_price
    )

    if len(search_result) == 0:
        return pd.DataFrame()

    search_ids = search_result["Property_ID"].tolist()

    # Step 2 — find similar customers
    similar_customers = find_similar_customers(
        search_ids
    )

    # Step 3 — get their wishlist
    wishlist_ids = get_wishlist_from_customers(
        similar_customers
    )

    # IMPORTANT FIX
    # wishlist must also match search result
    wishlist_props = search_result[
        search_result["Property_ID"].isin(wishlist_ids)
    ]

    # 40% wishlist + 60% search

    n = 10
    n1 = int(n * 0.4)
    n2 = int(n * 0.6)

    if len(wishlist_props) > 0:
        part1 = wishlist_props.sample(
            min(n1, len(wishlist_props)),
            random_state=1
        )
    else:
        part1 = pd.DataFrame()

    part2 = search_result.sample(
        min(n2, len(search_result)),
        random_state=1
    )

    final = pd.concat([part1, part2])

    return final


# -------------------------
# INPUT
# -------------------------

print("\nSearch Property\n")

city = input("Enter city: ")

ptype = input("Enter property type: ")

bhk_input = input("Enter BHK (ex: 3 or 3bhk): ")
bhk = int("".join(filter(str.isdigit, bhk_input)))

max_price = int(input("Enter max price: "))


# -------------------------
# RUN
# -------------------------

result = recommend(
    city,
    ptype,
    bhk,
    max_price
)


if len(result) == 0:
    print("\nNo properties found")

else:
    print("\nRecommended Properties:\n")

    print(result[[
        "Property_ID",
        "City_Town",
        "Property_Type",
        "Bedrooms",
        "Price_INR"
    ]])