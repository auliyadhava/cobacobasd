import streamlit as st

st.title("Radio Buttons, Checkboxes and Buttons")
page_names = ['Perhitungan Mol', 'Perhitungan Vstp', 'Perhitungan Vrtp', 'Perhitungan Molaritas', 'Perhitungan Normalitas']
page = st.radio('Navigation', page_names)
st.write("**The variable 'page' returns: **", page)

st.image('IMG\Vtuber.png')

if page == 'Perhitungan Mol':
    # input 1
    massa = st.number_input(label="Masukkan massa dalam gram", value=0.001, placeholder="Type a number...")

    # input 2
    bm = st.number_input(label="Masukkan BM dalam satuan gram per mol", value=0.001, placeholder="Type a number...")
    
    ans = massa / bm
    st.write(f"{massa} / {bm} = {ans:.3f}")
    st.success(f"Answer = {ans}")


if page == 'Perhitungan Vstp':
    n = st.number_input(label="Masukkan nilai n dalam satuan")

    atm = st.number_input(label="Masukkan nilai atm dalam satuan (diasumsikan 22,4)")

    ans = n * atm
    st.write(f"{n} * {atm} = {ans:.3f}")

if page == 'Perhitungan Vrtp':
    n = st.number_input(label="Masukkan nilai n dalam satuan")

    atm = st.number_input(label="Masukkan nilai atm dalam satuan (diasumsikan 22,4)")

    ans = n * atm
    st.write(f"{n} * {atm} = {ans:.3f}")

if page == 'Perhitungan Molaritas':
    # input 1
    massa = st.number_input(label="Masukkan massa dalam gram")

    # input 2
    bm = st.number_input(label="Masukkan BM dalam satuan gram per mol")
    
    atm = st.number_input(label="Masukkan nilai atm dalam satuan (diasumsikan 22,4)")

    ans = massa / bm * volume
    st.write(f"{massa} / {bm} * {volume} = {ans:.3f}")

if page == 'Perhitungan Normalitas':
    # input 1
    massa = st.number_input(label="Masukkan massa dalam gram")

    # input 2
    be = st.number_input(label="Masukkan BM dalam satuan gram per mol")
    
    atm = st.number_input(label="Masukkan nilai atm dalam satuan (diasumsikan 22,4)")

    ans = massa / bm * volume
    st.write(f"{massa} / {bm} * {volume} = {ans:.3f}")

    st.success(f"Answer = {ans}")