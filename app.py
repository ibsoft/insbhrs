from datetime import date
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Create necessary directories if they don't exist
os.makedirs(os.path.join(app.root_path, 'static', 'images'), exist_ok=True)


def experience_duration(range_label, start_year, start_month, end_year=None, end_month=None, language='en'):
    end = date.today() if end_year is None or end_month is None else date(end_year, end_month, 1)
    total_months = ((end.year - start_year) * 12) + (end.month - start_month) + 1
    years, months = divmod(total_months, 12)

    if language == 'el':
        parts = []
        if years:
            parts.append(f"{years} {'έτος' if years == 1 else 'έτη'}")
        if months:
            parts.append(f"{months} {'μήνας' if months == 1 else 'μήνες'}")
    elif language == 'es':
        parts = []
        if years:
            parts.append(f"{years} {'año' if years == 1 else 'años'}")
        if months:
            parts.append(f"{months} {'mes' if months == 1 else 'meses'}")
    else:
        parts = []
        if years:
            parts.append(f"{years} {'yr' if years == 1 else 'yrs'}")
        if months:
            parts.append(f"{months} {'mo' if months == 1 else 'mos'}")

    return f"{range_label} · {' '.join(parts)}"


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
            'projects_intro': 'A selection of security, AI, infrastructure, and citizen-science projects from my public GitHub work.',
            'featured': 'Featured',
            'github_profile': 'Go to my GitHub page',
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
            'projects_intro': 'Μια επιλογή έργων ασφάλειας, τεχνητής νοημοσύνης, υποδομών και επιστήμης πολιτών από τη δημόσια δουλειά μου στο GitHub.',
            'featured': 'Προτεινόμενο',
            'github_profile': 'Μετάβαση στη σελίδα μου στο GitHub',
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
            'projects_intro': 'Una selección de proyectos de seguridad, inteligencia artificial, infraestructura y ciencia ciudadana de mi trabajo público en GitHub.',
            'featured': 'Destacado',
            'github_profile': 'Ir a mi página de GitHub',
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
                'duration': experience_duration('Mar 2004 - Present', 2004, 3),
                'location': 'Greece - Athens',
                'icon': 'fas fa-shield-alt',
                'description': 'At UNIXFOR S.A., I work at the intersection of AI governance, cybersecurity, digital transformation, and secure technology operations, helping deliver resilient and practical solutions across complex business and operational environments.\n\nWith more than 13 years of experience in Information Security Management, my focus is on ensuring that emerging technologies, security controls, and operational processes are aligned with real business needs, regulatory expectations, and long-term sustainability. A key part of my role involves supporting the responsible and secure adoption of AI-driven capabilities, including AI governance, Agentic AI, and machine learning-related initiatives, with emphasis on risk management, accountability, oversight, and practical implementation.\n\nIn parallel, I contribute to the strengthening of cybersecurity posture across infrastructure, systems, and operational workflows. My work includes risk assessments, vulnerability analysis, policy development, compliance support, control design, security testing, user awareness, and the implementation of practical countermeasures against evolving threats.\n\nMy broader technical background includes technical architecture, UNIX/Linux and Windows systems, virtualization, cloud computing, networking, and operations management, allowing me to bridge strategy with execution and governance with operational reality.'
            },
            {
                'title': 'Unix Systems Engineer',
                'company': 'FIRST TELECOM S.A',
                'duration': experience_duration('Mar 2003 - Mar 2004', 2003, 3, 2004, 3),
                'location': 'Greece',
                'icon': 'fas fa-server',
                'description': 'Hands-on Network administration manager, with converged-network designs for the internet users. Responsible for the design and implementation of First telecoms ADSL network. Designed and operated the companys Data Center and communication infrastructure. Emphasis in Internet VOIP services, and client connectivity to companys voice network with secure gateways and high SLAs. Responsible for leading teams of Consultants, Engineers and Project Managers in Systems and e-commerce rollouts.'
            },
            {
                'title': 'Unix Systems Engineer and Network Operations',
                'company': 'STS-Net',
                'duration': experience_duration('Jan 2002 - Mar 2003', 2002, 1, 2003, 3),
                'location': 'Greece',
                'icon': 'fas fa-network-wired',
                'description': 'Directed and designed all network backbones, system architecture and IT staff. In charge of all aspects of large and small projects for various clients including involvement in initial marketing, development of presentations, physical layer design and installation of systems, client training, and maintenance of completed systems.'
            },
            {
                'title': 'Unix Systems Engineer & IT Manager',
                'company': 'Servcom Ltd.',
                'duration': experience_duration('Jan 2001 - Jan 2002', 2001, 1, 2002, 1),
                'location': 'Greece',
                'icon': 'fas fa-cogs',
                'description': 'Managing and maintaining Unix networks. Leading companys IT department: I was responsible for the maintenance of a network of SCO Unix computer systems, supporting applications in rm-cobol, that belonged to various shipping, insurance agencies, municipal government agencies, hospital units, Hellenic air-lines etc.'
            },
            {
                'title': 'Telecommunication Engineer',
                'company': 'Hellenic Army',
                'duration': experience_duration('Dec 1995 - Dec 2000', 1995, 12, 2000, 12),
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
                'description': 'A secure chat application for private conversations, using hash-based access so only participants with the shared secret can enter and read the protected messages.',
                'url': 'https://github.com/ibsoft/HashWhisper',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/HashWhisper',
                'tags': ['Security', 'Secure Chat', 'Privacy'],
                'featured': True
            },
            {
                'name': 'SkyFrame',
                'description': 'An astronomical image gallery for organizing and presenting sky captures, observations, and visual astronomy material in a clean web interface.',
                'url': 'https://github.com/ibsoft/SkyFrame',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/SkyFrame',
                'tags': ['Astronomy', 'Gallery', 'Web App']
            },
            {
                'name': 'helpdesk_pro',
                'description': 'An IT helpdesk ticketing system for tracking support requests, managing incidents, and keeping technical service workflows organized.',
                'url': 'https://github.com/ibsoft/helpdesk_pro',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/helpdesk_pro',
                'tags': ['ITSM', 'Helpdesk', 'Operations'],
                'featured': True
            },
            {
                'name': 'CloudRollouts',
                'description': 'A fleet update rollout server for coordinating staged software updates, controlled deployments, and operational release management across many systems.',
                'url': 'https://github.com/ibsoft/CloudRollouts',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/CloudRollouts',
                'tags': ['DevOps', 'Deployments', 'Automation']
            },
            {
                'name': 'CipherDrop',
                'description': 'A one-time, end-to-end encrypted drop system for safely sending sensitive information without leaving long-lived exposed messages behind.',
                'url': 'https://github.com/ibsoft/CipherDrop',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/CipherDrop',
                'tags': ['Security', 'Encryption', 'Privacy']
            },
            {
                'name': 'ELE',
                'description': 'An AI assistant project focused on practical automation, interactive support, and intelligent task handling through a simple application interface.',
                'url': 'https://github.com/ibsoft/ELE',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/ELE',
                'tags': ['AI', 'Assistant', 'Automation']
            },
            {
                'name': 'JAIID_WEB',
                'description': 'The web interface for JAIID, bringing artificial intelligence impact detection results and astronomy analysis tools into an accessible browser experience.',
                'url': 'https://github.com/ibsoft/JAIID_WEB',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/JAIID_WEB',
                'tags': ['AI', 'Astronomy', 'Web App']
            },
            {
                'name': 'JAIID',
                'description': 'The Jovian Artificial Intelligence Impact Detector, an AI-assisted astronomy project for identifying and analyzing possible impact flashes on Jupiter.',
                'url': 'https://github.com/ibsoft/JAIID',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/JAIID',
                'tags': ['AI', 'Astronomy', 'Citizen Science'],
                'featured': True
            },
            {
                'name': 'GnuProxy',
                'description': 'A secure Postfix mail proxy frontend for building an SMTP gateway between a mail server and the internet with stronger filtering and protection controls.',
                'url': 'https://github.com/ibsoft/GnuProxy',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/GnuProxy',
                'tags': ['Mail Security', 'Postfix', 'Infrastructure']
            },
            {
                'name': 'BlackFox',
                'description': 'A Bash-based administration tool that builds bad-reputation blocking lists for NGINX, Apache, and UFW Firewall using data from 218 list providers.',
                'url': 'https://github.com/ibsoft/BlackFox',
                'image': 'https://opengraph.githubassets.com/1/ibsoft/BlackFox',
                'tags': ['Security', 'Bash', 'Firewall'],
                'featured': True
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
            'experience': [
                {
                    'title': 'Διαχειριστής Ασφάλειας Πληροφοριακών Συστημάτων - Κυβερνοασφάλεια & Σύμβουλος AI/ML',
                    'company': 'UNIXFOR S.A.',
                    'duration': experience_duration('Μάρτιος 2004 - Σήμερα', 2004, 3, language='el'),
                    'location': 'Αθήνα, Ελλάδα',
                    'icon': 'fas fa-shield-alt',
                    'description': """Στην UNIXFOR S.A. εργάζομαι στο σημείο όπου συναντιούνται η κυβερνοασφάλεια, η διακυβέρνηση τεχνητής νοημοσύνης, ο ψηφιακός μετασχηματισμός και η ασφαλής λειτουργία τεχνολογικών υποδομών. Ο ρόλος μου είναι να βοηθώ στη δημιουργία λύσεων που δεν είναι μόνο τεχνικά σωστές, αλλά και πρακτικές, ανθεκτικές και ευθυγραμμισμένες με τις πραγματικές ανάγκες της επιχείρησης.

Με πολυετή εμπειρία στη διαχείριση ασφάλειας πληροφοριών, δίνω έμφαση στη σύνδεση των τεχνολογιών, των ελέγχων ασφαλείας και των διαδικασιών με τη στρατηγική, τη συμμόρφωση και τη βιωσιμότητα του οργανισμού. Τα τελευταία χρόνια σημαντικό μέρος της δουλειάς μου αφορά την υπεύθυνη και ασφαλή υιοθέτηση λύσεων AI, Agentic AI και machine learning, με έμφαση στη διαχείριση κινδύνου, τη λογοδοσία, την επίβλεψη και την πρακτική εφαρμογή.

Παράλληλα, συμβάλλω στην ενίσχυση της κυβερνοασφάλειας σε υποδομές, συστήματα και επιχειρησιακές ροές. Η καθημερινή μου δουλειά περιλαμβάνει αξιολογήσεις κινδύνου, ανάλυση ευπαθειών, πολιτικές ασφάλειας, υποστήριξη συμμόρφωσης, σχεδιασμό ελέγχων, δοκιμές ασφάλειας, ευαισθητοποίηση χρηστών και πρακτικά μέτρα προστασίας απέναντι σε εξελισσόμενες απειλές.

Το ευρύτερο τεχνικό μου υπόβαθρο σε UNIX/Linux, Windows, virtualization, cloud, δίκτυα και λειτουργία συστημάτων με βοηθά να γεφυρώνω τη στρατηγική με την υλοποίηση και τη διακυβέρνηση με την πραγματική καθημερινότητα των τεχνικών ομάδων."""
                },
                {
                    'title': 'Unix Systems Engineer',
                    'company': 'FIRST TELECOM S.A.',
                    'duration': experience_duration('Μάρτιος 2003 - Μάρτιος 2004', 2003, 3, 2004, 3, language='el'),
                    'location': 'Ελλάδα',
                    'icon': 'fas fa-server',
                    'description': """Στη FIRST TELECOM S.A. εργάστηκα ως Unix Systems Engineer με άμεση εμπλοκή στη διαχείριση δικτύων, στον σχεδιασμό συγκλινουσών υποδομών και στην υποστήριξη υπηρεσιών συνδεσιμότητας για χρήστες internet.

Είχα την ευθύνη για τον σχεδιασμό και την υλοποίηση του ADSL δικτύου της εταιρείας, καθώς και για τον σχεδιασμό, τη λειτουργία και τη συντήρηση του Data Center και της επικοινωνιακής υποδομής. Η δουλειά μου είχε έντονη έμφαση σε υπηρεσίες internet, VoIP και ασφαλή διασύνδεση πελατών με το φωνητικό δίκτυο της εταιρείας, με στόχο υψηλή διαθεσιμότητα και σταθερή ποιότητα υπηρεσίας.

Συμμετείχα επίσης στον συντονισμό ομάδων συμβούλων, μηχανικών και project managers για υλοποιήσεις συστημάτων, λύσεις e-commerce και τεχνολογικές υποδομές προσανατολισμένες στις ανάγκες πελατών."""
                },
                {
                    'title': 'Unix Systems Engineer και Network Operations',
                    'company': 'STS-Net',
                    'duration': experience_duration('Ιανουάριος 2002 - Μάρτιος 2003', 2002, 1, 2003, 3, language='el'),
                    'location': 'Ελλάδα',
                    'icon': 'fas fa-network-wired',
                    'description': """Στην STS-Net είχα την ευθύνη για τον σχεδιασμό και την καθοδήγηση δικτυακών backbones, αρχιτεκτονικής συστημάτων και τεχνικών ομάδων IT. Συμμετείχα σε μικρά και μεγάλα έργα για διαφορετικούς πελάτες, από την αρχική ανάλυση και παρουσίαση μέχρι τον φυσικό σχεδιασμό, την εγκατάσταση, την εκπαίδευση χρηστών και τη συντήρηση των ολοκληρωμένων συστημάτων.

Ο ρόλος αυτός μου έδωσε βαθιά επαφή με την πραγματική λειτουργία δικτύων και συστημάτων, συνδυάζοντας τεχνικό σχεδιασμό, υλοποίηση στο πεδίο, υποστήριξη πελατών και διαχείριση ομάδων."""
                },
                {
                    'title': 'Unix Systems Engineer & IT Manager',
                    'company': 'Servcom Ltd.',
                    'duration': experience_duration('Ιανουάριος 2001 - Ιανουάριος 2002', 2001, 1, 2002, 1, language='el'),
                    'location': 'Ελλάδα',
                    'icon': 'fas fa-cogs',
                    'description': """Στη Servcom Ltd. διαχειρίστηκα και συντήρησα Unix δίκτυα, έχοντας παράλληλα την ευθύνη του τμήματος IT της εταιρείας. Υποστήριζα δίκτυο συστημάτων SCO Unix που φιλοξενούσαν εφαρμογές RM/COBOL για οργανισμούς με κρίσιμες επιχειρησιακές ανάγκες.

Οι πελάτες περιλάμβαναν ναυτιλιακές εταιρείες, ασφαλιστικά γραφεία, δημοτικούς οργανισμούς, νοσοκομειακές μονάδες, αεροπορικές εταιρείες και άλλους φορείς που βασίζονταν στη σταθερότητα των συστημάτων τους. Η εμπειρία αυτή ενίσχυσε την ικανότητά μου να δουλεύω με legacy περιβάλλοντα, παραγωγικά συστήματα και πελάτες που χρειάζονται αξιοπιστία στην πράξη."""
                },
                {
                    'title': 'Μηχανικός Τηλεπικοινωνιών',
                    'company': 'Ελληνικός Στρατός',
                    'duration': experience_duration('Δεκέμβριος 1995 - Δεκέμβριος 2000', 1995, 12, 2000, 12, language='el'),
                    'location': 'Ελλάδα',
                    'icon': 'fas fa-military',
                    'description': """Στον Ελληνικό Στρατό υπηρέτησα ως μηχανικός τηλεπικοινωνιών, έχοντας την ευθύνη ομάδας στρατιωτικών μηχανικών για τη διατήρηση εξοπλισμού, συστημάτων και υλικών σε επιχειρησιακή ετοιμότητα.

Αυτή η περίοδος διαμόρφωσε ουσιαστικά τον επαγγελματικό μου χαρακτήρα. Μου έδωσε πειθαρχία, αίσθημα ευθύνης, ηγεσία υπό πίεση και προσανατολισμό στην αποστολή. Κατά τη διάρκεια της υπηρεσίας μου έλαβα την ανώτερη αναγνώριση της Μονάδας από τον Στρατηγό ως Most Valuable Team Leader, τιμή που αντανακλά τη συνέπεια, την αξιοπιστία και την προσπάθεια της ομάδας που είχα την ευθύνη να καθοδηγώ."""
                }
            ],
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
                    'duration': experience_duration('Marzo de 2004 - Actualidad', 2004, 3, language='es'),
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
                    'duration': experience_duration('Marzo de 2003 - Marzo de 2004', 2003, 3, 2004, 3, language='es'),
                    'location': 'Grecia',
                    'icon': 'fas fa-server',
                    'description': """En FIRST TELECOM S.A. trabajé como ingeniero de sistemas Unix con un rol muy práctico en administración de redes, diseño de infraestructuras convergentes y soporte de servicios de conectividad para usuarios de internet.

Fui responsable del diseño y la implementación de la red ADSL de la compañía, así como del diseño, operación y mantenimiento de su Data Center y de la infraestructura de comunicaciones. Mi trabajo tuvo un fuerte enfoque en servicios de internet, VoIP y conectividad segura de clientes hacia la red de voz de la empresa, manteniendo altos niveles de disponibilidad y calidad de servicio.

También participé en la coordinación de equipos de consultores, ingenieros y project managers para despliegues de sistemas, soluciones de e-commerce e infraestructuras tecnológicas orientadas a clientes."""
                },
                {
                    'title': 'Unix Systems Engineer and Network Operations',
                    'company': 'STS-Net',
                    'duration': experience_duration('Enero de 2002 - Marzo de 2003', 2002, 1, 2003, 3, language='es'),
                    'location': 'Grecia',
                    'icon': 'fas fa-network-wired',
                    'description': """En STS-Net fui responsable del diseño y dirección de backbones de red, arquitectura de sistemas y coordinación del equipo técnico de IT. Participé en proyectos de diferentes tamaños para clientes diversos, cubriendo tanto la fase inicial de análisis y presentación como el diseño físico, la instalación, la formación de usuarios y el mantenimiento posterior de los sistemas implementados.

Este rol me permitió trabajar muy cerca de la operación real de redes y sistemas, combinando diseño técnico, ejecución en campo, soporte al cliente y gestión de equipos."""
                },
                {
                    'title': 'Unix Systems Engineer & IT Manager',
                    'company': 'Servcom Ltd.',
                    'duration': experience_duration('Enero de 2001 - Enero de 2002', 2001, 1, 2002, 1, language='es'),
                    'location': 'Grecia',
                    'icon': 'fas fa-cogs',
                    'description': """En Servcom Ltd. gestioné y mantuve redes Unix, liderando el departamento de IT de la compañía. Fui responsable del mantenimiento de una red de sistemas SCO Unix que daban soporte a aplicaciones desarrolladas en RM/COBOL para distintos tipos de organizaciones.

Los entornos que atendíamos incluían compañías navieras, agencias de seguros, organismos municipales, unidades hospitalarias, aerolíneas y otros clientes con necesidades operativas críticas. Esta experiencia reforzó mi capacidad para trabajar con sistemas legacy, entornos de producción sensibles y clientes que dependían directamente de la estabilidad de sus plataformas tecnológicas."""
                },
                {
                    'title': 'Telecommunication Engineer',
                    'company': 'Hellenic Army',
                    'duration': experience_duration('Diciembre de 1995 - Diciembre de 2000', 1995, 12, 2000, 12, language='es'),
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

    project_description_translations = {
        'el': {
            'HashWhisper': 'Ασφαλής εφαρμογή συνομιλίας για ιδιωτικές συζητήσεις, με πρόσβαση βασισμένη σε hash ώστε μόνο οι συμμετέχοντες με το κοινό μυστικό να μπορούν να μπουν και να διαβάσουν τα προστατευμένα μηνύματα.',
            'SkyFrame': 'Συλλογή αστρονομικών εικόνων για οργάνωση και παρουσίαση λήψεων ουρανού, παρατηρήσεων και οπτικού υλικού αστρονομίας μέσα από καθαρό web περιβάλλον.',
            'helpdesk_pro': 'Σύστημα IT helpdesk για παρακολούθηση αιτημάτων υποστήριξης, διαχείριση περιστατικών και οργάνωση τεχνικών ροών εργασίας.',
            'CloudRollouts': 'Διακομιστής διάθεσης ενημερώσεων για στόλους συστημάτων, με υποστήριξη σταδιακών αναβαθμίσεων και ελεγχόμενων παραγωγικών deployments.',
            'CipherDrop': 'Σύστημα μίας χρήσης, end-to-end κρυπτογραφημένων αποστολών για ασφαλή μεταφορά ευαίσθητων πληροφοριών χωρίς μακροχρόνια εκτεθειμένα μηνύματα.',
            'ELE': 'Έργο βοηθού τεχνητής νοημοσύνης με έμφαση στην πρακτική αυτοματοποίηση, τη διαδραστική υποστήριξη και τη διαχείριση εργασιών μέσα από απλό περιβάλλον εφαρμογής.',
            'JAIID_WEB': 'Το web περιβάλλον του JAIID, που φέρνει αποτελέσματα ανίχνευσης προσκρούσεων με τεχνητή νοημοσύνη και εργαλεία αστρονομικής ανάλυσης στον browser.',
            'JAIID': 'Το Jovian Artificial Intelligence Impact Detector, ένα AI-assisted έργο αστρονομίας για εντοπισμό και ανάλυση πιθανών λάμψεων πρόσκρουσης στον Δία.',
            'GnuProxy': 'Ασφαλές frontend mail proxy για Postfix, σχεδιασμένο για δημιουργία SMTP gateway ανάμεσα σε mail server και internet με ενισχυμένα φίλτρα και ελέγχους προστασίας.',
            'BlackFox': 'Εργαλείο διαχείρισης σε Bash που δημιουργεί λίστες αποκλεισμού κακής φήμης για NGINX, Apache και UFW Firewall, αξιοποιώντας δεδομένα από 218 παρόχους λιστών.'
        },
        'es': {
            'HashWhisper': 'Aplicación de chat segura para conversaciones privadas, con acceso basado en hashes para que solo los participantes con el secreto compartido puedan entrar y leer los mensajes protegidos.',
            'SkyFrame': 'Galería de imágenes astronómicas para organizar y presentar capturas del cielo, observaciones y material visual de astronomía en una interfaz web limpia.',
            'helpdesk_pro': 'Sistema de tickets para IT helpdesk orientado al seguimiento de solicitudes de soporte, la gestión de incidencias y la organización de flujos técnicos.',
            'CloudRollouts': 'Servidor de despliegue de actualizaciones para flotas de sistemas, pensado para coordinar actualizaciones graduales y despliegues controlados.',
            'CipherDrop': 'Sistema de entregas cifradas de extremo a extremo y de un solo uso para enviar información sensible sin dejar mensajes expuestos de larga duración.',
            'ELE': 'Proyecto de asistente de inteligencia artificial centrado en automatización práctica, soporte interactivo y gestión inteligente de tareas desde una interfaz sencilla.',
            'JAIID_WEB': 'La interfaz web de JAIID, que lleva resultados de detección de impactos con inteligencia artificial y herramientas de análisis astronómico al navegador.',
            'JAIID': 'El Jovian Artificial Intelligence Impact Detector, un proyecto de astronomía asistido por IA para identificar y analizar posibles destellos de impacto en Júpiter.',
            'GnuProxy': 'Frontend seguro de proxy de correo para Postfix, diseñado para crear una pasarela SMTP entre un servidor de correo e internet con filtros y controles de protección reforzados.',
            'BlackFox': 'Herramienta de administración basada en Bash que genera listas de bloqueo de mala reputación para NGINX, Apache y UFW Firewall usando datos de 218 proveedores de listas.'
        }
    }

    for project in profile_data['projects']:
        localized_description = project_description_translations.get(current_lang, {}).get(project['name'])
        if localized_description:
            project['description'] = localized_description

    project_tag_translations = {
        'el': {
            'Security': 'Ασφάλεια',
            'Secure Chat': 'Ασφαλής συνομιλία',
            'Privacy': 'Ιδιωτικότητα',
            'Astronomy': 'Αστρονομία',
            'Gallery': 'Συλλογή',
            'Web App': 'Web εφαρμογή',
            'ITSM': 'ITSM',
            'Helpdesk': 'Helpdesk',
            'Operations': 'Λειτουργία',
            'DevOps': 'DevOps',
            'Deployments': 'Deployments',
            'Automation': 'Αυτοματοποίηση',
            'Encryption': 'Κρυπτογράφηση',
            'AI': 'AI',
            'Assistant': 'Βοηθός',
            'Citizen Science': 'Επιστήμη πολιτών',
            'Mail Security': 'Ασφάλεια email',
            'Postfix': 'Postfix',
            'Infrastructure': 'Υποδομές',
            'Bash': 'Bash',
            'Firewall': 'Firewall'
        },
        'es': {
            'Security': 'Seguridad',
            'Secure Chat': 'Chat seguro',
            'Privacy': 'Privacidad',
            'Astronomy': 'Astronomía',
            'Gallery': 'Galería',
            'Web App': 'Aplicación web',
            'ITSM': 'ITSM',
            'Helpdesk': 'Helpdesk',
            'Operations': 'Operaciones',
            'DevOps': 'DevOps',
            'Deployments': 'Despliegues',
            'Automation': 'Automatización',
            'Encryption': 'Cifrado',
            'AI': 'IA',
            'Assistant': 'Asistente',
            'Citizen Science': 'Ciencia ciudadana',
            'Mail Security': 'Seguridad de correo',
            'Postfix': 'Postfix',
            'Infrastructure': 'Infraestructura',
            'Bash': 'Bash',
            'Firewall': 'Firewall'
        }
    }

    if current_lang in project_tag_translations:
        tag_translations = project_tag_translations[current_lang]
        for project in profile_data['projects']:
            project['tags'] = [tag_translations.get(tag, tag) for tag in project.get('tags', [])]

    return render_template(
        'index.html',
        data=profile_data,
        ui=ui_translations[current_lang],
        languages=languages,
        current_lang=current_lang
    )


if __name__ == '__main__':
    app.run(debug=True)
