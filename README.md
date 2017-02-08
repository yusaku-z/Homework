# 学校の課題2

パブリッシャ(count.py)に入力された文字をサブスクライバ(twice.py)で受け取り、決められた文字を表示します。

<動作>

「・」は「t」, 「-」は「-」で入力

アルファベットA～Z, SOSを表示可能

アルファベット, SOSは以下のように対応している

A:t-   B:-ttt C:-t-t  D:-tt  E:t   F:tt-t G:--t  H:tttt  I:tt 

J:t---  K:-t-  L:t-tt  M:--   N:-t  O:---  P:t--t  Q:--t-  R:t-t

S:ttt   T:-    U:tt-  V:ttt- W:t--  X:-tt-  Y:-t--  Z:--tt  SOS:ttt---ttt


<使い方>

1．端末を3つ起動する。

2．端末1で以下のコマンドを実行し、ROSを起動させる。

$ roscore

3．端末2で以下のコマンドを実行する。

$ ~/catkin_ws/src/mypkg/scripts

$ vi count.py

$ vi twice.py

$ chmod 755 count.py

$ chmod 755 twice.py

$ rosrun mypkg count.py

4．端末3で以下のコマンドを実行する。

$ rosrun mypkg twice.py

5．端末1,2,3の終了

$ ^c
