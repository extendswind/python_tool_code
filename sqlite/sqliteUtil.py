#!/bin/python

import sqlite3
import random


class SqliteOperator:
  def __init__(self, dbFile):
    self.conn = sqlite3.connect(dbFile)
    self.cursor = self.conn.cursor()

  # 此表中的USED用于检核奖品是否使用过
  # 不同于QrImgInfo表中的USED
  def createUserLuckyInfoTable(self):
    self.cursor.execute('''CREATE TABLE TestTable
       (ID INT PRIMARY KEY     NOT NULL,
        ATTR1 VARCHAR,
        REMARK   NVARCHAR);''')
    print("Table created successfully")
    self.conn.commit()


  # 插入数据
   def insertData(self, id, attr1, remark=""):
    sqlStr = "INSERT INTO TestTable (ID, ATTR1, REMARK) VALUES ({}, {}, {})" \
     .format(id, attr1, remark)
    self.cursor.execute(sqlStr)
    self.conn.commit()


  # 根据ID查询一条数据
  def queryUserById(self, id):
    sqlStr = "select * from TestTable where ID = {}".format(id)
    self.cursor.execute(sqlStr)
    for row in self.cursor:
      return row

  
  # 查询所有数据
  def queryAll(self):
    self.cursor.execute("SELECT * from TestTable")
    for row in self.cursor:
      print(row)


  # 判断ID是否存在
  def idExists(self, table, id):
    sqlStr = "select count(*) from {} where ID = {}".format(table, id)
    self.cursor.execute(sqlStr)
    count = self.cursor.fetchone()[0]
    if count == 0:
      return False
    else:
      return True


  # 更新某一条数据
  def updateData(self, id):
    sqlStr = "update TestTable set Attr1 = 1 where ID = {}".format(id)
    self.cursor.execute(sqlStr)
    self.conn.commit()


  # 关闭数据连接
  def __del__(self):
    self.conn.close()


if __name__ == '__main__':
  oper = SqliteOperator('data_test.db')
#   oper.createTable()
  # print(oper.idExists('QrImgInfo', 80285468) )
  # print(oper.queryUserById(802854684))
#  oper.queryAll()
