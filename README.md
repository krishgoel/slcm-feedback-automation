# Semester-End Feedback Automation Script
An automation script for filling out semester-end feedback on my college portal - [SLCM](https://mujslcm.jaipur.manipal.edu:122/) at [Manipal, Jaipur](https://jaipur.manipal.edu/). If you need help with a similar task for a different college, feel free to reach out to me!

## Steps to Run the Script on Your Computer
Before you try to run this on your machine, ensure that you have Python and pip installed in your environment.

_For my not so technological advanced friends, download [Python 3](https://www.python.org/downloads/) and [pip](https://phoenixnap.com/kb/install-pip-windows)._

### 1. Clone this repository
1. Open up the terminal on your computer.
2. Type in the following command: ```git clone https://github.com/KrishGoel/slcm-feedback-automation.git```
3. Then type in this command: ```cd slcm-feedback-automation```

### 2. Create an Environment Variables File
1. Open up a text editor on your computer.
2. Type in the following text, replacing the parts in quotes with your own information:
	```
	NAME="your-name"
	REGISTRATION_NUMBER="your-registration-number"
	PASSWORD="your-password"
	```

	For example, _naman.219301542@muj.manipal.edu_ will be
	
	```
	NAME="naman"
	REGISTRATION_NUMBER="219301542"
	PASSWORD="baniyaBro7*"
	```

3. Save the file as ```.env``` in the same directory as the script.

### 3. Run the script
1. Make sure you're in the slcm-feedback-automation directory in the terminal.
2. Type in the following command: ```python ./script.py```
3. Press enter, and the script will run!

## Voila