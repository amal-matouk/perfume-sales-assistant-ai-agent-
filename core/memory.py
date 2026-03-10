from database import SessionLocal, ChatHistory


def load_memory(phone_number: str):
    db = SessionLocal()

    chats = db.query(ChatHistory) \
        .filter(ChatHistory.phone_number == phone_number) \
        .all()

    history_text = "\n".join(
        [f"User: {c.user_message}\nBot: {c.bot_response}" for c in chats]
    )

    db.close()
    return history_text


def save_chat(phone_number, user_message, bot_response):

    db = SessionLocal()

    chat = ChatHistory(
        phone_number=phone_number,
        user_message=user_message,
        bot_response=bot_response
    )

    db.add(chat)
    db.commit()
    db.close()