# insertData_sqlite3.py
import sqlite3
 
DB_Name = 'db.sqlite3'
# 连接数据库，如果不存在则会在当前目录创建
conn = sqlite3.connect(DB_Name)
try:
    # 创建游标
    cursor = conn.cursor()

    # 向STUDENT表插入数据的SQL语句
    # SQL = '''
    #       INSERT INTO `rbac_menu` (id, name, icon, path, is_frame, is_show, sort, component, pid_id) VALUES (33,"出库统计", "system", "grainout", false, true, 101, "system/grainout/index", 1);
    #       '''
    SQL = '''
          UPDATE rbac_menu SET name = '玉米入库' WHERE id = 29
          '''
    
    # 插入数据
    cursor.execute(SQL)
 
    # 提交到数据库
    conn.commit()
    print('插入数据到表STUDENT成功')
except Exception as e:
    print(e)
    # 回滚
    conn.rollback()
    print('插入数据到表STUDENT失败')
finally:
    # 关闭数据库
    conn.close()
