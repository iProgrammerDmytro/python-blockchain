import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


subscribe_key = "sub-c-4ed05400-6121-49f3-bd1d-6a52441a6ae6"
publish_key = "pub-c-e69dccee-46b5-40af-b359-77f6ab9c97c4"

pnconfig = PNConfiguration()
pnconfig.subscribe_key = subscribe_key
pnconfig.publish_key = publish_key
pubnub = PubNub(pnconfig)

TEST_CHANNEL = "TEST_CHANNEL"

pubnub.subscribe().channels([TEST_CHANNEL]).execute()


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f"\n-- Incoming message_object: {message_object}")


pubnub.add_listener(Listener())


def main():
    time.sleep(1)

    pubnub.publish().channel(TEST_CHANNEL).message({"foo": "bar"}).sync()


if __name__ == "__main__":
    main()
