import streamlit as st
import time
import os
from google import genai
import automation
import voice_engine

# Page Config (Dark Mode & Wide Layout)
st.set_page_config(page_title="MHZALY AI - Multi-Agent Dashboard", layout="wide", page_icon="🤖")

# Custom CSS for Stonic AI Sci-Fi Styling
st.markdown("""
<style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stApp { background-color: #0a0c10; }
    .orb-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 180px;
    }
    .glowing-orb {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        background: radial-gradient(circle, #00f2fe 0%, #4facfe 50%, #000 100%);
        box-shadow: 0 0 35px #00f2fe;
        animation: pulse 2s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 20px #00f2fe; }
        100% { transform: scale(1.08); box-shadow: 0 0 45px #00f2fe; }
    }
    .agent-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        min-height: 140px;
    }
    .status-badge {
        color: #00f2fe;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 MHZALY - Multi-Agent AI System")

# Top Layout: 3 Columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🧠 System State")
    st.markdown("---")
    st.markdown("🟢 **Status:** Active & Online")
    st.markdown("📂 **Memory:** Connected")
    st.markdown("⚡ **Core Model:** Gemini 2.5/1.5 Flash")
    st.markdown("🛠️ **Active Skills:**")
    st.code("- WhatsApp Calls & Messages\n- Google Search & YouTube\n- Screen Vision\n- Auto Tweet\n- Teams Controls")

with col2:
    st.subheader("🌐 MHZALY Orchestrator")
    # Animated Glowing Orb Visualizer
    st.markdown('<div class="orb-container"><div class="glowing-orb"></div></div>', unsafe_allow_html=True)
    st.caption("<center>MHZALY BRAIN ACTIVE</center>", unsafe_allow_html=True)

with col3:
    st.subheader("🗣️ Voice & Command Console")
    st.markdown("---")
    
    # Live Voice Button on Web Dashboard
    if st.button("🎤 Click to Speak Voice Command"):
        with st.spinner("MHZALY Listening via Microphone..."):
            recognized_text = voice_engine.listen_user()
            if recognized_text:
                st.success(f"Voice Recognized: {recognized_text}")
                if "call" in recognized_text.lower():
                    contact = recognized_text.lower().split("call")[-1].replace("ko", "").replace("whatsapp", "").strip()
                    res = automation.whatsapp_action(contact, action_type="call")
                    st.info(res)
                elif "open" in recognized_text.lower() or "kholo" in recognized_text.lower():
                    target = recognized_text.lower().replace("open", "").replace("kholo", "").strip()
                    res = automation.open_app_or_site(target)
                    st.info(res)
                        
    user_query = st.text_input("Or Type Command / Query:", placeholder="e.g. call noor fatimah, kholo chrome")
    
    if st.button("🚀 Execute Text Command") and user_query:
        st.info(f"Command: {user_query}")
        with st.spinner("MHZALY Multi-Agents Processing..."):
            if "call" in user_query.lower():
                contact = user_query.lower().split("call")[-1].replace("ko", "").replace("whatsapp", "").strip()
                res = automation.whatsapp_action(contact, action_type="call")
                st.success(res)
            elif "open" in user_query.lower() or "kholo" in user_query.lower():
                target = user_query.lower().replace("open", "").replace("kholo", "").strip()
                res = automation.open_app_or_site(target)
                st.success(res)
            else:
                st.success("Query processed by MHZALY Core Brain.")

st.markdown("---")
st.subheader("👥 Active Sub-Agents Workfloor (Worker Agents)")

# 4 Parallel Sub-Agent Workstations
ag1, ag2, ag3, ag4 = st.columns(4)

with ag1:
    st.markdown("""
    <div class="agent-card">
        <h4>📞 WhatsApp Agent (Worker 1)</h4>
        <p>Status: <span class="status-badge">Ready / Active</span></p>
        <small>Executes WhatsApp searches, contact selection & calls</small>
    </div>
    """, unsafe_allow_html=True)

with ag2:
    st.markdown("""
    <div class="agent-card">
        <h4>💻 Coding & Expert Agent (Worker 2)</h4>
        <p>Status: <span class="status-badge">Ready</span></p>
        <small>Python, C++, Web, Cyber Security & Algorithms</small>
    </div>
    """, unsafe_allow_html=True)

with ag3:
    st.markdown("""
    <div class="agent-card">
        <h4>🌐 Web Research Agent (Worker 3)</h4>
        <p>Status: <span class="status-badge">Ready</span></p>
        <small>Google Search, YouTube Player & Twitter</small>
    </div>
    """, unsafe_allow_html=True)

with ag4:
    st.markdown("""
    <div class="agent-card">
        <h4>👁️ Screen Vision Agent (Worker 4)</h4>
        <p>Status: <span class="status-badge">Ready</span></p>
        <small>Analyzes Laptop Screen & Live Stream</small>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("MHZALY AI Assistant - Powered by Gemini & Python Multi-Agent Architecture")