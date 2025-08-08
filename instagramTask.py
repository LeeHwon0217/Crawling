import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(webdriver)
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(3)  # 초기 로딩 대기

# XPath 경로
login_id_xpath = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input'
login_pw_xpath = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input'
login_btn_xpath = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div[1]/div[3]/button'
select_postpone_btn = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div'
find_btn = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div'
search = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/input'
search_travel = '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]'
result01 = '//html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[2]/div/div[1]/div[3]/div/a/div[1]/div[2]'
like = '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/div/div'
comment = '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
enter = '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]'

# 로그인
driver.find_element(By.XPATH, login_id_xpath).send_keys("Handsome_Ryuzy")
time.sleep(1)
driver.find_element(By.XPATH, login_pw_xpath).send_keys("HandsomeRyuzy")
time.sleep(1)
driver.find_element(By.XPATH, login_btn_xpath).click()
time.sleep(7)

# 로그인 후 "나중에 하기" 버튼 클릭
driver.find_element(By.XPATH, select_postpone_btn).click()
time.sleep(5)

# 검색 아이콘 클릭
driver.find_element(By.XPATH, find_btn).click()
time.sleep(5)

# 검색창에 해시태그 입력
driver.find_element(By.XPATH, search).send_keys("#여")
time.sleep(5)

# 자동완성된 해시태그 클릭
driver.find_element(By.XPATH, search_travel).click()
time.sleep(5)

# 결과 세 번째 게시물 클릭
driver.find_element(By.XPATH, result01).click()
time.sleep(9)

driver.get('https://www.instagram.com/p/DLrbFT_SnVY/')
time.sleep(3)  # 초기 로딩 대기

# 좋아요 버튼에 hover 후 클릭
like_button = driver.find_element(By.XPATH, like)
actions.move_to_element(like_button).perform()
time.sleep(1)
like_button.click()
time.sleep(2)

# 댓글 작성
comment_box = driver.find_element(By.XPATH, comment)
comment_box.send_keys("부러워요!")
time.sleep(3)

# 댓글 입력 버튼에 hover 후 클릭
enter_button = driver.find_element(By.XPATH, enter)
actions.move_to_element(enter_button).click().perform()
time.sleep(10)
