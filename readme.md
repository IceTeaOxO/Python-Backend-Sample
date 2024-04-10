## 安裝
```
pip install -r requirements.txt
```

## 說明
這是一個python flask backend 範本，套用MVC架構(沒有view)

在app/routes新增路由

models新增DB model，並在models/__init__.py引入

controller負責處理API request

若有需要可另外新增services

## dockerfile
```
docker build -t imageName .
```