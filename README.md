# drf-user-team-create-api
## Online management system for create users, team and team-members

## Setup and Local Installation

### To set up and run the project locally, follow these steps:

#### 1.  Clone the repository:

```python
git clone https://github.com/OleksandrYanchuk/py-airport-api-service.git
```
#### 2. Open the folder:
```python
cd py-airport-api-service
```
#### 3. Create a virtual environment:
```python
python -m venv venv
```
#### 4. Activate the virtual environment:
   
##### - For Windows:
```python
venv\Scripts\activate
```
##### -	For macOS and Linux:
```python
source venv/bin/activate
```
#### 5. Setting up Environment Variables:

##### 1. Rename a file name `.env_sample` to `.env` in the project root directory.

##### 2. Make sure to replace all enviroment keys with your actual enviroment data.

#### 6. For run application manually make next steps:

```python
pip install -r requirements.txt
```
```python
python manage.py migrate
```
#### 7.Run server:
```python
python manage.py runserver
```
#### 8. Open your web browser and go to http://localhost:8000 to access the application.

#### 9. If necessary, it is possible to register a new user using the following link:
```python
http://localhost:8000/api/user/register/
```
##### You can get information about the available tokens for the user at the following link:
```python
http://localhost:8000/api/user/token/
```
## Test users were created to test the API
admin:
- email: admin@admin.com
- pass: 1234admin

user:
- email: user@user.com
- pass: 1234user
user1:
- email: user1@user.com
- pass: 1234user
user2:
- email: user2@user.com
- pass: 1234user
