import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from show_about_page import show_about_page





page = st.sidebar.selectbox(
    "Explore Or Predict", ("Predict", "Explore", "About"))

if page == "Predict":
    show_predict_page()
elif page == "Explore":
    show_explore_page()
else:
    # Handle the case when neither "Predict" nor "Explore" is selected
    st.title("Welcome to the App")
    st.write("Please select an option from the sidebar.")
    show_about_page()

footer_html = """
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #000;
    padding: 1px 0;
    text-align: center;
    font-size: 12px;
    color: #333;
}
</style>
<div class="footer">
    <p>© 2023 DMW</p>
</div>
</div>
"""

# Add the footer to the Streamlit app using st.markdown
st.markdown(footer_html, unsafe_allow_html=True)
