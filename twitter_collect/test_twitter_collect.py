import pytest
from twitter_collect import twitter_connection_setup as tw


def test_twitter_setup():
    assert (tw.twitter_setup() is not None)

