# Python-for-Cybersecurity

Step-by-step explanation:

1. Import libraries

  a) requests → sends HTTP requests to Amazon

  b) BeautifulSoup → parses HTML content

  c) time → delays execution

  d) datetime → logs time of price checks

2. Set product URL

  a) The user pastes the Amazon product link they want to track

3. Use HTTP headers

  a) Prevents Amazon from blocking the request

  b) Mimics a real browser

4. Fetch product page

  a) requests.get() downloads the webpage

5. Parse HTML

  a) BeautifulSoup extracts product title and price

6. Display results

  a) Prints title, price, and timestamp

7. Save data

  a) Appends price history to price_log.txt

8. Loop execution

  a) Script checks price every hour automatically
