TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.mysql",  # 数据库选择
            "credentials": {  # 配置项
                "host": "127.0.0.1",
                "port": "3306",
                "user": "root",
                "password": "123456",
                "database": "fastapi",
                "minsize": 1,
                "maxsize": 5,
                "charset": "utf8mb4",
                "echo": True
            }
        },
    },
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        }
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai"
}
