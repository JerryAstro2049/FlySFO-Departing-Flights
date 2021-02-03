# FlySFO Departing Flights

So basically, this is a small `Scrapy` + `Selenium` + `ChromeDriver` project that gets San Francisco International Airport (SFO)'s departing flights from www.flysfo.com

## User Guide:

Use the command below to activate our spider and get the flights:

under `FlySFO-Departing-Flights\Crawler`:

`scrapy crawl FlySFO`

That's it!

## Requirements:

### Python 3.7

This is a recommendation, I think close versions are also fine though

### Scrapy

Use the command below to install `Scrapy`:

`pip install scrapy`

### Selenium

Use the command below to install `Selenium`:

`pip install selenium`

### Google Chrome

This project uses `Selenium` to visit web pages through `Google Chrome`

`Google Chrome` official website:

https://www.google.com/chrome/

### ChromeDriver

To operate `Google Chrome` automatically through `Selenium` instead of us clicking and typing in the browser, we'll need `ChromeDriver`

##### Downloading:

Do notice that the `ChromeDriver`'s version must match with that of the `Google Chrome` on your computer!

`ChromeDriver` official website:

https://chromedriver.chromium.org/

##### Next, put the `chromedriver.exe` under the following 2 paths:

1. `C:\Program Files (x86)\Google\Chrome\Application`

2. *your* Python installation directory
