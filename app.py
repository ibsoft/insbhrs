from flask import Flask, render_template
import os

app = Flask(__name__)

# Create necessary directories if they don't exist
os.makedirs(os.path.join(app.root_path, 'static', 'images'), exist_ok=True)


@app.route('/')
def index():
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

    return render_template('index.html', data=profile_data)


if __name__ == '__main__':
    app.run(debug=True)
