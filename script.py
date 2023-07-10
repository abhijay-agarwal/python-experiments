import requests
from bs4 import BeautifulSoup

url = "https://www.bloomberg.com/quote/GOOGL:US"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

print(soup.prettify())

# Find the element containing the stock price
price_element = soup.find("h3", class_="priceText__0550103750")

# Extract the text of the element, if the element is NoneType then the string should say not found
text = price_element.text if price_element else "not found"

# Print the element
print(price_element)

# Print the text of the element
print(text)