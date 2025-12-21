# Python-for-Cybersecurity

<img width="1920" height="940" alt="{7E7B06BD-604C-4EFB-9FA6-C47E801753AF}" src="https://github.com/user-attachments/assets/5cd72649-a304-43e7-9698-8a85e3c576e4" />
<img width="1920" height="1014" alt="{29A9BEB7-2CD0-484D-BE9C-1ABAD64BFA27}" src="https://github.com/user-attachments/assets/0a6a6a0b-754d-4ed6-9c29-2a5d1b437480" />
<img width="1919" height="385" alt="{F32AA128-6C87-43EF-B77B-DB3F10346EB1}" src="https://github.com/user-attachments/assets/8fc5e771-6f4b-42b2-9153-ec5bef3c0d43" />

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
