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

## 开发
```bash
python manage.py
```

## 部署

```bash
docker build -t ImageName[:imageTag] .
docker run -p 80:8888 ImageName[:imageTag]
```


# TODO

1. 数据库外挂
2. JWT 权限认证
