import streamlit as st

# 🎨 페이지 설정
st.set_page_config(
    page_title="✨ MBTI 진로 추천 🌟",
    page_icon="💼",
    layout="centered"
)

# 💖 타이틀
st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b6e;'>
    🌟 MBTI 기반 직업 추천 💼✨
    </h1>
    <h4 style='text-align: center;'>
    🔮 나의 성격에 딱 맞는 직업을 찾아보세요! 🎯
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")

# 🎯 MBTI 선택
mbti = st.selectbox(
    "👉 당신의 MBTI를 선택하세요 🎭",
    [
        "INTJ", "INTP", "ENTJ", "ENTP",
        "INFJ", "INFP", "ENFJ", "ENFP",
        "ISTJ", "ISFJ", "ESTJ", "ESFJ",
        "ISTP", "ISFP", "ESTP", "ESFP"
    ]
)

# 💡 직업 데이터
career_dict = {
    "INTJ": ["🧠 데이터 과학자", "📊 전략 컨설턴트", "🔬 연구원"],
    "INTP": ["💻 개발자", "🧬 과학자", "📐 설계 엔지니어"],
    "ENTJ": ["👔 CEO", "📈 경영 컨설턴트", "💼 프로젝트 매니저"],
    "ENTP": ["🚀 창업가", "🎤 마케팅 전문가", "📢 광고 기획자"],
    "INFJ": ["🧑‍⚕️ 상담사", "📚 작가", "🌿 심리학자"],
    "INFP": ["🎨 예술가", "📖 작가", "🌈 디자이너"],
    "ENFJ": ["👩‍🏫 교사", "🤝 조직 리더", "🗣️ 강사"],
    "ENFP": ["🎭 배우", "📱 콘텐츠 크리에이터", "📣 마케터"],
    "ISTJ": ["📋 공무원", "💰 회계사", "📊 관리자"],
    "ISFJ": ["🏥 간호사", "👩‍🏫 교사", "🛎️ 서비스 관리자"],
    "ESTJ": ["📊 관리자", "🏢 경영 관리자", "📈 관리자"],
    "ESFJ": ["🎉 이벤트 플래너", "🧑‍💼 HR 전문가", "🤝 코디네이터"],
    "ISTP": ["🔧 엔지니어", "🚗 정비사", "🛠️ 기술 전문가"],
    "ISFP": ["🎨 디자이너", "📸 사진작가", "🎶 음악가"],
    "ESTP": ["🏎️ 스포츠 선수", "💼 영업 전문가", "🚓 경찰"],
    "ESFP": ["🎤 가수", "💃 댄서", "🎬 배우"]
}

# 🌟 버튼
if st.button("✨ 추천 결과 보기 💫"):
    
    st.markdown(
        f"""
        <h2 style='text-align:center; color:#6a5acd;'>
        🎉 {mbti}에게 추천하는 직업 🎉
        </h2>
        """,
        unsafe_allow_html=True
    )

    careers = career_dict[mbti]

    for job in careers:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(90deg, #ffdde1, #ee9ca7);
                padding: 15px;
                border-radius: 15px;
                margin: 10px 0;
                text-align: center;
                font-size: 20px;
                font-weight: bold;
            ">
            {job} 💖
            </div>
            """,
            unsafe_allow_html=True
        )

    st.success("✅ 당신의 성향에 딱 맞는 직업이에요! 🌟")

# 🎈 하단 꾸미기
st.write("")
st.markdown(
    """
    <hr>
    <h4 style='text-align:center; color:gray;'>
    💡 진로는 정답이 없어요! 자신에게 맞는 길을 찾아보세요 🌈✨
    </h4>
    """,
    unsafe_allow_html=True
)
``
