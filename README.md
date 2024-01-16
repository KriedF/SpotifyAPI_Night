# Assignment Package (ASSIGNMENTPKG)

This Python package provides a script (`analysis.py`) that utilizes the Spotify API to analyze your recent tracks and find the most listened-to artist at night. It measures the time taken to fetch and filter tracks, providing insights into your listening habits.

## Table of Contents

- [Files and Folders](#files-and-folders)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Configuration](#configuration)
- [License](#license)
- [Code of Conduct](#code-of-conduct)

## Files and Folders

- **analysis.py:** The main script that analyzes recent tracks using the Spotify API.
- **configs:** Folder containing configuration files.
  - **analysis_config.yml:** Configuration file for analysis parameters (e.g., time range, track limit).
  - **system_config.yml:** Configuration file for system-level parameters (e.g., Spotify API credentials).
  - **user_config.yml:** Configuration file for user-specific parameters.
- **CONDUCT.md:** Code of conduct document.
- **LICENSE.md:** License file (MIT License).
- **README.md:** Documentation for the Assignment Package.
- **setup.py:** Setup file for packaging and distribution.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Usage
Set up your Spotify API credentials in configs/system_config.yml.

Customize analysis parameters in configs/analysis_config.yml.

Run the script: python -m assignmentpkg.analysis

### Configuration
configs/system_config.yml: Configure your Spotify API credentials.
configs/user_config.yml: Configure user-specific parameters.
configs/analysis_config.yml: Set analysis parameters such as time range and track limit.

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.

### Code of Conduct
Please read CONDUCT.md for details on our code of conduct.
