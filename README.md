google sheets에 연동된 google forms 응답을 google cloud platform api와 python gspread library를 통해 수집
수집된 응답을 pandas dataframe을 통해 편차를 구하고, 편차와 응답 제출 시간을 기준으로 정렬하여 순위를 구함
streamlit micro web app으로 deploy