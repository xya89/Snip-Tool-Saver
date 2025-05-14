import streamlit as st 
from PIL import ImageGrab
import io
from datetime import datetime

st.title("📸 Screenshot Saver")
st.write("Take a screenshot using `Win + Shift + S`, then press the button below to paste and save.")

if st.button("📋 Paste from Clipboard"):
    try:
        img = ImageGrab.grabclipboard()
        if img:
            st.image(img, caption="Pasted Image", use_column_width=True)

            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            img_bytes = io.BytesIO()
            img.save(img_bytes, format="PNG")
            st.download_button(
                label="💾 Download PNG",
                data=img_bytes.getvalue(),
                file_name=filename,
                mime="image/png"
            )
        else:
            st.warning("No image found in clipboard. Try using `Win + Shift + S` again.")
    except Exception as e:
        st.error(f"Error grabbing image: {e}")
