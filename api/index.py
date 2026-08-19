"""Vercel用の入口。

Vercelは api/ 以下のファイルを関数として動かし、その中の `app` をWSGIアプリとして扱う。
中身はルートの app.py をそのまま使うので、ロジックは1箇所のままにできる。
（Procfile経由のRenderも app.py を直接見ているため、両方が同じコードで動く）
"""

import os
import sys

# Vercelの実行時はこのファイルのあるディレクトリが起点になるため、
# ルートの app.py を import できるようパスを通す。
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# `app` だけを取り込む。`from app import *` にすると app.py 側の `handler`
# （LINEのWebhookHandler）が入り込み、Vercelが関数の入口と誤認するため避ける。
from app import app  # noqa: E402

__all__ = ["app"]
