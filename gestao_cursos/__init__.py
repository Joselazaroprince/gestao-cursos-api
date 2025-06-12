# gestao_cursos_api/__init__.py
import pymysql

pymysql.install_as_MySQLdb()
pymysql.version_info = (1, 4, 6, 'final', 0)  # Evita warnings