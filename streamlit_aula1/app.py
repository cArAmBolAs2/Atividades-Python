import streamlit as st
import pandas as pd

st.write("Olá, mundo")

nome = "Gabriel"
idade = 19
st.write(nome, idade)

st.title("Meu primeiro dash")
st.subheader("Gabriel")

dados = {
  'Matérias': ['Português', 'Matemática', 'Python', 'Frame'],
  'Notas': [5, 9, 7, 10]
}
df = pd.DataFrame(dados)

st.write(df)