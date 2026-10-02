import streamlit as st
import numpy as np

st.set_page_config(page_title="Kalkulator Matriks Interaktif", layout="centered")

st.title("🔢 Kalkulator Matriks Interaktif")

# Pilihan Operasi
option = st.selectbox("Pilih Operasi Matriks:", ["Perkalian (A × B)", "Penjumlahan (A + B)", "Pengurangan (A - B)", "Determinan"])

st.markdown("---")

if option == "Perkalian (A × B)":
    st.subheader("Perkalian Matriks A (2x3) dan B (3x2)")
    
    col1, col2, col3 = st.columns([3, 3, 3])
    
    # Matriks A
    with col1:
        st.markdown("**Matriks A (2x3)**")
        a11 = st.number_input("A11", value=2.0, key="a11")
        a12 = st.number_input("A12", value=1.0, key="a12")
        a13 = st.number_input("A13", value=3.0, key="a13")
        a21 = st.number_input("A21", value=4.0, key="a21")
        a22 = st.number_input("A22", value=0.0, key="a22")
        a23 = st.number_input("A23", value=2.0, key="a23")
        A = np.array([[a11, a12, a13], [a21, a22, a23]])

    # Matriks B
    with col2:
        st.markdown("**Matriks B (3x2)**")
        b11 = st.number_input("B11", value=5.0, key="b11")
        b12 = st.number_input("B12", value=2.0, key="b12")
        b21 = st.number_input("B21", value=1.0, key="b21")
        b22 = st.number_input("B22", value=4.0, key="b22")
        b31 = st.number_input("B31", value=3.0, key="b31")
        b32 = st.number_input("B32", value=7.0, key="b32")
        B = np.array([[b11, b12], [b21, b22], [b31, b32]])

    # Hasil AB
    with col3:
        st.markdown("**Hasil Matriks AB**")
        res = np.dot(A, B)
        st.dataframe(res)

    st.markdown("---")
    # Slider Pilihan Posisi elemen
    row_idx = st.slider("Baris Hasil (1-2)", 1, 2, 1) - 1
    col_idx = st.slider("Kolom Hasil (1-2)", 1, 2, 1) - 1
    
    val_res = res[row_idx, col_idx]
    st.info(f"**(AB)₃₃ Detail Calculation:**\n\n$(AB)_{{{row_idx+1}{col_idx+1}}} = ({A[row_idx,0]} \\cdot {B[0,col_idx]}) + ({A[row_idx,1]} \\cdot {B[1,col_idx]}) + ({A[row_idx,2]} \\cdot {B[2,col_idx]}) = {val_res}$")

elif option == "Determinan":
    st.subheader("Kalkulator Determinan Matriks Persegi (N x N)")
    n = st.number_input("Masukkan ukuran matriks N x N:", min_value=2, max_value=5, value=2)
    
    mat = []
    st.write("Masukkan Elemen Matriks:")
    for i in range(n):
        cols = st.columns(n)
        row = []
        for j in range(n):
            val = cols[j].number_input(f"M[{i+1},{j+1}]", value=1.0 if i==j else 0.0, key=f"det_{i}_{j}")
            row.append(val)
        mat.append(row)
    
    mat_arr = np.array(mat)
    det_val = np.linalg.det(mat_arr)
    st.success(f"### **Determinan Matriks |M| = {det_val:.4f}**")

else: # Penjumlahan / Pengurangan
    st.subheader(f"Operasi {option}")
    n_row = st.number_input("Jumlah Baris:", min_value=1, max_value=4, value=2)
    n_col = st.number_input("Jumlah Kolom:", min_value=1, max_value=4, value=2)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Matriks A")
        A = np.ones((n_row, n_col))
    with col2:
        st.write("Matriks B")
        B = np.ones((n_row, n_col))
        
    if option == "Penjumlahan (A + B)":
        st.write("Hasil (A + B):")
        st.dataframe(A + B)
    else:
        st.write("Hasil (A - B):")
        st.dataframe(A - B)