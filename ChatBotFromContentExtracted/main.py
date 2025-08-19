import requests
import xml.etree.ElementTree as ET
import time
from bs4 import BeautifulSoup

# Main sitemap (directly contains URLs, no sub-sitemaps)
MAIN_SITEMAP = "https://www.ndis.gov.au/sitemap.xml"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
OUTPUT_FILE = "ndis_pages_text.txt"

# Namespace for parsing XML
NAMESPACE = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def fetch_xml(url):
    """Fetch and parse XML from a URL"""
    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()
    return ET.fromstring(response.content)

def extract_urls_from_sitemap(sitemap_url):
    """Extract all page URLs from a flat sitemap"""
    root = fetch_xml(sitemap_url)
    return [elem.text for elem in root.findall("ns:url/ns:loc", NAMESPACE)]

def fetch_visible_text(url):
    """Download page and extract visible text"""
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts, styles, and hidden tags
        for script in soup(["script", "style", "noscript"]):
            script.decompose()

        # Get visible text only
        text = soup.get_text(separator="\n", strip=True)
        return text
    except Exception as e:
        print(f"  !! Failed to fetch {url}: {e}")
        return None

def main():
    print("Fetching sitemap...")
    urls = extract_urls_from_sitemap(MAIN_SITEMAP)
    print(f"Found {len(urls)} URLs in sitemap")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for url in urls:
            print(f"Downloading page: {url}")
            text = fetch_visible_text(url)
            if text:
                f.write(f"=== {url} ===\n{text}\n\n")
            # Delay to avoid hammering NDIS server
            time.sleep(1)

    print(f"\n✅ Done! Extracted text from {len(urls)} pages")
    print(f"Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
