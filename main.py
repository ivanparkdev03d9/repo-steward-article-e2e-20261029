"""Local scheme/hostname checks for the Repo Steward publication smoke test."""
import argparse
import json
import sys
from urllib.parse import urlsplit


def inspect_url(url):
    """Return a boolean result; never contact the URL or modify files."""
    try:
        parsed = urlsplit(url)
        host = parsed.hostname
        valid = bool(parsed.scheme in ("http", "https") and host
                     and not any(character.isspace() for character in url))
        return {"url": url, "valid": valid, "scheme": parsed.scheme,
                "host": host, "path": parsed.path}
    except ValueError:
        return {"url": url, "valid": False, "error": "URL parsing failed"}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Local HTTP(S) scheme and hostname checker; no network")
    parser.add_argument("urls", nargs="+", help="one or more URL strings")
    args = parser.parse_args(argv)
    results = [inspect_url(url) for url in args.urls]
    print(json.dumps(results))
    return 0 if all(result["valid"] for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
