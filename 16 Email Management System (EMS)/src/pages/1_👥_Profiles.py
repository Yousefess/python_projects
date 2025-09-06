import streamlit as st

from src.utils.db import DatabaseManager

# Initialize the DatabaseManager
db = DatabaseManager()


def main():
    st.title("👥 Profiles")

    # Add new profile
    st.header("Add New Profile")
    with st.form("add_profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with col2:
            title = st.text_input("Title")
            profession = st.text_input("Profession")
        submit_button = st.form_submit_button("Add Profile")

    if submit_button:
        if name and email and title and profession:
            profile_id = db.add_profile(name, email, title, profession)
            st.success(f"Profile added successfully with ID: {profile_id}")
        else:
            st.error("Please fill in all fields")

    # View and delete existing profiles
    st.header("Existing Profiles")
    profiles = db.get_all_profiles()

    if not profiles:
        st.info("No profiles found. Add a new profile above.")
    else:
        for profile in profiles:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Name:** {profile['name']}")
                st.write(f"**Email:** {profile['email']}")
                st.write(f"**Title:** {profile['title']}")
                st.write(f"**Profession:** {profile['profession']}")
            with col2:
                if st.button("Delete", key=f"delete_{profile.doc_id}"):
                    db.delete_profile(profile.doc_id)
                    st.success("Profile deleted successfully")
                    st.experimental_rerun()
            st.divider()


if __name__ == "__main__":
    main()
