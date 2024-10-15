#!/bin/bash

# 获取脚本所在目录
SHELL_FOLDER=$(cd "$(dirname "$0")"; pwd)
echo "Script directory: $SHELL_FOLDER"

# 输出当前的 PYTHONPATH
echo "Current PYTHONPATH: $PYTHONPATH"

# 设置 Python 环境变量
export PYTHONUNBUFFERED=1
export PYTHONPATH=$PYTHONPATH:$SHELL_FOLDER

# 设置环境变量为 development
export ENVIRONMENT=development

# 设置代理（如果需要）
export HTTP_PROXY="http://172.22.220.64:7890"
export HTTPS_PROXY="http://172.22.220.64:7890"

python main.py
