import streamlit as st
import os

# Page Configuration
st.set_page_config(
    page_title="Bonifacio Village QC - House for Sale", 
    page_icon="🏠", 
    layout="wide"
)

# --- HERO BANNER / FACADE SECTION ---
st.title("🏠 2-Storey Corner Lot Home for Sale")
st.subheader("Bonifacio Village, Quezon City | High-Elevation & 100% Flood-Free")

# Facade / Frontage Photo Display
facade_path = "facade.jpg"

if os.path.exists(facade_path):
    st.image(facade_path, caption="Facade & Frontage - Bonifacio Village, QC", use_container_width=True)
else:
    st.info("💡 **Frontage / Facade Photo:** I-upload ang larawan sa ibaba o maglagay ng 'facade.jpg' sa folder.")
    uploaded_facade = st.file_uploader("Upload Facade Photo", type=["jpg", "jpeg", "png"], key="facade_uploader")
    if uploaded_facade:
        st.image(uploaded_facade, caption="Facade & Frontage - Bonifacio Village, QC", use_container_width=True)

st.markdown("---")

# --- MAIN CONTENT SECTION ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Photo Gallery")
    
    # Helper function para sa karagdagang larawan
    def load_or_upload_image(file_name, label, key):
        if os.path.exists(file_name):
            st.image(file_name, caption=label, use_container_width=True)
        else:
            uploaded = st.file_uploader(f"Upload {label}", type=["jpg", "jpeg", "png"], key=key)
            if uploaded:
                st.image(uploaded, caption=label, use_container_width=True)

    load_or_upload_image("living_room.jpg", "Spacious Living Room", "img_living")
    load_or_upload_image("patio.jpg", "Relaxing Downstairs Patio", "img_patio")
    load_or_upload_image("library.jpg", "Family Area with Mini Library", "img_library")

with col2:
    st.header("✨ Property Overview")
    st.markdown("### 💰 **Asking Price:** ₱25,000,000")
    st.markdown("📍 **Location:** Bonifacio Village, Brgy. Pasong Tamo, Quezon City *(Access Road via Mira Nila along Congressional)*")
    
    st.markdown("---")
    st.markdown("### 📋 Property Features")
    st.markdown("""
    * ✅ **Lot Area:** 126 sqm
    * ✅ **Floor Area:** 200 sqm
    * ✅ **Layout:** 2-Storey Corner Lot
    * ✅ **Bedrooms:** 4 Bedrooms
    * ✅ **Bathrooms:** 3 Full Bathrooms + 1 Downstairs Powder Room
    * ✅ **Parking:** 2-Car Garage inside + space for 3 cars in front
    * ✅ **Highlights:** Solid Wood Flooring upstairs, Family Area w/ mini library, Balcony, & Dirty Kitchen.
    * ✅ **Security & Amenities:** 24/7 Gated Security, Clubhouse, Basketball Court, & Children's Playground.
    """)

    st.markdown("### 📍 Prime Location & Accessibility")
    st.markdown("""
    * 🎓 **Schools (Around 10 mins):** UP Diliman, Ateneo de Manila University, Miriam College
    * 🛍️ **Malls (Around 15 mins):** SM North EDSA, TriNoma, Vertis North, Solaire North
    * 🏥 **Hospitals:** Philippine Heart Center & East Avenue Medical Center
    """)

st.markdown("---")

# --- CONTACT & INQUIRY SECTION ---
st.header("📞 Schedule a Viewing / Inquire Now")
st.write("For direct inquiries, call or message: **09524656801**")
st.caption("📌 Serious buyers and real estate agents are welcome.")

with st.form("inquiry_form"):
    st.write("Or fill out the form below and we will get back to you:")
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number / Email")
    message = st.text_area("Message or Preferred Date of Viewing")
    submitted = st.form_submit_button("Submit Inquiry")
    
    if submitted:
        if name and phone:
            st.success(f"Salamat, {name}! Natanggap namin ang iyong inquiry. Tutawagan ka namin sa {phone} sa lalong madaling panahon.")
        else:
            st.error("Pakilagay ang iyong pangalan at phone number.")
