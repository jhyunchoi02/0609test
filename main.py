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
    "INFJ": ["📚 작가", "🌿 심리학자", "🧑‍🏫 상담사"],
    "INFP": ["🎨 디자이너", "🎶 음악가", "📖 소설가"],
    "ENFJ": ["👩‍🏫 교사", "🤝 리더", "🎙️ 강연가"],
    "ENFP": ["🎬 크리에이터", "📱 유튜버", "🎭 배우"],
    "ISTJ": ["📋 공무원", "💰 회계사", "🏢 관리자"],
    "ISFJ": ["🏥 간호사", "💖 사회복지사", "👩‍🏫 교사"],
    "ESTJ": ["📊 관리자", "⚖️ 판사", "🏛️ 공공기관 리더"],
    "ESFJ": ["🎉 이벤트 플래너", "🧑‍💼 인사담당자", "🤝 코디네이터"],
    "ISTP": ["🔧 엔지니어", "🚗 정비사", "🛠️ 기술전문가"],
    "ISFP": ["📸 사진작가", "🎨 화가", "🎼 작곡가"],
    "ESTP": ["🏎️ 스포츠선수", "🚓 경찰", "💼 영업전문가"],
    "ESFP": ["🎤 가수", "💃 댄서", "🎬 배우"]
}

# ✨ 버튼
if st.button("💖 직업 추천 받기 ✨"):

    st.balloons()

    st.markdown(
        f"""
        <h2 style='text-align:center; color:#6a5acd;'>
        🎉 {mbti} 추천 직업 🎉
        </h2>
        """,
        unsafe_allow_html=True
    )

    careers = career_dict[mbti]

    for job in careers:
        st.markdown(
            f"<div class='card'>{job} 🌟</div>",
            unsafe_allow_html=True
        )

    st.success("✅ 당신에게 잘 어울리는 직업이에요 💖")

# 🌈 하단 문구
st.markdown("""
<hr>
<h4 style='text-align:center; color:gray;'>
🚀 여러분의 꿈을 응원합니다 🌈✨
</h4>
""", unsafe_allow_html=True)
