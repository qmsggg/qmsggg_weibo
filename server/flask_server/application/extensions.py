# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建数据库的基类
Base = declarative_base()

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://qmsggg:qmsggg@localhost:3306/weibo')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

session = DBSession()