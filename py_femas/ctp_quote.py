#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : HaiFeng
# @Email   : 24918700@qq.com
# @Time    : 2018/12/10


import os
import sys
import platform
import ctypes
import copy
from .ctp_struct import *


class Quote:

    def __init__(self):

        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"lib{'64' if sys.maxsize > 2 ** 32 else '32'}")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_quote.' + ('dll' if 'Windows' in platform.system() else 'so'))
        if not os.path.exists(absolute_dllfile_path):
            print('缺少DLL接口文件')
            return

        # make log dir for api log
        logdir = os.path.join(os.getcwd(), 'log')
        if not os.path.exists(logdir):
            os.mkdir(logdir)

        dlldir = os.path.split(absolute_dllfile_path)[0]
        # change work directory
        cur_path = os.getcwd()
        os.chdir(dlldir)

        self.h = CDLL(absolute_dllfile_path)

        self.h.CreateApi.argtypes = []
        self.h.CreateApi.restype = c_void_p

        self.h.CreateSpi.argtypes = []
        self.h.CreateSpi.restype = c_void_p

        self.api = None
        self.spi = None
        self.nRequestID = 0
        self.h.Release.argtypes = [c_void_p]
        self.h.Release.restype = c_void_p

        self.h.Init.argtypes = [c_void_p]
        self.h.Init.restype = c_void_p

        self.h.Join.argtypes = [c_void_p]
        self.h.Join.restype = c_void_p

        self.h.SetUseMultiChannel.argtypes = [c_void_p, c_bool]
        self.h.SetUseMultiChannel.restype = c_void_p

        self.h.RegisterMultiChannel.argtypes = [c_void_p, c_void_p]
        self.h.RegisterMultiChannel.restype = c_void_p

        self.h.RegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.RegisterFront.restype = c_void_p

        self.h.RegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.RegisterNameServer.restype = c_void_p

        self.h.RegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.RegisterSpi.restype = c_void_p

        self.h.SubscribeMarketDataTopic.argtypes = [c_void_p, c_int32, c_void_p]
        self.h.SubscribeMarketDataTopic.restype = c_void_p

        self.h.SubMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.SubMarketData.restype = c_void_p

        self.h.UnSubMarketData.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.UnSubMarketData.restype = c_void_p

        self.h.GetMarketTopic.argtypes = [c_void_p, c_void_p]
        self.h.GetMarketTopic.restype = c_void_p

        self.h.GetMarketData.argtypes = [c_void_p, c_void_p, c_void_p]
        self.h.GetMarketData.restype = c_void_p

        self.h.SetHeartbeatTimeout.argtypes = [c_void_p, c_void_p]
        self.h.SetHeartbeatTimeout.restype = c_void_p

        self.h.ReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogin.restype = c_void_p

        self.h.ReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogout.restype = c_void_p
        os.chdir(cur_path)

    def CreateApi(self):
        self.api = self.h.CreateApi()
        return self.api

    def CreateSpi(self):
        self.spi = self.h.CreateSpi()
        return self.spi

    def Release(self):
        self.h.Release(self.api)

    def Init(self):
        self.h.Init(self.api)

    def Join(self):
        self.h.Join(self.api)

    def SetUseMultiChannel(self, bUseMulti: bool = 1):
        self.h.SetUseMultiChannel(self.api, bUseMulti)

    def RegisterMultiChannel(self, char=1):
        self.h.RegisterMultiChannel(self.api, char)

    def RegisterFront(self, pszFrontAddress: str):
        self.h.RegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))

    def RegisterNameServer(self, pszNsAddress: str):
        self.h.RegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))

    def RegisterSpi(self, pSpi):
        self.h.RegisterSpi(self.api, pSpi)

    def SubscribeMarketDataTopic(self, nTopicID: int = 1, nResumeType: USTP_TE_RESUME_TYPE = 1):
        self.h.SubscribeMarketDataTopic(self.api, nTopicID, nResumeType.value)

    def SubMarketData(self, ppInstrumentID: str, nCount: int = 1):
        ca1 = (ctypes.c_char_p * 1)()
        ca1[0] = bytes(ppInstrumentID, encoding='ascii')
        self.h.SubMarketData(self.api, ca1, nCount)

    def UnSubMarketData(self, ppInstrumentID: str, nCount: int = 1):
        ca1 = (ctypes.c_char_p * 1)()
        ca1[0] = bytes(ppInstrumentID, encoding='ascii')
        self.h.UnSubMarketData(self.api, ca1, nCount)

    def GetMarketTopic(self, pExchangeID: str):
        self.h.GetMarketTopic(self.api, bytes(pExchangeID, encoding='ascii'))

    def GetMarketData(self, pExchangeID: str, pInstrumentID: str):
        self.h.GetMarketData(self.api, bytes(pExchangeID, encoding='ascii'), bytes(pInstrumentID, encoding='ascii'))

    def SetHeartbeatTimeout(self, int=1):
        self.h.SetHeartbeatTimeout(self.api, int)

    def ReqUserLogin(self, TradingDay: str = '', UserID: str = '', BrokerID: str = '', Password: str = '', UserProductInfo: str = '', InterfaceProductInfo: str = '', ProtocolInfo: str = '', IPAddress: str = '', MacAddress: str = '', DataCenterID: int = 0, UserProductFileSize: int = 0, Authenticate2Type: TUstpFtdcAuthenticate2TypeType = list(TUstpFtdcAuthenticate2TypeType)[0], Authenticate2Password: str = '', TerminalCode: str = '', PasswordEncrypt: str = ''):
        pReqUserLogin = CUstpFtdcReqUserLoginField()
        pReqUserLogin.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqUserLogin.UserID = bytes(UserID, encoding='ascii')
        pReqUserLogin.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserLogin.Password = bytes(Password, encoding='ascii')
        pReqUserLogin.UserProductInfo = bytes(UserProductInfo, encoding='ascii')
        pReqUserLogin.InterfaceProductInfo = bytes(InterfaceProductInfo, encoding='ascii')
        pReqUserLogin.ProtocolInfo = bytes(ProtocolInfo, encoding='ascii')
        pReqUserLogin.IPAddress = bytes(IPAddress, encoding='ascii')
        pReqUserLogin.MacAddress = bytes(MacAddress, encoding='ascii')
        pReqUserLogin.DataCenterID = DataCenterID
        pReqUserLogin.UserProductFileSize = UserProductFileSize
        pReqUserLogin.Authenticate2Type = Authenticate2Type.value
        pReqUserLogin.Authenticate2Password = bytes(Authenticate2Password, encoding='ascii')
        pReqUserLogin.TerminalCode = bytes(TerminalCode, encoding='ascii')
        pReqUserLogin.PasswordEncrypt = bytes(PasswordEncrypt, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLogin(self.api, byref(pReqUserLogin), self.nRequestID)

    def ReqUserLogout(self, BrokerID: str = '', UserID: str = ''):
        pReqUserLogout = CUstpFtdcReqUserLogoutField()
        pReqUserLogout.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqUserLogout.UserID = bytes(UserID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserLogout(self.api, byref(pReqUserLogout), self.nRequestID)

    def RegCB(self):
        self.h.SetOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnFrontConnected.restype = None
        self.evOnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.SetOnFrontConnected(self.spi, self.evOnFrontConnected)

        self.h.SetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnFrontDisconnected.restype = None
        self.evOnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.SetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)

        self.h.SetOnHeartBeatWarning.argtypes = [c_void_p, c_void_p]
        self.h.SetOnHeartBeatWarning.restype = None
        self.evOnHeartBeatWarning = CFUNCTYPE(None, c_int32)(self.__OnHeartBeatWarning)
        self.h.SetOnHeartBeatWarning(self.spi, self.evOnHeartBeatWarning)

        self.h.SetOnPackageStart.argtypes = [c_void_p, c_void_p]
        self.h.SetOnPackageStart.restype = None
        self.evOnPackageStart = CFUNCTYPE(None, c_int32, c_int32)(self.__OnPackageStart)
        self.h.SetOnPackageStart(self.spi, self.evOnPackageStart)

        self.h.SetOnPackageEnd.argtypes = [c_void_p, c_void_p]
        self.h.SetOnPackageEnd.restype = None
        self.evOnPackageEnd = CFUNCTYPE(None, c_int32, c_int32)(self.__OnPackageEnd)
        self.h.SetOnPackageEnd(self.spi, self.evOnPackageEnd)

        self.h.SetOnRspError.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspError.restype = None
        self.evOnRspError = CFUNCTYPE(None, POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspError)
        self.h.SetOnRspError(self.spi, self.evOnRspError)

        self.h.SetOnRspUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserLogin.restype = None
        self.evOnRspUserLogin = CFUNCTYPE(None, POINTER(CUstpFtdcRspUserLoginField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogin)
        self.h.SetOnRspUserLogin(self.spi, self.evOnRspUserLogin)

        self.h.SetOnRspUserLogout.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserLogout.restype = None
        self.evOnRspUserLogout = CFUNCTYPE(None, POINTER(CUstpFtdcRspUserLogoutField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserLogout)
        self.h.SetOnRspUserLogout(self.spi, self.evOnRspUserLogout)

        self.h.SetOnRtnDepthMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnDepthMarketData.restype = None
        self.evOnRtnDepthMarketData = CFUNCTYPE(None, POINTER(CUstpFtdcDepthMarketDataField))(self.__OnRtnDepthMarketData)
        self.h.SetOnRtnDepthMarketData(self.spi, self.evOnRtnDepthMarketData)

        self.h.SetOnRspSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspSubMarketData.restype = None
        self.evOnRspSubMarketData = CFUNCTYPE(None, POINTER(CUstpFtdcSpecificInstrumentField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspSubMarketData)
        self.h.SetOnRspSubMarketData(self.spi, self.evOnRspSubMarketData)

        self.h.SetOnRspUnSubMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUnSubMarketData.restype = None
        self.evOnRspUnSubMarketData = CFUNCTYPE(None, POINTER(CUstpFtdcSpecificInstrumentField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUnSubMarketData)
        self.h.SetOnRspUnSubMarketData(self.spi, self.evOnRspUnSubMarketData)

        self.h.SetOnRspGetMarketTopic.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspGetMarketTopic.restype = None
        self.evOnRspGetMarketTopic = CFUNCTYPE(None, POINTER(CUstpFtdcRspMarketTopicField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGetMarketTopic)
        self.h.SetOnRspGetMarketTopic(self.spi, self.evOnRspGetMarketTopic)

        self.h.SetOnRspGetMarketData.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspGetMarketData.restype = None
        self.evOnRspGetMarketData = CFUNCTYPE(None, POINTER(CUstpFtdcRspDepthMarketDataField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspGetMarketData)
        self.h.SetOnRspGetMarketData(self.spi, self.evOnRspGetMarketData)

    def __OnFrontConnected(self):
        self.OnFrontConnected()

    def __OnFrontDisconnected(self, nReason):
        self.OnFrontDisconnected(nReason)

    def __OnHeartBeatWarning(self, nTimeLapse):
        self.OnHeartBeatWarning(nTimeLapse)

    def __OnPackageStart(self, nTopicID, nSequenceNo):
        self.OnPackageStart(nTopicID, nSequenceNo)

    def __OnPackageEnd(self, nTopicID, nSequenceNo):
        self.OnPackageEnd(nTopicID, nSequenceNo)

    def __OnRspError(self, pRspInfo, nRequestID, bIsLast):
        self.OnRspError(copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserLogin(copy.deepcopy(POINTER(CUstpFtdcRspUserLoginField).from_param(pRspUserLogin).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserLogout(self, pRspUserLogout, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserLogout(copy.deepcopy(POINTER(CUstpFtdcRspUserLogoutField).from_param(pRspUserLogout).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnDepthMarketData(self, pDepthMarketData):
        self.OnRtnDepthMarketData(copy.deepcopy(POINTER(CUstpFtdcDepthMarketDataField).from_param(pDepthMarketData).contents))

    def __OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspSubMarketData(copy.deepcopy(POINTER(CUstpFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspUnSubMarketData(copy.deepcopy(POINTER(CUstpFtdcSpecificInstrumentField).from_param(pSpecificInstrument).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspGetMarketTopic(self, pRspMarketTopic, pRspInfo, nRequestID, bIsLast):
        self.OnRspGetMarketTopic(copy.deepcopy(POINTER(CUstpFtdcRspMarketTopicField).from_param(pRspMarketTopic).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspGetMarketData(self, pRspDepthMarketData, pRspInfo, nRequestID, bIsLast):
        self.OnRspGetMarketData(copy.deepcopy(POINTER(CUstpFtdcRspDepthMarketDataField).from_param(pRspDepthMarketData).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def OnFrontConnected(self, ):
        print('===OnFrontConnected===: ')

    def OnFrontDisconnected(self, nReason: int):
        print('===OnFrontDisconnected===: nReason: int')

    def OnHeartBeatWarning(self, nTimeLapse: int):
        print('===OnHeartBeatWarning===: nTimeLapse: int')

    def OnPackageStart(self, nTopicID: int, nSequenceNo: int):
        print('===OnPackageStart===: nTopicID: int, nSequenceNo: int')

    def OnPackageEnd(self, nTopicID: int, nSequenceNo: int):
        print('===OnPackageEnd===: nTopicID: int, nSequenceNo: int')

    def OnRspError(self, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspError===: pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserLogin(self, pRspUserLogin: CUstpFtdcRspUserLoginField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserLogin===: pRspUserLogin: CUstpFtdcRspUserLoginField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserLogout(self, pRspUserLogout: CUstpFtdcRspUserLogoutField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserLogout===: pRspUserLogout: CUstpFtdcRspUserLogoutField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnDepthMarketData(self, pDepthMarketData: CUstpFtdcDepthMarketDataField):
        print('===OnRtnDepthMarketData===: pDepthMarketData: CUstpFtdcDepthMarketDataField')

    def OnRspSubMarketData(self, pSpecificInstrument: CUstpFtdcSpecificInstrumentField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspSubMarketData===: pSpecificInstrument: CUstpFtdcSpecificInstrumentField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUnSubMarketData(self, pSpecificInstrument: CUstpFtdcSpecificInstrumentField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUnSubMarketData===: pSpecificInstrument: CUstpFtdcSpecificInstrumentField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspGetMarketTopic(self, pRspMarketTopic: CUstpFtdcRspMarketTopicField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspGetMarketTopic===: pRspMarketTopic: CUstpFtdcRspMarketTopicField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspGetMarketData(self, pRspDepthMarketData: CUstpFtdcRspDepthMarketDataField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspGetMarketData===: pRspDepthMarketData: CUstpFtdcRspDepthMarketDataField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')
