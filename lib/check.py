from pythonping import ping
from config import ICMP_DESTINATION_HOST, ICMP_TIMEOUT

def check():
    try:
        result = ping(ICMP_DESTINATION_HOST, timeout=ICMP_TIMEOUT, count=1)
        return result.success()
    except OSError:
        return False