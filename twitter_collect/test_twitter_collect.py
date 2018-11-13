from twitter_collect import twitter_connection_setup

def test_twitter_setup():
    assert twitter_connection_setup.twitter_setup()is not None
