import streamlit as st


def show_about_page():

    # HTML content with CSS styles
    about_content = """
    <div style="background-color:rgb(146, 108, 5); color: #fff; padding: 20px; border-radius: 5px; text-align: center;">
        <h2>About This App</h2>
        <p>This app is designed to predict software developer salaries based on various factors.</p>
        <p>It's created by <strong>DMW</strong> and is meant for educational purposes.</p>
        <p>Feel free to explore the salary predictions and data visualizations in the "Explore" section.</p>
    </div>
    """

    # Display the about_content using st.markdown
    st.markdown(about_content, unsafe_allow_html=True)
