from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Create necessary directories if they don't exist
os.makedirs(os.path.join(app.root_path, 'static', 'images'), exist_ok=True)


@app.route('/')
def index():
    languages = {
        'en': 'English',
        'el': 'Ελληνικά',
        'es': 'Español'
    }
    current_lang = request.args.get('lang', 'en')
    if current_lang not in languages:
        current_lang = 'en'

    ui_translations = {
        'en': {
            'about': 'About Me',
            'education': 'Education',
            'languages': 'Languages',
            'professional_experience': 'Professional Experience',
            'skills': 'Professional Skills & Certifications',
            'projects': 'Selected Projects',
            'citizen_science': 'Citizen Science',
            'visit': 'Visit',
            'ceo_of': 'CEO of',
            'learn_more': 'Learn More',
            'contact': 'CONTACT',
            'status': 'STATUS',
            'available': 'Available for Security Consulting & AI Governance Projects',
            'copyright': '2024 Professional Profile. All rights reserved.',
            'education_name': 'Military School of Telecommunications',
            'language_names': ['Greek', 'English', 'Spanish']
        },
        'el': {
            'about': 'Σχετικά με εμένα',
            'education': 'Εκπαίδευση',
            'languages': 'Γλώσσες',
            'professional_experience': 'Επαγγελματική Εμπειρία',
            'skills': 'Επαγγελματικές Δεξιότητες & Πιστοποιήσεις',
            'projects': 'Επιλεγμένα Έργα',
            'citizen_science': 'Επιστήμη Πολιτών',
            'visit': 'Επίσκεψη',
            'ceo_of': 'CEO της',
            'learn_more': 'Μάθετε Περισσότερα',
            'contact': 'ΕΠΙΚΟΙΝΩΝΙΑ',
            'status': 'ΚΑΤΑΣΤΑΣΗ',
            'available': 'Διαθέσιμος για έργα Συμβουλευτικής Ασφάλειας και Διακυβέρνησης AI',
            'copyright': '2024 Επαγγελματικό Προφίλ. Με επιφύλαξη παντός δικαιώματος.',
            'education_name': 'Στρατιωτική Σχολή Τηλεπικοινωνιών',
            'language_names': ['Ελληνικά', 'Αγγλικά', 'Ισπανικά']
        },
        'es': {
            'about': 'Sobre mí',
            'education': 'Educación',
            'languages': 'Idiomas',
            'professional_experience': 'Experiencia Profesional',
            'skills': 'Competencias Profesionales y Certificaciones',
            'projects': 'Proyectos Seleccionados',
            'citizen_science': 'Ciencia Ciudadana',
            'visit': 'Visitar',
            'ceo_of': 'CEO de',
            'learn_more': 'Más información',
            'contact': 'CONTACTO',
            'status': 'ESTADO',
            'available': 'Disponible para consultoría de seguridad y proyectos de gobernanza de IA',
            'copyright': '2024 Perfil profesional. Todos los derechos reservados.',
            'education_name': 'Escuela Militar de Telecomunicaciones',
            'language_names': ['Griego', 'Inglés', 'Español']
        }
    }

    # Professional data
    profile_data = {
        'name': 'Security Professional',
        'title': 'Information Systems Security Manager - Cyber Security - ML/AI Consultant - VAPT - Researcher',
        'brand': {
            'name': 'CyberPhylax',
            'url': 'https://cyberphylax.com',
            'role': 'Founder',
            'description': 'Leading CyberPhylax Offensive Security with a mission to detect, prevent, and defend modern AI-enabled organizations against modern threats.',
            'logo': 'images/cyberphylax-logo.png',
            'emblem': 'images/cyberphylax-emblem.png'
        },
        'about': """Over twenty years of progressive Information Security Technology leadership experience encompassing a significant depth of professional services, systems development and technology management. Result oriented management style, capable of building and motivating teams with a profound sense of urgency towards realizing a shared corporate vision and mission. Quality focused and passionate in pursuit of excellence.

As a former military professional, I bring discipline, structure, mission focus, and a deep sense of responsibility to every environment I serve. That background continues to shape how I lead teams, manage risk, perform under pressure, and approach complex operational challenges. It reinforced values that remain central to my professional identity: integrity, preparedness, resilience, precision, and commitment to duty.

My expertise spans cybersecurity, infrastructure architecture, systems analysis, disaster recovery, quality assurance, strategic planning, organizational design, vendor management, budgeting, asset management, customer service, team leadership, and cost optimization, backed by deep technical experience in malware analysis, reverse engineering, ethical hacking, penetration testing, and cyber forensics. I excel at aligning technical depth with business priorities and turning complexity into practical strategy, resilient operations, and measurable results.

In recent years, I have expanded my main focus into artificial intelligence, AI governance, and the secure design of autonomous systems. My work and interests in this space include prompt engineering, AI behavior auditing, model integrity, agent workflow design, AI orchestration, prompt injection analysis, adversarial AI defense, model exploit research, LLM security, and AI-driven process transformation. I am particularly interested in helping organizations adopt advanced AI capabilities in ways that remain secure, controlled, auditable, and aligned with operational and business realities.

Beyond my professional responsibilities, I am also a community instructor, amateur astronomer, contributor to the development of astronomical and scientific applications using AI, active participant in astronomy-related scientific programs as a citizen scientist, and involved in astronomy outreach and science communication. These activities reflect the same values that define my professional path: discipline, curiosity, lifelong learning, principled leadership, and a strong belief in using technology and knowledge to create meaningful and lasting impact.""",

        'experience': [
            {
                'title': 'IT Information Systems Security Manager - Cyber Security & AI/ML Consultant',
                'company': 'UNIXFOR S.A',
                'duration': 'Mar 2004 - Present · 22 yrs 3 mos',
                'location': 'Greece - Athens',
                'icon': 'fas fa-shield-alt',
                'description': 'At UNIXFOR S.A., I work at the intersection of AI governance, cybersecurity, digital transformation, and secure technology operations, helping deliver resilient and practical solutions across complex business and operational environments.\n\nWith more than 13 years of experience in Information Security Management, my focus is on ensuring that emerging technologies, security controls, and operational processes are aligned with real business needs, regulatory expectations, and long-term sustainability. A key part of my role involves supporting the responsible and secure adoption of AI-driven capabilities, including AI governance, Agentic AI, and machine learning-related initiatives, with emphasis on risk management, accountability, oversight, and practical implementation.\n\nIn parallel, I contribute to the strengthening of cybersecurity posture across infrastructure, systems, and operational workflows. My work includes risk assessments, vulnerability analysis, policy development, compliance support, control design, security testing, user awareness, and the implementation of practical countermeasures against evolving threats.\n\nMy broader technical background includes technical architecture, UNIX/Linux and Windows systems, virtualization, cloud computing, networking, and operations management, allowing me to bridge strategy with execution and governance with operational reality.'
            },
            {
                'title': 'Unix Systems Engineer',
                'company': 'FIRST TELECOM S.A',
                'duration': 'Mar 2003 - Mar 2004 · 1 yr 1 mo',
                'location': 'Greece',
                'icon': 'fas fa-server',
                'description': 'Hands-on Network administration manager, with converged-network designs for the internet users. Responsible for the design and implementation of First telecoms ADSL network. Designed and operated the companys Data Center and communication infrastructure. Emphasis in Internet VOIP services, and client connectivity to companys voice network with secure gateways and high SLAs. Responsible for leading teams of Consultants, Engineers and Project Managers in Systems and e-commerce rollouts.'
            },
            {
                'title': 'Unix Systems Engineer and Network Operations',
                'company': 'STS-Net',
                'duration': 'Jan 2002 - Mar 2003 · 1 yr 3 mos',
                'location': 'Greece',
                'icon': 'fas fa-network-wired',
                'description': 'Directed and designed all network backbones, system architecture and IT staff. In charge of all aspects of large and small projects for various clients including involvement in initial marketing, development of presentations, physical layer design and installation of systems, client training, and maintenance of completed systems.'
            },
            {
                'title': 'Unix Systems Engineer & IT Manager',
                'company': 'Servcom Ltd.',
                'duration': 'Jan 2001 - Jan 2002 · 1 yr 1 mo',
                'location': 'Greece',
                'icon': 'fas fa-cogs',
                'description': 'Managing and maintaining Unix networks. Leading companys IT department: I was responsible for the maintenance of a network of SCO Unix computer systems, supporting applications in rm-cobol, that belonged to various shipping, insurance agencies, municipal government agencies, hospital units, Hellenic air-lines etc.'
            },
            {
                'title': 'Telecommunication Engineer',
                'company': 'Hellenic Army',
                'duration': 'Dec 1995 - Dec 2000 · 5 yrs 1 mo',
                'location': 'Greece',
                'icon': 'fas fa-military',
                'description': 'Responsible for a team of military engineers in preserving the army supplies in readiness. I was awarded the highest honors from the Unit\'s General as the most Valuable Team Leader.'
            }
        ],

        'skills': [
            'Advanced Malware Analysis: Ransomware',
            'Business Continuity Management',
            'Communications and Network Security',
            'Designing and implementing security Policies',
            'Ethical Hacking: Malware threats',
            'Ethical Hacking: Penetration Testing',
            'GDPR: the big picture',
            'Hacking the Human',
            'Introduction to Penetration Testing Using Metasploit',
            'Malicious Code and Threats',
            'Malware analysis and detection',
            'Malware analysis fundamentals',
            'Network security Monitoring (NSM) with security Onion',
            'Penetration Testing and Ethical Hacking with Kali Linux',
            'Penetration testing with the Metasploit framework',
            'Penetration testing – Life Cycle Explained',
            'Physical Security',
            'Risk Assessment and Management',
            'Security Awareness: Phishing',
            'Security Awareness: Portable data protection and destruction',
            'Security Management',
            'Security Operations',
            'Web application penetration testing'
        ],
        'projects': [
            {
                'name': 'HashWhisper',
                'description': 'A deep analysis tool for advanced hashing and cryptographic workflow automation.',
                'url': 'https://github.com/ibsoft/HashWhisper',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/HashWhisper'
            },
            {
                'name': 'SkyFrame',
                'description': 'A cloud-native orchestration framework for observability and deployment control.',
                'url': 'https://github.com/ibsoft/SkyFrame',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/SkyFrame'
            },
            {
                'name': 'helpdesk_pro',
                'description': 'A professional support ticketing and helpdesk platform for enterprise teams.',
                'url': 'https://github.com/ibsoft/helpdesk_pro',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/helpdesk_pro'
            },
            {
                'name': 'CloudRollouts',
                'description': 'Software release management tooling for cloud-based feature rollouts and canary deployments.',
                'url': 'https://github.com/ibsoft/CloudRollouts',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/CloudRollouts'
            },
            {
                'name': 'SkyFrame',
                'description': 'A cloud-native orchestration framework for observability and deployment control.',
                'url': 'https://github.com/ibsoft/SkyFrame',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/SkyFrame'
            },
            {
                'name': 'helpdesk_pro',
                'description': 'A professional support ticketing and helpdesk platform for enterprise teams.',
                'url': 'https://github.com/ibsoft/helpdesk_pro',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/helpdesk_pro'
            },
            {
                'name': 'CloudRollouts',
                'description': 'Software release management tooling for cloud-based feature rollouts and canary deployments.',
                'url': 'https://github.com/ibsoft/CloudRollouts',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/CloudRollouts'
            },
            {
                'name': 'CipherDrop',
                'description': 'Secure secret exchange and encrypted communication tooling for sensitive operations.',
                'url': 'https://github.com/ibsoft/CipherDrop',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/CipherDrop'
            },
            {
                'name': 'ELE',
                'description': 'An enterprise-level engineering platform for secure system design and collaboration.',
                'url': 'https://github.com/ibsoft/ELE',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/ELE'
            },
            {
                'name': 'JAIID_WEB',
                'description': 'AI-enabled frontend for JΑΙΙD, bringing Jovian impact flash detection insights to a modern web interface.',
                'url': 'https://github.com/ibsoft/JAIID_WEB',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/JAIID_WEB'
            },
            {
                'name': 'JAIID',
                'description': 'Jovian Artificial Intelligence Impact Detector for real-time detection and analysis of Jupiter impact flashes.',
                'url': 'https://github.com/ibsoft/JAIID',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/JAIID'
            },
            {
                'name': 'GnuProxy',
                'description': 'A powerful proxy solution for GNU/Linux environments with advanced security and routing.',
                'url': 'https://github.com/ibsoft/GnuProxy',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/GnuProxy'
            },
            {
                'name': 'BlackFox',
                'description': 'A stealthy security and monitoring toolkit designed for advanced defensive operations.',
                'url': 'https://github.com/ibsoft/BlackFox',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/BlackFox'
            }
        ],
        'citizen_science': {
            'title': 'Jovian Impact Flash Detection & Amateur Astronomy',
            'description': 'As an active citizen scientist and amateur astronomer, I contribute to the development and application of AI-driven astronomical research. My work includes participating in citizen science programs focused on Jupiter impact monitoring and detection. Through JAIID (Jovian Artificial Intelligence Impact Detector), I bridge the gap between professional scientific methods and community-driven discovery, leveraging advanced AI models to enhance our understanding of celestial events and contribute to the broader scientific community.',
            'url': 'https://github.com/ibsoft/JAIID',
            'image': 'static/images/jaid.jpg'
        }
    }

    localized_profile = {
        'el': {
            'title': 'Διαχειριστής Ασφάλειας Πληροφοριακών Συστημάτων - Κυβερνοασφάλεια - Σύμβουλος ML/AI - VAPT - Ερευνητής',
            'brand': {
                'role': 'Ιδρυτής',
                'description': 'Ηγεσία της CyberPhylax Offensive Security με αποστολή τον εντοπισμό, την πρόληψη και την άμυνα σύγχρονων οργανισμών που αξιοποιούν AI απέναντι σε σύγχρονες απειλές.'
            },
            'about': """Πάνω από είκοσι χρόνια εμπειρίας στον χώρο της τεχνολογίας και της ασφάλειας πληροφοριών, με πορεία που συνδυάζει επαγγελματικές υπηρεσίες, ανάπτυξη συστημάτων και τεχνολογική διοίκηση. Στη δουλειά μου με ενδιαφέρει το αποτέλεσμα, αλλά όχι με οποιονδήποτε τρόπο. Δίνω μεγάλη σημασία στην ποιότητα, στη συνέπεια και στη δημιουργία ομάδων που μπορούν να κινηθούν με κοινή κατεύθυνση, καθαρό στόχο και πραγματική αίσθηση ευθύνης.

Η στρατιωτική μου εμπειρία έχει επηρεάσει βαθιά τον τρόπο με τον οποίο εργάζομαι και ηγούμαι. Μου έδωσε πειθαρχία, δομή, επιχειρησιακή σκέψη και δυνατότητα να λειτουργώ με ψυχραιμία κάτω από πίεση. Αυτά τα στοιχεία εξακολουθούν να με καθοδηγούν στον τρόπο που διαχειρίζομαι κινδύνους, παίρνω αποφάσεις και αντιμετωπίζω σύνθετες τεχνικές και επιχειρησιακές προκλήσεις.

Η εμπειρία μου καλύπτει τομείς όπως κυβερνοασφάλεια, αρχιτεκτονική υποδομών, ανάλυση συστημάτων, disaster recovery, διασφάλιση ποιότητας, στρατηγικός σχεδιασμός, οργανωτικός σχεδιασμός, διαχείριση προμηθευτών, προϋπολογισμός, asset management, εξυπηρέτηση πελατών, ηγεσία ομάδων και βελτιστοποίηση κόστους. Παράλληλα, έχω ισχυρό τεχνικό υπόβαθρο σε malware analysis, reverse engineering, ethical hacking, penetration testing και digital forensics.

Τα τελευταία χρόνια το ενδιαφέρον μου έχει στραφεί όλο και περισσότερο στην τεχνητή νοημοσύνη, στη διακυβέρνηση AI και στον ασφαλή σχεδιασμό αυτόνομων συστημάτων. Ασχολούμαι με prompt engineering, έλεγχο συμπεριφοράς AI, model integrity, agent workflows, AI orchestration, prompt injection analysis, adversarial AI defense, model exploit research, LLM security και αξιοποίηση της AI για τον μετασχηματισμό επιχειρησιακών διαδικασιών.

Πέρα από την επαγγελματική μου δραστηριότητα, συμμετέχω ενεργά σε δράσεις εκπαίδευσης, επιστήμης και τεχνολογίας. Είμαι εκπαιδευτής κοινότητας, ερασιτέχνης αστρονόμος, συνεισφέρω στην ανάπτυξη αστρονομικών και επιστημονικών εφαρμογών με AI και συμμετέχω σε προγράμματα αστρονομίας ως πολίτης επιστήμονας (citizen scientist). Με ενδιαφέρει ιδιαίτερα η σύνδεση της επιστήμης με την κοινότητα και η διάδοση της γνώσης με τρόπο πρακτικό, αξιόπιστο και ουσιαστικό.""",
            'citizen_science': {
                'title': 'Ανίχνευση λάμψεων πρόσκρουσης στον Δία και ερασιτεχνική αστρονομία',
                'description': """Ως ενεργός πολίτης επιστήμονας (citizen scientist) και ερασιτέχνης αστρονόμος, συμμετέχω σε δράσεις που συνδυάζουν την παρατήρηση του ουρανού, την επιστημονική μεθοδολογία και την τεχνητή νοημοσύνη. Το ενδιαφέρον μου εστιάζει ιδιαίτερα στην παρακολούθηση του Δία και στην ανίχνευση πιθανών λάμψεων πρόσκρουσης, ένα πεδίο όπου οι ερασιτέχνες αστρονόμοι μπορούν να προσφέρουν πραγματική αξία στην επιστημονική κοινότητα.

Μέσω του JAIID, συμβάλλω στη σύνδεση της ερασιτεχνικής αστρονομίας με πιο οργανωμένες και επαγγελματικές μεθόδους ανάλυσης. Στόχος μου είναι οι παρατηρήσεις της κοινότητας να μπορούν να αξιοποιούνται με πιο δομημένο, αξιόπιστο και επιστημονικά χρήσιμο τρόπο, υποστηρίζοντας τη συνεργασία ανάμεσα σε τεχνολογία, επιστήμη και ανθρώπινη περιέργεια."""
            }
        },
        'es': {
            'title': 'Responsable de Seguridad de Sistemas de Información - Ciberseguridad - Consultor ML/IA - VAPT - Investigador',
            'brand': {
                'role': 'Fundador',
                'description': """Lidero CyberPhylax Offensive Security con una misión clara: ayudar a las organizaciones modernas, cada vez más impulsadas por IA, a detectar riesgos reales, prevenir incidentes y fortalecer sus defensas frente a las amenazas actuales.

CyberPhylax nace con la idea de ir más allá de los análisis superficiales. Su enfoque combina pruebas de seguridad autorizadas, criterio humano, metodologías estructuradas y apoyo de inteligencia artificial para ofrecer evaluaciones más claras, útiles y orientadas a la reducción real del riesgo."""
            },
            'about': """Más de veinte años de experiencia en liderazgo tecnológico y seguridad de la información, combinando servicios profesionales, desarrollo de sistemas y gestión de tecnología. A lo largo de mi carrera he trabajado con un enfoque claro en resultados, calidad y mejora continua, siempre procurando formar equipos sólidos, motivados y alineados con una visión común.

Mi trayectoria en el ámbito militar marcó profundamente mi forma de liderar, trabajar bajo presión y asumir responsabilidades. Me ha dado disciplina, estructura, sentido de misión y una fuerte responsabilidad ante cada reto. Esa experiencia sigue siendo parte de mi manera de liderar, tomar decisiones bajo presión, gestionar riesgos y afrontar situaciones operativas complejas.

Mi experiencia cubre áreas como ciberseguridad, arquitectura de infraestructuras, análisis de sistemas, recuperación ante desastres, aseguramiento de calidad, planificación estratégica, diseño organizativo, gestión de proveedores, presupuestos, gestión de activos, atención al cliente, liderazgo de equipos y optimización de costes. También cuento con una sólida base técnica en análisis de malware, ingeniería inversa, hacking ético, pruebas de penetración y análisis forense digital.

En los últimos años, mi foco se ha ampliado hacia la inteligencia artificial, la gobernanza de IA y el diseño seguro de sistemas autónomos. Me interesan especialmente la ingeniería de prompts, la auditoría del comportamiento de sistemas de IA, la integridad de modelos, el diseño de flujos con agentes, la orquestación de IA, la defensa frente a ataques de prompt injection, la seguridad de LLM, la investigación de riesgos en modelos y la transformación de procesos mediante IA.

Más allá de mi actividad profesional, participo activamente en iniciativas de divulgación y ciencia ciudadana. Soy instructor comunitario, astrónomo aficionado, colaborador en el desarrollo de aplicaciones astronómicas y científicas con IA, y promotor de proyectos que acercan la ciencia y la tecnología a más personas.""",
            'experience': [
                {
                    'title': 'IT Information Systems Security Manager - Cyber Security & AI/ML Consultant',
                    'company': 'UNIXFOR S.A.',
                    'duration': 'Marzo de 2004 - Actualidad · 22 años 3 meses',
                    'location': 'Atenas, Grecia',
                    'icon': 'fas fa-shield-alt',
                    'description': """En UNIXFOR S.A. trabajo en la intersección entre gobernanza de inteligencia artificial, ciberseguridad, transformación digital y operaciones tecnológicas seguras. Mi objetivo es ayudar a diseñar y mantener soluciones prácticas, resilientes y alineadas con las necesidades reales del negocio, incluso en entornos operativos complejos.

Durante más de 13 años de experiencia en gestión de seguridad de la información, me he centrado en asegurar que las tecnologías emergentes, los controles de seguridad y los procesos operativos no funcionen de forma aislada, sino conectados con la estrategia, los requisitos regulatorios y la sostenibilidad a largo plazo de la organización.

Una parte importante de mi trabajo actual está relacionada con la adopción responsable y segura de capacidades basadas en IA, incluyendo gobernanza de IA, Agentic AI e iniciativas vinculadas a machine learning. En este contexto, mi enfoque está en la gestión del riesgo, la responsabilidad, la supervisión humana, la trazabilidad y la implementación práctica, no solo en la innovación por sí misma.

En paralelo, contribuyo al fortalecimiento de la postura de ciberseguridad en infraestructuras, sistemas y flujos operativos. Mi trabajo incluye evaluaciones de riesgo, análisis de vulnerabilidades, desarrollo de políticas, apoyo en cumplimiento normativo, diseño de controles, pruebas de seguridad, concienciación de usuarios y aplicación de medidas prácticas frente a amenazas en constante evolución.

Mi experiencia técnica más amplia incluye arquitectura tecnológica, sistemas UNIX/Linux y Windows, virtualización, cloud computing, redes y gestión de operaciones. Esto me permite conectar la estrategia con la ejecución, y la gobernanza con la realidad diaria de los sistemas y equipos técnicos."""
                },
                {
                    'title': 'Unix Systems Engineer',
                    'company': 'FIRST TELECOM S.A.',
                    'duration': 'Marzo de 2003 - Marzo de 2004 · 1 año 1 mes',
                    'location': 'Grecia',
                    'icon': 'fas fa-server',
                    'description': """En FIRST TELECOM S.A. trabajé como ingeniero de sistemas Unix con un rol muy práctico en administración de redes, diseño de infraestructuras convergentes y soporte de servicios de conectividad para usuarios de internet.

Fui responsable del diseño y la implementación de la red ADSL de la compañía, así como del diseño, operación y mantenimiento de su Data Center y de la infraestructura de comunicaciones. Mi trabajo tuvo un fuerte enfoque en servicios de internet, VoIP y conectividad segura de clientes hacia la red de voz de la empresa, manteniendo altos niveles de disponibilidad y calidad de servicio.

También participé en la coordinación de equipos de consultores, ingenieros y project managers para despliegues de sistemas, soluciones de e-commerce e infraestructuras tecnológicas orientadas a clientes."""
                },
                {
                    'title': 'Unix Systems Engineer and Network Operations',
                    'company': 'STS-Net',
                    'duration': 'Enero de 2002 - Marzo de 2003 · 1 año 3 meses',
                    'location': 'Grecia',
                    'icon': 'fas fa-network-wired',
                    'description': """En STS-Net fui responsable del diseño y dirección de backbones de red, arquitectura de sistemas y coordinación del equipo técnico de IT. Participé en proyectos de diferentes tamaños para clientes diversos, cubriendo tanto la fase inicial de análisis y presentación como el diseño físico, la instalación, la formación de usuarios y el mantenimiento posterior de los sistemas implementados.

Este rol me permitió trabajar muy cerca de la operación real de redes y sistemas, combinando diseño técnico, ejecución en campo, soporte al cliente y gestión de equipos."""
                },
                {
                    'title': 'Unix Systems Engineer & IT Manager',
                    'company': 'Servcom Ltd.',
                    'duration': 'Enero de 2001 - Enero de 2002 · 1 año 1 mes',
                    'location': 'Grecia',
                    'icon': 'fas fa-cogs',
                    'description': """En Servcom Ltd. gestioné y mantuve redes Unix, liderando el departamento de IT de la compañía. Fui responsable del mantenimiento de una red de sistemas SCO Unix que daban soporte a aplicaciones desarrolladas en RM/COBOL para distintos tipos de organizaciones.

Los entornos que atendíamos incluían compañías navieras, agencias de seguros, organismos municipales, unidades hospitalarias, aerolíneas y otros clientes con necesidades operativas críticas. Esta experiencia reforzó mi capacidad para trabajar con sistemas legacy, entornos de producción sensibles y clientes que dependían directamente de la estabilidad de sus plataformas tecnológicas."""
                },
                {
                    'title': 'Telecommunication Engineer',
                    'company': 'Hellenic Army',
                    'duration': 'Diciembre de 1995 - Diciembre de 2000 · 5 años 1 mes',
                    'location': 'Grecia',
                    'icon': 'fas fa-military',
                    'description': """En el Hellenic Army trabajé como ingeniero de telecomunicaciones, liderando un equipo de ingenieros militares responsable de mantener equipamiento, sistemas y suministros en estado operativo y preparados para su uso.

Esta etapa fue fundamental para mi desarrollo profesional y personal. Me enseñó disciplina, responsabilidad, liderazgo bajo presión y orientación a la misión. Durante mi servicio, recibí el máximo reconocimiento de la Unidad por parte del General como Most Valuable Team Leader, un honor que refleja el compromiso, la fiabilidad y el desempeño del equipo que tuve la responsabilidad de liderar."""
                }
            ],
            'citizen_science': {
                'title': 'Detección de destellos de impacto en Júpiter y astronomía amateur',
                'description': """Como científico ciudadano activo y astrónomo aficionado, participo en proyectos que combinan astronomía, investigación científica e inteligencia artificial. Mi trabajo se centra especialmente en el monitoreo de Júpiter y en la detección de posibles destellos de impacto, un área donde la colaboración entre astrónomos aficionados y la comunidad científica puede aportar información valiosa.

A través de JAIID, contribuyo a acercar métodos científicos profesionales a la astronomía amateur, facilitando que las observaciones realizadas por la comunidad puedan analizarse de forma más estructurada y útil. Para mí, este tipo de trabajo demuestra cómo la ciencia ciudadana, la tecnología y la pasión por la exploración espacial pueden trabajar juntas para apoyar nuevos descubrimientos."""
            }
        }
    }

    for key, value in localized_profile.get(current_lang, {}).items():
        if isinstance(value, dict):
            profile_data[key].update(value)
        else:
            profile_data[key] = value

    return render_template(
        'index.html',
        data=profile_data,
        ui=ui_translations[current_lang],
        languages=languages,
        current_lang=current_lang
    )


if __name__ == '__main__':
    app.run(debug=True)
