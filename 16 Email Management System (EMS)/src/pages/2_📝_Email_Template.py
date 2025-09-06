import streamlit as st

from src.utils.db import DatabaseManager

# Initialize the DatabaseManager
db = DatabaseManager()


def main():
    st.title("📝 Email Templates")

    # Add new template
    st.header("Add New Template")
    with st.form("add_template_form"):
        template_name = st.text_input("Template Name")
        template_body = st.text_area("Template Body", height=200)
        submit_button = st.form_submit_button("Add Template")

        if submit_button:
            if template_name and template_body:
                template_id = db.add_template(template_name, template_body)
                st.success(
                    f"Template added successfully with ID: {template_id}")
            else:
                st.error("Please fill in both the template name and body")

    # View and delete existing templates
    st.header("Existing Templates")
    templates = db.get_all_templates()

    if not templates:
        st.info("No templates found. Add a new template above.")
    else:
        for template in templates:
            with st.expander(f"Template: {template['name']}"):
                st.write("**Template Body:**")
                st.text_area(
                    "", value=template["body"], height=150, key=f"body_{template_id}")

                if st.button("Delete", key=f"delete_{template.doc_id}"):
                    db.delete_template(template.doc_id)
                    st.success("Template deleted successfully")
                    st.experimental_rerun()


if __name__ == "__main__":
    main()
