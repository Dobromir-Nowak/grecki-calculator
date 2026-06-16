import numpy as np
import streamlit as st

# (weight, coefficient) points
points = [
    (0.2, 1.1),
    (0.5, 1.5),
    (1.0, 2.3),
    (2.0, 3.0),
]

weights = np.array([p[0] for p in points])
coeffs = np.array([p[1] for p in points])

def coefficient(weight):
    return np.interp(weight, weights, coeffs)

def price(weight):
    c = coefficient(weight)
    return c * weight * 100  # whatever the formula is



# streamlit

fish_weight = st.number_input("Fish weight [g]", 0.0)

if fish_weight:
    st.write("Price per kg:", price(fish_weight))

total_weight = st.number_input("Total weight [kg]", 1.0)

if total_weight:
    st.write("Total price:", total_weight*price(fish_weight))