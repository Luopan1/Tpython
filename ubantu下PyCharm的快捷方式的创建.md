//  Ubantu创建.sh文件的快捷方式，在usr/share/applications/下使用vim编辑。
#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm Professional Edition
Icon=/opt/pycharm-2018.2.1/bin/pycharm.png
Exec="/opt/pycharm-2018.2.1/bin/pycharm.sh" %f
Comment=Python IDE for Professional Developers
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-pycharm

//ubantu下搭某个东西
# 1.安装python#
apt-get update
apt-get install python-gevent python-pip
