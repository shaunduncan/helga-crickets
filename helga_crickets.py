import time

from functools import partial

import smokesignal

from twisted.internet import task

from helga import settings
from helga.plugins import match


# Keep track of which channels should receive the message
_scheduled = {}


def _do_crickets(client):
    global _scheduled

    timeout = _get_timeout()
    for channel, last in iter(_scheduled.items()):
        if int(time.time() - last) < timeout:
            continue
        client.msg(channel, '*crickets*')
        del _scheduled[channel]


def _get_timeout():
    # Default timeout of 5 minutes
    return getattr(settings, 'CRICKETS_TIMEOUT', 5 * 60)


@smokesignal.on('signon')
def _init_schedule(client):
    """
    Initializes the looping call to check for cricket responses
    """
    loop = task.LoopingCall(partial(_do_crickets, client))
    loop.start(_get_timeout())


@match(r'^(.*)$')
def crickets(client, channel, nick, message, matches):
    global _scheduled

    line = matches[0]

    if line.endswith('?'):
        _scheduled[channel] = time.time()
    else:
        try:
            del _scheduled[channel]
        except KeyError:
            pass
