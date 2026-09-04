import streamlit as st

st.title("🧮 Calculadora")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro número:", value=0.0)

with col2:
    num2 = st.number_input("Segundo número:", value=0.0)

operacao = st.selectbox("Escolha uma operação:", 
    ["Adição", "Subtração", "Multiplicação", "Divisão"])

if st.button("Calcular", use_container_width=True):
    if operacao == "Adição":
        resultado = num1 + num2
    elif operacao == "Subtração":
        resultado = num1 - num2
    elif operacao == "Multiplicação":
        resultado = num1 * num2
    else:
        if num2 == 0:
            st.error("❌ Erro: Não é possível dividir por zero!")
        else:
            resultado = num1 / num2
    
    if operacao != "Divisão" or num2 != 0:
        st.success(f"✅ Resultado: {resultado}")