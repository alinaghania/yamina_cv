import streamlit as st
from PIL import Image
import os

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Alina Ghani | Anthropic Application",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Force light theme
    st.markdown("""
    <style>
        .stApp {
            background-color: white;
            color: black;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Dictionnaire de traductions (English only)
    translations = {
        "title": "Alina Ghani",
        "subtitle": "Applied AI, Product Engineer",
        "tab_feed": "Portfolio",
        "tab_motivation": "Why Anthropic",
        "tab_skills": "Skills",
        "tab_contact": "Contact",
        "feed_title": "My AI Journey",
        "motivation_title": "Why Anthropic?",
        "skills_title": "Technical Excellence",
        "contact_title": "Let's Connect",
        "seeking": "Seeking Applied AI, Product Engineer Role - London",
        "motivation_text": "Since the release of ChatGPT in 2021, I've had the opportunity to build prototypes, websites, and small AI tools at lightning speed, and to explain them to others. I suddenly felt more capable, more creative, even more intelligent. That feeling of excitement and empowerment completely changed the way I see work, creation, and learning. And now, more than anything, I want to share that feeling with others. I want people to feel what I felt, that sense of being *more* thanks to AI.\n\nNot a single day goes by where I feel bored. Sometimes I feel overwhelmed, yes, but always in the best way possible. Whether it's text, image, or voice generation, building together with AI makes me feel alive. Isn't that what we're all looking for? I feel incredibly grateful to live at a time where this kind of creation is possible, and I know there's no place I'd rather be than in the middle of it.\n\nClaude is, hands down, my favorite model to \"vibe-code\" with. It has become a true partner in how I build and think. The product is simply exceptional, and when you're already a power user and a fan, it doesn't feel like \"selling\" anything. It feels like sharing something you genuinely believe in.",
        "contact_button": "Let's Talk AI",
        "footer_text": "Applied AI Product Engineer • Anthropic Dream Candidate 2025"
    }
    
    # CSS Anthropic-inspired design
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        
        :root {
            --anthropic-black: #1a1a1a;
            --anthropic-orange: #ff6b35;
            --anthropic-blue: #4a90e2;
            --white: #ffffff;
            --light-gray: #f5f5f5;
            --medium-gray: #e0e0e0;
            --text-gray: #333333;
        }
        
        /* General styles */
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--white);
            color: var(--anthropic-black);
            line-height: 1.6;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            letter-spacing: -0.02em;
        }
        
        /* Header Hero */
        .header-hero {
            background: linear-gradient(135deg, var(--anthropic-black) 0%, #2d2d2d 100%);
            padding: 5rem 2rem;
            color: var(--white);
            text-align: center;
            margin-bottom: 3rem;
            position: relative;
            overflow: hidden;
        }
        
        .header-hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 20%, var(--anthropic-orange) 0%, transparent 50%),
                        radial-gradient(circle at 70% 80%, var(--anthropic-blue) 0%, transparent 50%);
            opacity: 0.1;
            animation: pulse 6s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.1; }
            50% { opacity: 0.2; }
        }
        
        .hero-title {
            font-family: 'Inter', sans-serif;
            font-size: 4rem;
            font-weight: 700;
            letter-spacing: -0.03em;
            margin-bottom: 1rem;
            position: relative;
            z-index: 1;
        }
        
        .hero-subtitle {
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            font-weight: 400;
            margin-bottom: 2rem;
            position: relative;
            z-index: 1;
            color: var(--anthropic-orange);
        }
        
        /* Section containers */
        .section-container {
            max-width: 1200px;
            margin: 0 auto 4rem auto;
            padding: 0 2rem;
        }
        
        .section-title {
            font-family: 'Inter', sans-serif;
            font-size: 2.5rem;
            font-weight: 600;
            text-align: center;
            margin-bottom: 3rem;
            letter-spacing: -0.02em;
            position: relative;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -1rem;
            left: 50%;
            transform: translateX(-50%);
            width: 80px;
            height: 3px;
            background: linear-gradient(90deg, var(--anthropic-orange), var(--anthropic-blue));
        }
        
        /* Instagram-style grid */
        .insta-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }
        
        .insta-card {
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            transition: all 0.3s ease;
            cursor: pointer;
            height: 300px;
            background-color: var(--light-gray);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .insta-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .insta-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 12px;
        }
        
        .insta-placeholder {
            text-align: center;
        }
        
        .insta-placeholder-text {
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 300;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        
        /* Skills grid */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }
        
        .skill-card {
            background-color: var(--white);
            border: 2px solid var(--medium-gray);
            border-radius: 12px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        
        .skill-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, var(--anthropic-orange), var(--anthropic-blue));
            transform: translateY(100%);
            transition: transform 0.3s ease;
        }
        
        .skill-card:hover::before {
            transform: translateY(0);
        }
        
        .skill-card:hover {
            color: var(--white);
            border-color: var(--anthropic-orange);
        }
        
        .skill-card > * {
            position: relative;
            z-index: 1;
        }
        
        .skill-title {
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            font-weight: 600;
            margin-bottom: 1rem;
            letter-spacing: -0.01em;
        }
        
        .skill-items {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            font-weight: 400;
            line-height: 1.8;
        }
        
        /* Experience cards */
        .experience-card {
            border: 2px solid var(--medium-gray);
            border-radius: 12px;
            margin-bottom: 2rem;
            overflow: hidden;
            background-color: var(--white);
        }
        
        .experience-header {
            background: linear-gradient(135deg, var(--anthropic-black), #2d2d2d);
            color: var(--white);
            padding: 1.5rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .experience-title {
            font-family: 'Inter', sans-serif;
            font-size: 1.4rem;
            font-weight: 600;
            letter-spacing: -0.01em;
        }
        
        .experience-date {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            font-weight: 400;
            color: var(--anthropic-orange);
        }
        
        .experience-content {
            padding: 2rem;
            background-color: var(--white);
        }
        
        .experience-role {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            font-weight: 600;
            color: var(--anthropic-blue);
            margin-bottom: 1rem;
        }
        
        .experience-list {
            list-style: none;
            padding: 0;
        }
        
        .experience-item {
            font-family: 'Inter', sans-serif;
            font-size: 0.95rem;
            font-weight: 400;
            line-height: 1.7;
            margin-bottom: 0.8rem;
            padding-left: 1.5rem;
            position: relative;
        }
        
        .experience-item::before {
            content: '▶';
            position: absolute;
            left: 0;
            color: var(--anthropic-orange);
        }
        
        /* Motivation section */
        .motivation-container {
            background: linear-gradient(135deg, var(--light-gray), var(--white));
            border: 2px solid var(--medium-gray);
            border-radius: 16px;
            padding: 3rem;
            text-align: left;
            margin-bottom: 4rem;
        }
        
        .motivation-quote {
            font-family: 'Inter', sans-serif;
            font-size: 1.1rem;
            font-weight: 400;
            line-height: 1.6;
            margin-bottom: 2rem;
            color: var(--anthropic-black);
        }
        
        .motivation-text {
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 400;
            line-height: 1.7;
            margin-bottom: 1.5rem;
        }
        
        /* Contact container */
        .contact-container {
            background: linear-gradient(135deg, var(--anthropic-black), #2d2d2d);
            color: var(--white);
            padding: 3rem;
            border-radius: 16px;
            text-align: center;
            margin-top: 4rem;
        }
        
        .contact-title {
            font-family: 'Inter', sans-serif;
            font-size: 2.2rem;
            font-weight: 600;
            letter-spacing: -0.02em;
            margin-bottom: 2rem;
        }
        
        .contact-info {
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 400;
            line-height: 2;
        }
        
        .contact-link {
            color: var(--anthropic-orange);
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .contact-link:hover {
            color: var(--anthropic-blue);
        }
        
        /* Buttons */
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, var(--anthropic-orange), var(--anthropic-blue));
            color: var(--white);
            padding: 1rem 3rem;
            font-family: 'Inter', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            letter-spacing: -0.01em;
            text-decoration: none;
            border: none;
            border-radius: 8px;
            transition: all 0.3s ease;
            margin-top: 2rem;
        }
        
        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(255, 107, 53, 0.3);
        }
        
        /* Tabs override */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            border-bottom: 2px solid var(--medium-gray);
            background-color: var(--white);
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            background-color: var(--white);
            color: var(--text-gray);
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            font-size: 0.95rem;
            border: none;
            border-bottom: 3px solid transparent;
            border-radius: 0;
            padding: 0 2rem;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--white) !important;
            color: var(--anthropic-orange) !important;
            border-bottom: 3px solid var(--anthropic-orange) !important;
        }
        
        /* Mobile responsive */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .insta-grid {
                grid-template-columns: 1fr;
                gap: 1rem;
            }
            
            .experience-header {
                flex-direction: column;
                gap: 0.5rem;
                text-align: center;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header Hero
    st.markdown(f"""
    <div class="header-hero">
        <h1 class="hero-title">{translations['title']}</h1>
        <p class="hero-subtitle">{translations['subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabs
    tabs = st.tabs([translations['tab_feed'], translations['tab_motivation'], translations['tab_skills'], translations['tab_contact']])
    
    # Tab 1: Portfolio (Instagram style with actual photos)
    with tabs[0]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{translations['feed_title']}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Instagram-style grid
        cols = st.columns(3)
        for i in range(9):
            with cols[i % 3]:
                image_path = f"pics_ali/{i+1}.jpeg"
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    st.image(image, use_container_width=True)
                else:
                    # Placeholder with styled text
                    st.markdown(f"""
                    <div class="insta-card">
                        <div class="insta-placeholder">
                            <div class="insta-placeholder-text">AI Journey #{i+1}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Tab 2: Why Anthropic
    with tabs[1]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{translations['motivation_title']}</h2>
            <div class="motivation-container">
                <p class="motivation-text">
                    {translations['motivation_text']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tab 3: Skills (using the card format)
    with tabs[2]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{translations['skills_title']}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Skills in card format
        skills_data = [
            ("Generative AI & LLMs", "Claude, OpenAI GPT, Langchain, Vertex AI, RAG, Advanced Prompting"),
            ("Engineering & Platforms", "Python, SQL, React, Node.js, Azure (AZ-900, AI-900), Git, Docker"),
            ("Product & Solutions", "Customer Discovery, POC Development, Technical Architecture, Solution Design"),
            ("Communication & Collaboration", "Cross-functional Teamwork, Stakeholder Alignment, Customer Onboarding"),
            ("Computer Vision", "Mediapipe, OpenCV, Python, Real-time Processing"),
            ("Data Engineering", "ETL Pipelines, Data Cleaning, SQL, Database Optimization"),
            ("Customer Success", "Technical Advisory, Solution Architecture, Implementation Support"),
            ("AI Safety & Ethics", "Responsible AI Development, Risk Assessment, Safe Deployment"),
            ("Cross-functional Leadership", "Technical Communication, Team Coordination, Project Management")
        ]
        
        # Create grid of skill cards
        cols = st.columns(3)
        for i, (title, items) in enumerate(skills_data):
            with cols[i % 3]:
                st.markdown(f"""
                <div class="skill-card">
                    <h3 class="skill-title">{title}</h3>
                    <div class="skill-items">{items}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Tab 4: Contact
    with tabs[3]:
        st.markdown(f"""
        <div class="contact-container">
            <h2 class="contact-title">{translations['contact_title']}</h2>
            <div class="contact-info">
                <p>alinaghani13@gmail.com</p>
                <p>+33 6 36 12 27 62</p>
                <p><a href="https://www.linkedin.com/in/alina-ghani/" class="contact-link">LinkedIn: Alina Ghani</a></p>
                <p>Paris, France → London, UK</p>
                <p>Ready for international opportunities</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Call to action
        st.markdown(f"""
        <div style="text-align: center; margin-top: 3rem;">
            <a href="mailto:alinaghani13@gmail.com" class="cta-button" style="text-decoration: none; color: white;">
                {translations['contact_button']}
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, var(--anthropic-black), #2d2d2d); color: #fff; padding: 3rem; text-align: center; margin-top: 4rem; border-radius: 16px;">
        <p style="font-family: 'Inter', sans-serif; font-size: 1.8rem; font-weight: 600; letter-spacing: -0.02em; margin-bottom: 1rem;">
            ALINA GHANI
        </p>
        <p style="font-family: 'Inter', sans-serif; font-size: 1rem; font-weight: 400; color: var(--anthropic-orange);">
            {translations['footer_text']}
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; font-weight: 400; margin-top: 1rem; opacity: 0.7;">
            Building AI that's safe, beneficial, and truly useful
        </p>
    </div>
    """, unsafe_allow_html=True)

# Point d'entrée
if __name__ == "__main__":
    main()