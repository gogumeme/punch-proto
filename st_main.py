import streamlit as st
# import pandas as pd
from streamlit_gsheets import GSheetsConnection

if 'n' not in st.session_state:
    st.session_state.n = 3

conn = st.connection("gsheets", type=GSheetsConnection)
df_origin = conn.read(worksheet="설문지 응답 시트1", usecols=[0,1,2])

def click_button():
    st.session_state.n -= 1


st.title('Punch Gacha Prototype')
num = st.number_input('점수입력', 0, 999)

df_diff = df_origin.copy()
df_diff['편차'] = df_diff['몇점이 나올까요?'] - num

df_result = df_diff[df_diff['편차'] > -1]
df_result = df_result.sort_values(by=['편차', '타임스탬프'], ascending=[True, True])
df_result.columns = ['제출일시', '이메일', '점수', '편차']
n = st.session_state.n

st.dataframe(df_result)