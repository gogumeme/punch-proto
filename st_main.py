import streamlit as st
import pandas as pd
import numpy as np
import gspread as gs

def get_gs_data():
    json_file_name = 'key.json'
    gc = gs.service_account(filename=json_file_name)

    sheet_key = '1Dsyp3RQ-lMAwywzktioVxsqjbvTy-OiFf-H7d4XLoYQ'
    doc = gc.open_by_key(sheet_key)
    worksheet = doc.worksheet('설문지 응답 시트1')
    record_list = worksheet.get_all_records()
    return record_list

if 'n' not in st.session_state:
    st.session_state.n = 3

gs_records = get_gs_data()
df_origin = pd.DataFrame(gs_records)

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