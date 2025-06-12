# Firefox Add-on Downloader

A Scrapy project for crawling and downloading the top 100 Firefox browser extensions.

## Project Overview

This repository contains a Scrapy-based solution to:
- Fetch basic information of the top 100 popular Firefox add-ons
- Retrieve direct download URLs for each extension
- Batch download extensions to a specified local directory

firefox_addon_downloader/  
├── addon/                # Download storage directory (create manually)  
├── scrapy.cfg           # Scrapy project configuration  
├── down.py              # Python script for downloading extensions  
├── requirements.txt     # Dependencies list  
└── firefox_addon/       # Scrapy project directory  
    ├── spiders/         # Crawler scripts  
    │   ├── __init__.py  
    │   ├── firefox_addon_list.py  # Crawler for top 100 list  
    │   └── firefox_addon_file.py  # Crawler for download URLs  
    ├── items.py         # Data model definitions  
    ├── middlewares.py   # Optional (proxy/UA rotation)  
    └── settings.py      # Crawler configurations  



    
## Features

- ⚡ Fast crawling with Scrapy framework
- 📂 Organized output files for add-on info and URLs
- 📥 Automated download script for batch operations

## Prerequisites

- Python 3.6+
- Scrapy (`pip install scrapy`)
- Python requests library (`pip install requests`)

## Quick Start

### Step 1: Crawl top 100 add-on list
```bash
scrapy crawl firefox_addon_list
```
- Output: recommanded100.txt (contains add-on names, IDs, and basic info)
- The file is created in the project root directory.

### Step 2: Fetch download URLs  
```bash
scrapy crawl firefox_addon_file
```
- Output: recommanded100_url.txt (contains direct .xpi download links)
- The script reads add-on IDs from recommanded100.txt to search for URLs.



### Step 3: Download extensions
```bash
python3 down.py
```

- Requirement: Create an addon/ directory in the project root before running.
- Result: Extensions are saved as .xpi files in the addon/ directory.
- Progress: The script will display download progress for each file.
