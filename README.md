# Real-Time Shipping Rate Calculator 📦

This is a command-line application built with Python that helps users find the cheapest shipping rates for a package in real-time. It uses the Shippo API to fetch rates from multiple carriers and provides a clean, interactive terminal interface for the user.

## Features

* **Interactive CLI**: A user-friendly command-line interface guides the user through the process.
* **Real-Time Rates**: Connects to the Shippo API to get up-to-the-minute shipping costs from major carriers.
* **Rate Comparison**: Displays all available shipping options and highlights the most affordable one.
* **Error Handling**: Validates user input to ensure that dimensional data is numeric, preventing application crashes.
* **Secure API Key Management**: Uses a `.env` file to securely store and access the Shippo API key, keeping it out of the source code.

## Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.x](https://www.python.org/downloads/)
* A free [Shippo API Key](https://goshippo.com/)

## Setup and Installation

Follow these steps to get the application running on your local machine.

**1. Clone the Repository**
```bash
git clone [URL_TO_YOUR_GITHUB_REPOSITORY]
cd [REPOSITORY_FOLDER_NAME]
```

**2. Install Dependencies**
This project uses a `requirements.txt` file to manage its dependencies. Run the following command in your terminal to install them:
```bash
pip install -r requirements.txt
```

**3. Set Up Your Environment File**
The application requires a Shippo API key to function.

* Create a new file in the root of the project directory named `.env`.
* Open the `.env` file and add your Shippo API key in the following format:

```
SHIPPO_API_KEY="your_actual_shippo_api_key_goes_here"
```

## How to Run the Application

Once the setup is complete, you can run the application with the following command from the project's root directory:

```bash
python main.py
```

The application will then guide you through the process of entering the origin address, destination address, and package details.

## Author

* **Steven Vandegrift**