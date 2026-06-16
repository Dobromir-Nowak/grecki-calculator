import numpy as np
import streamlit as st





# # (weight, coefficient) points
# points = [
#     (0.2, 1.1),
#     (0.5, 1.5),
#     (1.0, 2.3),
#     (2.0, 3.0),
# ]

# weights = np.array([p[0] for p in points])
# coeffs = np.array([p[1] for p in points])

# def coefficient(weight):
#     return np.interp(weight, weights, coeffs)

# def price(weight):
#     c = coefficient(weight)
#     return c * weight * 100  # whatever the formula is











weight_g_data = np.array([
    1, 3, 5, 7, 10, 13, 15, 17, 20, 23,
    27, 30, 33, 36, 40, 45, 50, 55, 60, 65,
    70, 75, 80, 85, 90, 100, 120, 150, 170, 200
])

W_data = np.array([
    13.300, 8.000, 5.000, 3.750, 3.161, 2.875, 2.744, 2.639, 2.513, 2.412,
    2.301, 2.230, 2.166, 2.108, 2.038, 1.959, 1.887, 1.822, 1.762, 1.707,
    1.656, 1.608, 1.563, 1.522, 1.483, 1.413, 1.302, 1.195, 1.160, 1.157
])

def W_interp(fish_weight_g):
    return np.interp(fish_weight_g, weight_g_data, W_data) # interpolated W value




# streamlit

# inputs
H = st.number_input("H:", 7.50)
fish_weight_g = st.number_input("Fish weight [g]", 100.0)

# values
W = W_interp(fish_weight_g)
price_kg = W*H
price_fish = price_kg * (fish_weight_g/1000)

# printing 
if fish_weight_g:
    st.write("Price per kg:", round((price_kg),2))
    st.write("Price per fish:", round(price_fish, 4))
    st.write("W:", round(W, 3))

total_weight = st.number_input("Total weight [kg]", 1.0)

if total_weight:
    st.write("Total price:", round(total_weight*price_kg,2))