#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2017/1/17'
"""

import os

# 切换到 generate 目录下
os.chdir(os.path.dirname(os.path.abspath(__file__)))
src_dir = '../lnx64'   # 看穿式监管
data_type_file_name = 'USTPFtdcUserApiDataType'

import g_enum
g_enum.src_dir = src_dir
g_enum.data_type_file_name = 'USTPFtdcUserApiDataType'
g_enum.run()

import g_struct
g_struct.src_dir = src_dir
g_struct.struct_file_name = 'USTPFtdcUserApiStruct'
g_struct.run()

import g_c_py
g_c_py.src_dir = src_dir
g_c_py.spi_class_name = 'trade'
g_c_py.file_src = 'USTPFtdcTraderApi'
g_c_py.lib_name = 'libUSTPtraderapiAF'   # 看穿式监管
g_c_py.api_class_name = 'CUstpFtdcTraderApi'
g_c_py.info_struct_name = 'CUstpFtdcRspInfoField'
g_c_py.create_api = 'CUstpFtdcTraderApi::CreateFtdcTraderApi'
g_c_py.run(True, True) # 生成c+  py
# g_c_py.run(False, True)
g_c_py.spi_class_name = 'quote'
g_c_py.file_src = 'USTPFtdcMduserApi'
g_c_py.lib_name = 'libUSTPmduserapiAF'   # 看穿式监管
g_c_py.api_class_name = 'CUstpFtdcMduserApi'
g_c_py.info_struct_name = 'CUstpFtdcRspInfoField'
g_c_py.create_api = 'CUstpFtdcMduserApi::CreateFtdcMduserApi'
g_c_py.run(True, True)
# g_c_py.run(False, True)
