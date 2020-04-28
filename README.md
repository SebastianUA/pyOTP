# PyOTP

I would like to introduce the python script that generate OTP from MFA key that you provide from CLI.

## Install software

First of all, install ```python3```, for example:

```bash
$ brew install python3
```

NOTE: You have to install HOMEBREW, the command here:

```bash
$ sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Secondly, installing PIP:

```bash
$ sudo easy_install pip
```

After that, install requiriments:

```bash
$ pip3.7 install -r requirements.txt
```

To get a help, run:

```bash
$ python3 get_OTP.py --help
usage: python3 script_name.py {ARGS}

optional arguments:
  -h, --help     show this help message and exit
  --version      show program's version number and exit
  --acc ACCOUNT  Account name
  --path PATH    Path to .aws/credentials file
  --show-acc     Show account names

created by Vitalii Natarov
```



## Examples:

To use this py-script, run the next command:

```bash
$ python3 get_OTP.py --acc aws-acc
Please add [aws-acc] account to /Users/captain/.aws/credentials
EXAMPLE:
    [aws-acc]
    aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXX
    aws_secret_access_key = YYYYYYYYYYYYYYYYYYYYYYYY
    region = us-east-1
    mfa_authorisation_key = ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

 You can use the following ones:   ['default', 'LinuxNotes', 'test', 'test-long-term']
```

As can you see, the AWS account does not exist. Add all needs to the `~/.aws/credentials` file to generate OTP. When you're having set up an account and will run the command, you can see the next result:

```bash
$ python3 get_OTP.py --acc aws-acc
Current OTP for aws-acc:  034480
```

I would like to optimize that script to work with other scripts that use OTP by automatically way and put additional functionality.

Of course, you can add alias for this script, for example:

```bash
$ echo 'alias get_OTP="python3 /Users/captain/Projects/python/pyotp/get_OTP.py"' >> ~/.zshrc
```



## Authors

Created and maintained by [Vitaliy Natarov](https://github.com/SebastianUA). An email: [vitaliy.natarov@yahoo.com](vitaliy.natarov@yahoo.com).



## License

Apache 2 Licensed. See [LICENSE](https://github.com/SebastianUA/pyOTP/blob/master/LICENSE) for full details.
