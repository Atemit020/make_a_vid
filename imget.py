from selenium import webdriver
from PIL import Image

driver = webdriver.Firefox()
driver.get('https://www.reddit.com/r/Showerthoughts/comments/1223q93/people_who_live_alone_have_a_higher_chance_of/')

driver.get_screenshot_as_file("wow.png")

driver.quit()
print("end")

im = Image.open(r"./wow.png")
width, height = im.size

left = 5
top = height / 4
right = 164
bottom = 3 * height / 4

im1 = im.crop((322, 275, 960, 440))

im1.save("wow_cropper.png")