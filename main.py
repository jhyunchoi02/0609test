import streamlit as st

# 🌈 페이지 설정
st.set_page_config(
    page_title="🌟 MBTI 진로 추천",
    page_icon="💼",
    layout="centered"
)

# 🎨 CSS 꾸미기
st.markdown("""
<style>
.main {
    background: linear-gradient(to bottom, #ffe0f0, #e0f7ff);
}

.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #ff4b91;
}

.sub-title {
    text-align: center;
    font-size: 22px;
    color: #555;
}

.card {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 20px;
    border-radius: 20px;
    margin-top: 15px;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    color: white;
    box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# 🌟 제목
st.markdown(
    "<div class='big-title'>✨ MBTI 진로 추천 사이트 💼🌈</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>🔮 나에게 어울리는 직업을 찾아보세요! 🎯</div>",
    unsafe_allow_html=True
)

st.write("")
st.write("")

# 🎭 MBTI 선택
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요 💖",
    [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)

# 💼 직업 추천 데이터
career_dict = {
