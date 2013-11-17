import socket

def get_client_ip(request):
    """
    Given an http request, return a client ip address, remote ip address
              and forwarded ip address.
    
    Args:
        request (Request): Django request object
              
    IP Address = forwarded IP if it exists, otherwise the remote address
    Remote IP = The client IP address assuming it has not gone through proxy
    Forwarded IP = the client IP if it has gone through proxy. 
    """
    remote_ip = request.META.get('REMOTE_ADDR',"")
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR',"")
    ip_address = remote_ip if not forwarded_ip else forwarded_ip
    return {'ip_address':ip_address, 'remote_ip':remote_ip, 'forwarded_ip':forwarded_ip}


def lookup_domain(ip_address):
    """
    Given an IP address, try to lookup up the hostname, any host aliases and ip addresses
    for this ip.
    
    Args:
        ip_address (string): IP Address of host to lookup
    """
    hostname =  ''
    aliaslist = ipaddrlist = []
    if ip_address:
        try:
            hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(ip_address)
        except socket.herror:
            pass
        except socket.gaierror:
            pass
        except socket.error:
            pass
    return {'hostname':hostname, 'aliaslist':aliaslist, 'ipaddrlist':ipaddrlist,}

