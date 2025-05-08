import streamlit as st

# --- Simple Drone Design Assisting Bot ---
st.title("🚀 Drone Design Assisting Bot")

st.write("""
Welcome! I can help you with basic drone design suggestions. 
Just input your requirements, and I’ll recommend components.
""")

# User Inputs
mission_type = st.selectbox("Select Mission Type", ["Racing", "Aerial Photography", "Payload Delivery", "Survey/Mapping"])
payload_weight = st.number_input("Payload Weight (grams)", min_value=0)
flight_time = st.number_input("Desired Flight Time (minutes)", min_value=1)

if st.button("Get Recommendations"):
    # Simple logic (placeholder)
    if mission_type == "Racing":
        st.success("✅ Recommended: Lightweight carbon fiber frame, 2306 2400KV motors, 5-inch propellers, 4S LiPo battery (1500mAh)")
    elif mission_type == "Aerial Photography":
        st.success("✅ Recommended: 450mm frame, 2212 920KV motors, 10-inch propellers, 3S or 4S LiPo (5200mAh), gimbal for camera")
    elif mission_type == "Payload Delivery":
        if payload_weight > 1000:
            st.success("✅ Recommended: Heavy-lift frame, 3510 or larger motors, 15-inch props, 6S LiPo (10000mAh), strong ESCs")
        else:
            st.success("✅ Recommended: Medium-lift quad, 2814 700KV motors, 12-inch props, 4S or 6S battery")
    elif mission_type == "Survey/Mapping":
        st.success("✅ Recommended: Fixed-wing airframe, efficient motor, 10-12 inch props, long-range 4S or 6S battery")

    # Basic flight time warning
    if flight_time > 30:
        st.warning("⚠ High flight time! Consider using larger batteries or fixed-wing designs for endurance.")

st.write("\n💡 Want a more advanced version? Let me know!")
