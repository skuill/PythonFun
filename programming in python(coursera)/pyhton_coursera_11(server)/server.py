import asyncio


class ClientServerProtocol(asyncio.Protocol):
    local_storage = {}
    
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        print('Data received: {}'.format(data))
        resp = self.process_data(data.decode())
        print('Send responce: {}'.format(resp))
        self.transport.write(resp.encode())
        
    def process_data(self, data):
        data = data.replace("\n", "")
        if "put" in data:
            put_parsed = data.split(" ")
            if (len(put_parsed) == 4):
                put_tup = (put_parsed[2], put_parsed[3])
                if put_parsed[1] in self.local_storage:
                    if put_tup not in self.local_storage[put_parsed[1]]:
                        self.local_storage[put_parsed[1]].append(put_tup)
                else:
                    self.local_storage[put_parsed[1]] = [put_tup]
                return "ok\n\n"
            else:
                return "error\nwrong command\n\n"
        elif "get" in data:
            get_parsed = data.split(" ")
            if (len(get_parsed) == 2):
                metrics = []
                if (get_parsed[1] == "*"):
                    for key in self.local_storage.keys():
                        metrics.append(key)
                else:
                    metrics.append(get_parsed[1])
                result = "ok\n"
                for metric in metrics:
                    if (metric in self.local_storage):
                        for tup in self.local_storage.get(metric):
                            result = "{}{} {} {}\n".format(result, metric, tup[0], tup[1])
                return "{}\n".format(result)

def run_server(host, port):     
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
            ClientServerProtocol,
            host, port
            )

    server = loop.run_until_complete(coro)
    
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    
run_server('127.0.0.1', 8182)