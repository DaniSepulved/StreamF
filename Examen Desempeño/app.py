from unicodedata import category
import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
products = ["Laptop", "Phone", "Tablet", "Headphones"]
categories = ["Electronics", "Accessories"]
data = {
    "Date": np.random.choice(dates, 50),
    "Product": np.random.choice(products, 50),
    "Category": np.random.choice(categories, 50),
    "Price": np.random.uniform(50, 500, 50).round(2),
    "Quantity": np.random.randint(1, 5, 50)
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
df.to_csv("sales_data.csv", index=False)


st.title("Análisis Básico de Ventas")

df = pd.read_csv('sales_data.csv')

st.write("Dataset")
st.dataframe(df)

st.subheader("Datos Completos")

category = st.selectbox("Elige una categoria:", ["Accessories", "Electronics"])
df_filtrado = df[df['Category'] == category]

st.subheader("Datos Filtrados")
st.dataframe(df_filtrado)


min_price = 104.94
max_price = 487.27

price_range = st.slider("Selecciona un precios:", min_price, max_price, (104.94, 487.27))
df_filtrado2 = df[(df["Price"] >= price_range[0]) & (df["Price"] <= price_range[1])]

st.subheader("Datos Filtrados")
st.dataframe(df_filtrado2)


st.subheader("Ver un producto por indice")
indice = st.slider("Selecciona un índice", 0, len(df) - 1, 0)
st.write(df.iloc[indice])

st.subheader("Estadísticas")
if not df_filtrado2.empty:

    total_sales = df_filtrado2['Total_Sales'].sum()
    avg_price = df_filtrado2['Price'].mean()

    col1, col2 = st.columns(2)
    col1.metric("Total de Ventas", f"${total_sales:,.2f}")
    col2.metric("Precio Promedio", f"${avg_price:,.2f}")
else:
    st.write("No hay datos para los filtros seleccionados.")
