<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/log-exec.svg?maxAge=3600)](https://pypi.org/project/log-exec/)
[![](https://img.shields.io/npm/v/log-exec.svg?maxAge=3600)](https://www.npmjs.com/package/log-exec)
[![Travis](https://api.travis-ci.org/looking-for-a-job/log-exec.svg?branch=master)](https://travis-ci.org/looking-for-a-job/log-exec/)

#### Installation
```bash
$ [sudo] npm i -g log-exec
```
```bash
$ [sudo] pip install log-exec
```

#### Config
```bash
$ export LOG_COMMAND=~/Library/Logs/log-command # /usr/local/var/log/log-command by default
```

#### Scripts usage
command|`usage`
-|-
`log-exec` |`usage: log-exec command [args ...]`

#### Examples
```bash
$ log-command script.sh
```

or use `log-command` as interpreter:

`script.sh`
```bash
#!/usr/bin/env log-command bash
...
```

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>