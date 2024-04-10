# 使用官方 Python 鏡像作為基礎鏡像
FROM python:3.10

# 設定工作目錄為 /app
WORKDIR /app

# 將 requirements.txt 複製到工作目錄
COPY requirements.txt .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製整個專案到工作目錄
COPY . .

# 指定 Flask 應用的入口點
CMD ["python", "run.py"]
