import streamlit as st

st.set_page_config(page_title="Properties for Sale", page_icon="🏡", layout="wide")

st.title("🏡 Featured Properties for Sale")
st.write("Pumili ng property sa ibaba o gamitin ang sidebar sa kaliwa para makita ang kumpletong detalye.")

st.markdown("---")

# PROPERTY 1 CARD
col1, col2 = st.columns([1, 2])
with col1:
    st.image("facade.jpg", use_container_width=True) # Siguraduhing may facade.jpg ka
with col2:
    st.subheader("🏠 2-Storey Home in Bonifacio Village, QC")
    st.write("💰 **Price:** ₱25,000,000")
    st.write("📍 **Location:** Bonifacio Village, Brgy. Pasong Tamo, Quezon City")
    st.write("🛏️ 4 Bedrooms | 🛁 3 Baths | 📐 LA: 126 sqm | FA: 200 sqm")
    # Link papunta sa pahina ng Bonifacio Village
    st.page_link("pages/1_Bonifacio_Village.py", label="👉 Tingnan ang Kumpletong Detalye at Photos", icon="🔍")

st.markdown("---")

# PROPERTY 2 CARD (Halimbawa para sa susunod mong benta)
col3, col4 = st.columns([1, 2])
with col3:
    st.image("house2_facade.jpg", use_container_width=True) # Lagyan ng sample image
with col4:
    st.subheader("🏡 Modern Townhouse in Quezon City")
    st.write("💰 **Price:** ₱12,500,000")
    st.write("📍 **Location:** Tandang Sora, Quezon City")
    st.write("🛏️ 3 Bedrooms | 🛁 2 Baths | 📐 LA: 80 sqm | FA: 140 sqm")
    st.page_link("pages/2_Another_House.py", label="👉 Tingnan ang Kumpletong Detalye at Photos", icon="🔍")