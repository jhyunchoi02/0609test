import streamlit as st

# 🌈 페이지 설정
st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="💼",
    layout="centered"
)

# 🎨 스타일 꾸미기
st.markdown("""
<style>
body {
    background-color: #fdf6ff;
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
    color: #666666;
}

.card {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    padding: 20px;
    border-radius: 20px;
    margin: 15px 0;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    color: white;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# 🌟 제목
st.markdown(
    "<div class='big-title'>🌈 MBTI 진로 추천 사이트 ✨</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>💖 나의 성격에 어울리는 직업 찾기 💼</div>",
    unsafe_allow_html=True
)

st.write("")

# 🎭 MBTI 선택
mbti = st.selectbox(
    "👉 MBTI를 선택하세요 🎯",
    [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)

# 💼 추천 직업 데이터
career_dict = {
    "INTJ": ["🧠 데이터 과학자", "🔬 연구원", "📊 전략가"],
    "INTP": ["💻 개발자", "🧪 과학자", "📐 엔지니어"],
    "ENTJ": ["👔 CEO", "📈 경영 컨설턴트", "🚀 사업가"],
    "ENTP": ["💡 창업가", "📢 광고기획자", "🎤 마케터"],
