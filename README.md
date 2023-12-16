# Omatcha_detection
## 本パッケージについて
* 本パッケージは、株式会社アールティ様([公式サイト](https://rt-net.jp/))より販売されているCRANE-X7をROS環境で
運用する際に使用できるパッケージです。使用するにはCRANE-X7本体とアールティ様から配布されている[CRANE-X7のオリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)、環境構築が必要となります。


本パッケージは上記の[CRANE-X7のオリジナルパッケージ](https://github.com/rt-net/crane_x7_ros)を元に2023年度の設計製作論実習3内でチーム大三元が開発を行なったものです。


CRANE-X7についての詳しい情報は、アールティ様より公開されている[CRANE-X7](https://github.com/rt-net/crane_x7)よりご確認ください。
このパッケージはアールティ様の定めるライセンスに則って開発を行なっております。詳しいライセンス情報は**LICENSE**をご確認ください。


* このパッケージはCRANE-X7を使ってお抹茶を点てるためのパッケージです。本アプリケーションはこのOmatcha_detectionと[Omatcha_actions](https://github.com/Orbital-G/Omatcha_actions)の二つのパッケージをセットで使用する必要があります。合わせてのインストールをお願いします。


CRANE-X7、お抹茶の粉が入った容器、茶筅、お湯と茶碗を用意して配置し、パッケージ内のスクリプトを実行することで、お抹茶を点てることができます。