
/*

SIMPLE STRINGS
```
+PING\r\n
+Ok\r\n
+PONG\r\n
```

ERRORS
```
-ERR unknown command 'GETT'\r\n
-Error message\r\n
-ERR unknown command 'foobar'
-WRONGTYPE Operation against a key holding the wrong kind of value
```

BULK STRINGS
```
$13\r\nHello, World!\r\n
$6\r\nfoobar\r\n
$0\r\n\r\n  (empty string)
$-1\r\n (Null)
```

ARRAYS
```
*2\r\n$3\r\nfoo\r\n$3\r\nbar\r\n
*3\r\n$3\r\nSET\r\n$5\r\nmykey\r\n$8\r\nmy value\r\n
*2\r\n$3\r\nfoo\r\n$3\r\nbar\r\n
*3\r\n:1\r\n:2\r\n:3\r\n
*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$6\r\nfoobar\r\n
*-1\r\n //(Null Array)
*0\r\n //(empty array)

// An array of two arrays
*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Foo\r\n-Bar\r\n

*3\r\n$3\r\nfoo\r\n$-1\r\n$3\r\nbar\r\n
//["foo",nil,"bar"]
```

INTEGERS
```
:99\r\n
:0\r\n
:1000\r\n
```

>The above RESP data type encodes a two elements Array consisting of
an Array that contains three Integers 1, 2, 3 and an array of a
Simple String and an Error.

> Single elements of an Array may be Null. This is used in Redis
replies in order to signal that this elements are missing and not empty strings.
This can happen with the SORT command when used with the GET pattern option
when the specified key is missing.

# Sending commands to a Redis Server

> A client sends to the Redis server a RESP Array consisting of just Bulk Strings.
> A Redis server replies to clients sending any valid RESP data type as reply.

```
CLIENT: *2\r\n$4\r\nLLEN\r\n$6\r\nmylist\r\n
SERVER: :48293\r\n
```

> Sometimes you have only telnet in your hands and you need to send a command to the Redis server.


```
C: PING
S: +PONG

C: EXISTS somekey
S: :0
```

>For example, ERR is the generic error, while WRONGTYPE is a
more specific error that implies that the client tried to perform
an operation against the wrong data type.

>return a null object and not an empty Array when Redis replies with a Null Array.
This is necessary to distinguish between an empty list and a different condition

>BLPOP command times out, it returns a Null Array that has a count of -1

source:
- https://redisgreen.net/blog/beginners-guide-to-redis-protocol/
- https://redis.io/topics/protocol
- https://redisgreen.net/blog/reading-and-writing-redis-protocol/

*/
