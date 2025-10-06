# LINEbot 実践メモ

## 🔹 前提
- AWSの勉強用としてLINEbotを作成
- **フロントエンド**：LINEアプリ  
- **バックエンド**：AWS（Lambda / API Gateway / DynamoDB）

---

## 🔹 システム構成

### フロントエンド
- LINEアプリ  
  - LINE Messaging APIを使用してメッセージ送受信

### バックエンド

#### Computing
- AWS Lambda
  - メッセージ処理
  - DBへの保存・取り出し

#### API
- AWS API Gateway
  - Webhook受け取り・ルーティング

#### DB / ストレージ
- AWS DynamoDB
  - メッセージの保存と取り出し

#### アクセス管理
- AWS IAM
  - LambdaやDynamoDBのアクセス権限を管理
  - 最小権限の原則で設定

---

## 🔹 Lambda関数一覧

### code01：オウム返し

<img src="/image/code01.png" alt="code01" width="150" height="150">



**機能**  
- 送信したメッセージをそのまま返信  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン

---

### code02：DB追加

<img src="/image/code02.png" alt="code02" width="150" height="150">

**機能**  
- 送信したメッセージをDynamoDBに格納  
- DynamoDBのキーを返信  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン  
- `DYNAMO_TABLE_NAME`：DynamoDBのテーブル名

---

### code03：DB取り出し

<img src="/image/code03.png" alt="code03" width="150" height="150">

**機能**  
- 送信したキー（code02で返信されたもの）からDynamoDBのメッセージを取得して返信  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン  
- `DYNAMO_TABLE_NAME`：DynamoDBのテーブル名

---

### code04：chatgptとの会話

<img src="/image/code04.png" alt="code04" width="150" height="150">

**機能**  
- ChatGPTとの会話  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン  
- `OPENAI_API_KEY`：ChatGPTのアクセストークン

## 🔹 ポイント
- `code01`：返信専用  
- `code02`：保存＋返信  
- `code03`：取得＋返信  
- `code04`：ChatGPTとの会話
---

💡 **補足**
- 各Lambda関数は環境変数で設定した情報を使って動作します  
- DynamoDBを使う場合はテーブル名やキーの管理に注意してください
