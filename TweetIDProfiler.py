## Goal - Extract timestamp, datacenter, server and sequence from tweet ID.

import datetime 

## Logic given from twitter thread, takes tweet ID as an input.  
def id_to_utc_time(id):
    return (id >> 22) + 1288834974657


## Input: Tweet URL
## Output: [timestamp datacentrenum servernum sequencenum] 
def TweetIDProfiler(tweetURL):
    tweetAttributes = []
    tweetParts = tweetURL.split('/')
#    print(tweetParts[5])
    ## Get tweet ID
    tweetID = int(tweetParts[5])
    ## Convert to binary
    binaryID = bin(tweetID)
#    print(binaryID)
    ## Get the components
    binaryID = binaryID[2:len(binaryID)]
#    print(binaryID)
    ## Timestamp isn't actaully needed in binary form given the logic above.
    timestamp = binaryID[0:39]
#    print(timestamp)

    dec_time = id_to_utc_time(tweetID)
    time = (datetime.datetime.fromtimestamp (dec_time / 1000).strftime ("%Y-%m-%d %H:%M:%S"))
#    print(time)
    tweetAttributes.append(time)

    datacentre = binaryID[39:39+5]
#    print(datacentre)
    tweetAttributes.append(int(datacentre,2))

    server = binaryID[39+5:39+10]
#    print(server)
    tweetAttributes.append(int(server,2))

    sequence = binaryID[39+10:39+22]
#    print(sequence)
    tweetAttributes.append(int(sequence,2))

    return tweetAttributes


## Testing
print(TweetIDProfiler("https://twitter.com/realDonaldTrump/status/1226595698793230348"))
## Expected outcome: 7:56 PM Feb 9, 2020
