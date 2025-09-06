import streamlit as st

st.set_page_config(page_title="Email Management System")

st.image("https://cdn.intheloop.io/blog/wp-content/uploads/2019/03/loop-email-shared-inbox-feature.jpg")
st.title("📧 Email Management System")

# Add dashboard content here ()
st.write("Here you'll see an overview of your email activities ...")

# Placeholder for recent emails
st.subheader("Recent Emails")
st.table({
    "Recipient": ["John Doe", "Jane Smith"],
    "Subject": ["Meeting tomorrow", "Project update"],
    "Date": ["2023-05-01", "2024-04-30"]
})

# Placeholder for statistics
st.subheader("Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Emails Sent", "50")
col2.metric("Open Rate", "75%")
col3.metric("Response Rate", "40%")
