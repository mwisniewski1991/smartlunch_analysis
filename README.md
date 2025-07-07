# Lunch Tracker - SmartLunch Data Analysis Project

## 📋 Project Overview

This project is a comprehensive data collection and analysis system for tracking meal prices, restaurant ratings, and menu availability from SmartLunch delivery service. The system was designed to gather data over 6 months to analyze pricing trends, restaurant performance, and meal availability patterns.

The project includes comprehensive analysis in `ANALYSIS_ENG.md` or `ANALYSIS_PL.md`.


## 🎯 Project Goals

- **Data Collection**: Automatically scrape restaurant and menu data from SmartLunch API
- **Price Analysis**: Track meal pricing trends over time
- **Restaurant Analytics**: Monitor restaurant ratings and performance
- **Menu Availability**: Analyze meal availability patterns
- **Business Intelligence**: Provide insights for lunch delivery optimization

## 🏗️ Architecture

### Technology Stack

**Data Collection:**
- **Python** with `requests` library for API scraping
- **SQLite** database for data storage
- **SQLAlchemy** for database operations

**Analysis:**
- **Jupyter Notebook** for data exploration
- **Pandas** for data manipulation
- **Altair** for data visualization

**Monitoring:**
- **Telegram Bot** for notifications
- **Cron jobs** for automated scheduling

## 📁 Project Structure

```
lunch_analysis/
├── app/                         # Main application directory
│   ├── src/                     # Core application modules
│   │   ├── auth_example.py      # Authentication template
│   │   ├── config.py            # Configuration settings
│   │   ├── directory_manager.py # File system operations
│   │   └── scraper.py           # API scraping logic
│   ├── src_bot/                 # Telegram bot integration
│   │   ├── auth_example.py      # Bot credentials template
│   │   └── telegram_bot.py      # Notification system
│   ├── src_db/                  # Database operations
│   │   ├── config.py            # Database configuration
│   │   ├── db_auth.py           # Database authentication
│   │   ├── db_manager.py        # Database management
│   │   ├── files_reader.py      # Data file processing
│   │   └── models.py            # Database models
│   ├── data_example/            # Sample data structure
│   │   ├── menus/               # Scraped menu data
│   │   ├── restaurants/         # Restaurant information
│   │   └── scrap_plan/          # Scraping schedules
│   ├── app_scrap_*.py           # Main scraping applications
│   ├── app_scrap_*.bash         # Bash wrappers for cron
│   ├── app_db_*.py              # Database loading scripts
│   ├── Analysis.ipynb           # Data analysis notebook
│   └── req.txt                  # Python dependencies
├── utils/                       # Utility files
│   └── charts/                  # Generated analysis charts
├── ANALYSIS_PL.md               # Comprehensive analysis report. Polish version
├── ANALYSIS_ENG.md              # Comprehensive analysis report. English version
└── README.md                    # Project documentation
```

## 🔄 Data Collection Process

### 1. Scraping Schedule

The system operates on a carefully planned schedule:

**Daily Operations (00:30):**
- `app_scrap_restaurants.py` - Collects restaurant information and creates scraping plan
- `app_scrap_restaurants.bash` - Bash wrapper for cron scheduling

**Menu Scraping (5x daily):**
- **Times**: 01:00, 06:00, 12:00, 18:00, 23:00
- `app_scrap_menu.py` - Scrapes menu data based on the daily plan
- `app_scrap_menu.bash` - Bash wrapper for cron scheduling

### 2. Data Types Collected

#### Scrap Plan
- **Purpose**: Defines which restaurants and menus to scrape each day
- **Format**: JSON with restaurant IDs and menu availability
- **Location**: `data/scrap_plan/YYYY/M/D/YYYYMMDD.json`

#### Restaurant Data
- **Content**: Restaurant details, ratings, delivery information
- **Format**: JSON files per restaurant
- **Location**: `data/restaurants/YYYY/M/D/restaurant_id.json`

#### Menu Data
- **Content**: Meal details, prices, availability, ratings
- **Format**: JSON files with menu items
- **Location**: `data/menus/YYYY/M/D/place_menu_timestamp_orderdate.json`

### 3. Supported Locations

The system tracks data for multiple SmartLunch delivery locations for TME:
- **CLR** (ID: 1195)
- **CLŁ** (ID: 1194) 
- **Biurowiec TME** (ID: 1203)
- **Oddział Gdynia** (ID: 1204)
- **Oddział Kraków** (ID: 1205)

## 🗄️ Database Schema

### Core Tables

**Restaurants**
- `id` - Restaurant identifier
- `name` - Restaurant name

**Restaurants_rates**
- `id` - Rate record identifier
- `id_restaurants` - Foreign key to restaurant
- `rate_date` - Date of rating
- `rate` - Average rating score
- `rates_count` - Number of ratings

**Scrap_plan**
- `id` - Plan record identifier
- `place_id` - Delivery location ID
- `scrap_day` - Day of scraping
- `order_date` - Order deadline
- `menu_id` - Menu identifier
- `restaurant_id` - Restaurant identifier

**Meals**
- `id` - Meal identifier
- `name_pl` - Meal name in Polish

**Menus**
- `id` - Menu record identifier
- `menu_id` - Menu identifier
- `place_id` - Delivery location ID
- `scrap_datetime` - When data was collected
- `order_date` - Order deadline
- `meal_id` - Meal identifier
- `total_price` - Meal price in cents
- `is_vege` - Vegetarian flag
- `is_cold` - Cold meal flag
- `avg_rate` - Average meal rating
- `rates_count` - Number of meal ratings
- `dishes_left` - Remaining quantity

## 📊 Data Analysis

The project includes comprehensive analysis in `ANALYSIS.md` covering:

### Key Metrics Analyzed
- **Meal Availability**: Number of unique meals available per day
- **Restaurant Rankings**: Rating-based restaurant performance
- **Price Trends**: Average, minimum, and maximum meal prices over time
- **Rating History**: Restaurant rating changes over time
- **Order Patterns**: Meal availability patterns before order deadlines

### Visualization Examples
- Line charts showing price trends over time
- Bar charts for restaurant rankings
- Interactive plots for rating history analysis



## 🔔 Notifications

The system includes Telegram bot integration for monitoring:
- Scraping completion notifications
- Error alerts
- Daily status updates

## 📝 Key Learnings

### Technical Insights
- **Cron Scheduling**: Proper timezone handling (UTC vs local) is crucial
- **Database Design**: Simpler schema designs are more maintainable for small projects
- **Data Pipeline**: Integrated pipeline approach is better than individual script execution
- **Error Handling**: Robust error handling prevents data loss during scraping

### Business Insights
- **Price Stability**: Meal prices showed relative stability over the tracking period
- **Restaurant Performance**: Clear leaders emerged in restaurant ratings
- **Availability Patterns**: Meal availability varies significantly before order deadlines
- **Seasonal Effects**: Holiday periods impact restaurant availability and pricing


## 📄 License
This project is for educational and research purposes. Please respect SmartLunch's terms of service when using this code.

## ⚠️ Important Notes

- **API Rate Limiting**: The system includes delays between requests to respect API limits
- **Data Privacy**: Only public menu and restaurant data is collected
- **Credential Security**: Never commit actual API credentials to version control
- **Backup Strategy**: Regular database backups are recommended for long-term data preservation