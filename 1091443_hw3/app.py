from flask import Flask, render_template, request, send_file,send_from_directory,jsonify
import subprocess
import os

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/download', methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        # 獲取 textarea_data 的內容
        textContent = request.form.get('textarea_data')
        # 指定要下載的資料夾路徑和檔案名稱
        directory = 'static'
        filename = 'example.txt'

        # 將輸入的內容寫入檔案
        with open(f'{directory}/{filename}', 'w', encoding='utf-8') as file:
            if textContent:
                file.write(textContent)
                print("1")
        subprocess.run(['python', 'hw3.py'])

        # 回傳圖片檔案
        image_filename = 'my_logo.png'
        print("3")
        return send_from_directory(directory, image_filename)

    return ''  # 處理 GET 請求的回應


if __name__ == "__main__":
    app.run(debug=True,threaded=True)
 