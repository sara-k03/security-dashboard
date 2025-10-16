import socket 
import struct
import textwrap

# Loop to listen for packets
def main():
    # to connect with other computers
    connection = socket.socket( socket.AF_PACKET, socket.SOCKET_RAW, socket.ntohs( 3 ) ) 
    
    while True: # Going to keep looping and listening for any data that comes across
        raw_data, addr = connection.recvfrom( 65536 )
        dest_mac, src_mac, eth_proto, data = ethernet_frame( raw_data )
        print( '\nEthernet Frame: ' )
        print( 'Destination: {}, Source: {}, Protocol: {}'.format( dest_mac, src_mac, eth_proto ) )
 

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

main()