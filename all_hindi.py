import streamlit as st
import smtplib
from email.message import EmailMessage

# Global sender credentials (सभी पृष्ठों के लिए)
SENDER_EMAIL = "tensortitans2612@gmail.com"
SENDER_PASSWORD = "hjcy lblh gwhv jmzk"

# App Title & Layout
st.set_page_config(page_title="सेफरूट सिस्टम", layout="wide")

# Sidebar Navigation (Dropdown on Right)
st.sidebar.title("🍃 केयरवॉल्ट SOS हब")
page = st.sidebar.selectbox("एक विकल्प चुनें", ["📄 यात्रा विवरण जोड़ें", "📍 स्थान का पता लगाएं", "🚨 आपातकालीन SOS प्रणाली"])

# ------------------------ यात्रा विवरण जोड़ें (Add Travel Details) Page ------------------------
if page == "📄 यात्रा विवरण जोड़ें":
    st.title("🚖 सेफरूट आपातकालीन रिपोर्टिंग प्रणाली")

    # हार्डकोडेड रिसीवर ईमेल (Editable)
    default_receivers = "siddhantpatil1543@gmail.com, siddhantpatil1540@gmail.com, maitreyeeb2004@gmail.com"
    receiver_emails = st.text_area("📥 रिसीवर ईमेल दर्ज करें (संपादन योग्य)", default_receivers)

    # वाहन और ड्राइवर विवरण
    vehicle_number = st.text_input("🚗 वाहन संख्या", placeholder="उदाहरण के लिए, MH12AB1234 दर्ज करें")
    vehicle_type = st.selectbox("🚘 वाहन प्रकार", ["कार", "बाइक", "ऑटो", "अन्य"])
    vehicle_color = st.text_input("🎨 वाहन का रंग", placeholder="उदाहरण: सफेद, काला, लाल")
    driver_name = st.text_input("🧑‍✈️ ड्राइवर का नाम (Uber/Ola)", placeholder="ड्राइवर का नाम दर्ज करें")
    location = st.text_area("📍 स्थान विवरण", placeholder="अपना वर्तमान स्थान या Google Maps लिंक दर्ज करें")
    message = st.text_area("📝 अतिरिक्त संदेश (वैकल्पिक)", placeholder="अपनी आपातकालीन स्थिति का वर्णन करें")

    # वाहन/ड्राइवर की छवि अपलोड करें (वैकल्पिक)
    uploaded_file = st.file_uploader("📷 वाहन/ड्राइवर की छवि अपलोड करें (वैकल्पिक)", type=["png", "jpg", "jpeg"])

    # ईमेल भेजने का बटन
    if st.button("🚀 आपातकालीन रिपोर्ट भेजें"):
        if receiver_emails and vehicle_number and vehicle_color and driver_name and location:
            email_list = [email.strip() for email in receiver_emails.split(",")]

            # ईमेल सामग्री का निर्माण
            email_body = f"""
            🚨 *सेफरूट सिस्टम से आपातकालीन सूचना* 🚨
            
            📌 *वाहन विवरण:*
            - वाहन संख्या: {vehicle_number}
            - वाहन प्रकार: {vehicle_type}
            - वाहन का रंग: {vehicle_color}
            
            👤 *ड्राइवर विवरण:*
            - ड्राइवर का नाम: {driver_name}
            
            📍 *स्थान:*
            {location}
            
            📝 *अतिरिक्त संदेश:*
            {message if message else "कोई अतिरिक्त जानकारी उपलब्ध नहीं है।"}
            """

            # ईमेल बनाएं
            msg = EmailMessage()
            msg["From"] = SENDER_EMAIL
            msg["To"] = ", ".join(email_list)
            msg["Subject"] = "🚨 सेफरूट आपातकालीन सूचना"
            msg.set_content(email_body)

            # यदि कोई छवि अपलोड की गई हो तो उसे जोड़ें
            if uploaded_file is not None:
                file_data = uploaded_file.read()
                file_name = uploaded_file.name
                msg.add_attachment(file_data, maintype="image", subtype=file_name.split(".")[-1], filename=file_name)

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
                server.quit()
                
                st.success(f"✅ आपातकालीन रिपोर्ट सफलतापूर्वक भेज दी गई है: {', '.join(email_list)}")
            except Exception as e:
                st.error(f"❌ ईमेल भेजने में विफल: {e}")
        else:
            st.warning("⚠️ कृपया भेजने से पहले सभी आवश्यक फ़ील्ड भरें।")

# ------------------------ स्थान का पता लगाएं (Track Location) Page ------------------------
elif page == "📍 स्थान का पता लगाएं":
    st.title("📍 प्रियजन का स्थान पता लगाएं")

    user_email = st.text_input("📧 आपका ईमेल", placeholder="अपना ईमेल दर्ज करें")
    user_password = st.text_input("🔑 आपका ईमेल पासवर्ड", type="password", placeholder="अपना पासवर्ड दर्ज करें")

    # स्थान पता लगाने का बटन (लिंक पर रीडायरेक्ट करता है)
    if st.button("🚀 प्रियजन का स्थान पता लगाएं"):
        st.markdown("[🔗 यहां क्लिक करें स्थान पता लगाने के लिए](https://1543siddhant.github.io/Map-Live-Tracking/)", unsafe_allow_html=True)

# ------------------------ आपातकालीन SOS प्रणाली (Emergency SOS System) Page ------------------------
elif page == "🚨 आपातकालीन SOS प्रणाली":
    st.title("🚨 आपातकालीन SOS प्रणाली")
    st.markdown("### ⚠️ **तत्काल सहायता चाहिए?** अपना स्थान और विवरण के साथ आपातकालीन ईमेल भेजें।")

    # डिफ़ॉल्ट रिसीवर ईमेल
    DEFAULT_RECEIVERS = [
        "siddhantpatil1543@gmail.com",
        "siddhantpatil1540@gmail.com"
    ]

    # डिफ़ॉल्ट ईमेल विषय और संदेश
    DEFAULT_SUBJECT = "🚨 तत्काल: आपातकालीन सहायता आवश्यक!"
    DEFAULT_MESSAGE = "मैं एक आपात स्थिति में हूँ और तुरंत सहायता की आवश्यकता है! कृपया तुरंत मदद करें।"

    # रिसीवर ईमेल इनपुट (Editable)
    receiver_emails = st.text_area("📥 रिसीवर ईमेल (कॉमा द्वारा अलग)", ", ".join(DEFAULT_RECEIVERS))

    # विषय (निश्चित, संपादन योग्य नहीं)
    st.text_input("📌 विषय", DEFAULT_SUBJECT, disabled=True)

    # संदेश (Editable)
    message = st.text_area("📝 संदेश", DEFAULT_MESSAGE)

    # छवि अपलोड करें (वैकल्पिक)
    uploaded_file = st.file_uploader("📷 छवि अपलोड करें (वैकल्पिक)", type=["png", "jpg", "jpeg"])

    # आपातकालीन कॉल और स्थान साझा करना
    st.markdown("📞 **क्या आपको आपातकालीन कॉल करनी है?**")
    st.markdown("[📲 आपातकालीन सेवाओं को कॉल करें (भारत)](tel:112)")

    st.markdown("📍 **तुरंत अपना स्थान साझा करें:**")
    if st.button("📡 लाइव स्थान साझा करें"):
        st.markdown("[🔗 यहां क्लिक करें अपना स्थान साझा करने के लिए](https://1543siddhant.github.io/Map-Live-Tracking/)", unsafe_allow_html=True)

    # ईमेल भेजने का बटन
    if st.button("🚀 आपातकालीन ईमेल भेजें"):
        if receiver_emails and message:
            email_list = [email.strip() for email in receiver_emails.split(",")]
            
            # ईमेल बनाएं
            msg = EmailMessage()
            msg["From"] = SENDER_EMAIL
            msg["To"] = ", ".join(email_list)
            msg["Subject"] = DEFAULT_SUBJECT
            msg.set_content(message)

            # यदि कोई छवि अपलोड की गई हो तो उसे जोड़ें
            if uploaded_file is not None:
                file_data = uploaded_file.read()
                file_name = uploaded_file.name
                msg.add_attachment(file_data, maintype="image", subtype=file_name.split(".")[-1], filename=file_name)

            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.send_message(msg)
                server.quit()
                
                st.success(f"✅ आपातकालीन ईमेल सफलतापूर्वक भेज दी गई है: {', '.join(email_list)}")
            except Exception as e:
                st.error(f"❌ ईमेल भेजने में विफल: {e}")
        else:
            st.warning("⚠️ कृपया सुनिश्चित करें कि भेजने से पहले सभी फ़ील्ड भरे गए हैं।")
