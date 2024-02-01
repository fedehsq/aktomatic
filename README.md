# Aktomatic - Project Setup Guide

## What is [Akto](https://www.akto.io/)
Akto is an instant, open source API security platform that takes only 60 secs to get started.  
Akto is used by security teams to maintain a continuous inventory of APIs, test APIs for vulnerabilities and find runtime issues.  
Akto offers coverage for all OWASP top 10 and HackerOne Top 10 categories including BOLA, authentication, SSRF, XSS, security configurations, etc.  
Akto's powerful testing engine runs variety of business logic tests by reading traffic data to understand API traffic pattern leading to reduced false positives. Akto can integrate with multiple traffic sources - burpsuite, AWS, postman, GCP, gateways, etc.  
Akto enables security and engineering teams to secure their APIs by doing three things:
1. **API inventory**
2. **Run business logic tests in CI/CD**
3. **Find vulnerabilities in run-time**

## Introduction
Aktomatic is a tool to manage Akto API.  
This script provides a streamlined solution for security and engineering teams looking to enhance API security by seamlessly using Akto's powerful features via API calls.
## Script Functionality

1. **Read My Collections**:
    Effortlessly read and gather information about your Collections using Akto's API. This ensures that you have complete visibility into your existing API collections.

2. **Import Postman Collections**:
    Seamlessly import your Postman Collections into Akto, allowing you to leverage Akto's advanced security testing capabilities on your API definitions.

3. **Run Tests**:
    Execute comprehensive security tests on your Postman Collections directly through Akto's API. Benefit from Akto's intelligent testing engine, covering all OWASP top 10 and HackerOne Top 10 categories, to identify vulnerabilities and ensure robust API security.

4. **Download Results**:
    Retrieve detailed test results and reports generated by Akto, providing you with actionable insights into potential vulnerabilities and runtime issues. The download functionality allows for easy sharing and documentation.

## Getting Started

Follow these instructions to set up Akto on your local machine:

### 1. Prerequisites

Make sure you have the following installed on your system:

- Python 3
- pip (Python package installer)

### 2. Create a Virtual Environment

Create a virtual environment named ```venv``` using the following command:

    python3 -m virtualenv venv

### 3. Activate the Virtual Environment

Activate the virtual environment. Use the appropriate command based on your operating system:
    
    . venv/bin/activate


### 4. Install Dependencies

Install the required packages using pip:

    pip install -r requirements.txt

## Usage

### Prerequisites
Create ```.env``` file in the root directory of the project and add the following variables:

    X_API_KEY
    SERVER_URL
(Optional) You can try everything in a local instance of Akto. You can follow this steps to install Akto in your local machine: 
- Install Docker (https://docs.docker.com/get-docker/)
- Run the compose in ```akto/``` folder  
    ```
    docker compose up -d
    ```
- Go to http://localhost:9090/ and register a new user

You can create ```X_API_KEY``` following this steps:
- Go to your Akto server
- Login
- Go to https://your-instance/dashboard/settings/integrations/akto_apis and create a new API key


Now that the environment is set up, you can start working on Aktomatic script:
    
    python3 aktomatic.py --help

(Optional) Avoid to run ```python3``` every time you want to run the script:
    
    chmod 755 aktomatic.py
    ./aktomatic.py --help

(Optional) Create an alias to run the script:
    
    alias aktomatic=$PWD/aktomatic.py
    aktomatic --help

Output:

    usage: aktomatic.py [-h] [-i FILE] [-l ITEM] [-r COLLECTION] [-t COLLECTION]

    Aktomatic is a tool to manage Akto API.

    options:
    -h, --help            show this help message and exit
    -i FILE, --import FILE
                            Import a collection from Postman. Specify the path of the Postman collection file.
    -l ITEM, --list ITEM  Specify the type of item to list (e.g., collections, tests).
    -r COLLECTION, --read COLLECTION
                            Read endpoints from the collection. Specify collection name.
    -t COLLECTION, --test COLLECTION
                            Test all endpoints in a collection. Specify collection name.
