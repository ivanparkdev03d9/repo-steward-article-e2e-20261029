"""Deterministic tests: no network or external packages."""
import contextlib
import io
import json
import unittest
from main import inspect_url, main


class UrlSmokeTests(unittest.TestCase):
    def test_https(self):
        result = inspect_url("https://example.org/docs")
        self.assertIs(result["valid"], True)
        self.assertEqual(result["host"], "example.org")
        self.assertEqual(result["path"], "/docs")

    def test_http(self):
        self.assertIs(inspect_url("http://example.org")["valid"], True)

    def test_relative_path(self):
        self.assertIs(inspect_url("docs/readme.md")["valid"], False)

    def test_missing_host(self):
        self.assertIs(inspect_url("https:///docs")["valid"], False)

    def test_unsupported_scheme(self):
        self.assertIs(inspect_url("ftp://example.org")["valid"], False)

    def test_malformed_host(self):
        self.assertIs(inspect_url("https://[")["valid"], False)

    def test_whitespace(self):
        self.assertIs(inspect_url("https://exa mple.org")["valid"], False)

    def test_cli_success(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main(["https://example.org"])
        self.assertEqual(status, 0)
        self.assertIs(json.loads(output.getvalue())[0]["valid"], True)

    def test_cli_failure(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            status = main(["https://example.org", "relative/path"])
        self.assertEqual(status, 1)
        self.assertEqual([item["valid"] for item in json.loads(output.getvalue())], [True, False])


if __name__ == "__main__":
    unittest.main()
