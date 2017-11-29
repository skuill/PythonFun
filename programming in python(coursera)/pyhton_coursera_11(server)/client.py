import socket
import time

class Client:
    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        self._sock = socket.create_connection((self._host, self._port), timeout)
        
        
    def put(self, key, value, timestamp=None):
        timestamp_str = ''
        if not timestamp:
            timestamp_str = str(int(time.time()))
        else:
            timestamp_str = timestamp
        try:     
            put_str = "put {} {} {}\n".format(key, value, timestamp_str)
            self._sock.sendall(put_str.encode("utf8"))
            answer = self._sock.recv(4096)
            if not answer or "ok" not in answer.decode("utf8"):
                raise ClientError(answer)
        except Exception as error:
            raise ClientError(repr(error)) 
        
    def get(self, key):
        result_dict = {}
        try:            
            self._sock.sendall("get {}\n".format(key).encode("utf8"))
            answer = self._sock.recv(4096)
            if not answer:
                raise ClientError("receive error")
            answer_str = answer.decode("utf8")
            print (answer_str)
            if "ok" not in answer_str:
                raise ClientError(answer)
            else:
                answer_clear = answer_str.replace("\n\n", "").replace("ok", "")
                print ("HaHa1")
                print (answer_clear)
                print ("HaHa2")
                if answer_clear and answer != "\n":
                    for metric_str in answer_clear.split("\n"):
                        if metric_str:
                            metric_values = metric_str.split(" ")
                            if metric_values[0] in result_dict:
                                print ("HaHa3")
                                print (metric_values[0])
                                result_dict[metric_values[0]].append((int(metric_values[2]), float(metric_values[1])))
                                result_dict[metric_values[0]].sort(key=lambda tup: tup[0])
                            else:
                                print ("HaHa4")
                                print (metric_values[0], metric_values[2], metric_values[1])
                                result_dict[metric_values[0]] = [(int(metric_values[2]), float(metric_values[1]))]
        except Exception as error:
            raise ClientError(repr(error)) 
        return result_dict
        
class ClientError(Exception):
    def __init__(self, message):
        self.message = message