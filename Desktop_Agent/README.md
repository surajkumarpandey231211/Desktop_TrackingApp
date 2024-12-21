# DESKTOP AGENT APPLICATION
Develop a Python-based desktop agent application that tracks employee activity and uploads relevant data (e.g., screenshots) to Amazon S3 or a similar cloud storage service.
Employee Activity Tracker is a desktop application that monitors user activity, captures screenshots, and uploads them to an AWS S3 bucket. The application is designed for employees and employers to track work status and ensure productivity.

## FEATURES

- Screenshot Capture: Automatically takes screenshots at a user-defined interval.
- AWS S3 Integration:  Automatically upload captured screenshots and activity logs to Amazon S3 .
- Activity Monitoring: Tracks user activity such as active window focus.
- Error Handling and Resilience : 
                    1. No Internet Connection: Queue uploads and retry when the connection is restored.
                    2. Firewall Restrictions: Detect rewall issues and provide user-friendly error messaging.

## PROJECT STRUCTURE

Desktop Agent
    |
    |___project/
    |   │
    |   ├── app/
    |   │   ├── __init__.py
    |   │   ├── user_interface.py
    |   │   ├── monitoring.py
    |   │   ├── utils.py
    |   │   ├── config/
    |   │   │   ├── __init__.py
    |   │   │   ├── poller.py
    |   │   │   └── settings.py
    |   │   └── assets/
    |   │       ├── screenshots/
    |   │       |── logs/
    |   |       └── icon/
    |   │
    |   ├── tests/
    |   │   ├── __init__.py
    |   │   ├── test_gui.py
    |   │   ├── test_integration.py  # File for Integration tests.
    |   │   ├── test_monitoring.py   # File for Unit tests for the monitoring of the application.
    |   │   ├── test_poller.py
    |   │   ├── test_utils.py 
    |   │  
    |   ├── main.py
    |   └──requirements.txt
    └── README.md

## INSTALLATION

1. Clone the repository:

    ```bash
    git clone https://github.com/tusharrawat7890/Vinove_Python-Agent_project
    cd workstatusagent
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## TO RUN THE APPLICATION

1. First, open the terminal and then download all the dependencies.
2. Then, Do the AWS Configuration using `aws confiure` on terminal. 
<!-- This Step is `important` Don't miss out this step, without this step screenshot did't save on a `AWS s3 Bucket`. -->

3. Then, start the application using `python main.py`.
4. The application will open, and the interface will look like this: ![alt text](DEMO_IMAGE/image.png).
5. Enter all the configuration settings in the application.
6. Click `Start Tracking` to begin tracking and capturing screenshots.
7. To stop monitoring, click `Stop Tracking`.
8. Use the `Clear` button to reset all settings.


## CONFIGURATION

# CONFIGURATION FILE
The application uses `config/settings.py` for configuration. You can also configure settings directly through the GUI.

## GUI CONFIGURATION

- Screenshot Interval: Set the interval in minutes for capturing screenshots.
- AWS S3 Bucket Name: Enter the name of the AWS S3 Bucket.
- AWS Access Key and Secret Key: Provide your AWS credentials.
- AWS Region: Specify the AWS region.
- Timezone: Select the timezone for timestamping screenshots.
- Capture Screenshots: Enable or disable screenshot capturing.

## TESTING

The `EMPLOYEE ACTIVITY TRACKER` includes a suite of unit and integration tests to ensure the stability and reliability of the application. The tests are located in the `tests/` directory and cover various aspects of the application's functionality.

# RUNNING TESTS
1. Navigate to the project directory:

    ```bash
    python main.py
    ```

2. Run all tests using pytest:

    ```
    pytest
    ```

- This command will automatically discover and execute all the test cases in the tests/ directory.
## UNIT TESTS

- Unit tests are available for different modules of the application.

- To run the unit tests:

    ```bash
    python -m unittest discover -s tests
    ```

## INTEGRATION TESTS

- Integration tests ensure that different parts of the application work together as expected.

- To run the integration tests:

    ```bash
    python -m unittest tests/test_integration.py
    ```

## TEST STRUCTURE

- `test_gui.py`: Tests related to the graphical user interface.
- `test_integration.py`: Integration tests to verify that different modules work together as expected.
- `test_monitoring.py`: Unit tests for the monitoring module.
- `test_poller.py`: Tests for the configuration polling functionality.
- `test_utils.py`: Tests for utility functions used in the application.

## DEVELOPMENT

Feel free to contribute to the development of this application by submitting pull requests or reporting issues. For feature requests and bug reports, please open an issue on the repository.
