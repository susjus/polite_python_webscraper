"""selenium_example.py"""

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Chrome(options=opts)
browser.get('https://duckduckgo.com')
print('The title of the website is:\n' + browser.title + '\n')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

results = browser.find_elements_by_class_name('result')
print('The top search result for "real python" is:\n' + results[0].text + '\n')

browser.close()
quit()
