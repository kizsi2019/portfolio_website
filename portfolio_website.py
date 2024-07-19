import streamlit as st
import google.generativeai as genai


#api_key = st.secrets["GOOGLE_API_KEY"]
api_key ="AIzaSyADGtGn21QQclvyBzcEeVKzbVnjM1ZGnTs"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Zsigmond Kiss")

with col2:
    st.image("images/zsigmond.jpg")

st.title(" ")

persona = """
        You are Zsigmond AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Zsigmond: 

        Zsigmond Kiss Zsigmond Kiss is an innovator and programming instructor in Hungary. 
        He has his own family business: KissFilm-Studio Ltd. 
        He is a member of the Artificial Intelligence Coalition, the Edtech Coalition 
        and the Drone Coalition in Hungary. 
        He develops courses in Artificial Intelligence and drone programming. 
        His role model is Murtaza Hassan.
        His wife is a consultant: Plan B Immigrations is a Hungarian Immigration Law firm 
        that offers the following services to non-EU citizens:
        1. "Golden Visa": Hungarian Guest Investor Permanent Residence Permit
        2. Work permits
        3. Student Visas

        Zsigmond's Youtube Channel: https://www.youtube.com/c/KissFilmSt%C3%BAdi%C3%B3/featured
        Zsigmond's Email: zsigmond.kiss@gmail.com 
        Zsigmond's Facebook: https://www.facebook.com/profile.php?id=100063712953645
        Zsigmond's wife immigrations Facebook: https://www.facebook.com/profile.php?id=61562597890053
        """
        

st.title("Zsigmond's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")
st.subheader("Youtube Channel")
st.page_link("https://www.youtube.com/c/KissFilmSt%C3%BAdi%C3%B3/featured",
                 label="My family business is the youtube channel of KissFilm Studio Ltd.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Our Facebook Channels")

    st.page_link("https://www.facebook.com/profile.php?id=100063712953645",
                 label="Learning programming playfully facebook page")


with col2:
    st.title(" ")
    st.page_link("https://www.facebook.com/profile.php?id=61562597890053", label="Plan B Immigrations - New Life in Europe ")






st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 95)
st.slider("Robotics", 0, 100, 70)

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("zsigmond.kiss@gmail.com")
