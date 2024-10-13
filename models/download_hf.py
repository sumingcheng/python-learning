from huggingface_hub import snapshot_download

# 指定模型的标识符和目标下载目录
model_id = 'ModelTC/bge-large-zh-v1.5'
target_dir = '/home/smc/vchatbi-plugin-zz/models/bge-large-zh-v1.5'

# 使用 'snapshot_download' 函数，并设置 'cache_dir' 参数
model_dir = snapshot_download(repo_id=model_id, cache_dir=target_dir)

print(f"模型已下载到: {model_dir}")
