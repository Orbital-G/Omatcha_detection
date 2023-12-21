# Omatcha_detection
## 本パッケージについて
- このパッケージは株式会社アールティ様([公式サイト](https://rt-net.jp/))より販売されているCRANE-X7をROS環境で
運用する際に使用できるパッケージです。使用するにはCRANE-X7本体とアールティ様から配布されているCRANE-X7[オリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)、環境構築が必要となります。  
本パッケージは上記の[オリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)を元に2023年度の設計製作論実習3内でチーム大三元が開発を行なったものです。  

- 本アプリケーションはCRANE-X7を使ってお抹茶を点てるアプリケーションです。  
CRANE-X7、Intel RealSense、お抹茶の粉が入った容器、茶筅、お湯と茶碗を用意して配置し、パッケージ内のスクリプトを実行することで、お抹茶を点てることができます。  
このOmatcha_detectionと[Omatcha_actions](https://github.com/Orbital-G/Omatcha_actions)の二つのパッケージをセットで使用する必要があります。合わせてのインストールをお願いします。  

- このパッケージはアプリケーションのうち、物体検出の機能を担うパッケージです。Omatcha_actionsでアームの動作の制御を行います。

## 動作環境
* OS: Ubuntu20.04  
* ROS Distribution: ROS Noetic

## 使用機材
* CRANE-X7  
* Intel RealSense  
* 茶筅  
* 茶碗  
* 抹茶を入れる容器(直径30mm程度)  

## 環境構築
[こちらのスライド](https://github.com/ryuichiueda/my_slides/blob/master/robotdesign3_2021/lesson1.md)を元に
ROSのインストールとワークスペースの構築を行ってください。  
以降、ワークスペースはcatkiin_wsを例として説明します。  
1. catkin_ws/src内にCRANE-X7のROSパッケージをインストールしてください。
```sh
cd ~/catkin_ws/src  
git clone https://github.com/rt-net/crane_x7_ros.git  
```

2. catkin_ws/src内に二つのパッケージOmatcha_detectionとOmatcha_actionsをインストールしてビルドしてください。
```sh
cd ~/catkin_ws/src
git clone https://github.com/Orbital-G/Omatcha_detection.git
git clone https://github.com/Orbital-G/Omatcha_actions.git
cd ~/catkin_ws  
catkin_make  
```

3. RealSenseのインストール
RealSenseを使用するためにワークスペース内にソースコードをダウンロードしてパッケージをビルドしてください
```sh
cd ~/catkin_ws/src/
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
cd ~/catkin_ws/
catkin_make
```

## 実行方法
次にCRANE-X7をPCに接続し、以下のコマンドでデバイスドライバに実行権限を与えCRANE-X7とPCが通信できる状態にします。  
そしてオリジナルのパッケージ内のlaunchファイルを使用してROSノードが通信できるようにします。
```sh
sudo chmod 666 /dev/ttyUSB0
roslaunch crane_x7_bringup demo.launch
```

合わせて以下のコマンドでRealSenseを使用できる状態にしておきます。
```sh
roslaunch realsense2_camera rs_camera.launch  
```

CRANE-X7の正面に茶碗を、周囲の離れたところに抹茶の入った容器、茶筅を配置してください。  
なお、このアプリケーションは液体を扱います。機器の浸水等に注意してください。  
以下のコマンドを実行すると物体を探し、検出できると物体を掴みに行きます。

タブを新たに開いてOmatcha_detection内の行いたいコマンドを実行してください。  
detect_matcha:抹茶の容器を探すコマンド  
detect_chasen:茶筅を探すコマンド
```sh
./detect_matcha
./detect_chasen
```

次にタブを新たに開いてセットのパッケージOmatcha_actions内のコマンドを実行してください。
action_matcha:抹茶の容器を掴むコマンド  
action_chasen:茶筅を掴むコマンド
```sh
./action_matcha
./action_chasen
```

実際に本アプリケーションを実行した際の動画です。

https://github.com/Orbital-G/Omatcha_detection/assets/147364200/17e6c89e-84b5-47d0-828d-5f6ebd7feed1

## ライセンス
このパッケージOmatcha_detectionではYOLOv5を使用しています。
本リポジトリの内容はGPLv3に準拠し、公開しています。
