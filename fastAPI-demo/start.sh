#!/bin/bash

# 运行 Uvicorn 服务器以启动 ASGI web 应用程序
# 模块路径: app.main
# --reload: 在开发模式下运行，自动重新加载服务器当源代码更改时
# --lifespan off: 禁用生命周期事件处理
# :app 指的是 FastAPI 应用实例的名称，即在你的代码中创建的 app = FastAPI()

uvicorn app.main:app --reload --lifespan off

