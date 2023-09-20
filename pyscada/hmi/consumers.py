
from datetime import datetime
from channels.generic.http import AsyncHttpConsumer
from channels.exceptions import StopConsumer
import asyncio
import json
import logging

logger = logging.getLogger(__name__)

class ServerSentEventsConsumer(AsyncHttpConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keepalive = False
        logger.info("init consumer")

    async def handle(self, body):
        logger.info(f"handle {body}")
        await self.send_headers(headers=[
            (b"Cache-Control", b"no-cache"),
            (b"Content-Type", b"text/event-stream"),
            (b"Transfer-Encoding", b"chunked"),
        ])
        logger.info("2")
        await self.send_body(b'', more_body=True)
        await self.channel_layer.group_add('test123', self.channel_name)

    async def send_body(self, body, *, more_body=False):
        logger.info(f"send_body {body} {more_body}")
        if more_body:
            self.keepalive = True
        assert isinstance(body, bytes), "Body is not bytes"
        await self.send(
            {"type": "http.response.body", "body": body, "more_body": more_body}
        )

    async def http_request(self, message):
        logger.info(f"http request {message}")
        if "body" in message:
            self.body.append(message["body"])
        if not message.get("more_body"):
            try:
                logger.info("before handle")
                await self.handle(b"".join(self.body))
                logger.info("after handle")
            finally:
                logger.info("finally")
                if not self.keepalive:
                    logger.info("disconnect !")
                    await self.disconnect()
                    raise StopConsumer()

    async def receive(self, text_data):
        logger.info(f"receive {text_data}")

    async def chat_message(self, event):
        logger.info(f"chat message {event}")
        payload = 'id:5\nevent: test\ndata: 2\n\n'
        await self.send_body(payload.encode('utf-8'), more_body=True)

#        while True:
#            payload = "data: %s\n\n" % datetime.now().isoformat()
#            await self.send_body(payload.encode("utf-8"), more_body=True)
#            logger.info("3")
#            await asyncio.sleep(1)
#            logger.info("4")

class ExampleNotifier(ServerSentEventsConsumer):

    async def handle_user_data(self, event):
        logger.info(f"handle user data {event}")
        payload = 'event: message\nid: 5\ndata: %s\n\n' % json.dumps(event["message"])
        #payload = 'data: 654\n\n'
        #payload = 'id:5\nevent: message\ndata: 2\n\n'
        await self.send_body(payload.encode('utf-8'), more_body=True)
