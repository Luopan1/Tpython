####  Ubantu创建.sh文件的快捷方式，在usr/share/applications/下使用vim编辑 ####
#!/usr/bin/env xdg-open  </br  >
[Desktop Entry]    </br  >
Version=1.0   </br  >
Type=Application   </br  >
Name=PyCharm Professional Edition    </br  >
Icon=/opt/pycharm-2018.2.1/bin/pycharm.png   </br  >
Exec="/opt/pycharm-2018.2.1/bin/pycharm.sh" %f    </br  >
Comment=Python IDE for Professional Developers    </br  >
Categories=Development;IDE;    </br  >
Terminal=false      </br  >
StartupWMClass=jetbrains-pycharm    </br  >

#### ubantu下搭某个东西 ####
###### 1.安装python-pip ######
   apt-get update  </br   >
   apt-get install python-gevent python-pip </br  >
   pip install shadowsocks</br   >
###### 2.新建一个配置文件 ###### 
   vim /etc/ss.json</br   >

// 输入命令后进入编辑页面按i进入insert模式，输入下面的配置信息：</br   >
{</br   >
    "server":"0.0.0.0", </br   >
    "server_port":8388,  </br   >
    "local_port":1080,   </br   >
    "password":"barfoo!",   </br   >
    "timeout":600,   </br   >
    "method":"table"  </br   >
}
// server          服务器 IP (IPv4/IPv6)，注意这// 也将是服务端监听的 IP 地址  </br   >
// server_port     服务器端口  </br   >
// local_port      本地端端口  </br   >
// password        用来加密的密码  </br   >
// timeout         超时时间（秒）  </br   >
// method          加密方法，可选择 "bf-cfb", "aes-256-cfb", "des-cfb"等等。默认是一种不安全的加密，推荐用 "aes-256-cfb"  </br   >
###### 3.启动服务 ###### 
   ssserver -c /etc/ss.json -d start</br  >
###### 4.开机启动服务 ###### 
   /usr/local/bin/ssserver -c /etc/ss.json -d start</br  >

#### Ubantu下搭建MySQL服务 ####
###### 1.执行安装命令 ######
    sudo apt-get install mysql-server </br  >
    sudo apt isntall mysql-client   </br  >
    sudo apt install libmysqlclient-dev  </br  >

###### 2.测试是否安装成功 ######
    sudo netstat -tap | grep mysql </br>
###### 3.进入MySQL ###### 
    mysql -uroot -p</br>
###### 4.配置远程可访问 ###### 
    sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf </br>
    注释掉bind-address = 127.0.0.1 </br>
    保存退出，然后进入mysql服务，执行授权命令：</br>
    grant all on *.* to root@'%' identified by '你的密码' with grant option;</br>
    flush privileges;</br>
 ###### 5.重启MySQL服务 ###### 
    service mysql restart <br>
    
 **navicat配置：**  
 ![xxxx](Tpython3/11.png)
    
