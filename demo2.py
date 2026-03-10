import streamlit as st

st.set_page_config(page_title="Sidebar Icon Demo", page_icon="🧪", layout="centered")

# --- PNG logo at the top ---
# Place icon.png next to this file
st.sidebar.image("pizza-pie.png", width=100)
st.sidebar.markdown("**PIES - Patient Information Entry System**")
st.sidebar.markdown("---")

# --- Your existing sidebar widgets ---
contact_method = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    shipping_method = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    st.page_link("http://www.google.com", label="Google", icon="🌎")
    st.page_link("http://www.google.com", label="Dashboard", icon=":material/dashboard:")
    st.page_link("http://www.google.com", label="Patients", icon=":material/dashboard:")
    st.page_link("http://www.google.com", label="Samples", icon=":material/patient_list:")

st.title("Streamlit + Sidebar Logo")
st.write(f"**Contact via:** {contact_method}")
st.write(f"**Shipping:** {shipping_method}")