import socket


def syslog(message, siem_ip, siem_port):
    """
    Send syslog UDP packet to given host and port.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message, (siem_ip, siem_port))
        sock.close()
        return True
    except Exception as msg:
        return msg
        
