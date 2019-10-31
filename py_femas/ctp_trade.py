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


class Trade:

    def __init__(self):

        dllpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), f"lib{'64' if sys.maxsize > 2 ** 32 else '32'}")
        absolute_dllfile_path = os.path.join(dllpath, 'ctp_trade.' + ('dll' if 'Windows' in platform.system() else 'so'))
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
        sys.path.append(dlldir)
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

        self.h.RegisterFront.argtypes = [c_void_p, c_void_p]
        self.h.RegisterFront.restype = c_void_p

        self.h.RegisterQryFront.argtypes = [c_void_p, c_void_p]
        self.h.RegisterQryFront.restype = c_void_p

        self.h.RegisterNameServer.argtypes = [c_void_p, c_void_p]
        self.h.RegisterNameServer.restype = c_void_p

        self.h.RegisterSpi.argtypes = [c_void_p, c_void_p]
        self.h.RegisterSpi.restype = c_void_p

        self.h.SubscribePrivateTopic.argtypes = [c_void_p, c_void_p]
        self.h.SubscribePrivateTopic.restype = c_void_p

        self.h.SubscribePublicTopic.argtypes = [c_void_p, c_void_p]
        self.h.SubscribePublicTopic.restype = c_void_p

        self.h.SubscribeUserTopic.argtypes = [c_void_p, c_void_p]
        self.h.SubscribeUserTopic.restype = c_void_p

        self.h.SubscribeForQuote.argtypes = [c_void_p, c_void_p]
        self.h.SubscribeForQuote.restype = c_void_p

        self.h.SetHeartbeatTimeout.argtypes = [c_void_p, c_void_p]
        self.h.SetHeartbeatTimeout.restype = c_void_p

        self.h.OpenRequestLog.argtypes = [c_void_p, c_void_p]
        self.h.OpenRequestLog.restype = c_void_p

        self.h.OpenResponseLog.argtypes = [c_void_p, c_void_p]
        self.h.OpenResponseLog.restype = c_void_p

        self.h.RegisterDSProxyUserCert.argtypes = [c_void_p, c_void_p, c_void_p, c_void_p, c_int32]
        self.h.RegisterDSProxyUserCert.restype = c_void_p

        self.h.ReqUserLogin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogin.restype = c_void_p

        self.h.ReqUserLogout.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserLogout.restype = c_void_p

        self.h.ReqUserPasswordUpdate.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserPasswordUpdate.restype = c_void_p

        self.h.ReqOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqOrderInsert.restype = c_void_p

        self.h.ReqOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqOrderAction.restype = c_void_p

        self.h.ReqQuoteInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQuoteInsert.restype = c_void_p

        self.h.ReqQuoteAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQuoteAction.restype = c_void_p

        self.h.ReqForQuote.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqForQuote.restype = c_void_p

        self.h.ReqMarginCombAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqMarginCombAction.restype = c_void_p

        self.h.ReqUserDeposit.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqUserDeposit.restype = c_void_p

        self.h.ReqQryOrder.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryOrder.restype = c_void_p

        self.h.ReqQryTrade.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTrade.restype = c_void_p

        self.h.ReqQryUserInvestor.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryUserInvestor.restype = c_void_p

        self.h.ReqQryTradingCode.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryTradingCode.restype = c_void_p

        self.h.ReqQryInvestorAccount.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorAccount.restype = c_void_p

        self.h.ReqQryInstrument.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInstrument.restype = c_void_p

        self.h.ReqQryExchange.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryExchange.restype = c_void_p

        self.h.ReqQryInvestorPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorPosition.restype = c_void_p

        self.h.ReqQryComplianceParam.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryComplianceParam.restype = c_void_p

        self.h.ReqQryInvestorFee.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorFee.restype = c_void_p

        self.h.ReqQryInvestorMargin.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorMargin.restype = c_void_p

        self.h.ReqQryInvestorCombPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorCombPosition.restype = c_void_p

        self.h.ReqQryInvestorLegPosition.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInvestorLegPosition.restype = c_void_p

        self.h.ReqQryInstrumentGroup.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryInstrumentGroup.restype = c_void_p

        self.h.ReqQryClientMarginCombType.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryClientMarginCombType.restype = c_void_p

        self.h.ReqExecOrderInsert.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqExecOrderInsert.restype = c_void_p

        self.h.ReqExecOrderAction.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqExecOrderAction.restype = c_void_p

        self.h.ReqQrySystemTime.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQrySystemTime.restype = c_void_p

        self.h.ReqQryMarginPrefParam.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqQryMarginPrefParam.restype = c_void_p

        self.h.ReqDSUserCertification.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqDSUserCertification.restype = c_void_p

        self.h.ReqDSProxySubmitInfo.argtypes = [c_void_p, c_void_p, c_int32]
        self.h.ReqDSProxySubmitInfo.restype = c_void_p
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

    def RegisterFront(self, pszFrontAddress: str):
        self.h.RegisterFront(self.api, bytes(pszFrontAddress, encoding='ascii'))

    def RegisterQryFront(self, pszFrontAddress: str):
        self.h.RegisterQryFront(self.api, bytes(pszFrontAddress, encoding='ascii'))

    def RegisterNameServer(self, pszNsAddress: str):
        self.h.RegisterNameServer(self.api, bytes(pszNsAddress, encoding='ascii'))

    def RegisterSpi(self, pSpi):
        self.h.RegisterSpi(self.api, pSpi)

    def SubscribePrivateTopic(self, nResumeType: USTP_TE_RESUME_TYPE):
        self.h.SubscribePrivateTopic(self.api, nResumeType.value)

    def SubscribePublicTopic(self, nResumeType: USTP_TE_RESUME_TYPE):
        self.h.SubscribePublicTopic(self.api, nResumeType.value)

    def SubscribeUserTopic(self, nResumeType: USTP_TE_RESUME_TYPE):
        self.h.SubscribeUserTopic(self.api, nResumeType.value)

    def SubscribeForQuote(self, nResumeType: USTP_TE_RESUME_TYPE):
        self.h.SubscribeForQuote(self.api, nResumeType.value)

    def SetHeartbeatTimeout(self, to: int):
        self.h.SetHeartbeatTimeout(self.api, to)

    def OpenRequestLog(self, char):
        self.h.OpenRequestLog(self.api, char)

    def OpenResponseLog(self, char):
        self.h.OpenResponseLog(self.api, char)

    def RegisterDSProxyUserCert(self, AppID: str = '', AuthCode: str = '', EncryptType: TUstpFtdcDSKeyEncryptType = list(TUstpFtdcDSKeyEncryptType)[0], UserCertReqInfo: str = '', UserCertRspInfo: str = '', UserCertRspInfoLen: int = 0):
        pDSProxyUserUserInfo = CUstpFtdcDSProxyCheckUserInfoField()
        pDSProxyUserUserInfo.AppID = bytes(AppID, encoding='ascii')
        pDSProxyUserUserInfo.AuthCode = bytes(AuthCode, encoding='ascii')
        pDSProxyUserUserInfo.EncryptType = EncryptType.value
        pDSProxyUserCertIn = CUstpFtdcDSProxyUserCertInField()
        pDSProxyUserCertIn.UserCertReqInfo = bytes(UserCertReqInfo, encoding='ascii')
        pDProxyUserCertOut = CUstpFtdcDSProxyUserCertOutField()
        pDProxyUserCertOut.UserCertRspInfo = bytes(UserCertRspInfo, encoding='ascii')
        pDProxyUserCertOut.UserCertRspInfoLen = UserCertRspInfoLen
        self.nRequestID += 1
        self.h.RegisterDSProxyUserCert(self.api, byref(pDSProxyUserUserInfo), byref(pDSProxyUserCertIn), byref(pDProxyUserCertOut), self.nRequestID)

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

    def ReqUserPasswordUpdate(self, BrokerID: str = '', UserID: str = '', OldPassword: str = '', NewPassword: str = ''):
        pUserPasswordUpdate = CUstpFtdcUserPasswordUpdateField()
        pUserPasswordUpdate.BrokerID = bytes(BrokerID, encoding='ascii')
        pUserPasswordUpdate.UserID = bytes(UserID, encoding='ascii')
        pUserPasswordUpdate.OldPassword = bytes(OldPassword, encoding='ascii')
        pUserPasswordUpdate.NewPassword = bytes(NewPassword, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserPasswordUpdate(self.api, byref(pUserPasswordUpdate), self.nRequestID)

    def ReqOrderInsert(self, BrokerID: str = '', ExchangeID: str = '', OrderSysID: str = '', InvestorID: str = '', UserID: str = '', SeatNo: int = 0, InstrumentID: str = '', UserOrderLocalID: str = '', OrderPriceType: TUstpFtdcOrderPriceTypeType = list(TUstpFtdcOrderPriceTypeType)[0], Direction: TUstpFtdcDirectionType = list(TUstpFtdcDirectionType)[0], OffsetFlag: TUstpFtdcOffsetFlagType = list(TUstpFtdcOffsetFlagType)[0], HedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], LimitPrice: float = .0, Volume: int = 0, TimeCondition: TUstpFtdcTimeConditionType = list(TUstpFtdcTimeConditionType)[0], GTDDate: str = '', VolumeCondition: TUstpFtdcVolumeConditionType = list(TUstpFtdcVolumeConditionType)[0], MinVolume: int = 0, StopPrice: float = .0, ForceCloseReason: TUstpFtdcForceCloseReasonType = list(TUstpFtdcForceCloseReasonType)[0], IsAutoSuspend: int = 0, BusinessUnit: str = '', UserCustom: str = '', BusinessLocalID: int = 0, ActionDay: str = '',
                       ArbiType: TUstpFtdcArbiTypeType = list(TUstpFtdcArbiTypeType)[0], ClientID: str = ''):
        pInputOrder = CUstpFtdcInputOrderField()
        pInputOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputOrder.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pInputOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputOrder.UserID = bytes(UserID, encoding='ascii')
        pInputOrder.SeatNo = SeatNo
        pInputOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputOrder.UserOrderLocalID = bytes(UserOrderLocalID, encoding='ascii')
        pInputOrder.OrderPriceType = OrderPriceType.value
        pInputOrder.Direction = Direction.value
        pInputOrder.OffsetFlag = OffsetFlag.value
        pInputOrder.HedgeFlag = HedgeFlag.value
        pInputOrder.LimitPrice = LimitPrice
        pInputOrder.Volume = Volume
        pInputOrder.TimeCondition = TimeCondition.value
        pInputOrder.GTDDate = bytes(GTDDate, encoding='ascii')
        pInputOrder.VolumeCondition = VolumeCondition.value
        pInputOrder.MinVolume = MinVolume
        pInputOrder.StopPrice = StopPrice
        pInputOrder.ForceCloseReason = ForceCloseReason.value
        pInputOrder.IsAutoSuspend = IsAutoSuspend
        pInputOrder.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pInputOrder.UserCustom = bytes(UserCustom, encoding='ascii')
        pInputOrder.BusinessLocalID = BusinessLocalID
        pInputOrder.ActionDay = bytes(ActionDay, encoding='ascii')
        pInputOrder.ArbiType = ArbiType.value
        pInputOrder.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqOrderInsert(self.api, byref(pInputOrder), self.nRequestID)

    def ReqOrderAction(self, ExchangeID: str = '', OrderSysID: str = '', BrokerID: str = '', InvestorID: str = '', UserID: str = '', UserOrderActionLocalID: str = '', UserOrderLocalID: str = '', ActionFlag: TUstpFtdcActionFlagType = list(TUstpFtdcActionFlagType)[0], LimitPrice: float = .0, VolumeChange: int = 0, BusinessLocalID: int = 0, ClientID: str = ''):
        pOrderAction = CUstpFtdcOrderActionField()
        pOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pOrderAction.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pOrderAction.UserID = bytes(UserID, encoding='ascii')
        pOrderAction.UserOrderActionLocalID = bytes(UserOrderActionLocalID, encoding='ascii')
        pOrderAction.UserOrderLocalID = bytes(UserOrderLocalID, encoding='ascii')
        pOrderAction.ActionFlag = ActionFlag.value
        pOrderAction.LimitPrice = LimitPrice
        pOrderAction.VolumeChange = VolumeChange
        pOrderAction.BusinessLocalID = BusinessLocalID
        pOrderAction.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqOrderAction(self.api, byref(pOrderAction), self.nRequestID)

    def ReqQuoteInsert(self, BrokerID: str = '', ExchangeID: str = '', InvestorID: str = '', UserID: str = '', InstrumentID: str = '', Direction: TUstpFtdcDirectionType = list(TUstpFtdcDirectionType)[0], QuoteSysID: str = '', UserQuoteLocalID: str = '', QuoteLocalID: str = '', BidVolume: int = 0, BidOffsetFlag: TUstpFtdcOffsetFlagType = list(TUstpFtdcOffsetFlagType)[0], BidHedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], BidPrice: float = .0, AskVolume: int = 0, AskOffsetFlag: TUstpFtdcOffsetFlagType = list(TUstpFtdcOffsetFlagType)[0], AskHedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], AskPrice: float = .0, BusinessUnit: str = '', UserCustom: str = '', BidUserOrderLocalID: str = '', AskUserOrderLocalID: str = '', BidOrderLocalID: str = '', AskOrderLocalID: str = '', ReqForQuoteID: str = '', StandByTime: int = 0, ClientID: str = ''):
        pInputQuote = CUstpFtdcInputQuoteField()
        pInputQuote.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputQuote.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputQuote.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputQuote.UserID = bytes(UserID, encoding='ascii')
        pInputQuote.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputQuote.Direction = Direction.value
        pInputQuote.QuoteSysID = bytes(QuoteSysID, encoding='ascii')
        pInputQuote.UserQuoteLocalID = bytes(UserQuoteLocalID, encoding='ascii')
        pInputQuote.QuoteLocalID = bytes(QuoteLocalID, encoding='ascii')
        pInputQuote.BidVolume = BidVolume
        pInputQuote.BidOffsetFlag = BidOffsetFlag.value
        pInputQuote.BidHedgeFlag = BidHedgeFlag.value
        pInputQuote.BidPrice = BidPrice
        pInputQuote.AskVolume = AskVolume
        pInputQuote.AskOffsetFlag = AskOffsetFlag.value
        pInputQuote.AskHedgeFlag = AskHedgeFlag.value
        pInputQuote.AskPrice = AskPrice
        pInputQuote.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pInputQuote.UserCustom = bytes(UserCustom, encoding='ascii')
        pInputQuote.BidUserOrderLocalID = bytes(BidUserOrderLocalID, encoding='ascii')
        pInputQuote.AskUserOrderLocalID = bytes(AskUserOrderLocalID, encoding='ascii')
        pInputQuote.BidOrderLocalID = bytes(BidOrderLocalID, encoding='ascii')
        pInputQuote.AskOrderLocalID = bytes(AskOrderLocalID, encoding='ascii')
        pInputQuote.ReqForQuoteID = bytes(ReqForQuoteID, encoding='ascii')
        pInputQuote.StandByTime = StandByTime
        pInputQuote.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQuoteInsert(self.api, byref(pInputQuote), self.nRequestID)

    def ReqQuoteAction(self, BrokerID: str = '', ExchangeID: str = '', InvestorID: str = '', UserID: str = '', QuoteSysID: str = '', UserQuoteLocalID: str = '', UserQuoteActionLocalID: str = '', ActionFlag: TUstpFtdcActionFlagType = list(TUstpFtdcActionFlagType)[0], BusinessUnit: str = '', UserCustom: str = '', Direction: TUstpFtdcDirectionType = list(TUstpFtdcDirectionType)[0], ClientID: str = ''):
        pQuoteAction = CUstpFtdcQuoteActionField()
        pQuoteAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pQuoteAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQuoteAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pQuoteAction.UserID = bytes(UserID, encoding='ascii')
        pQuoteAction.QuoteSysID = bytes(QuoteSysID, encoding='ascii')
        pQuoteAction.UserQuoteLocalID = bytes(UserQuoteLocalID, encoding='ascii')
        pQuoteAction.UserQuoteActionLocalID = bytes(UserQuoteActionLocalID, encoding='ascii')
        pQuoteAction.ActionFlag = ActionFlag.value
        pQuoteAction.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        pQuoteAction.UserCustom = bytes(UserCustom, encoding='ascii')
        pQuoteAction.Direction = Direction.value
        pQuoteAction.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQuoteAction(self.api, byref(pQuoteAction), self.nRequestID)

    def ReqForQuote(self, ReqForQuoteID: str = '', BrokerID: str = '', ExchangeID: str = '', InvestorID: str = '', UserID: str = '', InstrumentID: str = '', Direction: TUstpFtdcDirectionType = list(TUstpFtdcDirectionType)[0], TradingDay: str = '', ReqForQuoteTime: str = '', ClientID: str = ''):
        pReqForQuote = CUstpFtdcReqForQuoteField()
        pReqForQuote.ReqForQuoteID = bytes(ReqForQuoteID, encoding='ascii')
        pReqForQuote.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqForQuote.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pReqForQuote.InvestorID = bytes(InvestorID, encoding='ascii')
        pReqForQuote.UserID = bytes(UserID, encoding='ascii')
        pReqForQuote.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pReqForQuote.Direction = Direction.value
        pReqForQuote.TradingDay = bytes(TradingDay, encoding='ascii')
        pReqForQuote.ReqForQuoteTime = bytes(ReqForQuoteTime, encoding='ascii')
        pReqForQuote.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqForQuote(self.api, byref(pReqForQuote), self.nRequestID)

    def ReqMarginCombAction(self, BrokerID: str = '', ExchangeID: str = '', UserID: str = '', InvestorID: str = '', HedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], UserActionLocalID: str = '', CombInstrumentID: str = '', CombVolume: int = 0, CombDirection: TUstpFtdcCombDirectionType = list(TUstpFtdcCombDirectionType)[0], ActionLocalID: str = '', Direction: TUstpFtdcDirectionType = list(TUstpFtdcDirectionType)[0], OrderSysID: str = '', CombActionStatus: TUstpFtdcCombActionStatusType = list(TUstpFtdcCombActionStatusType)[0]):
        pInputMarginCombAction = CUstpFtdcInputMarginCombActionField()
        pInputMarginCombAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputMarginCombAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputMarginCombAction.UserID = bytes(UserID, encoding='ascii')
        pInputMarginCombAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputMarginCombAction.HedgeFlag = HedgeFlag.value
        pInputMarginCombAction.UserActionLocalID = bytes(UserActionLocalID, encoding='ascii')
        pInputMarginCombAction.CombInstrumentID = bytes(CombInstrumentID, encoding='ascii')
        pInputMarginCombAction.CombVolume = CombVolume
        pInputMarginCombAction.CombDirection = CombDirection.value
        pInputMarginCombAction.ActionLocalID = bytes(ActionLocalID, encoding='ascii')
        pInputMarginCombAction.Direction = Direction.value
        pInputMarginCombAction.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pInputMarginCombAction.CombActionStatus = CombActionStatus.value
        self.nRequestID += 1
        self.h.ReqMarginCombAction(self.api, byref(pInputMarginCombAction), self.nRequestID)

    def ReqUserDeposit(self, BrokerID: str = '', UserID: str = '', InvestorID: str = '', Amount: float = .0, AmountDirection: TUstpFtdcAccountDirectionType = list(TUstpFtdcAccountDirectionType)[0], UserOrderLocalID: str = ''):
        pstpUserDeposit = CUstpFtdcstpUserDepositField()
        pstpUserDeposit.BrokerID = bytes(BrokerID, encoding='ascii')
        pstpUserDeposit.UserID = bytes(UserID, encoding='ascii')
        pstpUserDeposit.InvestorID = bytes(InvestorID, encoding='ascii')
        pstpUserDeposit.Amount = Amount
        pstpUserDeposit.AmountDirection = AmountDirection.value
        pstpUserDeposit.UserOrderLocalID = bytes(UserOrderLocalID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqUserDeposit(self.api, byref(pstpUserDeposit), self.nRequestID)

    def ReqQryOrder(self, BrokerID: str = '', UserID: str = '', ExchangeID: str = '', InvestorID: str = '', OrderSysID: str = '', InstrumentID: str = '', OrderStatus: TUstpFtdcOrderStatusType = list(TUstpFtdcOrderStatusType)[0], OrderType: TUstpFtdcOrderTypeType = list(TUstpFtdcOrderTypeType)[0], ClientID: str = ''):
        pQryOrder = CUstpFtdcQryOrderField()
        pQryOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryOrder.UserID = bytes(UserID, encoding='ascii')
        pQryOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryOrder.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pQryOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pQryOrder.OrderStatus = OrderStatus.value
        pQryOrder.OrderType = OrderType.value
        pQryOrder.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryOrder(self.api, byref(pQryOrder), self.nRequestID)

    def ReqQryTrade(self, BrokerID: str = '', UserID: str = '', ExchangeID: str = '', InvestorID: str = '', TradeID: str = '', InstrumentID: str = '', ClientID: str = ''):
        pQryTrade = CUstpFtdcQryTradeField()
        pQryTrade.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTrade.UserID = bytes(UserID, encoding='ascii')
        pQryTrade.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryTrade.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTrade.TradeID = bytes(TradeID, encoding='ascii')
        pQryTrade.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pQryTrade.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTrade(self.api, byref(pQryTrade), self.nRequestID)

    def ReqQryUserInvestor(self, BrokerID: str = '', UserID: str = ''):
        pQryUserInvestor = CUstpFtdcQryUserInvestorField()
        pQryUserInvestor.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryUserInvestor.UserID = bytes(UserID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryUserInvestor(self.api, byref(pQryUserInvestor), self.nRequestID)

    def ReqQryTradingCode(self, BrokerID: str = '', UserID: str = '', InvestorID: str = '', ExchangeID: str = '', ClientID: str = ''):
        pQryTradingCode = CUstpFtdcQryTradingCodeField()
        pQryTradingCode.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryTradingCode.UserID = bytes(UserID, encoding='ascii')
        pQryTradingCode.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryTradingCode.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryTradingCode.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryTradingCode(self.api, byref(pQryTradingCode), self.nRequestID)

    def ReqQryInvestorAccount(self, BrokerID: str = '', UserID: str = '', InvestorID: str = ''):
        pQryInvestorAccount = CUstpFtdcQryInvestorAccountField()
        pQryInvestorAccount.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorAccount.UserID = bytes(UserID, encoding='ascii')
        pQryInvestorAccount.InvestorID = bytes(InvestorID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorAccount(self.api, byref(pQryInvestorAccount), self.nRequestID)

    def ReqQryInstrument(self, ExchangeID: str = '', ProductID: str = '', InstrumentID: str = ''):
        pQryInstrument = CUstpFtdcQryInstrumentField()
        pQryInstrument.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInstrument.ProductID = bytes(ProductID, encoding='ascii')
        pQryInstrument.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInstrument(self.api, byref(pQryInstrument), self.nRequestID)

    def ReqQryExchange(self, ExchangeID: str = ''):
        pQryExchange = CUstpFtdcQryExchangeField()
        pQryExchange.ExchangeID = bytes(ExchangeID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryExchange(self.api, byref(pQryExchange), self.nRequestID)

    def ReqQryInvestorPosition(self, BrokerID: str = '', UserID: str = '', ExchangeID: str = '', InvestorID: str = '', InstrumentID: str = ''):
        pQryInvestorPosition = CUstpFtdcQryInvestorPositionField()
        pQryInvestorPosition.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorPosition.UserID = bytes(UserID, encoding='ascii')
        pQryInvestorPosition.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorPosition.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorPosition.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorPosition(self.api, byref(pQryInvestorPosition), self.nRequestID)

    def ReqQryComplianceParam(self, BrokerID: str = '', UserID: str = '', InvestorID: str = '', ExchangeID: str = '', ClientID: str = ''):
        pQryComplianceParam = CUstpFtdcQryComplianceParamField()
        pQryComplianceParam.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryComplianceParam.UserID = bytes(UserID, encoding='ascii')
        pQryComplianceParam.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryComplianceParam.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryComplianceParam.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryComplianceParam(self.api, byref(pQryComplianceParam), self.nRequestID)

    def ReqQryInvestorFee(self, BrokerID: str = '', UserID: str = '', InvestorID: str = '', ExchangeID: str = '', InstrumentID: str = '', ClientID: str = ''):
        pQryInvestorFee = CUstpFtdcQryInvestorFeeField()
        pQryInvestorFee.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorFee.UserID = bytes(UserID, encoding='ascii')
        pQryInvestorFee.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorFee.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorFee.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pQryInvestorFee.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorFee(self.api, byref(pQryInvestorFee), self.nRequestID)

    def ReqQryInvestorMargin(self, BrokerID: str = '', UserID: str = '', InvestorID: str = '', ExchangeID: str = '', InstrumentID: str = '', ClientID: str = ''):
        pQryInvestorMargin = CUstpFtdcQryInvestorMarginField()
        pQryInvestorMargin.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorMargin.UserID = bytes(UserID, encoding='ascii')
        pQryInvestorMargin.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorMargin.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorMargin.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pQryInvestorMargin.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorMargin(self.api, byref(pQryInvestorMargin), self.nRequestID)

    def ReqQryInvestorCombPosition(self, BrokerID: str = '', ExchangeID: str = '', InvestorID: str = '', HedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], CombInstrumentID: str = '', ClientID: str = ''):
        pQryInvestorCombPosition = CUstpFtdcQryInvestorCombPositionField()
        pQryInvestorCombPosition.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorCombPosition.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorCombPosition.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorCombPosition.HedgeFlag = HedgeFlag.value
        pQryInvestorCombPosition.CombInstrumentID = bytes(CombInstrumentID, encoding='ascii')
        pQryInvestorCombPosition.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorCombPosition(self.api, byref(pQryInvestorCombPosition), self.nRequestID)

    def ReqQryInvestorLegPosition(self, BrokerID: str = '', ExchangeID: str = '', InvestorID: str = '', HedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], LegInstrumentID: str = '', ClientID: str = ''):
        pQryInvestorLegPosition = CUstpFtdcQryInvestorLegPositionField()
        pQryInvestorLegPosition.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryInvestorLegPosition.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryInvestorLegPosition.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryInvestorLegPosition.HedgeFlag = HedgeFlag.value
        pQryInvestorLegPosition.LegInstrumentID = bytes(LegInstrumentID, encoding='ascii')
        pQryInvestorLegPosition.ClientID = bytes(ClientID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInvestorLegPosition(self.api, byref(pQryInvestorLegPosition), self.nRequestID)

    def ReqQryInstrumentGroup(self, ExchangeID: str = '', BrokerID: str = '', InstrumentID: str = ''):
        pQryUstpInstrumentGroup = CUstpFtdcQryUstpInstrumentGroupField()
        pQryUstpInstrumentGroup.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryUstpInstrumentGroup.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryUstpInstrumentGroup.InstrumentID = bytes(InstrumentID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryInstrumentGroup(self.api, byref(pQryUstpInstrumentGroup), self.nRequestID)

    def ReqQryClientMarginCombType(self, ExchangeID: str = '', BrokerID: str = '', InvestorID: str = '', HedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], InstrumentGroupID: str = ''):
        pQryClientMarginCombType = CUstpFtdcQryClientMarginCombTypeField()
        pQryClientMarginCombType.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pQryClientMarginCombType.BrokerID = bytes(BrokerID, encoding='ascii')
        pQryClientMarginCombType.InvestorID = bytes(InvestorID, encoding='ascii')
        pQryClientMarginCombType.HedgeFlag = HedgeFlag.value
        pQryClientMarginCombType.InstrumentGroupID = bytes(InstrumentGroupID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryClientMarginCombType(self.api, byref(pQryClientMarginCombType), self.nRequestID)

    def ReqExecOrderInsert(self, BrokerID: str = '', ExchangeID: str = '', OrderSysID: str = '', InvestorID: str = '', UserID: str = '', InstrumentID: str = '', UserOrderLocalID: str = '', OrderType: TUstpFtdcOrderTypeType = list(TUstpFtdcOrderTypeType)[0], DeliveryFlag: TUstpFtdcDeliveryFlagType = list(TUstpFtdcDeliveryFlagType)[0], HedgeFlag: TUstpFtdcHedgeFlagType = list(TUstpFtdcHedgeFlagType)[0], Volume: int = 0, UserCustom: str = '', ActionDay: str = '', BusinessLocalID: int = 0, BusinessUnit: str = ''):
        pInputExecOrder = CUstpFtdcInputExecOrderField()
        pInputExecOrder.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputExecOrder.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputExecOrder.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pInputExecOrder.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputExecOrder.UserID = bytes(UserID, encoding='ascii')
        pInputExecOrder.InstrumentID = bytes(InstrumentID, encoding='ascii')
        pInputExecOrder.UserOrderLocalID = bytes(UserOrderLocalID, encoding='ascii')
        pInputExecOrder.OrderType = OrderType.value
        pInputExecOrder.DeliveryFlag = DeliveryFlag.value
        pInputExecOrder.HedgeFlag = HedgeFlag.value
        pInputExecOrder.Volume = Volume
        pInputExecOrder.UserCustom = bytes(UserCustom, encoding='ascii')
        pInputExecOrder.ActionDay = bytes(ActionDay, encoding='ascii')
        pInputExecOrder.BusinessLocalID = BusinessLocalID
        pInputExecOrder.BusinessUnit = bytes(BusinessUnit, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqExecOrderInsert(self.api, byref(pInputExecOrder), self.nRequestID)

    def ReqExecOrderAction(self, ExchangeID: str = '', OrderSysID: str = '', BrokerID: str = '', InvestorID: str = '', UserID: str = '', UserOrderActionLocalID: str = '', UserOrderLocalID: str = '', ActionFlag: TUstpFtdcActionFlagType = list(TUstpFtdcActionFlagType)[0], VolumeChange: int = 0, BusinessLocalID: int = 0, OrderType: TUstpFtdcOrderTypeType = list(TUstpFtdcOrderTypeType)[0]):
        pInputExecOrderAction = CUstpFtdcInputExecOrderActionField()
        pInputExecOrderAction.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pInputExecOrderAction.OrderSysID = bytes(OrderSysID, encoding='ascii')
        pInputExecOrderAction.BrokerID = bytes(BrokerID, encoding='ascii')
        pInputExecOrderAction.InvestorID = bytes(InvestorID, encoding='ascii')
        pInputExecOrderAction.UserID = bytes(UserID, encoding='ascii')
        pInputExecOrderAction.UserOrderActionLocalID = bytes(UserOrderActionLocalID, encoding='ascii')
        pInputExecOrderAction.UserOrderLocalID = bytes(UserOrderLocalID, encoding='ascii')
        pInputExecOrderAction.ActionFlag = ActionFlag.value
        pInputExecOrderAction.VolumeChange = VolumeChange
        pInputExecOrderAction.BusinessLocalID = BusinessLocalID
        pInputExecOrderAction.OrderType = OrderType.value
        self.nRequestID += 1
        self.h.ReqExecOrderAction(self.api, byref(pInputExecOrderAction), self.nRequestID)

    def ReqQrySystemTime(self, ExchangeID: str = ''):
        pReqQrySystemTime = CUstpFtdcReqQrySystemTimeField()
        pReqQrySystemTime.ExchangeID = bytes(ExchangeID, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQrySystemTime(self.api, byref(pReqQrySystemTime), self.nRequestID)

    def ReqQryMarginPrefParam(self, BrokerID: str = '', ExchangeID: str = '', CombInstrumentID: str = '', CombInstrumentName: str = ''):
        pReqQryMarginPrefParam = CUstpFtdcReqQryMarginPrefParamField()
        pReqQryMarginPrefParam.BrokerID = bytes(BrokerID, encoding='ascii')
        pReqQryMarginPrefParam.ExchangeID = bytes(ExchangeID, encoding='ascii')
        pReqQryMarginPrefParam.CombInstrumentID = bytes(CombInstrumentID, encoding='ascii')
        pReqQryMarginPrefParam.CombInstrumentName = bytes(CombInstrumentName, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqQryMarginPrefParam(self.api, byref(pReqQryMarginPrefParam), self.nRequestID)

    def ReqDSUserCertification(self, AppID: str = '', AuthCode: str = '', EncryptType: TUstpFtdcDSKeyEncryptType = list(TUstpFtdcDSKeyEncryptType)[0]):
        pDSUserInfo = CUstpFtdcDSUserInfoField()
        pDSUserInfo.AppID = bytes(AppID, encoding='ascii')
        pDSUserInfo.AuthCode = bytes(AuthCode, encoding='ascii')
        pDSUserInfo.EncryptType = EncryptType.value
        self.nRequestID += 1
        self.h.ReqDSUserCertification(self.api, byref(pDSUserInfo), self.nRequestID)

    def ReqDSProxySubmitInfo(self, AppID: str = '', TerminalPubNetIP: str = '', TerminalPubNetPort: str = '', TerminalLoginTime: str = '', ExceptionFlag: TUstpFtdcDSExceptionFlagType = list(TUstpFtdcDSExceptionFlagType)[0], RelayID: str = '', TerminalSystemData: str = ''):
        pDSProxySubmitData = CUstpFtdcDSProxySubmitDataField()
        pDSProxySubmitData.AppID = bytes(AppID, encoding='ascii')
        pDSProxySubmitData.TerminalPubNetIP = bytes(TerminalPubNetIP, encoding='ascii')
        pDSProxySubmitData.TerminalPubNetPort = bytes(TerminalPubNetPort, encoding='ascii')
        pDSProxySubmitData.TerminalLoginTime = bytes(TerminalLoginTime, encoding='ascii')
        pDSProxySubmitData.ExceptionFlag = ExceptionFlag.value
        pDSProxySubmitData.RelayID = bytes(RelayID, encoding='ascii')
        pDSProxySubmitData.TerminalSystemData = bytes(TerminalSystemData, encoding='ascii')
        self.nRequestID += 1
        self.h.ReqDSProxySubmitInfo(self.api, byref(pDSProxySubmitData), self.nRequestID)

    def RegCB(self):
        self.h.SetOnFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnFrontConnected.restype = None
        self.evOnFrontConnected = CFUNCTYPE(None)(self.__OnFrontConnected)
        self.h.SetOnFrontConnected(self.spi, self.evOnFrontConnected)

        self.h.SetOnQryFrontConnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnQryFrontConnected.restype = None
        self.evOnQryFrontConnected = CFUNCTYPE(None)(self.__OnQryFrontConnected)
        self.h.SetOnQryFrontConnected(self.spi, self.evOnQryFrontConnected)

        self.h.SetOnFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnFrontDisconnected.restype = None
        self.evOnFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnFrontDisconnected)
        self.h.SetOnFrontDisconnected(self.spi, self.evOnFrontDisconnected)

        self.h.SetOnQryFrontDisconnected.argtypes = [c_void_p, c_void_p]
        self.h.SetOnQryFrontDisconnected.restype = None
        self.evOnQryFrontDisconnected = CFUNCTYPE(None, c_int32)(self.__OnQryFrontDisconnected)
        self.h.SetOnQryFrontDisconnected(self.spi, self.evOnQryFrontDisconnected)

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

        self.h.SetOnRspUserPasswordUpdate.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserPasswordUpdate.restype = None
        self.evOnRspUserPasswordUpdate = CFUNCTYPE(None, POINTER(CUstpFtdcUserPasswordUpdateField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserPasswordUpdate)
        self.h.SetOnRspUserPasswordUpdate(self.spi, self.evOnRspUserPasswordUpdate)

        self.h.SetOnRspOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspOrderInsert.restype = None
        self.evOnRspOrderInsert = CFUNCTYPE(None, POINTER(CUstpFtdcInputOrderField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderInsert)
        self.h.SetOnRspOrderInsert(self.spi, self.evOnRspOrderInsert)

        self.h.SetOnRspOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspOrderAction.restype = None
        self.evOnRspOrderAction = CFUNCTYPE(None, POINTER(CUstpFtdcOrderActionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspOrderAction)
        self.h.SetOnRspOrderAction(self.spi, self.evOnRspOrderAction)

        self.h.SetOnRspQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQuoteInsert.restype = None
        self.evOnRspQuoteInsert = CFUNCTYPE(None, POINTER(CUstpFtdcInputQuoteField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteInsert)
        self.h.SetOnRspQuoteInsert(self.spi, self.evOnRspQuoteInsert)

        self.h.SetOnRspQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQuoteAction.restype = None
        self.evOnRspQuoteAction = CFUNCTYPE(None, POINTER(CUstpFtdcQuoteActionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQuoteAction)
        self.h.SetOnRspQuoteAction(self.spi, self.evOnRspQuoteAction)

        self.h.SetOnRspForQuote.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspForQuote.restype = None
        self.evOnRspForQuote = CFUNCTYPE(None, POINTER(CUstpFtdcReqForQuoteField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspForQuote)
        self.h.SetOnRspForQuote(self.spi, self.evOnRspForQuote)

        self.h.SetOnRspMarginCombAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspMarginCombAction.restype = None
        self.evOnRspMarginCombAction = CFUNCTYPE(None, POINTER(CUstpFtdcInputMarginCombActionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspMarginCombAction)
        self.h.SetOnRspMarginCombAction(self.spi, self.evOnRspMarginCombAction)

        self.h.SetOnRspUserDeposit.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspUserDeposit.restype = None
        self.evOnRspUserDeposit = CFUNCTYPE(None, POINTER(CUstpFtdcstpUserDepositField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspUserDeposit)
        self.h.SetOnRspUserDeposit(self.spi, self.evOnRspUserDeposit)

        self.h.SetOnRtnFlowMessageCancel.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnFlowMessageCancel.restype = None
        self.evOnRtnFlowMessageCancel = CFUNCTYPE(None, POINTER(CUstpFtdcFlowMessageCancelField))(self.__OnRtnFlowMessageCancel)
        self.h.SetOnRtnFlowMessageCancel(self.spi, self.evOnRtnFlowMessageCancel)

        self.h.SetOnRtnTrade.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnTrade.restype = None
        self.evOnRtnTrade = CFUNCTYPE(None, POINTER(CUstpFtdcTradeField))(self.__OnRtnTrade)
        self.h.SetOnRtnTrade(self.spi, self.evOnRtnTrade)

        self.h.SetOnRtnOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnOrder.restype = None
        self.evOnRtnOrder = CFUNCTYPE(None, POINTER(CUstpFtdcOrderField))(self.__OnRtnOrder)
        self.h.SetOnRtnOrder(self.spi, self.evOnRtnOrder)

        self.h.SetOnErrRtnOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnOrderInsert.restype = None
        self.evOnErrRtnOrderInsert = CFUNCTYPE(None, POINTER(CUstpFtdcInputOrderField), POINTER(CUstpFtdcRspInfoField))(self.__OnErrRtnOrderInsert)
        self.h.SetOnErrRtnOrderInsert(self.spi, self.evOnErrRtnOrderInsert)

        self.h.SetOnErrRtnOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnOrderAction.restype = None
        self.evOnErrRtnOrderAction = CFUNCTYPE(None, POINTER(CUstpFtdcOrderActionField), POINTER(CUstpFtdcRspInfoField))(self.__OnErrRtnOrderAction)
        self.h.SetOnErrRtnOrderAction(self.spi, self.evOnErrRtnOrderAction)

        self.h.SetOnRtnInstrumentStatus.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnInstrumentStatus.restype = None
        self.evOnRtnInstrumentStatus = CFUNCTYPE(None, POINTER(CUstpFtdcInstrumentStatusField))(self.__OnRtnInstrumentStatus)
        self.h.SetOnRtnInstrumentStatus(self.spi, self.evOnRtnInstrumentStatus)

        self.h.SetOnRtnInvestorAccountDeposit.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnInvestorAccountDeposit.restype = None
        self.evOnRtnInvestorAccountDeposit = CFUNCTYPE(None, POINTER(CUstpFtdcInvestorAccountDepositResField))(self.__OnRtnInvestorAccountDeposit)
        self.h.SetOnRtnInvestorAccountDeposit(self.spi, self.evOnRtnInvestorAccountDeposit)

        self.h.SetOnRtnQuote.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnQuote.restype = None
        self.evOnRtnQuote = CFUNCTYPE(None, POINTER(CUstpFtdcRtnQuoteField))(self.__OnRtnQuote)
        self.h.SetOnRtnQuote(self.spi, self.evOnRtnQuote)

        self.h.SetOnErrRtnQuoteInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnQuoteInsert.restype = None
        self.evOnErrRtnQuoteInsert = CFUNCTYPE(None, POINTER(CUstpFtdcInputQuoteField), POINTER(CUstpFtdcRspInfoField))(self.__OnErrRtnQuoteInsert)
        self.h.SetOnErrRtnQuoteInsert(self.spi, self.evOnErrRtnQuoteInsert)

        self.h.SetOnErrRtnQuoteAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnQuoteAction.restype = None
        self.evOnErrRtnQuoteAction = CFUNCTYPE(None, POINTER(CUstpFtdcQuoteActionField), POINTER(CUstpFtdcRspInfoField))(self.__OnErrRtnQuoteAction)
        self.h.SetOnErrRtnQuoteAction(self.spi, self.evOnErrRtnQuoteAction)

        self.h.SetOnRtnForQuote.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnForQuote.restype = None
        self.evOnRtnForQuote = CFUNCTYPE(None, POINTER(CUstpFtdcReqForQuoteField))(self.__OnRtnForQuote)
        self.h.SetOnRtnForQuote(self.spi, self.evOnRtnForQuote)

        self.h.SetOnRtnMarginCombinationLeg.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnMarginCombinationLeg.restype = None
        self.evOnRtnMarginCombinationLeg = CFUNCTYPE(None, POINTER(CUstpFtdcMarginCombinationLegField))(self.__OnRtnMarginCombinationLeg)
        self.h.SetOnRtnMarginCombinationLeg(self.spi, self.evOnRtnMarginCombinationLeg)

        self.h.SetOnRtnMarginCombAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnMarginCombAction.restype = None
        self.evOnRtnMarginCombAction = CFUNCTYPE(None, POINTER(CUstpFtdcInputMarginCombActionField))(self.__OnRtnMarginCombAction)
        self.h.SetOnRtnMarginCombAction(self.spi, self.evOnRtnMarginCombAction)

        self.h.SetOnRtnUserDeposit.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnUserDeposit.restype = None
        self.evOnRtnUserDeposit = CFUNCTYPE(None, POINTER(CUstpFtdcstpUserDepositField))(self.__OnRtnUserDeposit)
        self.h.SetOnRtnUserDeposit(self.spi, self.evOnRtnUserDeposit)

        self.h.SetOnRspQueryUserLogin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQueryUserLogin.restype = None
        self.evOnRspQueryUserLogin = CFUNCTYPE(None, POINTER(CUstpFtdcRspUserLoginField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQueryUserLogin)
        self.h.SetOnRspQueryUserLogin(self.spi, self.evOnRspQueryUserLogin)

        self.h.SetOnRspQryOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryOrder.restype = None
        self.evOnRspQryOrder = CFUNCTYPE(None, POINTER(CUstpFtdcOrderField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryOrder)
        self.h.SetOnRspQryOrder(self.spi, self.evOnRspQryOrder)

        self.h.SetOnRspQryTrade.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTrade.restype = None
        self.evOnRspQryTrade = CFUNCTYPE(None, POINTER(CUstpFtdcTradeField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTrade)
        self.h.SetOnRspQryTrade(self.spi, self.evOnRspQryTrade)

        self.h.SetOnRspQryUserInvestor.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryUserInvestor.restype = None
        self.evOnRspQryUserInvestor = CFUNCTYPE(None, POINTER(CUstpFtdcRspUserInvestorField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryUserInvestor)
        self.h.SetOnRspQryUserInvestor(self.spi, self.evOnRspQryUserInvestor)

        self.h.SetOnRspQryTradingCode.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryTradingCode.restype = None
        self.evOnRspQryTradingCode = CFUNCTYPE(None, POINTER(CUstpFtdcRspTradingCodeField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryTradingCode)
        self.h.SetOnRspQryTradingCode(self.spi, self.evOnRspQryTradingCode)

        self.h.SetOnRspQryInvestorAccount.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorAccount.restype = None
        self.evOnRspQryInvestorAccount = CFUNCTYPE(None, POINTER(CUstpFtdcRspInvestorAccountField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorAccount)
        self.h.SetOnRspQryInvestorAccount(self.spi, self.evOnRspQryInvestorAccount)

        self.h.SetOnRspQryInstrument.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInstrument.restype = None
        self.evOnRspQryInstrument = CFUNCTYPE(None, POINTER(CUstpFtdcRspInstrumentField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrument)
        self.h.SetOnRspQryInstrument(self.spi, self.evOnRspQryInstrument)

        self.h.SetOnRspQryExchange.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryExchange.restype = None
        self.evOnRspQryExchange = CFUNCTYPE(None, POINTER(CUstpFtdcRspExchangeField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryExchange)
        self.h.SetOnRspQryExchange(self.spi, self.evOnRspQryExchange)

        self.h.SetOnRspQryInvestorPosition.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorPosition.restype = None
        self.evOnRspQryInvestorPosition = CFUNCTYPE(None, POINTER(CUstpFtdcRspInvestorPositionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorPosition)
        self.h.SetOnRspQryInvestorPosition(self.spi, self.evOnRspQryInvestorPosition)

        self.h.SetOnRspQryComplianceParam.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryComplianceParam.restype = None
        self.evOnRspQryComplianceParam = CFUNCTYPE(None, POINTER(CUstpFtdcRspComplianceParamField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryComplianceParam)
        self.h.SetOnRspQryComplianceParam(self.spi, self.evOnRspQryComplianceParam)

        self.h.SetOnRspQryInvestorFee.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorFee.restype = None
        self.evOnRspQryInvestorFee = CFUNCTYPE(None, POINTER(CUstpFtdcInvestorFeeField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorFee)
        self.h.SetOnRspQryInvestorFee(self.spi, self.evOnRspQryInvestorFee)

        self.h.SetOnRspQryInvestorMargin.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorMargin.restype = None
        self.evOnRspQryInvestorMargin = CFUNCTYPE(None, POINTER(CUstpFtdcInvestorMarginField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorMargin)
        self.h.SetOnRspQryInvestorMargin(self.spi, self.evOnRspQryInvestorMargin)

        self.h.SetOnRspQryInvestorCombPosition.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorCombPosition.restype = None
        self.evOnRspQryInvestorCombPosition = CFUNCTYPE(None, POINTER(CUstpFtdcRspInvestorCombPositionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorCombPosition)
        self.h.SetOnRspQryInvestorCombPosition(self.spi, self.evOnRspQryInvestorCombPosition)

        self.h.SetOnRspQryInvestorLegPosition.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInvestorLegPosition.restype = None
        self.evOnRspQryInvestorLegPosition = CFUNCTYPE(None, POINTER(CUstpFtdcRspInvestorLegPositionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInvestorLegPosition)
        self.h.SetOnRspQryInvestorLegPosition(self.spi, self.evOnRspQryInvestorLegPosition)

        self.h.SetOnRspQryInstrumentGroup.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryInstrumentGroup.restype = None
        self.evOnRspQryInstrumentGroup = CFUNCTYPE(None, POINTER(CUstpFtdcRspInstrumentGroupField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryInstrumentGroup)
        self.h.SetOnRspQryInstrumentGroup(self.spi, self.evOnRspQryInstrumentGroup)

        self.h.SetOnRspQryClientMarginCombType.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryClientMarginCombType.restype = None
        self.evOnRspQryClientMarginCombType = CFUNCTYPE(None, POINTER(CUstpFtdcRspClientMarginCombTypeField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryClientMarginCombType)
        self.h.SetOnRspQryClientMarginCombType(self.spi, self.evOnRspQryClientMarginCombType)

        self.h.SetOnRspExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspExecOrderInsert.restype = None
        self.evOnRspExecOrderInsert = CFUNCTYPE(None, POINTER(CUstpFtdcInputExecOrderField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderInsert)
        self.h.SetOnRspExecOrderInsert(self.spi, self.evOnRspExecOrderInsert)

        self.h.SetOnRspExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspExecOrderAction.restype = None
        self.evOnRspExecOrderAction = CFUNCTYPE(None, POINTER(CUstpFtdcInputExecOrderActionField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspExecOrderAction)
        self.h.SetOnRspExecOrderAction(self.spi, self.evOnRspExecOrderAction)

        self.h.SetOnRtnExecOrder.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnExecOrder.restype = None
        self.evOnRtnExecOrder = CFUNCTYPE(None, POINTER(CUstpFtdcExecOrderField))(self.__OnRtnExecOrder)
        self.h.SetOnRtnExecOrder(self.spi, self.evOnRtnExecOrder)

        self.h.SetOnErrRtnExecOrderInsert.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnExecOrderInsert.restype = None
        self.evOnErrRtnExecOrderInsert = CFUNCTYPE(None, POINTER(CUstpFtdcInputExecOrderField), POINTER(CUstpFtdcRspInfoField))(self.__OnErrRtnExecOrderInsert)
        self.h.SetOnErrRtnExecOrderInsert(self.spi, self.evOnErrRtnExecOrderInsert)

        self.h.SetOnErrRtnExecOrderAction.argtypes = [c_void_p, c_void_p]
        self.h.SetOnErrRtnExecOrderAction.restype = None
        self.evOnErrRtnExecOrderAction = CFUNCTYPE(None, POINTER(CUstpFtdcInputExecOrderActionField), POINTER(CUstpFtdcRspInfoField))(self.__OnErrRtnExecOrderAction)
        self.h.SetOnErrRtnExecOrderAction(self.spi, self.evOnErrRtnExecOrderAction)

        self.h.SetOnRtnTransferMoney.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRtnTransferMoney.restype = None
        self.evOnRtnTransferMoney = CFUNCTYPE(None, POINTER(CUstpFtdcSyncMoneyTransferField))(self.__OnRtnTransferMoney)
        self.h.SetOnRtnTransferMoney(self.spi, self.evOnRtnTransferMoney)

        self.h.SetOnRspQrySystemTime.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQrySystemTime.restype = None
        self.evOnRspQrySystemTime = CFUNCTYPE(None, POINTER(CUstpFtdcRspQrySystemTimeField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQrySystemTime)
        self.h.SetOnRspQrySystemTime(self.spi, self.evOnRspQrySystemTime)

        self.h.SetOnRspQryMarginPrefParam.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspQryMarginPrefParam.restype = None
        self.evOnRspQryMarginPrefParam = CFUNCTYPE(None, POINTER(CUstpFtdcRspQryMarginPrefParamField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspQryMarginPrefParam)
        self.h.SetOnRspQryMarginPrefParam(self.spi, self.evOnRspQryMarginPrefParam)

        self.h.SetOnRspDSUserCertification.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspDSUserCertification.restype = None
        self.evOnRspDSUserCertification = CFUNCTYPE(None, POINTER(CUstpFtdcDSUserCertRspDataField), POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspDSUserCertification)
        self.h.SetOnRspDSUserCertification(self.spi, self.evOnRspDSUserCertification)

        self.h.SetOnRspDSProxySubmitInfo.argtypes = [c_void_p, c_void_p]
        self.h.SetOnRspDSProxySubmitInfo.restype = None
        self.evOnRspDSProxySubmitInfo = CFUNCTYPE(None, POINTER(CUstpFtdcRspInfoField), c_int32, c_bool)(self.__OnRspDSProxySubmitInfo)
        self.h.SetOnRspDSProxySubmitInfo(self.spi, self.evOnRspDSProxySubmitInfo)

    def __OnFrontConnected(self):
        self.OnFrontConnected()

    def __OnQryFrontConnected(self):
        self.OnQryFrontConnected()

    def __OnFrontDisconnected(self, nReason):
        self.OnFrontDisconnected(nReason)

    def __OnQryFrontDisconnected(self, nReason):
        self.OnQryFrontDisconnected(nReason)

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

    def __OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserPasswordUpdate(copy.deepcopy(POINTER(CUstpFtdcUserPasswordUpdateField).from_param(pUserPasswordUpdate).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspOrderInsert(copy.deepcopy(POINTER(CUstpFtdcInputOrderField).from_param(pInputOrder).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspOrderAction(self, pOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspOrderAction(copy.deepcopy(POINTER(CUstpFtdcOrderActionField).from_param(pOrderAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast):
        self.OnRspQuoteInsert(copy.deepcopy(POINTER(CUstpFtdcInputQuoteField).from_param(pInputQuote).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQuoteAction(self, pQuoteAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspQuoteAction(copy.deepcopy(POINTER(CUstpFtdcQuoteActionField).from_param(pQuoteAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspForQuote(self, pReqForQuote, pRspInfo, nRequestID, bIsLast):
        self.OnRspForQuote(copy.deepcopy(POINTER(CUstpFtdcReqForQuoteField).from_param(pReqForQuote).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspMarginCombAction(self, pInputMarginCombAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspMarginCombAction(copy.deepcopy(POINTER(CUstpFtdcInputMarginCombActionField).from_param(pInputMarginCombAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspUserDeposit(self, pstpUserDeposit, pRspInfo, nRequestID, bIsLast):
        self.OnRspUserDeposit(copy.deepcopy(POINTER(CUstpFtdcstpUserDepositField).from_param(pstpUserDeposit).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnFlowMessageCancel(self, pFlowMessageCancel):
        self.OnRtnFlowMessageCancel(copy.deepcopy(POINTER(CUstpFtdcFlowMessageCancelField).from_param(pFlowMessageCancel).contents))

    def __OnRtnTrade(self, pTrade):
        self.OnRtnTrade(copy.deepcopy(POINTER(CUstpFtdcTradeField).from_param(pTrade).contents))

    def __OnRtnOrder(self, pOrder):
        self.OnRtnOrder(copy.deepcopy(POINTER(CUstpFtdcOrderField).from_param(pOrder).contents))

    def __OnErrRtnOrderInsert(self, pInputOrder, pRspInfo):
        self.OnErrRtnOrderInsert(copy.deepcopy(POINTER(CUstpFtdcInputOrderField).from_param(pInputOrder).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnOrderAction(self, pOrderAction, pRspInfo):
        self.OnErrRtnOrderAction(copy.deepcopy(POINTER(CUstpFtdcOrderActionField).from_param(pOrderAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnInstrumentStatus(self, pInstrumentStatus):
        self.OnRtnInstrumentStatus(copy.deepcopy(POINTER(CUstpFtdcInstrumentStatusField).from_param(pInstrumentStatus).contents))

    def __OnRtnInvestorAccountDeposit(self, pInvestorAccountDepositRes):
        self.OnRtnInvestorAccountDeposit(copy.deepcopy(POINTER(CUstpFtdcInvestorAccountDepositResField).from_param(pInvestorAccountDepositRes).contents))

    def __OnRtnQuote(self, pRtnQuote):
        self.OnRtnQuote(copy.deepcopy(POINTER(CUstpFtdcRtnQuoteField).from_param(pRtnQuote).contents))

    def __OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo):
        self.OnErrRtnQuoteInsert(copy.deepcopy(POINTER(CUstpFtdcInputQuoteField).from_param(pInputQuote).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo):
        self.OnErrRtnQuoteAction(copy.deepcopy(POINTER(CUstpFtdcQuoteActionField).from_param(pQuoteAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnForQuote(self, pReqForQuote):
        self.OnRtnForQuote(copy.deepcopy(POINTER(CUstpFtdcReqForQuoteField).from_param(pReqForQuote).contents))

    def __OnRtnMarginCombinationLeg(self, pMarginCombinationLeg):
        self.OnRtnMarginCombinationLeg(copy.deepcopy(POINTER(CUstpFtdcMarginCombinationLegField).from_param(pMarginCombinationLeg).contents))

    def __OnRtnMarginCombAction(self, pInputMarginCombAction):
        self.OnRtnMarginCombAction(copy.deepcopy(POINTER(CUstpFtdcInputMarginCombActionField).from_param(pInputMarginCombAction).contents))

    def __OnRtnUserDeposit(self, pstpUserDeposit):
        self.OnRtnUserDeposit(copy.deepcopy(POINTER(CUstpFtdcstpUserDepositField).from_param(pstpUserDeposit).contents))

    def __OnRspQueryUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        self.OnRspQueryUserLogin(copy.deepcopy(POINTER(CUstpFtdcRspUserLoginField).from_param(pRspUserLogin).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryOrder(copy.deepcopy(POINTER(CUstpFtdcOrderField).from_param(pOrder).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTrade(copy.deepcopy(POINTER(CUstpFtdcTradeField).from_param(pTrade).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryUserInvestor(self, pRspUserInvestor, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryUserInvestor(copy.deepcopy(POINTER(CUstpFtdcRspUserInvestorField).from_param(pRspUserInvestor).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryTradingCode(self, pRspTradingCode, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryTradingCode(copy.deepcopy(POINTER(CUstpFtdcRspTradingCodeField).from_param(pRspTradingCode).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorAccount(self, pRspInvestorAccount, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorAccount(copy.deepcopy(POINTER(CUstpFtdcRspInvestorAccountField).from_param(pRspInvestorAccount).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInstrument(self, pRspInstrument, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInstrument(copy.deepcopy(POINTER(CUstpFtdcRspInstrumentField).from_param(pRspInstrument).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryExchange(self, pRspExchange, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryExchange(copy.deepcopy(POINTER(CUstpFtdcRspExchangeField).from_param(pRspExchange).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorPosition(self, pRspInvestorPosition, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorPosition(copy.deepcopy(POINTER(CUstpFtdcRspInvestorPositionField).from_param(pRspInvestorPosition).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryComplianceParam(self, pRspComplianceParam, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryComplianceParam(copy.deepcopy(POINTER(CUstpFtdcRspComplianceParamField).from_param(pRspComplianceParam).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorFee(self, pInvestorFee, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorFee(copy.deepcopy(POINTER(CUstpFtdcInvestorFeeField).from_param(pInvestorFee).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorMargin(self, pInvestorMargin, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorMargin(copy.deepcopy(POINTER(CUstpFtdcInvestorMarginField).from_param(pInvestorMargin).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorCombPosition(self, pRspInvestorCombPosition, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorCombPosition(copy.deepcopy(POINTER(CUstpFtdcRspInvestorCombPositionField).from_param(pRspInvestorCombPosition).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInvestorLegPosition(self, pRspInvestorLegPosition, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInvestorLegPosition(copy.deepcopy(POINTER(CUstpFtdcRspInvestorLegPositionField).from_param(pRspInvestorLegPosition).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryInstrumentGroup(self, pRspInstrumentGroup, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryInstrumentGroup(copy.deepcopy(POINTER(CUstpFtdcRspInstrumentGroupField).from_param(pRspInstrumentGroup).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryClientMarginCombType(self, pRspClientMarginCombType, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryClientMarginCombType(copy.deepcopy(POINTER(CUstpFtdcRspClientMarginCombTypeField).from_param(pRspClientMarginCombType).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast):
        self.OnRspExecOrderInsert(copy.deepcopy(POINTER(CUstpFtdcInputExecOrderField).from_param(pInputExecOrder).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast):
        self.OnRspExecOrderAction(copy.deepcopy(POINTER(CUstpFtdcInputExecOrderActionField).from_param(pInputExecOrderAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRtnExecOrder(self, pExecOrder):
        self.OnRtnExecOrder(copy.deepcopy(POINTER(CUstpFtdcExecOrderField).from_param(pExecOrder).contents))

    def __OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo):
        self.OnErrRtnExecOrderInsert(copy.deepcopy(POINTER(CUstpFtdcInputExecOrderField).from_param(pInputExecOrder).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnErrRtnExecOrderAction(self, pInputExecOrderAction, pRspInfo):
        self.OnErrRtnExecOrderAction(copy.deepcopy(POINTER(CUstpFtdcInputExecOrderActionField).from_param(pInputExecOrderAction).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents))

    def __OnRtnTransferMoney(self, pSyncMoneyTransfer):
        self.OnRtnTransferMoney(copy.deepcopy(POINTER(CUstpFtdcSyncMoneyTransferField).from_param(pSyncMoneyTransfer).contents))

    def __OnRspQrySystemTime(self, pRspQrySystemTime, pRspInfo, nRequestID, bIsLast):
        self.OnRspQrySystemTime(copy.deepcopy(POINTER(CUstpFtdcRspQrySystemTimeField).from_param(pRspQrySystemTime).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspQryMarginPrefParam(self, pRspQryMarginPrefParam, pRspInfo, nRequestID, bIsLast):
        self.OnRspQryMarginPrefParam(copy.deepcopy(POINTER(CUstpFtdcRspQryMarginPrefParamField).from_param(pRspQryMarginPrefParam).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspDSUserCertification(self, pDSUserCertRspData, pRspInfo, nRequestID, bIsLast):
        self.OnRspDSUserCertification(copy.deepcopy(POINTER(CUstpFtdcDSUserCertRspDataField).from_param(pDSUserCertRspData).contents), copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def __OnRspDSProxySubmitInfo(self, pRspInfo, nRequestID, bIsLast):
        self.OnRspDSProxySubmitInfo(copy.deepcopy(POINTER(CUstpFtdcRspInfoField).from_param(pRspInfo).contents), nRequestID, bIsLast)

    def OnFrontConnected(self, ):
        print('===OnFrontConnected===: ')

    def OnQryFrontConnected(self, ):
        print('===OnQryFrontConnected===: ')

    def OnFrontDisconnected(self, nReason: int):
        print('===OnFrontDisconnected===: nReason: int')

    def OnQryFrontDisconnected(self, nReason: int):
        print('===OnQryFrontDisconnected===: nReason: int')

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

    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate: CUstpFtdcUserPasswordUpdateField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserPasswordUpdate===: pUserPasswordUpdate: CUstpFtdcUserPasswordUpdateField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspOrderInsert(self, pInputOrder: CUstpFtdcInputOrderField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspOrderInsert===: pInputOrder: CUstpFtdcInputOrderField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspOrderAction(self, pOrderAction: CUstpFtdcOrderActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspOrderAction===: pOrderAction: CUstpFtdcOrderActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQuoteInsert(self, pInputQuote: CUstpFtdcInputQuoteField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQuoteInsert===: pInputQuote: CUstpFtdcInputQuoteField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQuoteAction(self, pQuoteAction: CUstpFtdcQuoteActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQuoteAction===: pQuoteAction: CUstpFtdcQuoteActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspForQuote(self, pReqForQuote: CUstpFtdcReqForQuoteField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspForQuote===: pReqForQuote: CUstpFtdcReqForQuoteField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspMarginCombAction(self, pInputMarginCombAction: CUstpFtdcInputMarginCombActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspMarginCombAction===: pInputMarginCombAction: CUstpFtdcInputMarginCombActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspUserDeposit(self, pstpUserDeposit: CUstpFtdcstpUserDepositField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspUserDeposit===: pstpUserDeposit: CUstpFtdcstpUserDepositField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnFlowMessageCancel(self, pFlowMessageCancel: CUstpFtdcFlowMessageCancelField):
        print('===OnRtnFlowMessageCancel===: pFlowMessageCancel: CUstpFtdcFlowMessageCancelField')

    def OnRtnTrade(self, pTrade: CUstpFtdcTradeField):
        print('===OnRtnTrade===: pTrade: CUstpFtdcTradeField')

    def OnRtnOrder(self, pOrder: CUstpFtdcOrderField):
        print('===OnRtnOrder===: pOrder: CUstpFtdcOrderField')

    def OnErrRtnOrderInsert(self, pInputOrder: CUstpFtdcInputOrderField, pRspInfo: CUstpFtdcRspInfoField):
        print('===OnErrRtnOrderInsert===: pInputOrder: CUstpFtdcInputOrderField, pRspInfo: CUstpFtdcRspInfoField')

    def OnErrRtnOrderAction(self, pOrderAction: CUstpFtdcOrderActionField, pRspInfo: CUstpFtdcRspInfoField):
        print('===OnErrRtnOrderAction===: pOrderAction: CUstpFtdcOrderActionField, pRspInfo: CUstpFtdcRspInfoField')

    def OnRtnInstrumentStatus(self, pInstrumentStatus: CUstpFtdcInstrumentStatusField):
        print('===OnRtnInstrumentStatus===: pInstrumentStatus: CUstpFtdcInstrumentStatusField')

    def OnRtnInvestorAccountDeposit(self, pInvestorAccountDepositRes: CUstpFtdcInvestorAccountDepositResField):
        print('===OnRtnInvestorAccountDeposit===: pInvestorAccountDepositRes: CUstpFtdcInvestorAccountDepositResField')

    def OnRtnQuote(self, pRtnQuote: CUstpFtdcRtnQuoteField):
        print('===OnRtnQuote===: pRtnQuote: CUstpFtdcRtnQuoteField')

    def OnErrRtnQuoteInsert(self, pInputQuote: CUstpFtdcInputQuoteField, pRspInfo: CUstpFtdcRspInfoField):
        print('===OnErrRtnQuoteInsert===: pInputQuote: CUstpFtdcInputQuoteField, pRspInfo: CUstpFtdcRspInfoField')

    def OnErrRtnQuoteAction(self, pQuoteAction: CUstpFtdcQuoteActionField, pRspInfo: CUstpFtdcRspInfoField):
        print('===OnErrRtnQuoteAction===: pQuoteAction: CUstpFtdcQuoteActionField, pRspInfo: CUstpFtdcRspInfoField')

    def OnRtnForQuote(self, pReqForQuote: CUstpFtdcReqForQuoteField):
        print('===OnRtnForQuote===: pReqForQuote: CUstpFtdcReqForQuoteField')

    def OnRtnMarginCombinationLeg(self, pMarginCombinationLeg: CUstpFtdcMarginCombinationLegField):
        print('===OnRtnMarginCombinationLeg===: pMarginCombinationLeg: CUstpFtdcMarginCombinationLegField')

    def OnRtnMarginCombAction(self, pInputMarginCombAction: CUstpFtdcInputMarginCombActionField):
        print('===OnRtnMarginCombAction===: pInputMarginCombAction: CUstpFtdcInputMarginCombActionField')

    def OnRtnUserDeposit(self, pstpUserDeposit: CUstpFtdcstpUserDepositField):
        print('===OnRtnUserDeposit===: pstpUserDeposit: CUstpFtdcstpUserDepositField')

    def OnRspQueryUserLogin(self, pRspUserLogin: CUstpFtdcRspUserLoginField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQueryUserLogin===: pRspUserLogin: CUstpFtdcRspUserLoginField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryOrder(self, pOrder: CUstpFtdcOrderField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryOrder===: pOrder: CUstpFtdcOrderField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTrade(self, pTrade: CUstpFtdcTradeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTrade===: pTrade: CUstpFtdcTradeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryUserInvestor(self, pRspUserInvestor: CUstpFtdcRspUserInvestorField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryUserInvestor===: pRspUserInvestor: CUstpFtdcRspUserInvestorField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryTradingCode(self, pRspTradingCode: CUstpFtdcRspTradingCodeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryTradingCode===: pRspTradingCode: CUstpFtdcRspTradingCodeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorAccount(self, pRspInvestorAccount: CUstpFtdcRspInvestorAccountField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorAccount===: pRspInvestorAccount: CUstpFtdcRspInvestorAccountField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInstrument(self, pRspInstrument: CUstpFtdcRspInstrumentField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInstrument===: pRspInstrument: CUstpFtdcRspInstrumentField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryExchange(self, pRspExchange: CUstpFtdcRspExchangeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryExchange===: pRspExchange: CUstpFtdcRspExchangeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorPosition(self, pRspInvestorPosition: CUstpFtdcRspInvestorPositionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorPosition===: pRspInvestorPosition: CUstpFtdcRspInvestorPositionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryComplianceParam(self, pRspComplianceParam: CUstpFtdcRspComplianceParamField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryComplianceParam===: pRspComplianceParam: CUstpFtdcRspComplianceParamField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorFee(self, pInvestorFee: CUstpFtdcInvestorFeeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorFee===: pInvestorFee: CUstpFtdcInvestorFeeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorMargin(self, pInvestorMargin: CUstpFtdcInvestorMarginField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorMargin===: pInvestorMargin: CUstpFtdcInvestorMarginField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorCombPosition(self, pRspInvestorCombPosition: CUstpFtdcRspInvestorCombPositionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorCombPosition===: pRspInvestorCombPosition: CUstpFtdcRspInvestorCombPositionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInvestorLegPosition(self, pRspInvestorLegPosition: CUstpFtdcRspInvestorLegPositionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInvestorLegPosition===: pRspInvestorLegPosition: CUstpFtdcRspInvestorLegPositionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryInstrumentGroup(self, pRspInstrumentGroup: CUstpFtdcRspInstrumentGroupField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryInstrumentGroup===: pRspInstrumentGroup: CUstpFtdcRspInstrumentGroupField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryClientMarginCombType(self, pRspClientMarginCombType: CUstpFtdcRspClientMarginCombTypeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryClientMarginCombType===: pRspClientMarginCombType: CUstpFtdcRspClientMarginCombTypeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspExecOrderInsert(self, pInputExecOrder: CUstpFtdcInputExecOrderField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspExecOrderInsert===: pInputExecOrder: CUstpFtdcInputExecOrderField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspExecOrderAction(self, pInputExecOrderAction: CUstpFtdcInputExecOrderActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspExecOrderAction===: pInputExecOrderAction: CUstpFtdcInputExecOrderActionField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRtnExecOrder(self, pExecOrder: CUstpFtdcExecOrderField):
        print('===OnRtnExecOrder===: pExecOrder: CUstpFtdcExecOrderField')

    def OnErrRtnExecOrderInsert(self, pInputExecOrder: CUstpFtdcInputExecOrderField, pRspInfo: CUstpFtdcRspInfoField):
        print('===OnErrRtnExecOrderInsert===: pInputExecOrder: CUstpFtdcInputExecOrderField, pRspInfo: CUstpFtdcRspInfoField')

    def OnErrRtnExecOrderAction(self, pInputExecOrderAction: CUstpFtdcInputExecOrderActionField, pRspInfo: CUstpFtdcRspInfoField):
        print('===OnErrRtnExecOrderAction===: pInputExecOrderAction: CUstpFtdcInputExecOrderActionField, pRspInfo: CUstpFtdcRspInfoField')

    def OnRtnTransferMoney(self, pSyncMoneyTransfer: CUstpFtdcSyncMoneyTransferField):
        print('===OnRtnTransferMoney===: pSyncMoneyTransfer: CUstpFtdcSyncMoneyTransferField')

    def OnRspQrySystemTime(self, pRspQrySystemTime: CUstpFtdcRspQrySystemTimeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQrySystemTime===: pRspQrySystemTime: CUstpFtdcRspQrySystemTimeField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspQryMarginPrefParam(self, pRspQryMarginPrefParam: CUstpFtdcRspQryMarginPrefParamField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspQryMarginPrefParam===: pRspQryMarginPrefParam: CUstpFtdcRspQryMarginPrefParamField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspDSUserCertification(self, pDSUserCertRspData: CUstpFtdcDSUserCertRspDataField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspDSUserCertification===: pDSUserCertRspData: CUstpFtdcDSUserCertRspDataField, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')

    def OnRspDSProxySubmitInfo(self, pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool):
        print('===OnRspDSProxySubmitInfo===: pRspInfo: CUstpFtdcRspInfoField, nRequestID: int, bIsLast: bool')
