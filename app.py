import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Emad Khaled", layout="wide", page_icon="📈")

# --- PROFESSIONAL CSS WITH DARK BLUE ACCENTS ---
st.markdown("""
<style>
    /* Keep white background */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Reset spacing */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px;
        margin: auto;
    }
    
    header {visibility: hidden;}

    /* Professional card styling - Light with colored left border */
    .professional-card {
        background-color: #f5f8fa;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        margin: 15px 0;
        line-height: 1.7;
        color: #333333;
    }

    .metric-box {
        background: linear-gradient(135deg, #f5f8fa 0%, #e8f2ff 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        text-align: center;
        margin: 10px 0;
        color: #1a1a1a;
    }

    .metric-box h3 {
        color: #1E90FF;
        margin: 0;
        font-size: 32px;
    }

    .section-header {
        color: #1E90FF;
        border-bottom: 3px solid #1E90FF;
        padding-bottom: 12px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-weight: 700;
    }

    .skill-tag {
        display: inline-block;
        background-color: #e8f2ff;
        color: #1E90FF;
        padding: 8px 16px;
        border-radius: 20px;
        margin: 5px 5px 5px 0;
        font-size: 13px;
        font-weight: 600;
        border: 1px solid #1E90FF;
    }

    .experience-item {
        background-color: #f5f8fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E90FF;
        margin: 15px 0;
        color: #333333;
    }

    .experience-item h4 {
        margin: 0 0 5px 0;
        color: #1E90FF;
        font-weight: 700;
    }

    .experience-item p {
        margin: 5px 0;
        color: #555555;
        font-size: 14px;
    }

    /* Streamlit elements */
    h1, h2, h3 {
        color: #1a1a1a !important;
    }

    h1 {
        color: #1E90FF !important;
        font-weight: 700;
    }

    hr {
        border-color: #d0d0d0 !important;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #1E90FF !important;
        border: 1px solid #1E90FF !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 6px !important;
    }

    div.stButton > button:hover {
        background-color: #0d6fb8 !important;
        border: 1px solid #0d6fb8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Navigation state
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Simple navigation buttons
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"

with col2:
    if st.button("About", use_container_width=True):
        st.session_state.page = "About"

with col3:
    if st.button("Education", use_container_width=True):
        st.session_state.page = "Education"

with col4:
    if st.button("Experience", use_container_width=True):
        st.session_state.page = "Experience"

with col5:
    if st.button("Contact", use_container_width=True):
        st.session_state.page = "Contact"

st.divider()

# --- PAGE LOGIC ---
if st.session_state.page == "Home":
    col1, col2 = st.columns([1, 1.8], gap="large")
    
    with col1:
        try:
            st.image("profile_pic.png", width=280)
        except:
            st.info("Profile picture placeholder")
    
    with col2:
        st.title("Emad Khaled")
        st.subheader("Business Analytics & Quantitative Finance")
        
        st.markdown("""
        <div class="professional-card">
            <p>Computer Science and Statistics Dual Major at Tel Aviv University with expertise in quantitative analysis, financial modeling, and data-driven valuation methodologies.</p>
            <p><b>Current Focus:</b> Identifying mispricing opportunities in Israeli tech sector through regression analysis and fundamental analysis frameworks.</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("""
            <div class="metric-box">
            <h3>3+</h3>
            <p>Projects</p>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="metric-box">
            <h3>8+</h3>
            <p>Technical Skills</p>
            </div>
            """, unsafe_allow_html=True)
        with col_c:
            st.markdown("""
            <div class="metric-box">
            <h3>2026</h3>
            <p>Graduation</p>
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.page == "About":
    st.title("Professional Background")
    
    st.markdown("""
    <div class="professional-card">
    <h3>Overview</h3>
    <p>Data-driven analyst specializing in financial valuation and quantitative research. Strong foundation in statistical methodologies, software development, and financial modeling with proven ability to identify market inefficiencies through rigorous analytical frameworks.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Core Competencies</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<b>Analytical Skills</b>")
        skills_analytical = ["Statistical Inference", "Regression Analysis", "Hypothesis Testing", "Financial Modeling", "Valuation Methods", "Risk Analysis"]
        for skill in skills_analytical:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<b>Technical Skills</b>")
        skills_technical = ["Python", "SQL", "Pandas", "Matplotlib", "Git", "Excel/VBA", "Streamlit", "Statistics"]
        for skill in skills_technical:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Specialization Areas</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="professional-card">
        <b>Equity Research</b><br>
        Fundamental analysis of technology companies with focus on valuation multiples, growth trajectories, and comparative metrics.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="professional-card">
        <b>Quantitative Analysis</b><br>
        Data-driven research utilizing statistical methods to identify market patterns and valuation anomalies.
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "Education":
    st.title("Education")
    
    st.markdown("""
    <div class="experience-item">
    <h4>Tel Aviv University</h4>
    <p><b>Dual Major: Computer Science & Statistics</b></p>
    <p>Expected Graduation: 2026 | GPA: 3.8/4.0</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="section-header">Relevant Coursework</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Computer Science:**
        - Algorithms & Data Structures
        - Graph Theory & Shortest Paths
        - Database Systems
        - Object-Oriented Programming
        """)
    
    with col2:
        st.markdown("""
        **Statistics & Mathematics:**
        - Multiple Comparisons (Tukey-Kramer, Bonferroni)
        - Probability Theory
        - Linear Regression Analysis
        - Statistical Inference
        """)
    
    st.markdown('<h3 class="section-header">Technical Proficiency</h3>', unsafe_allow_html=True)
    
    proficiency = {
        "Python Programming": 92,
        "Statistical Analysis": 88,
        "Data Analysis & Visualization": 85,
        "SQL & Databases": 80,
        "Financial Modeling": 78
    }
    
    for skill, level in proficiency.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(level / 100, text=skill)
        with col2:
            st.write(f"{level}%")

elif st.session_state.page == "Experience":
    st.title("Projects & Experience")
    
    st.markdown("""
    <div class="experience-item">
    <h4>Israeli Technology Sector Valuation Analysis</h4>
    <p><b>Project Type:</b> Equity Research & Quantitative Analysis</p>
    <p><b>Duration:</b> Ongoing</p>
    <p><b>Description:</b> Comprehensive valuation study of publicly-traded Israeli technology companies including Monday.com, Wix, Fiverr, and Check Point. Analysis focused on identifying correlation between revenue growth rates and market valuation multiples.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Create valuation analysis visualization
        df = pd.DataFrame({
            'Ticker': ['MNDY', 'WIX', 'FVRR', 'CHKP'],
            'Growth': [30, 15, 10, 5],
            'Multiple': [10, 6, 4, 5]
        })
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.regplot(data=df, x='Growth', y='Multiple', ax=ax, color='#1E90FF', 
                   scatter_kws={'s': 150, 'alpha': 0.7}, line_kws={'color': '#00BFFF'})
        ax.set_xlabel("Revenue Growth Rate (%)", fontsize=11, fontweight='bold')
        ax.set_ylabel("EV/Revenue Multiple", fontsize=11, fontweight='bold')
        ax.set_title("Growth vs Valuation Multiple", fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.2)
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.markdown("""
        <div class="professional-card">
        <b>Key Findings:</b>
        <ul style="margin: 10px 0; padding-left: 20px;">
        <li>Strong positive correlation between growth and valuation</li>
        <li>MNDY trading at premium multiple</li>
        <li>FVRR potentially undervalued</li>
        <li>Market inefficiency detected</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown('<h3 class="section-header">Project Pipeline</h3>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Stock Valuation API",
            "status": "In Development",
            "description": "RESTful API for automated company valuation using fundamental metrics"
        },
        {
            "title": "Portfolio Optimization Framework",
            "status": "Planning",
            "description": "Modern Portfolio Theory implementation with risk-adjusted returns optimization"
        },
        {
            "title": "Financial Data Pipeline",
            "status": "In Development",
            "description": "Automated ETL system for financial data aggregation and analysis"
        }
    ]
    
    for proj in projects:
        status_color = "#4CAF50" if "In Development" in proj['status'] else "#FF9800" if "Planning" in proj['status'] else "#2196F3"
        st.markdown(f"""
        <div class="experience-item">
        <h4>{proj['title']}</h4>
        <p style="color: {status_color}; font-weight: bold; font-size: 12px;">{proj['status']}</p>
        <p>{proj['description']}</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "Contact":
    st.title("Contact Information")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="professional-card">
        <b>Email</b><br>
        <a href="mailto:emad.kha3@gmail.com">emad.kha3@gmail.com</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="professional-card">
        <b>LinkedIn</b><br>
        <a href="https://www.linkedin.com/in/emad-khaled-6b6528257/" target="_blank">linkedin.com/in/emad-khaled</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="professional-card">
        <b>GitHub</b><br>
        <a href="https://github.com/emad-khaled-dev" target="_blank">github.com/emad-khaled-dev</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    <div class="professional-card">
    <h3>Professional Inquiry</h3>
    <p>For project collaborations, internship opportunities, or professional discussions, please reach out via email or LinkedIn with relevant context.</p>
    </div>
    """, unsafe_allow_html=True)