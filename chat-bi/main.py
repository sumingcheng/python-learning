import uvicorn
from fastapi import FastAPI, HTTPException
import mysql.connector
import sys
from pydantic import BaseModel
import os
import logging
import sqlparse
import openai
from openai import OpenAIError
import re  # 用于正则表达式处理

from dotenv import load_dotenv

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 加载环境变量
ENV = os.getenv('ENVIRONMENT', 'development')

if ENV == 'development':
    load_dotenv(dotenv_path='.env.development')
elif ENV == 'production':
    load_dotenv(dotenv_path='.env.production')
else:
    load_dotenv()

app = FastAPI()


# 定义请求体模型
class QueryRequest(BaseModel):
    user_input: str


# 数据库连接函数
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', 13306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'chat-bi')
    )
    return connection


# 验证SQL查询，仅允许SELECT语句
def validate_sql_query(sql_query):
    parsed = sqlparse.parse(sql_query)
    for statement in parsed:
        if statement.get_type() != 'SELECT':
            raise ValueError("仅允许执行 SELECT 查询。")


# 将用户查询解析为SQL查询
def parse_query_to_sql(user_query):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    if not openai.api_key:
        raise ValueError("未找到 OpenAI API 密钥，请设置 OPENAI_API_KEY 环境变量。")

    # 提供数据库结构信息
    database_schema = """
    数据库包含以下表：

    表名：products
    字段：
      - id (INT, PRIMARY KEY)
      - name (VARCHAR(255))

    表名：sales
    字段：
      - id (INT, PRIMARY KEY)
      - product_id (INT)
      - amount (DECIMAL(10,2))
      - date (DATE)
    """

    messages = [
        {"role": "system", "content": f"你是一个将自然语言查询直接转换为针对 MySQL 数据库的 SQL 查询的助手。请只返回 SQL 查询，不要添加任何额外的说明、解释或文本。\n\n数据库结构：\n{database_schema}"},
        {"role": "user", "content": f"请将以下自然语言查询直接转换为 SQL 查询，只返回 SQL 语句：\n\n\"{user_query}\""}
    ]

    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',  # 或 'gpt-4'，如果有权限
            messages=messages,
            temperature=0,
            max_tokens=150,
            n=1,
            stop=None
        )
        raw_response = response['choices'][0]['message']['content'].strip()
        logging.info(f"原始 OpenAI 响应: {raw_response}")

        # 提取纯粹的 SQL 查询
        sql_query = raw_response

        # 如果包含代码块，提取其中的内容
        if "```" in raw_response:
            matches = re.findall(r"```(?:sql)?\s*(.*?)\s*```", raw_response, re.DOTALL)
            if matches:
                sql_query = matches[0].strip()
        else:
            # 寻找第一个以 SELECT 开头的语句
            select_index = raw_response.lower().find("select")
            if select_index != -1:
                sql_query = raw_response[select_index:].strip()

        logging.info(f"提取的 SQL 查询: {sql_query}")
        return sql_query
    except OpenAIError as e:
        logging.error(f"OpenAI API 错误: {e}")
        raise ValueError("解析查询失败，请稍后重试。")


# 执行 SQL 查询并返回结果
def execute_sql_query(sql_query):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        logging.info(f"执行 SQL 查询: {sql_query}")
        cursor.execute(sql_query)
        columns = cursor.column_names
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"columns": columns, "data": results}
    except mysql.connector.Error as err:
        logging.error(f"数据库错误: {err}")
        raise ValueError("数据库查询失败。")


# 将结果格式化为 echarts 可用的数据格式
def format_for_echarts(data):
    columns = data['columns']
    rows = data['data']
    echarts_data = {
        'columns': columns,
        'rows': [list(row) for row in rows]
    }
    return echarts_data


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
        uvicorn.run(app, host="0.0.0.0", port=9000)


if __name__ == "__main__":
    main()
