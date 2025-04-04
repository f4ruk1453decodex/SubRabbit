📄 README (İngilizce)
🐰 SubRabbit - Subdomain Scanner

SubRabbit is a fast subdomain scanner designed for security researchers and penetration testers. It helps in discovering subdomains of a given target domain efficiently. Whether you’re scanning a single domain or multiple domains, SubRabbit ensures fast scanning using DNS requests.
✨ Features:

    🌐 Scan a single domain or a list of domains.

    ⚡ Threading for faster subdomain discovery.

    🚀 Fast DNS-based scanning.

    📁 Results saved to a file.

💻 Requirements:

    Python 3.x

    requests library

    colorama library

    pystyle library

    fake_useragent library

    multiprocessing.dummy library

🛠️ Installation:

    Clone or download this repository.

    Install the necessary dependencies:

pip install -r requirements.txt

    Download rabbit.png and place it in the same directory as the script.

🏃 Usage:

To scan a target domain:

python subrabbit.py -t <target-domain>

To scan a list of domains:

python subrabbit.py -t <domain1> <domain2> <domain3> ...

⚡ Example:

python subrabbit.py -t example.com

The results will be saved in a file called found_example.com.txt.
