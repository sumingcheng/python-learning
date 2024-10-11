# learning
[配套文档](https://www.yuque.com/sumingcheng/python)

## 查看环境

```
conda env list
```

## 创建环境

```
conda create -n learning python=3.10.13
```

## 进入环境

```
conda activate learning
```

## 退出

```
conda deactivate
```

## 删除

```
conda remove -n learning --all
```

## 克隆环境

```
conda create --name new_env_name --clone existing_env_name
```

## 创建环境管理文件

**从 `.yml` 文件创建环境**： 可以通过 `environment.yml` 文件创建一个新的环境

```
conda env create -f environment.yml
```

## 导出环境

```
conda env export > environment.yml
```



