# Python-for-Cybersecurity

Step-by-step explanation:

Import libraries

requests → sends HTTP requests to Amazon

BeautifulSoup → parses HTML content

time → delays execution

datetime → logs time of price checks

Set product URL

The user pastes the Amazon product link they want to track

Use HTTP headers

Prevents Amazon from blocking the request

Mimics a real browser

Fetch product page

requests.get() downloads the webpage

Parse HTML

BeautifulSoup extracts product title and price

Display results

Prints title, price, and timestamp

Save data

Appends price history to price_log.txt

Loop execution

Script checks price every hour automatically
