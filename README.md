# youteube の URL を複数指定して動画をダウンロード

## 環境構築
環境は以下のとおりです。  
ホスト OS：windows  
仮想環境：DockerDesktop  
ゲスト OS： ubuntu  
```
git clone https://github.com/houdoukyokucho/ydl.git
cd ydl
docker-compose up -d
```
## ダウンロードの動画を指定する
urls.txt にダウンロードしたい youtube の URL を貼り付ける。
```
https://www.youtube.com/watch?v=CFLOiR2EbKM
https://www.youtube.com/watch?v=2U-qxm-wy5Q
https://www.youtube.com/watch?v=f7wQUOjSqhc
```
## ダウンロードを開始する
1. activete.bat をダブルクリックする。  
2. DOWNLOADED のフォルダの中に動画がダウンロードされます。  
