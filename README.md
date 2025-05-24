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

## Getting Started

There are two ways to use this application: downloading the pre-built version (recommended for most users) or running it from the source code (for developers).

### For Users (Recommended)

The easiest way to get started is to download the latest pre-built application. 
> [!Note] The release is currently only designed for Mac with ARM architecture, if you want to create a standalone, use the Source code along with Pyinstaller

1.  Navigate to the [**Releases Page**](URL_TO_YOUR_RELEASES_PAGE) for this repository.
2.  Under the latest release, download the `.zip` asset (e.g., `shipping-calculator-v1.0.zip`).
3.  Run the application. The first time you run it, the app will prompt you to enter your personal Shippo API key, which it will save for future use.

### For Developers (Running from Source)

If you wish to run or modify the source code directly:

1.  Clone the repository:
    ```bash
    git clone [URL_TO_YOUR_GITHUB_REPOSITORY]
    cd [REPOSITORY_FOLDER_NAME]
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Set Up Your Environment File
   The application requires a Shippo API key to function.
  * Create a new file in the root of the project directory named `.env`.
  * Open the `.env` file and add your Shippo API key in the following format:
    ```
    SHIPPO_API_KEY="your_actual_shippo_api_key_goes_here"
    ```
4.  Run the application:
    ```bash
    python main.py
    ```
## Author

* **Steven Vandegrift**
