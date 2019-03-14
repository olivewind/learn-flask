# learn flask


## 创建虚拟环境
```bash
virtualenv --no-site-packages venv
source venv/bin/activate
```

## 安装依赖
```bash
pip install -r requirements.txt 
```

## 初始化数据库 
```bash
python manage.py db init  
python manage.py db migrate  
```

## 启动开发环境
```bash
python manage.py
```