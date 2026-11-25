"""Command-line interface for the reference calculator."""

from __future__ import annotations

import argparse
import json

from .core import Observation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="semantic-density")
    subparsers = parser.add_subparsers(dest="command", required=True)

    score = subparsers.add_parser("score", help="calculate one observed score")
    score.add_argument("--nodes", type=int, required=True)
    score.add_argument("--reading-seconds", type=float, required=True)
    score.add_argument("--reflection-seconds", type=float, required=True)
    score.add_argument("--dispersion", type=float, required=True)
    score.add_argument("--precision", type=int, default=6)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "score":
        observation = Observation(
            nodes=args.nodes,
            reading_seconds=args.reading_seconds,
            reflection_seconds=args.reflection_seconds,
            dispersion=args.dispersion,
        )
        payload = {
            key: round(value, args.precision) if isinstance(value, float) else value
            for key, value in observation.as_dict().items()
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
