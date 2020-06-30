<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/log-exec.svg?maxAge=3600)](https://pypi.org/project/log-exec/)
[![](https://img.shields.io/npm/v/log-exec.svg?maxAge=3600)](https://www.npmjs.com/package/log-exec)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/log-exec/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/log-exec/actions)

### Installation
```bash
$ [sudo] pip install log-exec
```

```bash
$ [sudo] npm i -g log-exec
```

#### How it works
stdout and stderr are duplicated in log files:
```bash
$LOG_EXEC/<command>/out.log
$LOG_EXEC/<command>/err.log
```

#### Config
```bash
$ export LOG_EXEC=~/Library/Logs/log-exec # /usr/local/var/log/log-exec by default
```

#### Examples
```bash
$ log-exec script.sh
```

or use `log-exec` as interpreter:

`script.sh`
```bash
#!/usr/bin/env log-exec bash
...
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>