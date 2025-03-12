import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Hàm kiểm tra lỗi đăng nhập
def check_error_message(driver):
    try:
        error_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-error"))
        )
        return error_element.text.strip()  # Trả về nội dung lỗi nếu có
    except:
        return None  # Không có lỗi

# Hàm thực hiện đăng nhập
def login_drl(username, password):
    url = "http://drl.uit.edu.vn/user/login"
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--log-level=0")
    driver = webdriver.Edge(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.ID, "edit-name"))).send_keys(username)
        driver.find_element(By.ID, "edit-pass").send_keys(password)
        driver.find_element(By.ID, "edit-pass").send_keys(Keys.RETURN)

        # Kiểm tra URL thay đổi hoặc có lỗi hiển thị
        error_message = check_error_message(driver)
        if error_message:
            return "failure", error_message  # Nếu có lỗi thì trả về failure + nội dung lỗi
        elif url != driver.current_url:
            return "success", None  # Đăng nhập thành công, không có lỗi
        else:
            return "time out", "Không rõ nguyên nhân"  # Đăng nhập thất bại nhưng không có thông báo lỗi
    finally:
        driver.quit()

# Đọc dataset từ CSV
df = pd.read_csv("account.csv")

# Biến đếm số lượng kết quả đúng và sai
correct_count = 0
incorrect_count = 0
incorrect_cases = []

# Kiểm tra từng tài khoản trong dataset
for index, row in df.iterrows():
    result, error_message = login_drl(row["username"], row["password"])
    
    # So sánh với kết quả mong đợi
    if result == row["expected_result"]:
        correct_count += 1
    else:
        incorrect_count += 1
        incorrect_cases.append({
            "username": row["username"],
            "expected": row["expected_result"],
            "actual": result,
            "error_message": error_message
        })

# In kết quả tổng kết
print(f"✅ Số trường hợp đúng: {correct_count}")
print(f"❌ Số trường hợp sai: {incorrect_count}")

# In chi tiết các trường hợp sai
if incorrect_count > 0:
    print("\n❗ Các trường hợp sai:")
    for case in incorrect_cases:
        print(f"- User: {case['username']}, Kỳ vọng: {case['expected']}, Kết quả thực tế: {case['actual']}")
        if case["error_message"]:
            print(f"  ⚠️ Lỗi: {case['error_message']}")
