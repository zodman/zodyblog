#!/usr/bin/python

TWITTER_USER = "zodman"
TWITTER_PASSWORD = "******"

import sys
import readline
import urllib
import urllib2

def twitter_update(user, password, status):
    MAX_STATUS_LENGTH = 140
    if len(status) > MAX_STATUS_LENGTH:
        raise ValueError(
            "status length is %d, cannot be great than %d" %
            (len(status), MAX_STATUS_LENGTH))

    a = urllib2.HTTPBasicAuthHandler()
    a.add_password("Twitter API",
                   "http://twitter.com/statuses/update.xml",
                   user, password)
    o = urllib2.build_opener(a)

    params = urllib.urlencode({
        "status" : status,
        })

    print o.open("http://twitter.com/statuses/update.xml", params).read()

if __name__ == "__main__":
    if TWITTER_USER and TWITTER_PASSWORD:
        if len(sys.argv) == 2:
            twitter_update(TWITTER_USER, TWITTER_PASSWORD, sys.argv[1])
        else:
            status = raw_input("%s status: " % TWITTER_USER)
            twitter_update(TWITTER_USER, TWITTER_PASSWORD, status)
    else:
        if len(sys.argv) == 3:
            status = raw_input("%s status: " % sys.argv[1])
            twitter_update(sys.argv[1], sys.argv[2], status)
        elif len(sys.argv) == 4:
            twitter_update(sys.argv[1], sys.argv[2], sys.argv[3])
        else:
            print 'usage: %s username password ["status"]' % sys.argv[0]

