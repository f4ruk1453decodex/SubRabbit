# 🐰 SubRabbit - Subdomain Scanner

![Rabbit Logo]((https://github.com/f4ruk1453decodex/SubRabbit/blob/main/rabbit.png))

**SubRabbit** is a fast subdomain scanner designed for security researchers and penetration testers. It helps in discovering subdomains of a given target domain efficiently. Whether you’re scanning a single domain or multiple domains, SubRabbit ensures fast scanning using DNS requests.
### ✨ Features:
- 🌐 Scan a single domain or a list of domains.
- ⚡ Threading for faster subdomain discovery.
- 🚀 Fast DNS-based scanning.
- 📁 Results saved to a file.

### 🛠️ Installation:

1. Clone or download this repository.
2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```
### 🏃 Usage:
- To scan a target domain:
```python subrabbit.py -t <target-domain>```
- To scan a list of domains:
```python subrabbit.py -l yourlist.txt```

