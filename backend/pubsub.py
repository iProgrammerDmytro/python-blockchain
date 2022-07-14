import time
import os
from dotenv import load_dotenv

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback


load_dotenv()

SUBSCRIBE_KEY = os.getenv("SUBSCRIBE_KEY")
PUBLISH_KEY = os.getenv("PUBLISH_KEY")

pnconfig = PNConfiguration()
pnconfig.subscribe_key = SUBSCRIBE_KEY
pnconfig.publish_key = PUBLISH_KEY

TEST_CHANNEL = "TEST_CHANNEL"


class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(
            f"\n-- Channel: {message_object.channel} | Message: {message_object.message}"
        )


class PubSub:
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the condes of the blockchain network.
    """

    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()


def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, {"foo": "bar"})


if __name__ == "__main__":
    main()
