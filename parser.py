import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="""Python nmap and ddos script""",
        add_help=True,
        prog="python_nmap"
    )
    parser.add_argument(
        "-l",
        "--level",
        choices=["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"],
        required=False,
        dest="debug",
        default="INFO",
        help="""level of logging""",
        type=str,
    )
    parser.add_argument(
        "-t",
        "--target",
        required=True,
        dest="ip_address",
        help="""Address ip that you want to scan""",
        type=str,
    )
    parser.add_argument(
        "-p",
        "--port-range",
        required=True,
        dest="port_range",
        help="""Port range that you want to scan""",
        type=str,
    )

    return parser.parse_args()
