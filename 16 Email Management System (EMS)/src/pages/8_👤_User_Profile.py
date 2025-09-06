import streamlit as st

from src.utils.db import DatabaseManager

db = DatabaseManager()


def main():
    st.title("👤 User Profile")

    user_profile = db.get_user_profile()

    with st.form("user_profile_form"):
        name = st.text_input("Name", value=user_profile.get(
            'name', '') if user_profile else "")
        profession = st.text_input("Profession", value=user_profile.get(
            'profession', '') if user_profile else "")
        degree = st.text_input("Degree", value=user_profile.get(
            'degree', '') if user_profile else "")
        university = st.text_input("University", value=user_profile.get(
            'university', '') if user_profile else "")

        st.subheader("Social Media")
        col1, col2 = st.columns(2)
        with col1:
            linkedin = st.text_input("LinkedIn", value=user_profile.get(
                "social_media", {}).get("linkedin", "") if user_profile else "")
            twitter = st.text_input("Twitter", value=user_profile.get(
                "social_media", {}).get("twitter", "") if user_profile else "")
        with col2:
            github = st.text_input("GitHub", value=user_profile.get(
                "social_media", {}).get("github", "") if user_profile else "")
            linkedin = st.text_input("LinkedIn", value=user_profile.get(
                "social_media", {}).get("linkedin", "") if user_profile else "")

        email_signature = st.text_area("Email Signature", value=user_profile.get(
            "signature", "") if user_profile else "")


main()
