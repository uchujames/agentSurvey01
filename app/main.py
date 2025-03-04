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


##############################
# Use Local CSS File
###############################

# Define function to load CSS file
def load_css(file_name):
    with open(file_name) as f:
        css = f.read()
        st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Call the function to apply the CSS
load_css("styles.css")
