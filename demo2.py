import streamlit as st

st.set_page_config(page_title="Sidebar Icon Demo", page_icon="🧪", layout="centered")

# --- PNG logo at the top ---
# Place icon.png next to this file
st.sidebar.image("pizza-pie.png", width=100)
st.sidebar.markdown("**:rainbow[P.I.E.S]**")
st.sidebar.markdown("**Patient Information Entry System**")
st.sidebar.markdown("---")

# --- Your existing sidebar widgets ---
contact_method = st.sidebar.selectbox(
    "Pick a Drug to Show",
    ("Olaparib", "Pembrolizumab", "Osimertinib")
)

with st.sidebar:
    shipping_method = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    st.page_link("http://www.google.com", label="Dashboard", icon=":material/dashboard:")
    st.page_link("http://www.google.com", label="Patients", icon=":material/patient_list:")
    st.page_link("http://www.google.com", label="Samples", icon=":material/labs:")

if contact_method == "Olaparib":
    drug_content = "Olaparib (marketed as Lynparza) is an oral PARP inhibitor used to treat BRCA-mutated or HRD-positive cancers, including advanced ovarian, breast, pancreatic, and prostate cancers."
if contact_method == "Pembrolizumab":
    drug_content = "Pembrolizumab (brand name Keytruda) is a humanized monoclonal antibody, specifically an immune checkpoint inhibitor, used to treat various cancers by blocking the PD-1 protein on T-cells, which allows the immune system to recognize and attack cancer cells."
if contact_method == "Osimertinib":
    drug_content = "Osimertinib (Tagrisso) is a third-generation, oral targeted tyrosine kinase inhibitor (TKI) used to treat EGFR-mutated (exon 19 deletion/L858R or T790M) non-small cell lung cancer (NSCLC)."

st.title("Circulogene - Drug Information")
st.write(f"**Drug Chosen:** {contact_method}")
st.write(f"**Shipping:** {shipping_method}")
st.write(f"**Amy Content:** {drug_content}")
st.write(f"**:rainbow[Amy was here]**")

