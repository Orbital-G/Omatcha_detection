# Omatcha_detection
## 本パッケージについて
- このパッケージは株式会社アールティ様([公式サイト](https://rt-net.jp/))より販売されているCRANE-X7をROS環境で
運用する際に使用できるパッケージです。使用するにはCRANE-X7本体とアールティ様から配布されているCRANE-X7[オリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)、環境構築が必要となります。  
本パッケージは上記の[オリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)を元に2023年度の設計製作論実習3内でチーム大三元が開発を行なったものです。  

- 本アプリケーションはCRANE-X7を使ってお抹茶を点てるアプリケーションです。CRANE-X7、Intel realsense、お抹茶の粉が入った容器、茶筅、お湯と茶碗を用意して配置し、パッケージ内のスクリプトを実行することで、お抹茶を点てることができます。このOmatcha_detectionと[Omatcha_actions](https://github.com/Orbital-G/Omatcha_actions)の二つのパッケージをセットで使用する必要があります。合わせてのインストールをお願いします。　　
このパッケージはアプリケーションのうち、物体検出の機能を担うパッケージです。Omatcha_actionsでアームの動作の制御を行います。
