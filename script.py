from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()
import os
USERNAME = (f"{os.getenv('NAME')}.{os.getenv('REGISTRATION_NUMBER')}").lower()
PASSWORD = os.getenv("PASSWORD")

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)

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

	# Select "No" on all radio buttons
	no_buttons = browser.find_elements("xpath", "//input[@type='radio' and not(@class='yescheck')]")
	print("No buttons: ", len(no_buttons))
	for button in no_buttons:
		button.click()
	
	# Select "No" on all select boxes
	from selenium.webdriver.support.ui import Select
	dropdowns = browser.find_elements("xpath", "//select")
	print("Dropdowns: ", len(dropdowns))
	for dropdown in dropdowns:
		select = Select(dropdown)
		select.select_by_value("N")
	
	# Enter a message into the text box
	text_box = browser.find_element("xpath", "//textarea")
	text_box.send_keys("Filled by an automated script :)")
	
	# Submit Form
	submit_button = browser.find_element("xpath", "//button[@id='btnSubmit']")
	submit_button.click()

	# Back to feedback page
	browser.get("https://mujslcm.jaipur.manipal.edu:122/Student/Survey/FeedbackList")

print("Feedbacks:", feedbacks, "\n\n")
for feedback in feedbacks:
	if (feedback["status"] == "Pending"):
		fillFeedback(feedback["link"])
		print(f"Filled feedback for {feedback['link']}\n")
		feedback["status"] = "Completed"
		# print("Feedbacks Now:", feedbacks, "\n\n")
	else:
		continue