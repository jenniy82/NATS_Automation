import asyncio
from nats.aio.client import Client as NATS
import nkeys
# from stan.aio.client import Client as STAN





flows = """{"properties":{"sourceIp":"10.160.178.30","sourceNodeID":"2687540205173066847","sourceName":"FLOW"},"sessions":[{"prot":6,"sIP":"10.160.178.36","cIP":"10.160.112.1","sPrt":22,"cPrt":62198,"time":1584292380,"bid":true,"exporterIp":"127.0.0.1","dirConf":"HIGH"},{"prot":17,"sIP":"10.160.178.20","cIP":"10.160.112.1","sPrt":31364,"cPrt":62397,"time":1584292383,"bid":true,"exporterIp":"127.0.0.1","dirConf":"LOW"}]}"""
nc = NATS()
# sc = STAN()
# Start session with NATS Streaming cluster using
# the established NATS connection.
async def run(loop,sessions):
    print("publisher")
    await nc.connect("root:aristo1@10.160.178.30:4222",io_loop=loop)
    # await nc.connect("127.0.0.1:4222",io_loop=loop,)
    await nc.publish("flow.sessions", b"""{"properties":{"sourceIp":"10.160.178.30","sourceNodeID":"2687540205173066847","sourceName":"FLOW"},"sessions":[{"prot":6,"sIP":"10.160.178.36","cIP":"10.160.112.1","sPrt":22,"cPrt":62198,"time":0,"bid":true,"exporterIp":"127.0.0.1","dirConf":"HIGH"},{"prot":17,"sIP":"10.160.178.20","cIP":"10.160.112.1","sPrt":31364,"cPrt":62397,"time":1584292383,"bid":false,"exporterIp":"127.0.0.1","dirConf":"LOW"}]}""")
    await nc.publish("flow.sessions", b'sessions')
loop = asyncio.get_event_loop()
loop.run_until_complete(run(loop,flows))


