import json
import os
import boto3
import requests

# LINEのチャネルアクセストークン（環境変数から取得推奨）
CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

def lambda_handler(event, context):
    try:
        # LINE Webhookイベントを取得
        body = json.loads(event["body"])
        for ev in body["events"]:
            if ev["type"] == "message" and ev["message"]["type"] == "text":
                user_id = ev["source"]["userId"]
                user_message = ev["message"]["text"]

                # オウム返し（受け取ったメッセージをそのまま返す）
                send_reply(ev["replyToken"], f"あなたが送ったメッセージ: {user_message}")

        return {"statusCode": 200, "body": "OK"}

    except Exception as e:
        print(f"Webhook processing failed: {e}")
        return {"statusCode": 500, "body": "Internal Server Error"}


def send_reply(reply_token, text):
    """LINEに返信する関数"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}"
    }
    payload = {
        "replyToken": reply_token,
        "messages": [
            {"type": "text", "text": text}
        ]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=payload)
