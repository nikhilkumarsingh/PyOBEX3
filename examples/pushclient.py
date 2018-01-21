#!/usr/bin/env python

import bluetooth, os, struct, sys
from PyOBEX import client, headers, responses

if __name__ == "__main__":

    if len(sys.argv) != 4:
    
        sys.stderr.write("Usage: %s <device address> <port> <file name>\n" % sys.argv[0])
        sys.exit(1)
    
    device_address = sys.argv[1]
    port = int(sys.argv[2])
    file_name = sys.argv[3]
    
    c = client.Client(device_address, port)
    r = c.connect()
    
    if not isinstance(r, responses.ConnectSuccess):
        sys.stderr.write("Failed to connect.\n")
        sys.exit(1)
    
    c.put(file_name, bytes(open(file_name).read(), encoding="utf8"))
    c.disconnect()

    sys.exit()
