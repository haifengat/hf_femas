#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = 'test py ctp of se'
__author__ = 'HaiFeng'
__mtime__ = '20190506'

import sys

sys.path.append('.')
from py_ctp.trade import CtpTrade
from py_ctp.quote import CtpQuote
from py_ctp.enums import *
import time


class TestTrade(object):
    def __init__(self, addr: str, broker: str, investor: str, user: str, pwd: str, appid: str, auth_code: str, proc: str):
        self.front = addr
        self.broker = broker
        self.investor = user
        self.pwd = pwd
        self.appid = appid
        self.authcode = auth_code
        self.proc = proc

        self.t = CtpTrade(investor)
        self.t.OnConnected = self.on_connect
        self.t.OnUserLogin = lambda o, x: print('Trade logon:', x)
        self.t.OnDisConnected = lambda o, x: print(x)
        self.t.OnRtnNotice = lambda obj, time, msg: print(f'OnNotice: {time}:{msg}')
        self.t.OnErrRtnQuote = lambda obj, quote, info: None
        self.t.OnErrRtnQuoteInsert = lambda obj, o: None
        self.t.OnOrder = lambda obj, o: print(o)
        self.t.OnErrOrder = lambda obj, f, info: print(info)
        self.t.OnTrade = lambda obj, o: print(o)
        self.t.OnInstrumentStatus = lambda obj, inst, stat: None

    def on_connect(self, obj):
        self.t.ReqUserLogin(self.investor, self.pwd, self.broker, self.proc, self.appid, self.authcode)

    def run(self):
        self.t.ReqConnect(self.front)
        # self.t.ReqConnect('tcp://192.168.52.4:41205')

    def release(self):
        self.t.ReqUserLogout()


class TestQuote(object):
    """TestQuote"""

    def __init__(self, addr: str, broker: str, investor: str, pwd: str):
        """"""
        self.front = addr
        self.broker = broker
        self.investor = investor
        self.pwd = pwd

        self.q = CtpQuote()
        self.q.OnConnected = lambda x: self.q.ReqUserLogin(self.investor, self.pwd, self.broker)
        self.q.OnUserLogin = lambda o, i: self.q.ReqSubscribeMarketData('rb1910')
        self.q.OnTick = lambda t: print(f'{t.LastPrice}, {t.Volume}\n')

    def run(self):
        self.q.ReqConnect(self.front)

    def release(self):
        self.q.ReqUserLogout()


if __name__ == "__main__":
    front_trade = 'tcp://101.226.253.127:58002'
    front_quote = 'tcp://101.226.253.127:58005'
    broker = '0137'
    investor = '00000410a'
    pwd = '123456aa'
    appid = 'client_LB_1.0'
    auth_code = 'Q5V2UZ1G6AB2QCW4'
    proc = ''
    if investor == '':
        investor = input('invesotr:')
        pwd = input('password:')
        appid = input('appid:')
        auth_code = input('auth code:')
        proc = input('product info:')
    tt = TestTrade(front_trade, broker, investor[:-1], investor, pwd, appid, auth_code, proc)
    tt.run()
    time.sleep(5)
    if tt.t.logined:
        tt.t.ReqOrderInsert('IF1911', DirectType.Buy, OffsetType.Open, 3885, 3)

    qq = TestQuote(front_quote, broker, investor, pwd)
    qq.run()
    if qq.q.logined:
        qq.q.ReqSubscribeMarketData('IF1911')
    #
    # time.sleep(6)
    # for inst in tt.t.instruments.values():
    #     print(inst)
    input()
    tt.release()
    qq.release()
    input()
