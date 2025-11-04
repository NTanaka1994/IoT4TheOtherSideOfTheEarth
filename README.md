# IoT4TheOtherSideOfTheEarth
簡単に言えば理論上地球の裏側からでも操作できるドローンです(WEBserver.pyとUDP_server.pyをクラウドに上げれば)。ただ、予算の都合上タンク型ドローンにリモコンに左右前進スイッチを作りモータをパワートランジスタで動かしてドローンに着けた温湿度センサとCO2センサのそれぞれの値のダッシュボードとGPSでドローンの位置を地図上に表示するのを「templates」の「dashbord.html(あくまで動作確認用)」にやっています。<br>
<img width="2000" height="883" alt="image" src="https://github.com/user-attachments/assets/20a6e170-a8b1-4a67-8909-7be8309055ee" />

ちなみに全部RESTfulWebAPI(JSON)で動かしています。<br>
開発進捗<br>
10月30日、UDPサーバとWebサーバを作り、動作確認用ダッシュボードを作った。<br>
11月2日、パーツ購入<br>
11月3日、モーターとキャタピラが届く、ダッシュボードを実際に動かした<br>
11月4日、センサの作動結果のダッシュボードのフォルダを作成
