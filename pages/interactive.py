import streamlit as st

st.title("🤯 상호작용을 위한 앱 만들기")

# st.write("https://youtu.be/V96zzrlBxnk?list=PLSTJuHaq4hGVL0elWMRIuepBmKHq_QCpg")
st.link_button("유튜브 영상 바로가기", "https://youtu.be/V96zzrlBxnk?list=PLSTJuHaq4hGVL0elWMRIuepBmKHq_QCpg")

col1, col2 = st.columns(2)
with col1:
    st.image("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif", width = 500)
with col2:
    st.success("이미지에요!")
    st.info("이 캐릭터의 이름은 무엇일까요?")
    answer = st.text_input("이 캐릭터의 이름을 써주세요.")
    if answer =="쪼랩":
        st.success("맞았습니다!!!")
    else:
        st.warning("다시 생각해보세요!")

st.latex("2x^2-x+1")

tab1, tab2 = st.tabs(['봄', '여름'])
tab1.success("봄이에요!")
tab2.info("여름이에요....")

