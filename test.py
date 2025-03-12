# import subprocess
# from selenium import webdriver

# # Đường dẫn đến trình duyệt Edge và EdgeDriver
# edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
# edge_driver_path = "C:\\Users\\vthth\\Downloads\\edgedriver_win32\\msedgedriver.exe"

# # Cấu hình trình duyệt Edge
# options = webdriver.EdgeOptions()
# options.use_chromium = True  # Sử dụng Chromium
# options.binary_location = edge_path  # Đặt đường dẫn đến Edge
# # options.add_argument("--headless")  # Ẩn cửa sổ trình duyệt
# options.add_argument("--disable-gpu")  # Tắt GPU để tránh lỗi hiển thị

# # Khởi động trình duyệt Edge với EdgeDriver
# driver = webdriver.Edge(options=options)

# # Mở trang web cần kiểm tra
# url = "http://selenium.dev"
# url = "http://daa.uit.edu.vn"
# driver.get(url)


# # Đóng trình duyệt
# driver.quit()
