# IoT4TheOtherSideOfTheEarth
簡単に言えば理論上地球の裏側からでも操作できるドローンです(WEBserver.pyとUDP_server.pyをクラウドに上げれば)。ただ、予算の都合上タンク型ドローンにリモコンに左右前進スイッチを作りモータをパワートランジスタで動かしてドローンに着けた温湿度センサとCO2センサのそれぞれの値のダッシュボードとGPSでドローンの位置を地図上に表示するのを「templates」の「dashbord.html(あくまで動作確認用)」にやっています。<br>
<img width="2004" height="885" alt="image" src="https://github.com/user-attachments/assets/8fe69560-ff3c-4e90-863d-c3269c3f3095" />

ちなみに全部RESTfulWebAPI(JSON)で動かしています。<br>
開発進捗<br>
10月30日、UDPサーバとWebサーバを作り、動作確認用ダッシュボードを作った。<br>
