import subprocess

def port_scan(opened_ports,ip_address):
    """
        Scan specific target and ports using system nmap
    """
    #nmap -sCV -p22,80,1883,2222,3306,4506,8123,9080 192.168.10.126 -oN targeted
    ports = ",".join([opened_ports.strip('[]') if type(
        i) == str else str(i) for i in opened_ports])
    subprocess.run(["nmap","-sCV",f"-p{ports}",f"{ip_address}"])
    #"-sCV", "-p80,443","{ip_address}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True