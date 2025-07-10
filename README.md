# Data Updater Project

## Overview
The Data Updater project is designed to automate the process of downloading data from multiple dynamic Excel sheets and updating a SQL database. This application is structured into several modules, each responsible for a specific part of the data handling process.

## Project Structure
```
data-updater
├── src
│   ├── main.py          # Entry point of the application
│   ├── excel
│   │   └── downloader.py # Module for downloading Excel data
│   ├── sql
│   │   └── updater.py    # Module for updating the SQL database
│   └── utils
│       └── helpers.py    # Utility functions for the project
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd data-updater
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Functionality
- **Excel Data Downloading**: The application retrieves data from multiple dynamic Excel sheets using the `download_excel_data` function from the `downloader.py` module.
- **Database Updating**: After processing the downloaded data, the application updates the SQL database using the `update_database` function from the `updater.py` module.
- **Utility Functions**: Common tasks such as logging and data validation are handled by utility functions in the `helpers.py` module.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.


##before running the code create environment variable <multidrive_connection_string> for multidrive access 