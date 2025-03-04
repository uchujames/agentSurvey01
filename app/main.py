import os
import streamlit as st

st.title("AI Agent Survey")
st.header(":mailbox: Get in touch with me!")

# Store contact form in string (formsubmit.co) !!!SENDING TO MY EMAIL!!!
contact_form = """
    <form action="https://formsubmit.co/e9e77ea7a97a06e812eb0269699199b4" method="POST">
        <input type="hidden" name="_subject" value="AI Agent Survey">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder ="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
"""

#Alternative thank you page (age above, after page is built...)
# <input type="hidden" name="_next" value="https://yourdomain.co/thanks.html">

# Inject HMTL code into Streamlit app, using a markdown field
st.markdown(contact_form, unsafe_allow_html=True)


############################################
# LOAD CSS FILE USING ABSOLUTE PATH
############################################ 

# Define function to load CSS file using absolute path
def load_css(file_name):
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Create an absolute path to the CSS file
    css_path = os.path.join(script_dir, file_name)
    
    with open(css_path, "r") as f:
        css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Call the function to apply the CSS
try:
    load_css("styles.css")
except FileNotFoundError as e:
    st.error(f"Could not load CSS: {e}")
    # You can add a fallback here if needed