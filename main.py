from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pyfzf.pyfzf import FzfPrompt
import mpv
import os



player = mpv.MPV(ytdl=True)

options = Options()
options.add_argument("--headless")

driverService = Service("/snap/bin/geckodriver")
driver = webdriver.Firefox(service=driverService,options=options)


search_query = str(input("What would you like to watch: "))

driver.get(f"https://www.youtube.com/results?search_query={search_query}")

driver.implicitly_wait(3)

banner_element = driver.find_element(By.XPATH, "/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
banner_element.click()

results = driver.find_elements(By.ID, "video-title")

views = driver.find_elements(By.XPATH, """/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[4]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]""")

diction = {}

for i in range(len(results)):

    diction.update({results[i].text:results[i].get_attribute('href')})


fzf = FzfPrompt('/home/mirnosir/Downloads/fzf')
answer = fzf.prompt(diction)

print(diction[answer[0]])

link = diction[answer[0]]
os.system(f"mpv {link}")


driver.close()