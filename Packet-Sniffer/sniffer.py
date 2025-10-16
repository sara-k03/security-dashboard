from scapy.all import sniff, Ether

def packet_callback( packet): # function to be called everytime a new packet is captured
    if Ether in packet: # checks if packet has ethernet layer - some packets start at a higher IP layer
        eth = packet[ Ether ] # extracts ethernet header from packet - eth is a scapy object with attributes like src, dst, type
        print( f"\nEthernet Frame:" ) # makes each packet human readable
        print( f"Destination: {eth.dst}, Source: {eth.src}, Type: {hex(eth.type)}" )

sniff( prn=packet_callback, store=False )
