from setuptools import setup
import os
from os import path as os_path
import shutil

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        desc = f.read()
    return desc


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

# 删除无用文件
for bit in [32,64]:
    path = f'./py_femas/lib{bit}'
    for f in os.listdir(path):
        if os.path.isdir(f):
            continue
        if os.path.splitext(f)[1] not in ['.dll', '.so']:
            os.remove(f'./py_femas/lib{bit}/{f}')

long_description = read_file('setup.md')
long_description_content_type = "text/markdown",  # 指定包文档格式为markdown

# 生成requirements.txt pipreqs --encoding=utf8 --force py_femas

setup(
    name='py_femas',  # 包名
    python_requires='>=3.7.0',  # python环境
    version='0.0.2',  # 包的版本
    description="Python Femas futures api",  # 包简介，显示在PyPI上
    long_description=long_description,  # 读取的Readme文档内容
    long_description_content_type=long_description_content_type,  # 指定包文档格式为markdown
    author="HaiFeng",  # 作者相关信息
    author_email='haifengat@vip.qq.com',
    url='https://github.com/haifengat/hf_femas',
    # 指定包信息，还可以用find_packages()函数
    # packages=find_packages(),
    packages=['py_femas'],
    install_requires=read_requirements('requirements.txt'),  # 指定需要安装的依赖
    include_package_data=True,
    license="MIT License",
    platforms="any",
    data_files=['README.md'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
