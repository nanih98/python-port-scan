import time
import ipaddress
import re
import socket
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from concurrent.futures import as_completed
from pyfiglet import figlet_format
from termcolor import cprint
from parser import parse_args
from colors import LogColors
from port_scan import port_scan

# Configuration
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
opened_ports = []

def banner():
    return cprint(figlet_format('Python Nmap', font='banner'), 'green')


def validate_ip_address(ip_address):
    try:
        valid_address = ipaddress.ip_address(ip_address)
        logging.info(
            f"{LogColors.START_SUCCESS} {ip_address} is a valid address {LogColors.NOCOLOR}")
    except SystemExit:
        logging.error(
            f"{LogColors.START_ERROR} {ip_address} is not a valid address {LogColors.NOCOLOR}")


def extract_port_range(port_range):
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))

        return port_max, port_min


def connection(ip_address, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_address, port))
            opened_ports.append(port)
            return f"Port {port} opened in {ip_address}"
    except:
        pass


def main():
    start = time.perf_counter()
    args = parse_args()
    banner()

    logging.basicConfig(
        format="%(levelname)-2s %(message)s",
        level=args.debug,
        encoding='utf-8',
    )

    validate_ip_address(args.ip_address)
    extract_port_range(args.port_range)

    max_port, min_port = extract_port_range(args.port_range)
    ports = [ports for ports in range(min_port, max_port + 1)]

    # Multiprocessing, if not, that script is too slow
    # with ProcessPoolExecutor(max_workers=13) as executor:
    with ThreadPoolExecutor(max_workers=13) as executor:
        futures = [executor.submit(
            connection, args.ip_address, port) for port in ports]
        for future in as_completed(futures):
            if future.result() is not None:
                logging.info(
                    f"{LogColors.START_SUCCESS} {future.result()} {LogColors.NOCOLOR}")

    finish = time.perf_counter()

    port_scan(opened_ports,args.ip_address)

    print(f"Finished in {round(finish - start, 2)} second(s)")


if __name__ == '__main__':
    main()
