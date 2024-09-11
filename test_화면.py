import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 한글 폰트 설정 (폰트 경로는 시스템에 따라 다를 수 있음)
font_path = 'C:/Windows/Fonts/맑은 고딕'
font_prop = fm.FontProperties(fname=font_path)

plt.rcParams['font.family'] = font_prop.get_name()

# 가상의 대량 RPA 작업 데이터 생성
np.random.seed(0)
tasks = [f'작업 {chr(65 + i)}' for i in range(50)]
statuses = np.random.choice(['완료', '실패', '진행 중'], 50)
processed_items = np.random.randint(50, 200, size=50)
processing_times = np.random.randint(5, 30, size=50)

data = {
    '작업': tasks,
    '상태': statuses,
    '처리된 항목 수': processed_items,
    '처리 시간 (분)': processing_times
}

df = pd.DataFrame(data)

# Streamlit 제목 및 데이터프레임 표시
st.title("RPA 시스템 대시보드")

# 전체 데이터 표시
st.header("전체 작업 데이터")
st.dataframe(df)

# 상태별 처리된 항목 수 막대 그래프
st.header("상태별 처리된 항목 수")
status_summary = df.groupby('상태')['처리된 항목 수'].sum().reset_index()

fig, ax = plt.subplots()
ax.bar(status_summary['상태'], status_summary['처리된 항목 수'], color='skyblue')
ax.set_xlabel('상태', fontproperties=font_prop)
ax.set_ylabel('처리된 항목 수', fontproperties=font_prop)
ax.set_title('상태별 처리된 항목 수', fontproperties=font_prop)
st.pyplot(fig)

# 작업별 처리 시간 히스토그램
st.header("작업별 처리 시간 분포")
fig, ax = plt.subplots()
ax.hist(df['처리 시간 (분)'], bins=10, color='lightgreen', edgecolor='black')
ax.set_xlabel('처리 시간 (분)', fontproperties=font_prop)
ax.set_ylabel('빈도수', fontproperties=font_prop)
ax.set_title('작업별 처리 시간 분포', fontproperties=font_prop)
st.pyplot(fig)

# 상태별 작업 현황 필터링
st.header("상태별 작업 현황")
status_filter = st.selectbox("상태 선택", ["모두"] + list(df['상태'].unique()))
if status_filter != "모두":
    filtered_df = df[df['상태'] == status_filter]
else:
    filtered_df = df
st.dataframe(filtered_df)
