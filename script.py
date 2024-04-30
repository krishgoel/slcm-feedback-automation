from selenium import webdriver

import platform
system_platform = platform.system()

import os

USERNAME = os.getenv("NAME") + "." + os.getenv("REGISTRATION_NUMBER")
PASSWORD = os.getenv("PASSWORD")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
if system_platform == "Windows":
	chrome_options.add_experimental_option("detach", True)
	browser = webdriver.Chrome(options=chrome_options)
if system_platform == "Darwin":
	chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
	browser = webdriver.Chrome(options=chrome_options)

def login(loginPage = "https://mujslcm.jaipur.manipal.edu:122/Home/Index"):
	browser.get(loginPage)

	username_field = browser.find_element("name", "UserName")
	password_field = browser.find_element("name", "Password")
	username_field.send_keys(USERNAME)
	password_field.send_keys(PASSWORD)

	login_button = browser.find_element("id", "login_submitStudent")
	login_button.click()

login()

def listAllFeedbacks(feedbackPage= "https://mujslcm.jaipur.manipal.edu:122/Student/Survey/FeedbackList"):
	browser.get(feedbackPage)
	feedbacksFetch = browser.find_elements("class name", "btn-clean")

	feedbacks = [{"status": feedback.text, "link": feedback.get_attribute('href')} for feedback in feedbacksFetch]
	
	return(feedbacks)

feedbacks = listAllFeedbacks()

def fillFeedback(courseLink):
	browser.get(courseLink)

	no_buttons = browser.find_elements("xpath", "//input[@type='radio' and @class='yescheck']")
	for button in no_buttons:
		button.click()
	
	from selenium.webdriver.support.ui import Select
	dropdowns = browser.find_elements("xpath", "//select")
	for dropdown in dropdowns:
		select = Select(dropdown)
		select.select_by_value("Y")
	
	text_box = browser.find_element("xpath", "//textarea")
	text_box.send_keys("Great Experience.")
	
	submit_button = browser.find_element("xpath", "//button[@id='btnSubmit']")
	submit_button.click()

	browser.get("https://mujslcm.jaipur.manipal.edu:122/Student/Survey/FeedbackList")

feedbacks = listAllFeedbacks()

for feedback in feedbacks:
	if (feedback["status"] == "Pending"):
		fillFeedback(feedback["link"])
		feedback["status"] = "Completed"
	else:
		continue
