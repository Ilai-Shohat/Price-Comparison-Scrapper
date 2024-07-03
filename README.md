# Price Comparison Scraper

Welcome to the Price Comparison Scraper repository. This project aims to provide a tool that scrapes prices from various e-commerce websites, allowing users to compare prices of products across different platforms.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Price Comparison Scraper is a Python-based tool designed to help users find the best prices for products by scraping data from multiple e-commerce websites. It is built to be extensible and easy to use, making it a valuable asset for shoppers looking to make informed purchasing decisions.

## Features

- **Multi-site Scraping:** Supports scraping from various e-commerce websites.
- **Price Comparison:** Compares prices of the same product across different platforms.
- **Configurable:** Easy to configure for adding new websites and products.
- **Data Export:** Exports the scraped data into CSV format for further analysis.

## Installation

To install the Price Comparison Scraper, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/ilaish/Price-Comparison-Scrapper.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Price-Comparison-Scrapper
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the scraper, run the main script with the desired configuration:

```bash
python main.py
```

By default, the script will use the configuration provided in the `config.json` file. You can modify this file to add or remove websites, products, and other settings.

## Configuration

The scraper can be configured using the `config.json` file located in the project directory. The configuration file allows you to specify the following:

- **Websites:** List of e-commerce websites to scrape.
- **Products:** List of products to search for.
- **Output:** Settings for exporting the scraped data.

Example `config.json`:

```json
{
    "websites": [
        "https://example-ecommerce1.com",
        "https://example-ecommerce2.com"
    ],
    "products": [
        "laptop",
        "smartphone"
    ],
    "output": {
        "format": "csv",
        "file": "prices.csv"
    }
}
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request. For major changes, please discuss them in an issue first to ensure they align with the project's goals.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
