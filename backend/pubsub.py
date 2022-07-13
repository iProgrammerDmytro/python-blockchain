import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


subscribe_key = "test-key"
publish_key = "also-test-key"

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
