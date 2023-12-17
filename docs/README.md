# flask_e2e_project
# HHA 504 Final Project

## Technologies (approaches) utilized:  
- Github (Version Control)
- Flask (Python; Frotend & Backend)
- MySQL (Database via GCP or Azure)
- SQLAlchemy (ORM)
- .ENV (Environment Variables)
- Tailwind (Frontend Styling)
- Authorization (Google OAuth)
- API Service (Flask Backend)
- Logger and or Sentry.io (Debugging & Logging)
- Docker (Containerization)
- GCP or Azure (Deployment) 

## Project Description:
This is a flask app that displays data from the NYC Leading Causes of Death dataset. The data is stored in a MySQL database. The app is deployed on Azure. When opening the app, there is a button that asks the user to login with their gmail account. After logging in, the user will be able to see a dashboard with their account information. Clicking on the "Data" button will display the data from the database. Clicking on the "Dashboard" redirects the user to the dashboard, where the user can then click on the "Logout" button to logout of their account.

## Documentation:
+ More information about each process can be found in the respective scripts.
1. Extracting Data from API using [this link](https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/explore/query/.SELECT%0A%20%20%60year%60%2C%0A%20%20%60leading_cause%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60race_ethnicity%60%2C%0A%20%20%60deaths%60%2C%0A%20%20%60death_rate%60%2C%0A%20%20%60age_adjusted_death_rate%60%0AORDER%20BY%20%60year%60%20DESC%20NULL%20FIRST/page/filter).
2. Login to [Azure Portal](https://portal.azure.com/#home) and deploy a MySQL database and web app.
3. Login to [Google Cloud](https://console.cloud.google.com/) and enable the Google+ API and create credentials for OAuth.
4. Use SQLAlchemy to connect to the database and create a schema.
5. Use alembic to create a migration script.
6. Use MySQl Workbench to connect to the database.
7. Create a Python script to connect to the database.
8. Create a Python script to insert data into database.
9. Create flask app to display data from database.
10. Test run app on docker.
11. Deploy app to Azure.

## Steps to run the app:
### Run the app locally:
1. Clone the repo.
2. Create a virtual environment.
3. Install the requirements.
4. Create a .env file and add the variables. The template is provided later.
5. `cd` into the app folder and run the app using `python app.py`.
## Run the app on docker:
+ Using on VSCode requires installing the docker extension and docker desktop.
1. Clone the repo.
2. Create a virtual environment.
3. Install the requirements.
4. Create a .env file and add the variables. The template is provided later.
5. `cd` into the app folder and run the app using `docker build -t <image> .` and `docker run -p 5000:5000 <image>`.
6. Nagivate to port 5000 and view the app.
## Deploy the app on Azure:
* Using on VSCode requires install the Azure extension.
1. On the menu bar, click on the Azure icon.
2. Under Resources, click on App Services. Make sure an app service is created.
3. Click on the app service and click on Deploy to Web App. Select the folder where the app is located.
4. After the app is deployed, click on the app service and click on Browse Website.

## .ENV Template:
```
GOOGLE_CLIENT_ID = 
GOOGLE_CLIENT_SECRET = 

DB_URL = 

DB_HOST=
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
DB_PORT=
DB_CHARSET=
```
