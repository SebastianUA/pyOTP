#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import argparse
import pyotp
import os


class Bgcolors:
    def __init__(self):
        self.get = {
            'HEADER': '\033[95m',
            'OKBLUE': '\033[94m',
            'OKGREEN': '\033[92m',
            'WARNING': '\033[93m',
            'FAIL': '\033[91m',
            'ENDC': '\033[0m',
            'BOLD': '\033[1m',
            'UNDERLINE': '\033[4m'
        }


def get_acc_names(db_file):
    # db_file = '/Users/captain/.aws/credentials'
    if db_file is '':
        print('Please add PATH to .aws/credentials file inside this script(db_file variable)')
        print('For help, use: script_name.py -h')
        exit(1)
    config = configparser.ConfigParser()
    config.sections()
    config.read(db_file)

    return config.sections()


def get_creds_from_acc_name(acc_name, db_file):
    if db_file is '':
        print('Please add PATH to .aws/credentials file inside this script(db_file variable)')
        exit(1)
    config = configparser.ConfigParser()
    config.sections()
    config.read(db_file)
    if acc_name in config:
        if 'aws_access_key_id' in config[acc_name]:
            aws_access_key_id = config[acc_name]['aws_access_key_id']
        else:
            print('Please add aws_access_key_id to %s file for [%s] account' % (db_file, acc_name))
            exit(1)
        if 'aws_secret_access_key' in config[acc_name]:
            aws_secret_access_key = config[acc_name]['aws_secret_access_key']
        else:
            print('Please add aws_secret_access_key to %s file for [%s] account' % (db_file, acc_name))
            exit(1)
        if 'region' in config[acc_name]:
            region = config[acc_name]['region']
        else:
            print('Please add region to %s file for [%s] account' % (db_file, acc_name))
            exit(1)
        if 'mfa_authorisation_key' in config[acc_name]:
            mfa_authorisation_key = config[acc_name]['mfa_authorisation_key']
        else:
            print('Please add mfa_authorisation_key to %s file for [%s] account' % (db_file, acc_name))
            exit(1)
    else:
        print('Please add [%s] account to %s' % (acc_name, db_file))
        print(('EXAMPLE:\n'
               '    [%s]\n'
               '    aws_access_key_id = XXXXXXXXXXXXXXXXXXXXXXXX\n'
               '    aws_secret_access_key = YYYYYYYYYYYYYYYYYYYYYYYY\n'
               '    region = us-east-1\n'
               '    mfa_authorisation_key = ZZZZZZZZZZZZZZZZZZZZZZZZZZZZ\n'
               '    ') % acc_name)
        print(Bgcolors().get['HEADER'], 'You can use the following ones:', Bgcolors().get['ENDC'],
              Bgcolors().get['OKGREEN'], get_acc_names(db_file), Bgcolors().get['ENDC'])
        exit(1)

    return aws_access_key_id, aws_secret_access_key, region, mfa_authorisation_key


def generate_token(acc_name, db_file):
    account_creds = get_creds_from_acc_name(acc_name, db_file)
    totp = pyotp.TOTP(account_creds[3])
    print("Current OTP for %s:" % acc_name, Bgcolors().get['OKGREEN'], totp.now(), Bgcolors().get['ENDC'])
    return generate_token


def generate_token_without_output(acc_name, db_file):
    account_creds = get_creds_from_acc_name(acc_name, db_file)
    totp = pyotp.TOTP(account_creds[3])
    return totp.now()


def main():
    parser = argparse.ArgumentParser(prog='python3 script_name.py -h',
                                     usage='python3 script_name.py {ARGS}',
                                     add_help=True,
                                     prefix_chars='--/',
                                     epilog='''created by Vitalii Natarov''')
    parser.add_argument('--version', action='version', version='v1.0.1')
    parser.add_argument('--acc', dest='account', help='Account name', default='default')
    parser.add_argument('--path', dest='path', help='Path to .aws/credentials file',
                        default='~/.aws/credentials')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--show-acc', dest='show_acc', help='Show account names', action='store_true')
    # group.add_argument('--s', dest='show_acc', help='Show account names', action='store_true')
    results = parser.parse_args()
    ac_name = results.account
    path = os.path.expanduser(results.path)
    if path is not None:
        if results.show_acc:
            print(Bgcolors().get['HEADER'], 'You can use the following ones:', Bgcolors().get['ENDC'],
                Bgcolors().get['OKGREEN'], get_acc_names(path), Bgcolors().get['ENDC'])
        else:
            generate_token(ac_name, path)
    else:
        print('Please add [--path]')
        print('For help, use: script_name.py -h')
        exit(0)

if __name__ == '__main__':
    main()
