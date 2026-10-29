# Repo Steward source package and publication test

This page belongs only to [repo-steward-article-e2e-20261029](https://github.com/ivanparkdev03d9/repo-steward-article-e2e-20261029). It demonstrates an editable Telegraph article associated with one public test repository.

## What is included

The source-only ZIP contains three text files: `main.py`, `test_main.py`, and `requirements.txt`. It does not include an installer or binary. Documentation is available in the linked source repository.

`main.py` checks an HTTP(S) scheme and a nonempty hostname locally, rejects whitespace, and prints JSON. It does not contact the URLs or check whether a website is reachable. This is a small test utility, not a full URL validator.

## Run the example

After extracting your downloaded source ZIP, open its folder with Python 3.10 or later installed:

```bash
python main.py https://example.org
python -m unittest -v
```

There are no third-party dependencies. The nine tests cover valid URLs, missing hosts, unsupported schemes, relative paths, malformed hosts, whitespace, and CLI results.

## Download the source-only ZIP

The final download link below opens a dedicated prerelease on the separate file-storage account. Choose `source-files.zip` under Assets. That prerelease leaves the existing default archive unchanged.

This is an explicit end-to-end publication test. No license, reviews, search indexing, popularity or security certification is claimed.

## Downloads

[Open download release](https://github.com/Jeboseeer/todoapp-my-app-/releases/tag/repo-steward-e2e-20261029)
