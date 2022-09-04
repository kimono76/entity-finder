The selenium drivers are available in the github page

[github link](https://github.com/mozilla/geckodriver/releases)

# MacOS
to fix the MacOS notarization issue run this command in the driver's executable location

```sh
    xattr -r -d com.apple.quarantine geckodriver
```