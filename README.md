# Python-for-Cybersecurity

## Step-by-step explanation:

### 1. Import libraries

  - requests → sends HTTP requests to Amazon

  - BeautifulSoup → parses HTML content

  - time → delays execution

  - datetime → logs time of price checks

### 2. Set product URL

  - The user pastes the Amazon product link they want to track

### 3. Use HTTP headers

  - Prevents Amazon from blocking the request

  - Mimics a real browser

### 4. Fetch product page

  - requests.get() downloads the webpage

### 5. Parse HTML

  - BeautifulSoup extracts product title and price

### 6. Display results

  - Prints title, price, and timestamp

### 7. Save data

  - Appends price history to price_log.txt

### 8. Loop execution

  - Script checks price every hour automatically
