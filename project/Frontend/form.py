# import streamlit as st
# t1,t2 = st.tabs(["Login","Register"])
# with t2:
#     st.title("Registration Form")
#     with st.form("Registration form"):
#         st.text_input("Name",placeholder="Enter your name")
#         st.text_input("Email",placeholder="Enter your email")
#         st.text_input("Password",placeholder="Enter your password",type="password")
#         st.text_input("Confirm Password",placeholder="Enter your confirm password",type="password")
#         st.selectbox("Role",["","Trainer","Student"])
#         st.form_submit_button("Register")
# with t1:
#     st.title("Login Form")
#     with st.form("Login form"):
#         st.text_input("Email",placeholder="Enter your email")
#         st.text_input("Password",placeholder="Enter your password",type="password")
#         st.selectbox("Role",[" ","Trainer","Student"])
#         st.form_submit_button("Login")

import streamlit as st

t1, t2 = st.tabs(["🔐 Login", "📝 Register"])

with t1:
    st.title("🔐 Login Form")
    with st.form("Login form"):
        st.text_input("📧 Email", placeholder="Enter your email")
        st.text_input(
            "🔑 Password", placeholder="Enter your password", type="password"
        )
        st.selectbox("🎭 Role", [" ", "👨‍🏫 Trainer", "🎓 Student"])
        st.form_submit_button("🚀 Login")

with t2:
    st.title("📝 Registration Form")
    with st.form("Registration form"):
        st.text_input("👤 Name", placeholder="Enter your name")
        st.text_input("📧 Email", placeholder="Enter your email")
        st.text_input(
            "🔑 Password", placeholder="Enter your password", type="password"
        )
        st.text_input(
            "🔒 Confirm Password",
            placeholder="Enter your confirm password",
            type="password",
        )
        st.selectbox("🎭 Role", ["", "👨‍🏫 Trainer", "🎓 Student"])
        st.form_submit_button("✨ Register")

