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

### 1️⃣ code01：オウム返し

<img src="https://github.com/user-attachments/assets/55832faa-b5bc-4968-8046-971b0c0c2778" width="150" height="150" />

**機能**  
- 送信したメッセージをそのまま返信  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン

---

### 2️⃣ code02：DB追加

<img src="https://github.com/user-attachments/assets/aed06eb4-8446-4263-b37e-acbd2d3c4d5e" width="150" height="150" />

**機能**  
- 送信したメッセージをDynamoDBに格納  
- DynamoDBのキーを返信  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン  
- `DYNAMO_TABLE_NAME`：DynamoDBのテーブル名

---

### 3️⃣ code03：DB取り出し

<img src="https://github.com/user-attachments/assets/f80319e3-41be-4036-8a7a-630da54cfd8c" width="150" height="150" />

**機能**  
- 送信したキー（code02で返信されたもの）からDynamoDBのメッセージを取得して返信  

**環境変数**  
- `LINE_CHANNEL_ACCESS_TOKEN`：チャネルアクセストークン  
- `DYNAMO_TABLE_NAME`：DynamoDBのテーブル名

---

## 🔹 ポイント
- `code01`：返信専用  
- `code02`：保存＋返信  
- `code03`：取得＋返信

---

💡 **補足**
- 各Lambda関数は環境変数で設定した情報を使って動作します  
- DynamoDBを使う場合はテーブル名やキーの管理に注意してください
