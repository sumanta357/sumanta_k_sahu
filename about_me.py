import streamlit as st


## searchbar visualization
st.set_page_config(
    page_title="MY Website",
    page_icon="👋",
)
#Title on page setup 
st.write("# MY Website! 👋")
st.sidebar.success("Select a demo above.")
st.markdown(
    """
   **About me**
"""
)
#defining tab
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=100)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=100)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=100)
