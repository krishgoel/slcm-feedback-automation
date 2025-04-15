# Semester-End Feedback Automation Script

This script automates filling out the semester-end feedback form on the [SLCM portal](https://mujslcm.jaipur.manipal.edu/) for students at [Manipal University Jaipur](https://jaipur.manipal.edu/).  

## Prerequisites

Make sure Python 3 and pip are installed.  
Optional but recommended: install [Git](https://git-scm.com/downloads).

If you're new to this stuff, install:

- [Python 3](https://www.python.org/downloads/)
- [pip](https://phoenixnap.com/kb/install-pip-windows)
- [Git](https://git-scm.com/downloads)

## Setup Instructions

1. **Clone the repository**
	```bash
	git clone https://github.com/KrishGoel/slcm-feedback-automation.git
	```
	Or [download it as a zip](https://github.com/KrishGoel/slcm-feedback-automation) and extract it.

2. **Create a `.env` file**  
   Create a file named `.env` in the root directory of the project.  
   Add your credentials in the following format (provided in [`.env.example`](/.env.example)):
	```env
	NAME="krish"
	REGISTRATION_NUMBER="219310342"
	PASSWORD="NiceNiceNice3*"
	```
	Replace `NAME` and `REGISTRATION_NUMBER` with your name and registration number.

3. **Install Dependencies**
   Open a terminal in the project directory and run (ideally in a virtual environment):
	```bash
	pip install -r requirements.txt
	```

4. **Run the Script**
   In the terminal, run:
	```bash
	python main.py
	```
   This will open a browser window and start filling out the feedback form automatically.