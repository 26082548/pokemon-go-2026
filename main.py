from pokemon import create_app

app = create_app()

# เพิ่ม 2 บรรทัดนี้เข้าไปเพื่อให้ Flask เริ่มรันเซิร์ฟเวอร์
if __name__ == '__main__':
    app.run(debug=True)