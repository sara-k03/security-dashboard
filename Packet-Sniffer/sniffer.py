import socket 
import struct
import textwrap

# Start up with part 3

# Unpack ethernet frame (sender, receiver, data, etc)
def ethernet_frame( data ):
    # exclamation mark -> denotes that we're treating this as network data (converting from Big Endian to Little Endian)
    # proto --> protocol encapsulated in the packet's payload
    # This is only looking at the first 14 bytes
    dest_mac, src_mac, proto = struct.unpack( '! 6s 6s H', data[ : 14 ] )
    # we need to take this information and make it human-readable
    return get_mac_address( dest_mac ), get_mac_address( src_mac ), socket.htons( proto ), data[ 14 : ]

# Returns properly formatted MAC address (i.e. AA:BB:CC:DD:EE:FF)
def get_mac_address( bytes_addr ):
    # map() --> Runs each item in an iteratble through a function
    bytes_str = map( '{:02x}'.format, bytes_addr )
    mac_addr = ':'.join( bytes_str ).upper() 
    return mac_addr