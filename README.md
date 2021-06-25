# Initial Setup
- Install mysql
  ```
  sudo apt install mysql-server
  ```
- Make the mysql username and password **"root"**, ("should be true by default)
- Start the mysql server
  ```
  sudo systemctl start mysql
  ```
- Install virtualenv
  ```
  pip install virtualenv
  ```
- Create a virtual environment with virtualenv
  ```
  virtualenv env
  ```
- Activate virtual environment, **this must be done every time the project is opened**
  ```
  source ./env/bin/activate
  ```
- Install the requirments
  ```
  pip install requirements.txt
  ```
- Run the setup script to generate the python models for json schemas and for sql alchemy
  ```
  sh ./shell_scripts/setup.sh
  ```

# Installing New Requirments

- Whenever new requirments are installed using pip run
  ```
  pip freeze > requirements.txt
  ```
# Running Application Localy
- Ensure the virtual environment is running
  ```
  source ./env/bin/activate
  ```
