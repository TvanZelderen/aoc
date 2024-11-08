# Python_template
This is my template for python projects

To start this project please create a virtual environment using virtualenv

# To use the current environment
virtualenv venv
# To use a specific environment (Y)
virtualenv venv -p 3.Y 

Then activate the virtual environment using

.venv/Scripts/activate

Check the version using 

which python3

# Installing the required packages

pip install -r requirements.txt

# Formatting and linting
This project uses ruff

To lint:
ruff check
ruff check --fix

To format:
ruff format
