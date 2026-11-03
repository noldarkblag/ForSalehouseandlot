import streamlit as st

# Page Configuration
st.set_page_config(page_title="Bonifacio Village QC - House for Sale", page_icon="🏠", layout="wide")

# Header Section
st.title("🏠 2-Storey Home in Bonifacio Village, Quezon City")
st.subheader("High-Elevation | 100% Flood-Free | Prime Location")

st.markdown("---")

# Main Content Layout: 2 Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Photo Gallery")
    st.info("💡 Pumili ng mga larawan mula sa iyong computer (kahit anong file name):")
    
    # File uploaders
    img1 = st.file_uploader("Upload Facade / Frontage Photo", type=["jpg", "jpeg", "png"], key="1")
    if img1:
        st.image(img1, caption="Exterior & Frontage (Corner Lot)", use_container_width=True)

    img2 = st.file_uploader("Upload Living Room Photo", type=["jpg", "jpeg", "png"], key="2")
    if img2:
        st.image(img2, caption="Spacious Living Room", use_container_width=True)

    img3 = st.file_uploader("Upload Patio Photo", type=["jpg", "jpeg", "png"], key="3")
    if img3:
        st.image(img3, caption="Relaxing Downstairs Patio", use_container_width=True)

with col2:
    st.header("✨ Property Overview")
    st.write("💰 **Asking Price:** ₱25,000,000")
    st.write("📍 **Location:** Brgy. Pasong Tamo, Quezon City")
    
    st.markdown("### 📋 Details & Features")
    st.markdown("""
    * **Lot Area:** 126 sqm | **Floor Area:** 200 sqm
    * **Bedrooms:** 4 Bedrooms
    * **Bathrooms:** 3 Full Baths + 1 Powder Room (Downstairs)
    * **Parking:** 2-Car Garage inside + 3 cars parking space in front
    * **Special Features:** Solid Wood Flooring upstairs, Family Area w/ Mini Library, Balcony, & Dirty Kitchen.
    * **Security & Amenities:** 24/7 Gated Security, Clubhouse, Basketball Court, Playground.
    """)

    st.markdown("### 📍 Nearby Places")
    st.markdown("""
    * 🎓 **Schools (10 mins):** UP Diliman, Ateneo, Miriam College
    * 🛍️ **Malls (15 mins):** SM North EDSA, TriNoma, Vertis North, Solaire North
    * 🏥 **Hospitals:** Philippine Heart Center, East Avenue Medical Center
    """)

st.markdown("---")

# Contact & Inquiry Section
st.header("📞 Interested in a Property Viewing?")
st.write("Call or Message us directly at **09524656801**")

with st.form("inquiry_form"):
    st.write("Or leave your details below:")
    name = st.text_input("Name")
    phone = st.text_input("Phone Number")
    message = st.text_area("Message / Preferred Viewing Date")
    submitted = st.form_submit_button("Send Inquiry")
    
    if submitted:
        st.success(f"Thank you, {name}! We will contact you at {phone} shortly.")