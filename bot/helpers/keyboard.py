#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


def server_select(file_name: str, size: str):
    upload_selection = [
        [
            InlineKeyboardButton(
                "transfer.sh",
                callback_data=f'transfersh|{file_name}|{size}'
            ),
            InlineKeyboardButton(
                "File.io",
                callback_data=f"fileio|{file_name}|{size}"
            )
        ],
        [
            InlineKeyboardButton(
                "gofile.io",
                callback_data=f"gofileio|{file_name}|{size}"
            ),
            InlineKeyboardButton(
                "anonymfiles.com",
                callback_data=f"anonymfiles|{file_name}|{size}"
            )
        ]
    ]
    return InlineKeyboardMarkup(upload_selection)
