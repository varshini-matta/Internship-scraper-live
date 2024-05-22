# Project Overview
**Internify: Simplifying Internship Search**
This project automates the process of scraping internship listings from various websites and sends real-time notifications to students via email. This ensures that students do not miss any internship opportunities during the current period of high demand. The solution leverages Selenium for web scraping and AWS Lambda for serverless execution and notification delivery.

## Components

- **Selenium**
- **AWS Lambda**
- **API Gateway**
- **Email Notification System**

## Detailed Workflow

### 1. Scraping Internships Using Selenium

**Selenium** is a powerful tool for web automation that can interact with web pages just like a human would. It is used here to:

- **Navigate Websites**: Selenium scripts are written to access various internship listing websites, navigate through pages, and interact with web elements to extract necessary information such as internship title, company, location, application link, and deadlines.
- **Data Extraction**: The extracted data is parsed and structured into a usable format (e.g., JSON or CSV). This can include handling dynamic content that loads via JavaScript.

**Steps:**
1. Set up a Selenium WebDriver (e.g., ChromeDriver or FirefoxDriver).
2. Write scripts to load each internship website.
3. Identify HTML elements containing internship details using techniques such as XPath or CSS selectors.
4. Extract and store these details.

#### Example Screenshot 1: Selenium Scraping
![intern_csv](https://github.com/varshini-matta/Internship-scraper-live/assets/158460136/116ea1b8-0de6-4445-95c3-5e0bef8bd391)

### 2. AWS Lambda for Serverless Execution

**AWS Lambda** is a serverless compute service that runs code in response to events and automatically manages the underlying compute resources.

- **Periodic Execution**: Lambda functions can be triggered on a scheduled basis using Amazon CloudWatch Events (e.g., daily or weekly).
- **Running Selenium Scripts**: The Selenium scraping script is packaged and deployed as a Lambda function. This may require using a headless browser and ensuring all necessary dependencies (e.g., browser binaries) are included.

**Steps:**
1. Package the Selenium script and all dependencies.
2. Create a Lambda function and upload the package.
3. Set up CloudWatch Events to trigger the Lambda function on a schedule.
4. Ensure the function has the necessary permissions and resources (e.g., memory, execution time).
5. Use **API Gateway** to create an HTTP API endpoint that can trigger the Lambda function for real-time notifications.

#### Example Screenshot 2: AWS Lambda Configuration
![aws_lambda](https://github.com/varshini-matta/Internship-scraper-live/assets/158460136/2fce5589-c095-4eaa-bea3-8522a293f174)

### 3. Sending Email Notifications

Once the internships data is scraped, it needs to be sent to students via email. This is also handled within the Lambda function.

- **SMTP Service**: Use an SMTP service (e.g., Amazon SES, Gmail) to send emails.
- **Formatting Email Content**: Format the scraped data into a readable email format (e.g., plain text, HTML).
- **Sending Emails**: Use an SMTP client to send the formatted email to a list of recipients.

**Steps:**
1. Integrate with an SMTP service to send emails.
2. Format the scraped data into a well-structured email.
3. Send the email to the recipients.

#### Example Screenshot 3: Email Notification
![mail_notification](https://github.com/varshini-matta/Internship-scraper-live/assets/158460136/7ae18b1a-fc13-4f82-a2ef-0292db33fe51)
## Technical Setup

### Prerequisites

- AWS Account with Lambda, SES (if using Amazon SES), and CloudWatch permissions.
- Python environment for Selenium development.
- Email service credentials.

### Local Development

1. Develop and test the Selenium script locally.
2. Ensure all dependencies are working (e.g., headless browser setup).

### Packaging for Lambda

1. Package the Selenium script and dependencies into a deployment package (e.g., a ZIP file).
2. Include headless browser binaries in the package.

### Deploying to AWS Lambda

1. Create a Lambda function in the AWS Management Console.
2. Upload the deployment package.
3. Configure the function's execution role and permissions.
4. Set up CloudWatch Events for scheduling.
5. Configure API Gateway to trigger the Lambda function for real-time notifications.

### Testing and Monitoring

1. Test the Lambda function with sample inputs.
2. Monitor logs via CloudWatch Logs for debugging and performance tuning.



