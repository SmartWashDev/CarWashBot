from collections.abc import Awaitable, Callable

import nats
from nats.aio.client import Client
from nats.aio.msg import Msg
from nats.aio.subscription import Subscription


class NatsMessageProcessor:
    def __init__(
        self,
        nats_url: str,
        nats_subject: str,
        callback: Callable[[Msg], Awaitable[None]],
    ) -> None:
        self.nats_url = nats_url
        self.nats_subject = nats_subject
        self.callback = callback

        self._nc: Client | None = None
        self._sub: Subscription | None = None

    async def stop(self) -> None:
        if not self._nc:
            return

        if not self._sub:
            return

        await self._sub.unsubscribe()
        await self._nc.close()

    async def run(self) -> None:
        if not self._nc:
            self._nc = await nats.connect(self.nats_url)

        self._sub = await self._nc.subscribe(self.nats_subject, cb=self.callback)
