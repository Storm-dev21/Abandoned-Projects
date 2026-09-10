import requests
from bs4 import BeautifulSoup

try:
    res = requests.get('https://ipleak.com')
    res.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Find the span element containing the IP address
    ip_address_span = soup.find('span', string=lambda text: "IP address" in str(text))

    if ip_address_span:
        # Extract the text containing the IP address
        ip_address_text = ip_address_span.text.strip()
        # Extract only the IP address from the text
        ip_address = ip_address_text.split('&nbsp;')[-1]
        print("IP Address:", ip_address)
    else:
        print("Error: IP address span not found")

except requests.exceptions.RequestException as e:
    print("Error:", e)
