import streamlit as st
import time
import os
from google import genai
from automation import EnterpriseAutomationEngine
import voice_engine

st.set_page_config(page_title="MHZALY AI - Next-Gen System", layout="wide", page_icon="🤖")

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    .orb-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 170px;
    }
    .glow-sphere {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        background: radial-gradient(circle, #00f2fe 0%, #4facfe 60%, #000 100%);
        box-shadow: 0 0 40px #00f2fe;
    }
    .card-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 MHZALY - Next-Gen Multi-Agent System")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧠 System Overview")
    st.markdown("---")
    st.markdown("🟢 **Status:** Active & Online")
    st.markdown("📂 **Memory:** Connected")
    st.markdown("⚡ **AI Engine:** Gemini 2.5/1.5 Flash")
    st.code("Active Features:\n- WhatsApp Direct Calls & Messages\n- Google & YouTube Search\n- Teams & Email Controls\n- Screen Vision Analysis")

with col2:
    st.subheader("🌐 Core Orchestrator")
    st.markdown('<div class="orb-box"><div class="glow-sphere"></div></div>', unsafe_allow_html=True)
    st.caption("<center>SYSTEM ACTIVE & LISTENING</center>", unsafe_allow_html=True)

with col3:
    st.subheader("🗣️ Console & Voice")
    st.markdown("---")
    
    if st.button("🎤 Click to Speak"):
        with st.spinner("Listening..."):
            txt = voice_engine.listen_user()
            if txt:
                st.success(f"Recognized: {txt}")
                if "call" in txt.lower():
                    contact = txt.lower().split("call")[-1].replace("ko", "").replace("whatsapp", "").strip()
                    st.info(automation.whatsapp_action(contact, action_type="call"))
                elif "open" in txt.lower() or "kholo" in txt.lower():
                    target = txt.lower().replace("open", "").replace("kholo", "").strip()
                    st.info(automation.open_app_or_site(target))
                        
    user_cmd = st.text_input("Type Command:", placeholder="e.g. call noor fatimah, kholo chrome")
    if st.button("Execute") and user_cmd:
        if "call" in user_cmd.lower():
            contact = user_cmd.lower().split("call")[-1].replace("ko", "").replace("whatsapp", "").strip()
            st.success(automation.whatsapp_action(contact, action_type="call"))
        elif "open" in user_cmd.lower() or "kholo" in user_cmd.lower():
            target = user_cmd.lower().replace("open", "").replace("kholo", "").strip()
            st.success(automation.open_app_or_site(target))

st.markdown("---")
st.subheader("👥 Active Sub-Agents Workfloor")

a1, a2, a3, a4 = st.columns(4)

with a1:
    st.markdown('<div class="card-box"><h4>📞 WhatsApp Agent</h4><p>Status: <b style="color:#00f2fe;">Ready</b></p><small>Direct URI & Hotkey Calling</small></div>', unsafe_allow_html=True)
with a2:
    st.markdown('<div class="card-box"><h4>💻 Coding Agent</h4><p>Status: <b style="color:#00f2fe;">Ready</b></p><small>Python, C++, Web & Cyber Security</small></div>', unsafe_allow_html=True)
with a3:
    st.markdown('<div class="card-box"><h4>🌐 Web Agent</h4><p>Status: <b style="color:#00f2fe;">Ready</b></p><small>Google Search, YouTube & Twitter</small></div>', unsafe_allow_html=True)
with a4:
    st.markdown('<div class="card-box"><h4>👁️ Vision Agent</h4><p>Status: <b style="color:#00f2fe;">Ready</b></p><small>Analyzes Laptop Screen</small></div>', unsafe_allow_html=True)
