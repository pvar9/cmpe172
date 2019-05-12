# LinkMe

The purpose of this project is to connect employees within a company. 
Typically, LinkedIn and mutual friends are the primary ways for employees to expand their network. 
However, there are many employees who do not have a LinkedIn. 
This can be difficult for employees and especially new hires who are trying to connect with others and broaden their network.
LinkMe provides a solution to this issue by giving employees the opportunity to gain insight on other’s work and contributions within the company. 
From changing departments to different roles within a team, LinkMe keeps track of employee’s job history.
Employees can learn about one another, recommend members of similar experience to work together, and influence an internal network of familiarity within the company. 
This not only does LinkMe provide a way for employees to expand their network but also improve the work culture from within.

## Getting Started
The LinkMe_Application_Source v2 holds the most up to date working version for the application. Inside the directory the main.py file has the file to test the project on your machine.

### Prerequisites

The main libraries to install are listed below. More requirements maybe be needed. 

```
pip install flask
```
```
pip install WTForms
```

```
pip install flask_oidc
```

### Data/Database Creation

All of the data for the application is available on https://github.com/datacharmer/test_db provided by Instructor Andrew Bond in the project requirments. 

MySQL was used for the database requirements. All SQL queries can be found in database_connect.py

### Project Files Description

Front-End Components are located in ```/templates```. All styling components and images are located in ```/static```.

Back-End Components are located in ```database_connect.py main.py okta_api.py```

```client_secrets.json``` includes okta specific tokens for developer account [included for project purposes]


## Deployment
Deployment for the project was done on AWS EC2 instance. More information can be found here https://aws.amazon.com/ec2/.

## Authors

* **Priyank Varshney** 
* **Navina Mathew** 
