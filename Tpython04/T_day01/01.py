# 字符	    功能
# .	        匹配任意1个字符（除了\n）
# [ ]	    匹配[ ]中列举的字符
# \d	    匹配数字，即0-9
# \D	    匹配非数字，即不是数字
# \s	    匹配空白，即 空格，tab键
# \S	    匹配非空白
# \w	    匹配单词字符，即a-z、A-Z、0-9、_
# \W	    匹配非单词字符

# *         可以出现零次或者多次
# +         至少一次
# ？         一次或者没有
import re

s = """
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>
"""
resulut = re.sub(r"<\w+>+|</?\w+>|&nbsp;", "", s)
print(resulut)

