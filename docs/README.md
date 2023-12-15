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

## Documentation:
1. Extracting Data from API using [this link](https://data.cityofnewyork.us/Health/New-York-City-Leading-Causes-of-Death/jb7j-dtam/explore/query/.SELECT%0A%20%20%60year%60%2C%0A%20%20%60leading_cause%60%2C%0A%20%20%60sex%60%2C%0A%20%20%60race_ethnicity%60%2C%0A%20%20%60deaths%60%2C%0A%20%20%60death_rate%60%2C%0A%20%20%60age_adjusted_death_rate%60%0AORDER%20BY%20%60year%60%20DESC%20NULL%20FIRST/page/filter).
2. Login to [Azure Portal](https://portal.azure.com/#home) and deploy a MySQL database.
3. Use SQLAlchemy to connect to the database and create a schema.
4. Use alembic to create a migration script.
5. Use MySQl Workbench to connect to the database.
6. Create a Python script to connect to the database.
7. Create a Python script to insert data into database.
8. Create flask app to display data from database.
9. Test run app on docker.
9. Deploy app to Azure.