import asyncio


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        print('Send responce: {}'.format(resp))
        self.transport.write(resp.encode())
        
    def process_data(self, data):
        print('Data received: {}'.format(data))
        return "{}r".format(data)
        
loop = asyncio.get_event_loop()
coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8182
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()