import logging
import sys
import uvicorn
from fastapi import FastAPI, HTTPException

from app.settings import load_environment
from app.models import QueryRequest
from app.openai_utils import parse_query_to_sql
from app.sql_validation import validate_sql_query
from app.db import execute_sql_query
from app.formatting import format_for_echarts

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 加载环境变量
ENV = load_environment()

app = FastAPI()


# 处理查询请求的路由
@app.post("/query")
def handle_query(request: QueryRequest):
    try:
        user_input = request.user_input
        sql_query = parse_query_to_sql(user_input)
        validate_sql_query(sql_query)
        data = execute_sql_query(sql_query)
        echarts_data = format_for_echarts(data)
        return {"echarts_data": echarts_data}
    except Exception as e:
        logging.error(f"处理查询 '{request.user_input}' 时出错: {e}")
        # 开发环境返回详细错误信息
        if ENV == 'development':
            raise HTTPException(status_code=500, detail=str(e))
        else:
            raise HTTPException(status_code=500, detail="服务器内部错误，请稍后重试。")


# 主函数
def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        # 命令行测试模式
        user_input = input("请输入您的查询：")
        try:
            sql_query = parse_query_to_sql(user_input)
            print(f"生成的 SQL 查询：\n{sql_query}")
            data = execute_sql_query(sql_query)
            echarts_data = format_for_echarts(data)
            print(f"查询结果：\n{echarts_data}")
        except Exception as e:
            print(f"错误：{e}")
    else:
        # 运行 FastAPI 服务器
        uvicorn.run(app, host="0.0.0.0", port=13000)


if __name__ == "__main__":
    main()
