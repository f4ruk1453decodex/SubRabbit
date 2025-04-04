# SubRabbit - Subdomain Scanner

SubRabbit is a fast and efficient subdomain scanner designed to help security researchers and penetration testers discover subdomains of a target domain. With this tool, you can scan a single domain or a list of domains in parallel to quickly identify subdomains.

## Features:
- Scan a single domain or a list of domains.
- Utilizes threading to speed up the scanning process.
- Detects subdomains using DNS requests.
- Fast and lightweight for large-scale scans.

## Requirements:
- Python 3.x
- `requests` library
- `argparse` library
- `colorama` library
- `pystyle` library
- `fake_useragent` library
- `multiprocessing.dummy` library

### Installation:

1. Clone or download this repository.
2. Install the necessary dependencies:

```bash
pip install requests colorama pystyle fake_useragent
