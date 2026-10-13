import argparse
import time

from src.runner import run_monitoring


def main():
    parser = argparse.ArgumentParser(
        description="NetOps Sentinel continuous monitoring"
    )
    parser.add_argument(
        "--interval", type=int, default=60,
        help="Seconds between monitoring cycles"
    )
    parser.add_argument(
        "--cycles", type=int, default=1,
        help="Number of cycles; 0 means run until interrupted"
    )
    args = parser.parse_args()

    if args.interval < 1 or args.cycles < 0:
        parser.error("Interval must be >= 1 and cycles must be >= 0")

    completed = 0

    try:
        while args.cycles == 0 or completed < args.cycles:
            run_monitoring()
            completed += 1

            if args.cycles == 0 or completed < args.cycles:
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")


if __name__ == "__main__":
    main()
