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

## 创建环境文件管理

**从 `.yml` 文件创建环境**： 可以通过 `environment.yml` 文件创建一个新的环境

```
conda env create -f environment.yml
```

## 导出环境

```
conda env export > environment.yml
```

## 创建环境文件

```
```

```
name: learning
channels:
  - defaults     # 默认频道
  - conda-forge  # 添加社区频道（Conda Forge）
dependencies:
  - bzip2=1.0.8=h2bbff1b_6
  - ca-certificates=2024.9.24=haa95532_0
  - libffi=3.4.4=hd77b12b_1
  - openssl=3.0.15=h827c3e9_0
  - pip=24.2=py310haa95532_0
  - python=3.10.13=he1021f5_0
  - setuptools=75.1.0=py310haa95532_0
  - sqlite=3.45.3=h2bbff1b_0
  - tk=8.6.14=h0416ee5_0
  - tzdata=2024b=h04d1e81_0
  - vc=14.40=h2eaa2aa_1
  - vs2015_runtime=14.40.33807=h98bb1dd_1
  - wheel=0.44.0=py310haa95532_0
  - xz=5.4.6=h8cc25b3_1
  - zlib=1.2.13=h8cc25b3_1

```



