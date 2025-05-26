import streamlit as st
from PIL import Image
import os

def main():
    # Configuration de la page
    st.set_page_config(
        page_title="Yamina Ghani | Sephora Application",
        page_icon="💄",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Initialiser la langue dans session state
    if 'language' not in st.session_state:
        st.session_state.language = "English"
    
    # Dictionnaire de traductions
    translations = {
        "English": {
            "title": "Yamina Ghani",
            "subtitle": "Future Business & Data Analyst",
            "tab_feed": "✨ Dream Feed",
            "tab_experience": "💼 Experience",
            "tab_skills": "🎯 Skills",
            "tab_motivation": "💌 Motivation",
            "tab_contact": "📞 Contact",
            "feed_title": "My Sephora Journey",
            "experience_title": "Professional Journey",
            "skills_title": "Technical Excellence",
            "motivation_title": "Why Sephora?",
            "contact_title": "Let's Connect",
            "seeking": "Seeking Apprenticeship - September 2025",
            "ace_role": "Data & Business Analyst (Apprenticeship)",
            "ace_1": "Analyzed transaction data from multiple countries using Python and Excel",
            "ace_2": "Designed interactive Power BI dashboards for monthly transaction reports",
            "ace_3": "Delivered insights on customer behavior and regional performance",
            "ace_4": "Supported strategic business decisions through data-driven analysis",
            "eureka_role": "Assistant IT Teacher",
            "eureka_1": "Organized coding workshops and computer skills lessons",
            "eureka_2": "Coordinated hackathons for hands-on learning experiences",
            "eureka_3": "Sourced funding for student computer resources",
            "eureka_4": "Created interactive activities to enhance technical skills",
            "bde_role": "Board Member",
            "bde_1": "Organized all student events including WEI and campus activities",
            "bde_2": "Managed budgets and coordinated logistics for multiple events",
            "bde_3": "Led cross-functional teams to ensure successful event execution",
            "bde_4": "Developed leadership skills as class delegate for 6 years",
            "skills_data_processing": "Data Processing",
            "skills_data_viz": "Data Visualization",
            "skills_cloud": "Cloud & AI",
            "skills_pm": "Project Management",
            "skills_web": "Web & CMS",
            "skills_languages": "Languages",
            "skills_soft_title": "Soft Skills",
            "skills_leadership": "Leadership Excellence: 6 years as class delegate",
            "skills_analytical": "Analytical Mindset: Strong problem-solving and decision-making capabilities",
            "skills_communication": "Communication: Effective presenter and team collaborator",
            "skills_organization": "Organization: Proven ability to manage multiple projects simultaneously",
            "motivation_quote": "Beauty is not just about appearance, it's a science, data, an experience to analyze and optimize.",
            "motivation_text1": "My journey in Data & Marketing has convinced me that data analysis is the key to understanding and anticipating customer needs. At Sephora, I see the unique opportunity to combine my passion for data with my interest in the beauty industry.",
            "motivation_bring_title": "What I can bring to Sephora:",
            "motivation_bring_1": "✨ Strong technical expertise in data analysis and dashboard creation",
            "motivation_bring_2": "✨ Proven ability to transform complex data into actionable insights",
            "motivation_bring_3": "✨ Fresh perspective and positive energy for RGM projects",
            "motivation_bring_4": "✨ Genuine passion for the beauty industry and its challenges",
            "motivation_goals_title": "My goals at Sephora:",
            "motivation_goals_1": "📊 Master Revenue Growth Management specifics in beauty retail",
            "motivation_goals_2": "📈 Actively contribute to pricing and promotion strategy optimization",
            "motivation_goals_3": "🎯 Develop innovative decision-making tools",
            "motivation_goals_4": "🌟 Participate in Sephora's digital transformation",
            "perfect_match_title": "The Perfect Match",
            "perfect_match_subtitle": "Your Needs = My Skills",
            "perfect_match_1": "Pricing position control: Experience in transactional data analysis and KPI creation",
            "perfect_match_2": "Dashboards: Mastery of Power BI, Tableau and DataStudio for impactful dashboards",
            "perfect_match_3": "Impact analysis: Python and SQL skills for in-depth analysis",
            "perfect_match_4": "Competitive intelligence: Natural curiosity and rigorous methodology",
            "perfect_match_5": "Cross-functional collaboration: Experience in multi-team project management",
            "contact_ready": "Ready to reimagine the future of beauty with Sephora",
            "contact_available": "I am available for an interview at your convenience to discuss how my data analysis skills and passion for the beauty industry can contribute to the RGM France team's success.",
            "contact_availability": "Availability: 12-month apprenticeship starting September 2025",
            "contact_location": "Location: Neuilly-sur-Seine ✓",
            "contact_motivation": "Motivation: 200% 🚀",
            "contact_button": "Contact Me",
            "footer_text": "Future Business & Data Analyst RGM France • Sephora Dream Candidate 2025"
        },
        "Français": {
            "title": "Yamina Ghani",
            "subtitle": "Future Business & Data Analyst",
            "tab_feed": "✨ Feed de Rêve",
            "tab_experience": "💼 Expérience",
            "tab_skills": "🎯 Compétences",
            "tab_motivation": "💌 Motivation",
            "tab_contact": "📞 Contact",
            "feed_title": "Mon Parcours Sephora",
            "experience_title": "Parcours Professionnel",
            "skills_title": "Excellence Technique",
            "motivation_title": "Pourquoi Sephora ?",
            "contact_title": "Connectons-nous",
            "seeking": "Recherche Alternance - Septembre 2025",
            "ace_role": "Data & Business Analyst (Alternance)",
            "ace_1": "Analyse de données transactionnelles de plusieurs pays avec Python et Excel",
            "ace_2": "Conception de tableaux de bord interactifs Power BI pour les rapports mensuels",
            "ace_3": "Insights sur le comportement client et les performances régionales",
            "ace_4": "Support aux décisions stratégiques par l'analyse de données",
            "eureka_role": "Assistante Formatrice IT",
            "eureka_1": "Organisation d'ateliers de codage et de compétences informatiques",
            "eureka_2": "Coordination de hackathons pour l'apprentissage pratique",
            "eureka_3": "Recherche de financements pour les ressources informatiques étudiantes",
            "eureka_4": "Création d'activités interactives pour améliorer les compétences techniques",
            "bde_role": "Membre du Bureau",
            "bde_1": "Organisation de tous les événements étudiants incluant le WEI",
            "bde_2": "Gestion des budgets et coordination logistique pour plusieurs événements",
            "bde_3": "Direction d'équipes transversales pour assurer le succès des événements",
            "bde_4": "Développement du leadership en tant que déléguée de classe pendant 6 ans",
            "skills_data_processing": "Traitement de Données",
            "skills_data_viz": "Visualisation de Données",
            "skills_cloud": "Cloud & IA",
            "skills_pm": "Gestion de Projet",
            "skills_web": "Web & CMS",
            "skills_languages": "Langues",
            "skills_soft_title": "Soft Skills",
            "skills_leadership": "Excellence en Leadership : 6 ans déléguée de classe",
            "skills_analytical": "Esprit Analytique : Fortes capacités de résolution de problèmes",
            "skills_communication": "Communication : Présentatrice efficace et collaboratrice",
            "skills_organization": "Organisation : Capacité prouvée à gérer plusieurs projets simultanément",
            "motivation_quote": "La beauté n'est pas qu'une question d'apparence, c'est une science, une donnée, une expérience à analyser et à optimiser.",
            "motivation_text1": "Mon parcours en Data & Marketing m'a convaincue que l'analyse de données est la clé pour comprendre et anticiper les besoins des clients. Chez Sephora, je vois l'opportunité unique de combiner ma passion pour la data avec mon intérêt pour l'industrie de la beauté.",
            "motivation_bring_title": "Ce que je peux apporter à Sephora :",
            "motivation_bring_1": "✨ Une expertise technique solide en analyse de données et création de dashboards",
            "motivation_bring_2": "✨ Une capacité prouvée à transformer des données complexes en insights actionnables",
            "motivation_bring_3": "✨ Un regard neuf et une énergie positive pour contribuer aux projets RGM",
            "motivation_bring_4": "✨ Une vraie passion pour l'industrie de la beauté et ses enjeux",
            "motivation_goals_title": "Mes objectifs chez Sephora :",
            "motivation_goals_1": "📊 Maîtriser les spécificités du Revenue Growth Management dans le retail beauté",
            "motivation_goals_2": "📈 Contribuer activement à l'optimisation des stratégies prix et promotions",
            "motivation_goals_3": "🎯 Développer des outils d'aide à la décision innovants",
            "motivation_goals_4": "🌟 Participer à la transformation digitale de Sephora",
            "perfect_match_title": "Le Match Parfait",
            "perfect_match_subtitle": "Vos Besoins = Mes Compétences",
            "perfect_match_1": "Contrôle du positionnement tarifaire : Expérience en analyse de données transactionnelles et création de KPIs",
            "perfect_match_2": "Tableaux de bord : Maîtrise de Power BI, Tableau et DataStudio pour des dashboards impactants",
            "perfect_match_3": "Analyses d'impacts : Compétences en Python et SQL pour des analyses approfondies",
            "perfect_match_4": "Veille concurrentielle : Curiosité naturelle et méthodologie rigoureuse",
            "perfect_match_5": "Collaboration transversale : Expérience en gestion de projets multi-équipes",
            "contact_ready": "Prête à réimaginer le futur de la beauté avec Sephora",
            "contact_available": "Je suis disponible pour un entretien à votre convenance pour discuter de la façon dont mes compétences en data analyse et ma passion pour l'industrie de la beauté peuvent contribuer au succès de l'équipe RGM France.",
            "contact_availability": "Disponibilité : Alternance de 12 mois à partir de septembre 2025",
            "contact_location": "Localisation : Neuilly-sur-Seine ✓",
            "contact_motivation": "Motivation : 200% 🚀",
            "contact_button": "Contactez-moi",
            "footer_text": "Future Business & Data Analyst RGM France • Candidate de Rêve Sephora 2025"
        }
    }
    
    # Obtenir les traductions pour la langue sélectionnée
    t = translations[st.session_state.language]
    
    # CSS Chanel-inspired minimaliste
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap');
        
        :root {
            --black: #000000;
            --white: #ffffff;
            --off-white: #f8f8f8;
            --light-gray: #e5e5e5;
            --accent-red: #FF0000;
        }
        
        /* General styles */
        body {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--white);
            color: var(--black);
            line-height: 1.6;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Cormorant Garamond', serif;
            font-weight: 500;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }
        
        /* Header Hero */
        .header-hero {
            background-color: var(--black);
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
            background: linear-gradient(135deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
            animation: shine 3s infinite;
        }
        
        @keyframes shine {
            0% { transform: translateX(-100%); }
            100% { transform: translateX(100%); }
        }
        
        .hero-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 4rem;
            font-weight: 300;
            letter-spacing: 0.2em;
            margin-bottom: 1rem;
            text-transform: uppercase;
            position: relative;
            z-index: 1;
        }
        
        .hero-subtitle {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.2rem;
            font-weight: 300;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            margin-bottom: 2rem;
            position: relative;
            z-index: 1;
        }
        
        /* Section containers */
        .section-container {
            max-width: 1200px;
            margin: 0 auto 4rem auto;
            padding: 0 2rem;
        }
        
        .section-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 3rem;
            font-weight: 400;
            text-align: center;
            margin-bottom: 3rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            position: relative;
        }
        
        .section-title::after {
            content: '';
            position: absolute;
            bottom: -1rem;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 1px;
            background-color: var(--black);
        }
        
        /* Instagram Feed */
        .insta-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }
        
        .insta-card {
            position: relative;
            overflow: hidden;
            border: 1px solid var(--light-gray);
            transition: all 0.3s ease;
            cursor: pointer;
            height: 300px;
            background-color: var(--off-white);
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .insta-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .insta-placeholder {
            text-align: center;
        }
        
        .insta-placeholder-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .insta-placeholder-text {
            font-family: 'Montserrat', sans-serif;
            font-size: 1rem;
            font-weight: 300;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        
        /* Skills grid */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 4rem;
        }
        
        .skill-card {
            background-color: var(--off-white);
            border: 1px solid var(--black);
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        .skill-card:hover {
            background-color: var(--black);
            color: var(--white);
        }
        
        .skill-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 400;
            margin-bottom: 1rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        
        .skill-items {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            font-weight: 300;
            line-height: 1.8;
        }
        
        /* Experience cards */
        .experience-card {
            border: 1px solid var(--black);
            margin-bottom: 2rem;
            overflow: hidden;
        }
        
        .experience-header {
            background-color: var(--black);
            color: var(--white);
            padding: 1.5rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .experience-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 400;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }
        
        .experience-date {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            font-weight: 300;
            letter-spacing: 0.05em;
        }
        
        .experience-content {
            padding: 2rem;
            background-color: var(--white);
        }
        
        .experience-role {
            font-family: 'Montserrat', sans-serif;
            font-size: 1.1rem;
            font-weight: 400;
            color: var(--accent-red);
            margin-bottom: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .experience-list {
            list-style: none;
            padding: 0;
        }
        
        .experience-item {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.95rem;
            font-weight: 300;
            line-height: 1.8;
            margin-bottom: 0.8rem;
            padding-left: 1.5rem;
            position: relative;
        }
        
        .experience-item::before {
            content: '◆';
            position: absolute;
            left: 0;
            color: var(--accent-red);
        }
        
        /* Motivation section */
        .motivation-container {
            background-color: var(--off-white);
            border: 1px solid var(--black);
            padding: 3rem;
            text-align: center;
            margin-bottom: 4rem;
        }
        
        .motivation-quote {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2rem;
            font-weight: 300;
            font-style: italic;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        
        .motivation-text {
            font-family: 'Montserrat', sans-serif;
            font-size: 1rem;
            font-weight: 300;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Language buttons */
        .lang-container {
            position: absolute;
            bottom: 1rem;
            right: 2rem;
            display: flex;
            gap: 0.5rem;
            z-index: 10;
        }
        
        .lang-button {
            background-color: transparent;
            color: var(--white);
            border: 1px solid var(--white);
            padding: 0.5rem 1rem;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.8rem;
            font-weight: 400;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .lang-button:hover {
            background-color: var(--white);
            color: var(--black);
        }
        
        .lang-button.active {
            background-color: var(--white);
            color: var(--black);
        }
        .contact-container {
            background-color: var(--black);
            color: var(--white);
            padding: 3rem;
            text-align: center;
            margin-top: 4rem;
        }
        
        .contact-title {
            font-family: 'Cormorant Garamond', serif;
            font-size: 2.5rem;
            font-weight: 400;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 2rem;
        }
        
        .contact-info {
            font-family: 'Montserrat', sans-serif;
            font-size: 1rem;
            font-weight: 300;
            line-height: 2;
            letter-spacing: 0.05em;
        }
        
        .contact-link {
            color: var(--white);
            text-decoration: none;
            transition: color 0.3s ease;
        }
        
        .contact-link:hover {
            color: var(--accent-red);
        }
        
        /* Buttons */
        .cta-button {
            display: inline-block;
            background-color: var(--black);
            color: var(--white);
            padding: 1rem 3rem;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            font-weight: 400;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            text-decoration: none;
            border: 1px solid var(--black);
            transition: all 0.3s ease;
            margin-top: 2rem;
        }
        
        .cta-button:hover {
            background-color: var(--white);
            color: var(--black);
        }
        
        /* Tabs override */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0;
            border-bottom: 1px solid var(--black);
            background-color: var(--white);
        }
        
        .stTabs [data-baseweb="tab"] {
            height: 50px;
            background-color: var(--white);
            color: var(--black);
            font-family: 'Montserrat', sans-serif;
            font-weight: 400;
            font-size: 0.9rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            border: none;
            border-bottom: 3px solid transparent;
            border-radius: 0;
            padding: 0 2rem;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--white) !important;
            color: var(--black) !important;
            border-bottom: 3px solid var(--black) !important;
        }
        
        /* Mobile responsive */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .insta-grid {
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
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
        <h1 class="hero-title">{t['title']}</h1>
        <p class="hero-subtitle">{t['subtitle']}</p>
        <div class="lang-container">
            <button class="lang-button {'active' if st.session_state.language == 'English' else ''}" onclick="window.location.href='?lang=en'">EN</button>
            <button class="lang-button {'active' if st.session_state.language == 'Français' else ''}" onclick="window.location.href='?lang=fr'">FR</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Gérer le changement de langue via URL params
    query_params = st.query_params
    if 'lang' in query_params:
        if query_params['lang'] == 'en':
            st.session_state.language = 'English'
        elif query_params['lang'] == 'fr':
            st.session_state.language = 'Français'
        st.query_params.clear()
        st.rerun()
    
    # Language switcher buttons
    col1, col2, col3 = st.columns([10, 1, 1])
    with col2:
        if st.button("EN", key="en_button", use_container_width=True):
            st.session_state.language = "English"
            st.rerun()
    with col3:
        if st.button("FR", key="fr_button", use_container_width=True):
            st.session_state.language = "Français"
            st.rerun()
    
    # Tabs
    tabs = st.tabs([t['tab_feed'], t['tab_experience'], t['tab_skills'], t['tab_motivation'], t['tab_contact']])
    
    # Tab 1: Dream Feed (Instagram Style)
    with tabs[0]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{t['feed_title']}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Instagram-style grid
        cols = st.columns(3)
        for i in range(9):
            with cols[i % 3]:
                image_path = f"pics/{i+1}.jpeg"
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    st.image(image, use_container_width=True)
                else:
                    # Placeholder avec texte stylé
                    st.markdown(f"""
                    <div class="insta-card">
                        <div class="insta-placeholder">
                            <div class="insta-placeholder-icon">💄</div>
                            <div class="insta-placeholder-text">SEPHORA DREAM #{i+1}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
    
    # Tab 2: Experience
    with tabs[1]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{t['experience_title']}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Experience 1: ACE Money Transfer
        st.markdown(f"""
        <div class="experience-card">
            <div class="experience-header">
                <h3 class="experience-title">ACE Money Transfer</h3>
                <span class="experience-date">September 2023 - August 2025</span>
            </div>
            <div class="experience-content">
                <p class="experience-role">{t['ace_role']}</p>
                <ul class="experience-list">
                    <li class="experience-item">{t['ace_1']}</li>
                    <li class="experience-item">{t['ace_2']}</li>
                    <li class="experience-item">{t['ace_3']}</li>
                    <li class="experience-item">{t['ace_4']}</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Experience 2: EUREKA
        st.markdown(f"""
        <div class="experience-card">
            <div class="experience-header">
                <h3 class="experience-title">EUREKA Paris</h3>
                <span class="experience-date">September 2023</span>
            </div>
            <div class="experience-content">
                <p class="experience-role">{t['eureka_role']}</p>
                <ul class="experience-list">
                    <li class="experience-item">{t['eureka_1']}</li>
                    <li class="experience-item">{t['eureka_2']}</li>
                    <li class="experience-item">{t['eureka_3']}</li>
                    <li class="experience-item">{t['eureka_4']}</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Experience 3: BDE EFREI
        st.markdown(f"""
        <div class="experience-card">
            <div class="experience-header">
                <h3 class="experience-title">BDE EFREI</h3>
                <span class="experience-date">2023 - 2024</span>
            </div>
            <div class="experience-content">
                <p class="experience-role">{t['bde_role']}</p>
                <ul class="experience-list">
                    <li class="experience-item">{t['bde_1']}</li>
                    <li class="experience-item">{t['bde_2']}</li>
                    <li class="experience-item">{t['bde_3']}</li>
                    <li class="experience-item">{t['bde_4']}</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tab 3: Skills
    with tabs[2]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{t['skills_title']}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Skills Grid
        st.markdown(f"""
        <div class="skills-grid">
            <div class="skill-card">
                <h3 class="skill-title">{t['skills_data_processing']}</h3>
                <div class="skill-items">
                    Python<br>
                    SQL<br>
                    Excel<br>
                    Dataiku
                </div>
            </div>
            <div class="skill-card">
                <h3 class="skill-title">{t['skills_data_viz']}</h3>
                <div class="skill-items">
                    Power BI<br>
                    Tableau<br>
                    Excel Dashboards<br>
                    Google Data Studio
                </div>
            </div>
            <div class="skill-card">
                <h3 class="skill-title">{t['skills_cloud']}</h3>
                <div class="skill-items">
                    Azure Fundamentals (AZ-900)<br>
                    Azure AI Fundamentals (AI-900)<br>
                    Machine Learning Basics<br>
                    Cloud Architecture
                </div>
            </div>
            <div class="skill-card">
                <h3 class="skill-title">{t['skills_pm']}</h3>
                <div class="skill-items">
                    Jira<br>
                    Trello<br>
                    Agile Methodologies<br>
                    Team Leadership
                </div>
            </div>
            <div class="skill-card">
                <h3 class="skill-title">{t['skills_web']}</h3>
                <div class="skill-items">
                    Shopify<br>
                    WordPress<br>
                    Wix<br>
                    E-commerce Analytics
                </div>
            </div>
            <div class="skill-card">
                <h3 class="skill-title">{t['skills_languages']}</h3>
                <div class="skill-items">
                    French (Native)<br>
                    English (Fluent)<br>
                    Hindi (Native)<br>
                    International Mindset
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Soft Skills
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{t['skills_soft_title']}</h2>
            <div class="motivation-container">
                <p class="motivation-text">
                    <strong>{t['skills_leadership']}</strong><br><br>
                    <strong>{t['skills_analytical']}</strong><br><br>
                    <strong>{t['skills_communication']}</strong><br><br>
                    <strong>{t['skills_organization']}</strong>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tab 4: Motivation
    with tabs[3]:
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{t['motivation_title']}</h2>
            <div class="motivation-container">
                <p class="motivation-quote">
                    "{t['motivation_quote']}"
                </p>
                <p class="motivation-text">
                    {t['motivation_text1']}
                </p>
                <p class="motivation-text">
                    <strong>{t['motivation_bring_title']}</strong><br><br>
                    {t['motivation_bring_1']}<br>
                    {t['motivation_bring_2']}<br>
                    {t['motivation_bring_3']}<br>
                    {t['motivation_bring_4']}
                </p>
                <p class="motivation-text">
                    <strong>{t['motivation_goals_title']}</strong><br><br>
                    {t['motivation_goals_1']}<br>
                    {t['motivation_goals_2']}<br>
                    {t['motivation_goals_3']}<br>
                    {t['motivation_goals_4']}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Perfect Match
        st.markdown(f"""
        <div class="section-container">
            <h2 class="section-title">{t['perfect_match_title']}</h2>
            <div class="experience-card">
                <div class="experience-header">
                    <h3 class="experience-title">{t['perfect_match_subtitle']}</h3>
                </div>
                <div class="experience-content">
                    <ul class="experience-list">
                        <li class="experience-item"><strong>{t['perfect_match_1']}</strong></li>
                        <li class="experience-item"><strong>{t['perfect_match_2']}</strong></li>
                        <li class="experience-item"><strong>{t['perfect_match_3']}</strong></li>
                        <li class="experience-item"><strong>{t['perfect_match_4']}</strong></li>
                        <li class="experience-item"><strong>{t['perfect_match_5']}</strong></li>
                    </ul>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tab 5: Contact
    with tabs[4]:
        st.markdown(f"""
        <div class="contact-container">
            <h2 class="contact-title">{t['contact_title']}</h2>
            <div class="contact-info">
                <p>📧 yamina.ghani@efrei.net</p>
                <p>📱 07 68 11 53 52 62</p>
                <p>💼 <a href="https://www.linkedin.com/in/yamina-ghani/" class="contact-link">LinkedIn: Yamina Ghani</a></p>
                <p>📍 Paris, France</p>
                <p>🚗 Permis B</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Message personnalisé
        st.markdown(f"""
        <div class="section-container">
            <div class="motivation-container">
                <p class="motivation-quote">
                    "{t['contact_ready']}"
                </p>
                <p class="motivation-text">
                    {t['contact_available']}
                </p>
                <p class="motivation-text">
                    <strong>{t['contact_availability']}</strong><br>
                    <strong>{t['contact_location']}</strong><br>
                    <strong>{t['contact_motivation']}</strong>
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Call to action
        st.markdown(f"""
        <div style="text-align: center; margin-top: 3rem;">
            <a href="mailto:yamina.ghani@efrei.net" class="cta-button" style="text-decoration: none; color: white;">
                {t['contact_button']}
            </a>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div style="background-color: #000; color: #fff; padding: 2rem; text-align: center; margin-top: 4rem;">
        <p style="font-family: 'Cormorant Garamond', serif; font-size: 1.5rem; letter-spacing: 0.1em; margin-bottom: 1rem;">
            YAMINA GHANI
        </p>
        <p style="font-family: 'Montserrat', sans-serif; font-size: 0.9rem; font-weight: 300; letter-spacing: 0.05em;">
            {t['footer_text']}
        </p>
    </div>
    """, unsafe_allow_html=True)

# Point d'entrée
if __name__ == "__main__":
    main()