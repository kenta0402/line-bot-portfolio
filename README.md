# LINEbot

## 前提
・AWSの勉強をしており、実践としてLINEbotを作成しました。

<br>

## 構成
・Computing：AWS Lambda


・API：AWS API Gateway


・DB：AWS DynamoDB

<br>

## code01（オウム返し）

<img width="150" height="150" alt="code01" src="https://github.com/user-attachments/assets/55832faa-b5bc-4968-8046-971b0c0c2778" />

### 機能：送信したメッセージをそのまま返信
### 環境変数
#### ・LINE_CHANNEL_ACCESS_TOKEN：チャネルアクセストークン

<br>

## code02（DB追加）
<img width="150" height="150" alt="code02" src="https://github.com/user-attachments/assets/aed06eb4-8446-4263-b37e-acbd2d3c4d5e" />

### 機能：送信したメッセージDynamoDBに格納。キーを返信。
#### 環境変数
#### ・LINE_CHANNEL_ACCESS_TOKEN：チャネルアクセストークン
##### ・DYNAMO_TABLE_NAME：DynamoDBのテーブル名

<br>

## code03（DB取り出し）
<img width="150" height="150" alt="code03_png" src="https://github.com/user-attachments/assets/f80319e3-41be-4036-8a7a-630da54cfd8c" />

### 機能：送信したキーのメッセージをDynamoDBから取り出して返信。キーはcode02で返信されたもの。
#### 環境変数
##### ・LINE_CHANNEL_ACCESS_TOKEN：チャネルアクセストークン
##### ・DYNAMO_TABLE_NAME：DynamoDBのテーブル名
