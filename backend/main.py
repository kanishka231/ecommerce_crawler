import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_all_product_links(base_url, start_url, num_pages=5):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    product_links = set()
    for page_num in range(1, num_pages + 1):
        url = f"{start_url}&page={page_num}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page_num}: {response.status_code}")
            continue
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "/dp/" in href or "/gp/" in href:
                full_url = urljoin(base_url, href)
                product_links.add(full_url)
    return list(product_links)

if __name__ == "__main__":
    base_url = "https://www.flipkart.com/"  
    start_url = "https://www.flipkart.com/"
    links = get_all_product_links(base_url, start_url, num_pages=5)
    print("Found product links:")
    for link in links:
        print(link)
