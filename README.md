# Omatcha_detection
## 本パッケージについて
- このパッケージは株式会社アールティ様([公式サイト](https://rt-net.jp/))より販売されているCRANE-X7をROS環境で
運用する際に使用できるパッケージです。使用するにはCRANE-X7本体とアールティ様から配布されているCRANE-X7[オリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)、環境構築が必要となります。  
本パッケージは上記の[オリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)を元に2023年度の設計製作論実習3内でチーム大三元が開発を行なったものです。  

- このパッケージはCRANE-X7を使ってお抹茶を点てるためのパッケージです。本アプリケーションはこのOmatcha_detectionと[Omatcha_actions](https://github.com/Orbital-G/Omatcha_actions)の二つのパッケージをセットで使用する必要があります。合わせてのインストールをお願いします。
CRANE-X7、お抹茶の粉が入った容器、茶筅、お湯と茶碗を用意して配置し、パッケージ内のスクリプトを実行することで、お抹茶を点てることができます。

#環境構築

##本パッケージ及びCRANE-X7のROSパッケージのインストール
'''
$ cd ~/catkin_ws/src/ 
$ git clone https://github.com/rt-net/crane_x7_ros.git
$ git clone https://github.com/Orbital-G/Omatcha_detection.git
$ cd Omatcha_detection/scripts
$ pip install -r requirement.txt
$ (cd ~/catkin_ws && catkin_make)
'''

##実行手順
###CRANE_X7をセットアップ

###IntelRealSenseを取りつける

'''
$ cd src
$ sudo chmod 666 /dev/ttyUSB*
$ roslaunch crane_x7_bringup demo.launch fake_execution:=false
$ rosrun Omatcha_detection detect_pub.py
'''

