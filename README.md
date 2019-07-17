# Scrape-books-toscrape-com
This is the sample repository for using Scrapy with extract the contents from web
**This Code Works in Windows 10, if you are facing any issue, Please install Visual Studio Vc++ 14.0**

[This is the URL used for scraping data](http://books.toscrape.com/ "BooksToScrape.com")
http://books.toscrape.com

## Steps to Run 

1. Create Virtual ENV -- Best approach use venv

```bash
virtualenv venv
```

2. Install Scrapy using Pip ( If you get any error, check Visual Studio VC++ 14.0 installed in machine, **Only WINDOWS machine **

```bash
pip install scrapy 
```

3. Open in any of your editor (Recommended VS Code) Run in the cmd , 

```bash
scrapy scrapy crawl books -o books.csv
```

