#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = ''
__author__ = 'HaiFeng'
__mtime__ = '2018/12/10'

from ctypes import *
from .ctp_enum import *


class CUstpFtdcRspUserLoginField(Structure):
    """系统用户登录应答"""
    _fields_ = [
        ("TradingDay", c_char * 9),
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("LoginTime", c_char * 9),
        ("ExchangeTime", c_char * 9),
        ("MaxOrderLocalID", c_char * 21),
        ("TradingSystemName", c_char * 61),
        ("DataCenterID", c_int32),
        ("PrivateFlowSize", c_int32),
        ("UserFlowSize", c_int32),
        ("ActionDay", c_char * 9),
        ("FemasVersion", c_char * 21),
        ("FemasLifeCycle", c_int32),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def getLoginTime(self):
        '''登录成功时间'''
        return str(self.LoginTime, 'GBK')

    def getExchangeTime(self):
        '''登录成功时的交易所时间'''
        return str(self.ExchangeTime, 'GBK')

    def getMaxOrderLocalID(self):
        '''用户最大本地报单号'''
        return str(self.MaxOrderLocalID, 'GBK')

    def getTradingSystemName(self):
        '''交易系统名称'''
        return str(self.TradingSystemName, 'GBK')

    def getDataCenterID(self):
        '''数据中心代码'''
        return self.DataCenterID

    def getPrivateFlowSize(self):
        '''会员私有流当前长度'''
        return self.PrivateFlowSize

    def getUserFlowSize(self):
        '''交易员私有流当前长度'''
        return self.UserFlowSize

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getFemasVersion(self):
        '''飞马版本号'''
        return str(self.FemasVersion, 'GBK')

    def getFemasLifeCycle(self):
        '''飞马生命周期号'''
        return self.FemasLifeCycle

    def __str__(self):  # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'LoginTime'={self.getLoginTime()}, 'ExchangeTime'={self.getExchangeTime()}, 'MaxOrderLocalID'={self.getMaxOrderLocalID()}, 'TradingSystemName'={self.getTradingSystemName()}, 'DataCenterID'={self.getDataCenterID()}, 'PrivateFlowSize'={self.getPrivateFlowSize()}, 'UserFlowSize'={self.getUserFlowSize()}, 'ActionDay'={self.getActionDay()}, 'FemasVersion'={self.getFemasVersion()}, 'FemasLifeCycle'={self.getFemasLifeCycle()}"


class CUstpFtdcReqUserLogoutField(Structure):
    """用户登出请求"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class CUstpFtdcRspUserLogoutField(Structure):
    """用户登出响应"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class CUstpFtdcForceUserExitField(Structure):
    """强制用户退出"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class CUstpFtdcUserPasswordUpdateField(Structure):
    """用户口令修改"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("OldPassword", c_char * 41),
        ("NewPassword", c_char * 41),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def getOldPassword(self):
        '''旧密码'''
        return str(self.OldPassword, 'GBK')

    def getNewPassword(self):
        '''新密码'''
        return str(self.NewPassword, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'OldPassword'={self.getOldPassword()}, 'NewPassword'={self.getNewPassword()}"


class CUstpFtdcInputOrderField(Structure):
    """输入报单"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("OrderSysID", c_char * 31),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("SeatNo", c_int32),
        ("InstrumentID", c_char * 31),
        ("UserOrderLocalID", c_char * 21),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("LimitPrice", c_double),
        ("Volume", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char * 9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char * 21),
        ("UserCustom", c_char * 65),
        ("BusinessLocalID", c_int32),
        ("ActionDay", c_char * 9),
        ("ArbiType", c_char),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getSeatNo(self):
        '''指定通过此席位序号下单'''
        return self.SeatNo

    def getInstrumentID(self):
        '''合约代码/套利组合合约号'''
        return str(self.InstrumentID, 'GBK')

    def getUserOrderLocalID(self):
        '''用户本地报单号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getOrderPriceType(self):
        '''报单类型'''
        return TUstpFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TUstpFtdcOrderPriceTypeType)] else list(TUstpFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getOffsetFlag(self):
        '''开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTimeCondition(self):
        '''有效期类型'''
        return TUstpFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TUstpFtdcTimeConditionType)] else list(TUstpFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TUstpFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TUstpFtdcVolumeConditionType)] else list(TUstpFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getStopPrice(self):
        '''止损价止赢价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TUstpFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TUstpFtdcForceCloseReasonType)] else list(TUstpFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'SeatNo'={self.getSeatNo()}, 'InstrumentID'={self.getInstrumentID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'Volume'={self.getVolume()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'UserCustom'={self.getUserCustom()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'ActionDay'={self.getActionDay()}, 'ArbiType'={self.getArbiType()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcOrderActionField(Structure):
    """报单操作"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("OrderSysID", c_char * 31),
        ("BrokerID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("UserOrderActionLocalID", c_char * 21),
        ("UserOrderLocalID", c_char * 21),
        ("ActionFlag", c_char),
        ("LimitPrice", c_double),
        ("VolumeChange", c_int32),
        ("BusinessLocalID", c_int32),
        ("ClientID", c_char * 19),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserOrderActionLocalID(self):
        '''本次撤单操作的本地编号'''
        return str(self.UserOrderActionLocalID, 'GBK')

    def getUserOrderLocalID(self):
        '''被撤订单的本地报单编号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getActionFlag(self):
        '''报单操作标志'''
        return TUstpFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TUstpFtdcActionFlagType)] else list(TUstpFtdcActionFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'UserOrderActionLocalID'={self.getUserOrderActionLocalID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'ActionFlag'={self.getActionFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'VolumeChange'={self.getVolumeChange()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcMemDbField(Structure):
    """内存表导出"""
    _fields_ = [
        ("MemTableName", c_char * 61),
    ]

    def getMemTableName(self):
        '''内存表名'''
        return str(self.MemTableName, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'MemTableName'={self.getMemTableName()}"


class CUstpFtdcRspInfoField(Structure):
    """响应信息"""
    _fields_ = [
        ("ErrorID", c_int32),
        ("ErrorMsg", c_char * 81),
    ]

    def getErrorID(self):
        '''错误代码'''
        return self.ErrorID

    def getErrorMsg(self):
        '''错误信息'''
        return str(self.ErrorMsg, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ErrorID'={self.getErrorID()}, 'ErrorMsg'={self.getErrorMsg()}"


class CUstpFtdcQryOrderField(Structure):
    """报单查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("OrderSysID", c_char * 31),
        ("InstrumentID", c_char * 31),
        ("OrderStatus", c_char),
        ("OrderType", c_char),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getOrderStatus(self):
        '''报单状态'''
        return TUstpFtdcOrderStatusType(ord(self.OrderStatus)) if ord(self.OrderStatus) in [e.value for e in list(TUstpFtdcOrderStatusType)] else list(TUstpFtdcOrderStatusType)[0]

    def getOrderType(self):
        '''委托类型'''
        return TUstpFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TUstpFtdcOrderTypeType)] else list(TUstpFtdcOrderTypeType)[0]

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'OrderSysID'={self.getOrderSysID()}, 'InstrumentID'={self.getInstrumentID()}, 'OrderStatus'={self.getOrderStatus()}, 'OrderType'={self.getOrderType()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcQryTradeField(Structure):
    """成交查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("TradeID", c_char * 21),
        ("InstrumentID", c_char * 31),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'TradeID'={self.getTradeID()}, 'InstrumentID'={self.getInstrumentID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcQryInstrumentField(Structure):
    """合约查询"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("ProductID", c_char * 13),
        ("InstrumentID", c_char * 31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''产品代码'''
        return str(self.ProductID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}, 'InstrumentID'={self.getInstrumentID()}"


class CUstpFtdcRspInstrumentField(Structure):
    """合约查询应答"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("ProductID", c_char * 13),
        ("ProductName", c_char * 41),
        ("InstrumentID", c_char * 31),
        ("InstrumentName", c_char * 21),
        ("DeliveryYear", c_int32),
        ("DeliveryMonth", c_int32),
        ("MaxLimitOrderVolume", c_int32),
        ("MinLimitOrderVolume", c_int32),
        ("MaxMarketOrderVolume", c_int32),
        ("MinMarketOrderVolume", c_int32),
        ("VolumeMultiple", c_int32),
        ("PriceTick", c_double),
        ("Currency", c_char),
        ("LongPosLimit", c_int32),
        ("ShortPosLimit", c_int32),
        ("LowerLimitPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("InstrumentStatus", c_char),
        ("CreateDate", c_char * 9),
        ("OpenDate", c_char * 9),
        ("ExpireDate", c_char * 9),
        ("StartDelivDate", c_char * 9),
        ("EndDelivDate", c_char * 9),
        ("BasisPrice", c_double),
        ("IsTrading", c_int32),
        ("UnderlyingInstrID", c_char * 31),
        ("UnderlyingMultiple", c_int32),
        ("PositionType", c_char),
        ("StrikePrice", c_double),
        ("OptionsType", c_char),
        ("CurrencyID", c_char * 5),
        ("ArbiType", c_char),
        ("InstrumentID_1", c_char * 31),
        ("Direction_1", c_char),
        ("Ratio_1", c_double),
        ("InstrumentID_2", c_char * 31),
        ("Direction_2", c_char),
        ("Ratio_2", c_double),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''品种代码'''
        return str(self.ProductID, 'GBK')

    def getProductName(self):
        '''品种名称'''
        return str(self.ProductName, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getInstrumentName(self):
        '''合约名称'''
        return str(self.InstrumentName, 'GBK')

    def getDeliveryYear(self):
        '''交割年份'''
        return self.DeliveryYear

    def getDeliveryMonth(self):
        '''交割月'''
        return self.DeliveryMonth

    def getMaxLimitOrderVolume(self):
        '''限价单最大下单量'''
        return self.MaxLimitOrderVolume

    def getMinLimitOrderVolume(self):
        '''限价单最小下单量'''
        return self.MinLimitOrderVolume

    def getMaxMarketOrderVolume(self):
        '''市价单最大下单量'''
        return self.MaxMarketOrderVolume

    def getMinMarketOrderVolume(self):
        '''市价单最小下单量'''
        return self.MinMarketOrderVolume

    def getVolumeMultiple(self):
        '''数量乘数'''
        return self.VolumeMultiple

    def getPriceTick(self):
        '''报价单位'''
        return self.PriceTick

    def getCurrency(self):
        '''币种'''
        return TUstpFtdcCurrencyType(ord(self.Currency)) if ord(self.Currency) in [e.value for e in list(TUstpFtdcCurrencyType)] else list(TUstpFtdcCurrencyType)[0]

    def getLongPosLimit(self):
        '''多头限仓'''
        return self.LongPosLimit

    def getShortPosLimit(self):
        '''空头限仓'''
        return self.ShortPosLimit

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getPreSettlementPrice(self):
        '''昨结算'''
        return self.PreSettlementPrice

    def getInstrumentStatus(self):
        '''合约交易状态'''
        return TUstpFtdcInstrumentStatusType(ord(self.InstrumentStatus)) if ord(self.InstrumentStatus) in [e.value for e in list(TUstpFtdcInstrumentStatusType)] else list(TUstpFtdcInstrumentStatusType)[0]

    def getCreateDate(self):
        '''创建日'''
        return str(self.CreateDate, 'GBK')

    def getOpenDate(self):
        '''上市日'''
        return str(self.OpenDate, 'GBK')

    def getExpireDate(self):
        '''到期日'''
        return str(self.ExpireDate, 'GBK')

    def getStartDelivDate(self):
        '''开始交割日'''
        return str(self.StartDelivDate, 'GBK')

    def getEndDelivDate(self):
        '''最后交割日'''
        return str(self.EndDelivDate, 'GBK')

    def getBasisPrice(self):
        '''挂牌基准价'''
        return self.BasisPrice

    def getIsTrading(self):
        '''当前是否交易'''
        return self.IsTrading

    def getUnderlyingInstrID(self):
        '''基础商品代码'''
        return str(self.UnderlyingInstrID, 'GBK')

    def getUnderlyingMultiple(self):
        '''基础商品乘数'''
        return self.UnderlyingMultiple

    def getPositionType(self):
        '''持仓类型'''
        return TUstpFtdcPositionTypeType(ord(self.PositionType)) if ord(self.PositionType) in [e.value for e in list(TUstpFtdcPositionTypeType)] else list(TUstpFtdcPositionTypeType)[0]

    def getStrikePrice(self):
        '''执行价'''
        return self.StrikePrice

    def getOptionsType(self):
        '''期权类型'''
        return TUstpFtdcOptionsTypeType(ord(self.OptionsType)) if ord(self.OptionsType) in [e.value for e in list(TUstpFtdcOptionsTypeType)] else list(TUstpFtdcOptionsTypeType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getInstrumentID_1(self):
        '''第一腿合约代码'''
        return str(self.InstrumentID_1, 'GBK')

    def getDirection_1(self):
        '''第一腿买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction_1)) if ord(self.Direction_1) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getRatio_1(self):
        '''第一腿数量比例'''
        return self.Ratio_1

    def getInstrumentID_2(self):
        '''第二腿合约代码'''
        return str(self.InstrumentID_2, 'GBK')

    def getDirection_2(self):
        '''第二腿买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction_2)) if ord(self.Direction_2) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getRatio_2(self):
        '''第二腿数量比例'''
        return self.Ratio_2

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}, 'ProductName'={self.getProductName()}, 'InstrumentID'={self.getInstrumentID()}, 'InstrumentName'={self.getInstrumentName()}, 'DeliveryYear'={self.getDeliveryYear()}, 'DeliveryMonth'={self.getDeliveryMonth()}, 'MaxLimitOrderVolume'={self.getMaxLimitOrderVolume()}, 'MinLimitOrderVolume'={self.getMinLimitOrderVolume()}, 'MaxMarketOrderVolume'={self.getMaxMarketOrderVolume()}, 'MinMarketOrderVolume'={self.getMinMarketOrderVolume()}, 'VolumeMultiple'={self.getVolumeMultiple()}, 'PriceTick'={self.getPriceTick()}, 'Currency'={self.getCurrency()}, 'LongPosLimit'={self.getLongPosLimit()}, 'ShortPosLimit'={self.getShortPosLimit()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'InstrumentStatus'={self.getInstrumentStatus()}, 'CreateDate'={self.getCreateDate()}, 'OpenDate'={self.getOpenDate()}, 'ExpireDate'={self.getExpireDate()}, 'StartDelivDate'={self.getStartDelivDate()}, 'EndDelivDate'={self.getEndDelivDate()}, 'BasisPrice'={self.getBasisPrice()}, 'IsTrading'={self.getIsTrading()}, 'UnderlyingInstrID'={self.getUnderlyingInstrID()}, 'UnderlyingMultiple'={self.getUnderlyingMultiple()}, 'PositionType'={self.getPositionType()}, 'StrikePrice'={self.getStrikePrice()}, 'OptionsType'={self.getOptionsType()}, 'CurrencyID'={self.getCurrencyID()}, 'ArbiType'={self.getArbiType()}, 'InstrumentID_1'={self.getInstrumentID_1()}, 'Direction_1'={self.getDirection_1()}, 'Ratio_1'={self.getRatio_1()}, 'InstrumentID_2'={self.getInstrumentID_2()}, 'Direction_2'={self.getDirection_2()}, 'Ratio_2'={self.getRatio_2()}"


class CUstpFtdcInstrumentStatusField(Structure):
    """合约状态"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("ProductID", c_char * 13),
        ("ProductName", c_char * 41),
        ("InstrumentID", c_char * 31),
        ("InstrumentName", c_char * 21),
        ("DeliveryYear", c_int32),
        ("DeliveryMonth", c_int32),
        ("MaxLimitOrderVolume", c_int32),
        ("MinLimitOrderVolume", c_int32),
        ("MaxMarketOrderVolume", c_int32),
        ("MinMarketOrderVolume", c_int32),
        ("VolumeMultiple", c_int32),
        ("PriceTick", c_double),
        ("Currency", c_char),
        ("LongPosLimit", c_int32),
        ("ShortPosLimit", c_int32),
        ("LowerLimitPrice", c_double),
        ("UpperLimitPrice", c_double),
        ("PreSettlementPrice", c_double),
        ("InstrumentStatus", c_char),
        ("CreateDate", c_char * 9),
        ("OpenDate", c_char * 9),
        ("ExpireDate", c_char * 9),
        ("StartDelivDate", c_char * 9),
        ("EndDelivDate", c_char * 9),
        ("BasisPrice", c_double),
        ("IsTrading", c_int32),
        ("UnderlyingInstrID", c_char * 31),
        ("UnderlyingMultiple", c_int32),
        ("PositionType", c_char),
        ("StrikePrice", c_double),
        ("OptionsType", c_char),
        ("CurrencyID", c_char * 5),
        ("ArbiType", c_char),
        ("InstrumentID_1", c_char * 31),
        ("Direction_1", c_char),
        ("Ratio_1", c_double),
        ("InstrumentID_2", c_char * 31),
        ("Direction_2", c_char),
        ("Ratio_2", c_double),
        ("EnterDate", c_char * 9),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getProductID(self):
        '''品种代码'''
        return str(self.ProductID, 'GBK')

    def getProductName(self):
        '''品种名称'''
        return str(self.ProductName, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getInstrumentName(self):
        '''合约名称'''
        return str(self.InstrumentName, 'GBK')

    def getDeliveryYear(self):
        '''交割年份'''
        return self.DeliveryYear

    def getDeliveryMonth(self):
        '''交割月'''
        return self.DeliveryMonth

    def getMaxLimitOrderVolume(self):
        '''限价单最大下单量'''
        return self.MaxLimitOrderVolume

    def getMinLimitOrderVolume(self):
        '''限价单最小下单量'''
        return self.MinLimitOrderVolume

    def getMaxMarketOrderVolume(self):
        '''市价单最大下单量'''
        return self.MaxMarketOrderVolume

    def getMinMarketOrderVolume(self):
        '''市价单最小下单量'''
        return self.MinMarketOrderVolume

    def getVolumeMultiple(self):
        '''数量乘数'''
        return self.VolumeMultiple

    def getPriceTick(self):
        '''报价单位'''
        return self.PriceTick

    def getCurrency(self):
        '''币种'''
        return TUstpFtdcCurrencyType(ord(self.Currency)) if ord(self.Currency) in [e.value for e in list(TUstpFtdcCurrencyType)] else list(TUstpFtdcCurrencyType)[0]

    def getLongPosLimit(self):
        '''多头限仓'''
        return self.LongPosLimit

    def getShortPosLimit(self):
        '''空头限仓'''
        return self.ShortPosLimit

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getPreSettlementPrice(self):
        '''昨结算'''
        return self.PreSettlementPrice

    def getInstrumentStatus(self):
        '''合约交易状态'''
        return TUstpFtdcInstrumentStatusType(ord(self.InstrumentStatus)) if ord(self.InstrumentStatus) in [e.value for e in list(TUstpFtdcInstrumentStatusType)] else list(TUstpFtdcInstrumentStatusType)[0]

    def getCreateDate(self):
        '''创建日'''
        return str(self.CreateDate, 'GBK')

    def getOpenDate(self):
        '''上市日'''
        return str(self.OpenDate, 'GBK')

    def getExpireDate(self):
        '''到期日'''
        return str(self.ExpireDate, 'GBK')

    def getStartDelivDate(self):
        '''开始交割日'''
        return str(self.StartDelivDate, 'GBK')

    def getEndDelivDate(self):
        '''最后交割日'''
        return str(self.EndDelivDate, 'GBK')

    def getBasisPrice(self):
        '''挂牌基准价'''
        return self.BasisPrice

    def getIsTrading(self):
        '''当前是否交易'''
        return self.IsTrading

    def getUnderlyingInstrID(self):
        '''基础商品代码'''
        return str(self.UnderlyingInstrID, 'GBK')

    def getUnderlyingMultiple(self):
        '''基础商品乘数'''
        return self.UnderlyingMultiple

    def getPositionType(self):
        '''持仓类型'''
        return TUstpFtdcPositionTypeType(ord(self.PositionType)) if ord(self.PositionType) in [e.value for e in list(TUstpFtdcPositionTypeType)] else list(TUstpFtdcPositionTypeType)[0]

    def getStrikePrice(self):
        '''执行价'''
        return self.StrikePrice

    def getOptionsType(self):
        '''期权类型'''
        return TUstpFtdcOptionsTypeType(ord(self.OptionsType)) if ord(self.OptionsType) in [e.value for e in list(TUstpFtdcOptionsTypeType)] else list(TUstpFtdcOptionsTypeType)[0]

    def getCurrencyID(self):
        '''币种代码'''
        return str(self.CurrencyID, 'GBK')

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getInstrumentID_1(self):
        '''第一腿合约代码'''
        return str(self.InstrumentID_1, 'GBK')

    def getDirection_1(self):
        '''第一腿买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction_1)) if ord(self.Direction_1) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getRatio_1(self):
        '''第一腿数量比例'''
        return self.Ratio_1

    def getInstrumentID_2(self):
        '''第二腿合约代码'''
        return str(self.InstrumentID_2, 'GBK')

    def getDirection_2(self):
        '''第二腿买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction_2)) if ord(self.Direction_2) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getRatio_2(self):
        '''第二腿数量比例'''
        return self.Ratio_2

    def getEnterDate(self):
        '''进入本状态日期'''
        return str(self.EnterDate, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ProductID'={self.getProductID()}, 'ProductName'={self.getProductName()}, 'InstrumentID'={self.getInstrumentID()}, 'InstrumentName'={self.getInstrumentName()}, 'DeliveryYear'={self.getDeliveryYear()}, 'DeliveryMonth'={self.getDeliveryMonth()}, 'MaxLimitOrderVolume'={self.getMaxLimitOrderVolume()}, 'MinLimitOrderVolume'={self.getMinLimitOrderVolume()}, 'MaxMarketOrderVolume'={self.getMaxMarketOrderVolume()}, 'MinMarketOrderVolume'={self.getMinMarketOrderVolume()}, 'VolumeMultiple'={self.getVolumeMultiple()}, 'PriceTick'={self.getPriceTick()}, 'Currency'={self.getCurrency()}, 'LongPosLimit'={self.getLongPosLimit()}, 'ShortPosLimit'={self.getShortPosLimit()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'InstrumentStatus'={self.getInstrumentStatus()}, 'CreateDate'={self.getCreateDate()}, 'OpenDate'={self.getOpenDate()}, 'ExpireDate'={self.getExpireDate()}, 'StartDelivDate'={self.getStartDelivDate()}, 'EndDelivDate'={self.getEndDelivDate()}, 'BasisPrice'={self.getBasisPrice()}, 'IsTrading'={self.getIsTrading()}, 'UnderlyingInstrID'={self.getUnderlyingInstrID()}, 'UnderlyingMultiple'={self.getUnderlyingMultiple()}, 'PositionType'={self.getPositionType()}, 'StrikePrice'={self.getStrikePrice()}, 'OptionsType'={self.getOptionsType()}, 'CurrencyID'={self.getCurrencyID()}, 'ArbiType'={self.getArbiType()}, 'InstrumentID_1'={self.getInstrumentID_1()}, 'Direction_1'={self.getDirection_1()}, 'Ratio_1'={self.getRatio_1()}, 'InstrumentID_2'={self.getInstrumentID_2()}, 'Direction_2'={self.getDirection_2()}, 'Ratio_2'={self.getRatio_2()}, 'EnterDate'={self.getEnterDate()}"


class CUstpFtdcQryInvestorAccountField(Structure):
    """投资者资金查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}"


class CUstpFtdcRspInvestorAccountField(Structure):
    """投资者资金应答"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("AccountID", c_char * 13),
        ("PreBalance", c_double),
        ("Deposit", c_double),
        ("Withdraw", c_double),
        ("FrozenMargin", c_double),
        ("FrozenFee", c_double),
        ("FrozenPremium", c_double),
        ("Fee", c_double),
        ("CloseProfit", c_double),
        ("PositionProfit", c_double),
        ("Available", c_double),
        ("LongFrozenMargin", c_double),
        ("ShortFrozenMargin", c_double),
        ("LongMargin", c_double),
        ("ShortMargin", c_double),
        ("ReleaseMargin", c_double),
        ("DynamicRights", c_double),
        ("TodayInOut", c_double),
        ("Margin", c_double),
        ("Premium", c_double),
        ("Risk", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getAccountID(self):
        '''资金帐号'''
        return str(self.AccountID, 'GBK')

    def getPreBalance(self):
        '''上次结算准备金'''
        return self.PreBalance

    def getDeposit(self):
        '''入金金额'''
        return self.Deposit

    def getWithdraw(self):
        '''出金金额'''
        return self.Withdraw

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getFrozenFee(self):
        '''冻结手续费'''
        return self.FrozenFee

    def getFrozenPremium(self):
        '''冻结权利金'''
        return self.FrozenPremium

    def getFee(self):
        '''手续费'''
        return self.Fee

    def getCloseProfit(self):
        '''平仓盈亏'''
        return self.CloseProfit

    def getPositionProfit(self):
        '''持仓盈亏'''
        return self.PositionProfit

    def getAvailable(self):
        '''可用资金'''
        return self.Available

    def getLongFrozenMargin(self):
        '''多头冻结的保证金'''
        return self.LongFrozenMargin

    def getShortFrozenMargin(self):
        '''空头冻结的保证金'''
        return self.ShortFrozenMargin

    def getLongMargin(self):
        '''多头占用保证金'''
        return self.LongMargin

    def getShortMargin(self):
        '''空头占用保证金'''
        return self.ShortMargin

    def getReleaseMargin(self):
        '''当日释放保证金'''
        return self.ReleaseMargin

    def getDynamicRights(self):
        '''动态权益'''
        return self.DynamicRights

    def getTodayInOut(self):
        '''今日出入金'''
        return self.TodayInOut

    def getMargin(self):
        '''占用保证金'''
        return self.Margin

    def getPremium(self):
        '''期权权利金收支'''
        return self.Premium

    def getRisk(self):
        '''风险度'''
        return self.Risk

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'AccountID'={self.getAccountID()}, 'PreBalance'={self.getPreBalance()}, 'Deposit'={self.getDeposit()}, 'Withdraw'={self.getWithdraw()}, 'FrozenMargin'={self.getFrozenMargin()}, 'FrozenFee'={self.getFrozenFee()}, 'FrozenPremium'={self.getFrozenPremium()}, 'Fee'={self.getFee()}, 'CloseProfit'={self.getCloseProfit()}, 'PositionProfit'={self.getPositionProfit()}, 'Available'={self.getAvailable()}, 'LongFrozenMargin'={self.getLongFrozenMargin()}, 'ShortFrozenMargin'={self.getShortFrozenMargin()}, 'LongMargin'={self.getLongMargin()}, 'ShortMargin'={self.getShortMargin()}, 'ReleaseMargin'={self.getReleaseMargin()}, 'DynamicRights'={self.getDynamicRights()}, 'TodayInOut'={self.getTodayInOut()}, 'Margin'={self.getMargin()}, 'Premium'={self.getPremium()}, 'Risk'={self.getRisk()}"


class CUstpFtdcQryUserInvestorField(Structure):
    """可用投资者查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}"


class CUstpFtdcRspUserInvestorField(Structure):
    """可用投资者"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}"


class CUstpFtdcQryTradingCodeField(Structure):
    """交易编码查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcRspTradingCodeField(Structure):
    """交易编码查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("ClientID", c_char * 19),
        ("ClientRight", c_char),
        ("ClientHedgeFlag", c_char),
        ("IsActive", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getClientRight(self):
        '''客户编码权限'''
        return TUstpFtdcTradingRightType(ord(self.ClientRight)) if ord(self.ClientRight) in [e.value for e in list(TUstpFtdcTradingRightType)] else list(TUstpFtdcTradingRightType)[0]

    def getClientHedgeFlag(self):
        '''客户保值类型'''
        return TUstpFtdcHedgeFlagType(ord(self.ClientHedgeFlag)) if ord(self.ClientHedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getIsActive(self):
        '''是否活跃'''
        return TUstpFtdcIsActiveType(ord(self.IsActive)) if ord(self.IsActive) in [e.value for e in list(TUstpFtdcIsActiveType)] else list(TUstpFtdcIsActiveType)[0]

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'ClientID'={self.getClientID()}, 'ClientRight'={self.getClientRight()}, 'ClientHedgeFlag'={self.getClientHedgeFlag()}, 'IsActive'={self.getIsActive()}"


class CUstpFtdcQryExchangeField(Structure):
    """交易所查询请求"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}"


class CUstpFtdcRspExchangeField(Structure):
    """交易所查询应答"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("ExchangeName", c_char * 31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getExchangeName(self):
        '''交易所名称'''
        return str(self.ExchangeName, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'ExchangeName'={self.getExchangeName()}"


class CUstpFtdcQryInvestorPositionField(Structure):
    """投资者持仓查询请求"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("InstrumentID", c_char * 31),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'InstrumentID'={self.getInstrumentID()}"


class CUstpFtdcRspInvestorPositionField(Structure):
    """投资者持仓查询应答"""
    _fields_ = [
        ("InvestorID", c_char * 19),
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("ClientID", c_char * 19),
        ("InstrumentID", c_char * 31),
        ("Direction", c_char),
        ("HedgeFlag", c_char),
        ("UsedMargin", c_double),
        ("Position", c_int32),
        ("PositionCost", c_double),
        ("YdPosition", c_int32),
        ("YdPositionCost", c_double),
        ("FrozenMargin", c_double),
        ("FrozenPosition", c_int32),
        ("FrozenClosing", c_int32),
        ("YdFrozenClosing", c_int32),
        ("FrozenPremium", c_double),
        ("LastTradeID", c_char * 21),
        ("LastOrderLocalID", c_char * 13),
        ("SpeculationPosition", c_int32),
        ("ArbitragePosition", c_int32),
        ("HedgePosition", c_int32),
        ("SpecFrozenClosing", c_int32),
        ("HedgeFrozenClosing", c_int32),
        ("Currency", c_char * 5),
    ]

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getUsedMargin(self):
        '''优惠前占用保证金'''
        return self.UsedMargin

    def getPosition(self):
        '''今总持仓量'''
        return self.Position

    def getPositionCost(self):
        '''今日持仓成本'''
        return self.PositionCost

    def getYdPosition(self):
        '''昨持仓量'''
        return self.YdPosition

    def getYdPositionCost(self):
        '''昨日持仓成本'''
        return self.YdPositionCost

    def getFrozenMargin(self):
        '''冻结的保证金'''
        return self.FrozenMargin

    def getFrozenPosition(self):
        '''开仓冻结持仓'''
        return self.FrozenPosition

    def getFrozenClosing(self):
        '''平仓冻结持仓'''
        return self.FrozenClosing

    def getYdFrozenClosing(self):
        '''平昨仓冻结持仓'''
        return self.YdFrozenClosing

    def getFrozenPremium(self):
        '''冻结的权利金'''
        return self.FrozenPremium

    def getLastTradeID(self):
        '''最后一笔成交编号'''
        return str(self.LastTradeID, 'GBK')

    def getLastOrderLocalID(self):
        '''最后一笔本地报单编号'''
        return str(self.LastOrderLocalID, 'GBK')

    def getSpeculationPosition(self):
        '''投机持仓量'''
        return self.SpeculationPosition

    def getArbitragePosition(self):
        '''套利持仓量'''
        return self.ArbitragePosition

    def getHedgePosition(self):
        '''套保持仓量'''
        return self.HedgePosition

    def getSpecFrozenClosing(self):
        '''投机平仓冻结量'''
        return self.SpecFrozenClosing

    def getHedgeFrozenClosing(self):
        '''套保平仓冻结量'''
        return self.HedgeFrozenClosing

    def getCurrency(self):
        '''币种'''
        return str(self.Currency, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'InvestorID'={self.getInvestorID()}, 'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}, 'InstrumentID'={self.getInstrumentID()}, 'Direction'={self.getDirection()}, 'HedgeFlag'={self.getHedgeFlag()}, 'UsedMargin'={self.getUsedMargin()}, 'Position'={self.getPosition()}, 'PositionCost'={self.getPositionCost()}, 'YdPosition'={self.getYdPosition()}, 'YdPositionCost'={self.getYdPositionCost()}, 'FrozenMargin'={self.getFrozenMargin()}, 'FrozenPosition'={self.getFrozenPosition()}, 'FrozenClosing'={self.getFrozenClosing()}, 'YdFrozenClosing'={self.getYdFrozenClosing()}, 'FrozenPremium'={self.getFrozenPremium()}, 'LastTradeID'={self.getLastTradeID()}, 'LastOrderLocalID'={self.getLastOrderLocalID()}, 'SpeculationPosition'={self.getSpeculationPosition()}, 'ArbitragePosition'={self.getArbitragePosition()}, 'HedgePosition'={self.getHedgePosition()}, 'SpecFrozenClosing'={self.getSpecFrozenClosing()}, 'HedgeFrozenClosing'={self.getHedgeFrozenClosing()}, 'Currency'={self.getCurrency()}"


class CUstpFtdcQryComplianceParamField(Structure):
    """合规参数查询请求"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcRspComplianceParamField(Structure):
    """合规参数查询应答"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("ClientID", c_char * 19),
        ("DailyMaxOrder", c_int32),
        ("DailyMaxOrderAction", c_int32),
        ("DailyMaxErrorOrder", c_int32),
        ("DailyMaxOrderVolume", c_int32),
        ("DailyMaxOrderActionVolume", c_int32),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getDailyMaxOrder(self):
        '''每日最大报单笔'''
        return self.DailyMaxOrder

    def getDailyMaxOrderAction(self):
        '''每日最大撤单笔'''
        return self.DailyMaxOrderAction

    def getDailyMaxErrorOrder(self):
        '''每日最大错单笔'''
        return self.DailyMaxErrorOrder

    def getDailyMaxOrderVolume(self):
        '''每日最大报单手'''
        return self.DailyMaxOrderVolume

    def getDailyMaxOrderActionVolume(self):
        '''每日最大撤单手'''
        return self.DailyMaxOrderActionVolume

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'ClientID'={self.getClientID()}, 'DailyMaxOrder'={self.getDailyMaxOrder()}, 'DailyMaxOrderAction'={self.getDailyMaxOrderAction()}, 'DailyMaxErrorOrder'={self.getDailyMaxErrorOrder()}, 'DailyMaxOrderVolume'={self.getDailyMaxOrderVolume()}, 'DailyMaxOrderActionVolume'={self.getDailyMaxOrderActionVolume()}"


class CUstpFtdcQryUserField(Structure):
    """用户查询"""
    _fields_ = [
        ("StartUserID", c_char * 16),
        ("EndUserID", c_char * 16),
    ]

    def getStartUserID(self):
        '''交易用户代码'''
        return str(self.StartUserID, 'GBK')

    def getEndUserID(self):
        '''交易用户代码'''
        return str(self.EndUserID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'StartUserID'={self.getStartUserID()}, 'EndUserID'={self.getEndUserID()}"


class CUstpFtdcUserField(Structure):
    """用户"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("Password", c_char * 41),
        ("IsActive", c_char),
        ("UserName", c_char * 31),
        ("UserType", c_char),
        ("Department", c_char * 41),
        ("GrantFuncSet", c_char),
        ("SetUserID", c_char * 16),
        ("CommandDate", c_char * 9),
        ("CommandTime", c_char * 9),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getPassword(self):
        '''用户登录密码'''
        return str(self.Password, 'GBK')

    def getIsActive(self):
        '''是否活跃'''
        return TUstpFtdcIsActiveType(ord(self.IsActive)) if ord(self.IsActive) in [e.value for e in list(TUstpFtdcIsActiveType)] else list(TUstpFtdcIsActiveType)[0]

    def getUserName(self):
        '''用户名称'''
        return str(self.UserName, 'GBK')

    def getUserType(self):
        '''用户类型'''
        return TUstpFtdcUserTypeType(ord(self.UserType)) if ord(self.UserType) in [e.value for e in list(TUstpFtdcUserTypeType)] else list(TUstpFtdcUserTypeType)[0]

    def getDepartment(self):
        '''营业部'''
        return str(self.Department, 'GBK')

    def getGrantFuncSet(self):
        '''授权功能集'''
        return TUstpFtdcGrantFuncSetType(ord(self.GrantFuncSet)) if ord(self.GrantFuncSet) in [e.value for e in list(TUstpFtdcGrantFuncSetType)] else list(TUstpFtdcGrantFuncSetType)[0]

    def getSetUserID(self):
        '''修改用户编号'''
        return str(self.SetUserID, 'GBK')

    def getCommandDate(self):
        '''操作日期'''
        return str(self.CommandDate, 'GBK')

    def getCommandTime(self):
        '''操作时间'''
        return str(self.CommandTime, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'Password'={self.getPassword()}, 'IsActive'={self.getIsActive()}, 'UserName'={self.getUserName()}, 'UserType'={self.getUserType()}, 'Department'={self.getDepartment()}, 'GrantFuncSet'={self.getGrantFuncSet()}, 'SetUserID'={self.getSetUserID()}, 'CommandDate'={self.getCommandDate()}, 'CommandTime'={self.getCommandTime()}"


class CUstpFtdcQryInvestorFeeField(Structure):
    """投资者手续费率查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("InstrumentID", c_char * 31),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcInvestorFeeField(Structure):
    """投资者手续费率"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ClientID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("InstrumentID", c_char * 31),
        ("ProductID", c_char * 13),
        ("OpenFeeRate", c_double),
        ("OpenFeeAmt", c_double),
        ("OffsetFeeRate", c_double),
        ("OffsetFeeAmt", c_double),
        ("OTFeeRate", c_double),
        ("OTFeeAmt", c_double),
        ("ExecFeeRate", c_double),
        ("ExecFeeAmt", c_double),
        ("PerOrderAmt", c_double),
        ("PerCancelAmt", c_double),
        ("HedgeFlag", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getProductID(self):
        '''品种代码'''
        return str(self.ProductID, 'GBK')

    def getOpenFeeRate(self):
        '''开仓手续费按比例'''
        return self.OpenFeeRate

    def getOpenFeeAmt(self):
        '''开仓手续费按手数'''
        return self.OpenFeeAmt

    def getOffsetFeeRate(self):
        '''平仓手续费按比例'''
        return self.OffsetFeeRate

    def getOffsetFeeAmt(self):
        '''平仓手续费按手数'''
        return self.OffsetFeeAmt

    def getOTFeeRate(self):
        '''平今仓手续费按比例'''
        return self.OTFeeRate

    def getOTFeeAmt(self):
        '''平今仓手续费按手数'''
        return self.OTFeeAmt

    def getExecFeeRate(self):
        '''行权手续费按比例'''
        return self.ExecFeeRate

    def getExecFeeAmt(self):
        '''行权手续费按手数'''
        return self.ExecFeeAmt

    def getPerOrderAmt(self):
        '''每笔委托申报费'''
        return self.PerOrderAmt

    def getPerCancelAmt(self):
        '''每笔撤单申报费'''
        return self.PerCancelAmt

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ClientID'={self.getClientID()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}, 'ProductID'={self.getProductID()}, 'OpenFeeRate'={self.getOpenFeeRate()}, 'OpenFeeAmt'={self.getOpenFeeAmt()}, 'OffsetFeeRate'={self.getOffsetFeeRate()}, 'OffsetFeeAmt'={self.getOffsetFeeAmt()}, 'OTFeeRate'={self.getOTFeeRate()}, 'OTFeeAmt'={self.getOTFeeAmt()}, 'ExecFeeRate'={self.getExecFeeRate()}, 'ExecFeeAmt'={self.getExecFeeAmt()}, 'PerOrderAmt'={self.getPerOrderAmt()}, 'PerCancelAmt'={self.getPerCancelAmt()}, 'HedgeFlag'={self.getHedgeFlag()}"


class CUstpFtdcQryInvestorMarginField(Structure):
    """投资者保证金率查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("InstrumentID", c_char * 31),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcInvestorMarginField(Structure):
    """投资者保证金率"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ClientID", c_char * 19),
        ("ExchangeID", c_char * 11),
        ("InstrumentID", c_char * 31),
        ("ProductID", c_char * 13),
        ("LongMarginRate", c_double),
        ("LongMarginAmt", c_double),
        ("ShortMarginRate", c_double),
        ("ShortMarginAmt", c_double),
        ("HedgeFlag", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getProductID(self):
        '''品种代码'''
        return str(self.ProductID, 'GBK')

    def getLongMarginRate(self):
        '''多头占用保证金按比例'''
        return self.LongMarginRate

    def getLongMarginAmt(self):
        '''多头保证金按手数'''
        return self.LongMarginAmt

    def getShortMarginRate(self):
        '''空头占用保证金按比例'''
        return self.ShortMarginRate

    def getShortMarginAmt(self):
        '''空头保证金按手数'''
        return self.ShortMarginAmt

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ClientID'={self.getClientID()}, 'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}, 'ProductID'={self.getProductID()}, 'LongMarginRate'={self.getLongMarginRate()}, 'LongMarginAmt'={self.getLongMarginAmt()}, 'ShortMarginRate'={self.getShortMarginRate()}, 'ShortMarginAmt'={self.getShortMarginAmt()}, 'HedgeFlag'={self.getHedgeFlag()}"


class CUstpFtdcReqUserLoginField(Structure):
    """系统用户登录请求"""
    _fields_ = [
        ("TradingDay", c_char * 9),
        ("UserID", c_char * 16),
        ("BrokerID", c_char * 11),
        ("Password", c_char * 41),
        ("UserProductInfo", c_char * 41),
        ("InterfaceProductInfo", c_char * 41),
        ("ProtocolInfo", c_char * 41),
        ("IPAddress", c_char * 21),
        ("MacAddress", c_char * 21),
        ("DataCenterID", c_int32),
        ("UserProductFileSize", c_int32),
        ("Authenticate2Type", c_char),
        ("Authenticate2Password", c_char * 41),
        ("TerminalCode", c_char * 41),
        ("PasswordEncrypt", c_char * 3),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getPassword(self):
        '''密码'''
        return str(self.Password, 'GBK')

    def getUserProductInfo(self):
        '''用户端产品信息'''
        return str(self.UserProductInfo, 'GBK')

    def getInterfaceProductInfo(self):
        '''接口端产品信息'''
        return str(self.InterfaceProductInfo, 'GBK')

    def getProtocolInfo(self):
        '''协议信息'''
        return str(self.ProtocolInfo, 'GBK')

    def getIPAddress(self):
        '''IP地址'''
        return str(self.IPAddress, 'GBK')

    def getMacAddress(self):
        '''Mac地址'''
        return str(self.MacAddress, 'GBK')

    def getDataCenterID(self):
        '''数据中心代码'''
        return self.DataCenterID

    def getUserProductFileSize(self):
        '''客户端运行文件大小'''
        return self.UserProductFileSize

    def getAuthenticate2Type(self):
        '''客户认证类型'''
        return TUstpFtdcAuthenticate2TypeType(ord(self.Authenticate2Type)) if ord(self.Authenticate2Type) in [e.value for e in list(TUstpFtdcAuthenticate2TypeType)] else list(TUstpFtdcAuthenticate2TypeType)[0]

    def getAuthenticate2Password(self):
        '''客户认证密码'''
        return str(self.Authenticate2Password, 'GBK')

    def getTerminalCode(self):
        '''开发厂商终端编码'''
        return str(self.TerminalCode, 'GBK')

    def getPasswordEncrypt(self):
        '''密码加密类型'''
        return str(self.PasswordEncrypt, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'UserID'={self.getUserID()}, 'BrokerID'={self.getBrokerID()}, 'Password'={self.getPassword()}, 'UserProductInfo'={self.getUserProductInfo()}, 'InterfaceProductInfo'={self.getInterfaceProductInfo()}, 'ProtocolInfo'={self.getProtocolInfo()}, 'IPAddress'={self.getIPAddress()}, 'MacAddress'={self.getMacAddress()}, 'DataCenterID'={self.getDataCenterID()}, 'UserProductFileSize'={self.getUserProductFileSize()}, 'Authenticate2Type'={self.getAuthenticate2Type()}, 'Authenticate2Password'={self.getAuthenticate2Password()}, 'TerminalCode'={self.getTerminalCode()}, 'PasswordEncrypt'={self.getPasswordEncrypt()}"


class CUstpFtdcstpUserDepositField(Structure):
    """用户请求出入金"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("Amount", c_double),
        ("AmountDirection", c_char),
        ("UserOrderLocalID", c_char * 21),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getAmount(self):
        '''金额'''
        return self.Amount

    def getAmountDirection(self):
        '''出入金方向'''
        return TUstpFtdcAccountDirectionType(ord(self.AmountDirection)) if ord(self.AmountDirection) in [e.value for e in list(TUstpFtdcAccountDirectionType)] else list(TUstpFtdcAccountDirectionType)[0]

    def getUserOrderLocalID(self):
        '''用户本地报单号'''
        return str(self.UserOrderLocalID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'Amount'={self.getAmount()}, 'AmountDirection'={self.getAmountDirection()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}"


class CUstpFtdcstpTransferMoneyField(Structure):
    """用户主次席出入金"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("Amount", c_double),
        ("AmountDirection", c_char),
        ("UserOrderLocalID", c_char * 21),
        ("BankID", c_char * 11),
        ("BankPasswd", c_char * 36),
        ("AccountPasswd", c_char * 36),
        ("Currency", c_char * 5),
        ("SerialNo", c_char * 34),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getAmount(self):
        '''金额'''
        return self.Amount

    def getAmountDirection(self):
        '''出入金方向'''
        return TUstpFtdcAccountDirectionType(ord(self.AmountDirection)) if ord(self.AmountDirection) in [e.value for e in list(TUstpFtdcAccountDirectionType)] else list(TUstpFtdcAccountDirectionType)[0]

    def getUserOrderLocalID(self):
        '''用户本地报单号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getBankID(self):
        '''银行机构代码'''
        return str(self.BankID, 'GBK')

    def getBankPasswd(self):
        '''银行转账密码'''
        return str(self.BankPasswd, 'GBK')

    def getAccountPasswd(self):
        '''主席转账密码'''
        return str(self.AccountPasswd, 'GBK')

    def getCurrency(self):
        '''币种'''
        return str(self.Currency, 'GBK')

    def getSerialNo(self):
        '''次席资金流水号'''
        return str(self.SerialNo, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'Amount'={self.getAmount()}, 'AmountDirection'={self.getAmountDirection()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'BankID'={self.getBankID()}, 'BankPasswd'={self.getBankPasswd()}, 'AccountPasswd'={self.getAccountPasswd()}, 'Currency'={self.getCurrency()}, 'SerialNo'={self.getSerialNo()}"


class CUstpFtdcTradeField(Structure):
    """成交"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("TradingDay", c_char * 9),
        ("ParticipantID", c_char * 11),
        ("SeatID", c_char * 13),
        ("InvestorID", c_char * 19),
        ("ClientID", c_char * 19),
        ("UserID", c_char * 16),
        ("OrderUserID", c_char * 16),
        ("TradeID", c_char * 21),
        ("OrderSysID", c_char * 31),
        ("UserOrderLocalID", c_char * 21),
        ("InstrumentID", c_char * 31),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("TradePrice", c_double),
        ("TradeVolume", c_int32),
        ("TradeTime", c_char * 9),
        ("ClearingPartID", c_char * 11),
        ("UsedFee", c_double),
        ("UsedMargin", c_double),
        ("Premium", c_double),
        ("Position", c_int32),
        ("PositionCost", c_double),
        ("Available", c_double),
        ("Margin", c_double),
        ("FrozenMargin", c_double),
        ("BusinessLocalID", c_int32),
        ("ActionDay", c_char * 9),
        ("ArbiType", c_char),
        ("ArbiInstrumentID", c_char * 31),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getParticipantID(self):
        '''会员编号'''
        return str(self.ParticipantID, 'GBK')

    def getSeatID(self):
        '''下单席位号'''
        return str(self.SeatID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getUserID(self):
        '''用户编号'''
        return str(self.UserID, 'GBK')

    def getOrderUserID(self):
        '''下单用户编号'''
        return str(self.OrderUserID, 'GBK')

    def getTradeID(self):
        '''成交编号'''
        return str(self.TradeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getUserOrderLocalID(self):
        '''本地报单编号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getOffsetFlag(self):
        '''开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getTradePrice(self):
        '''成交价格'''
        return self.TradePrice

    def getTradeVolume(self):
        '''成交数量'''
        return self.TradeVolume

    def getTradeTime(self):
        '''成交时间'''
        return str(self.TradeTime, 'GBK')

    def getClearingPartID(self):
        '''清算会员编号'''
        return str(self.ClearingPartID, 'GBK')

    def getUsedFee(self):
        '''本次成交手续费'''
        return self.UsedFee

    def getUsedMargin(self):
        '''本次成交占用保证金'''
        return self.UsedMargin

    def getPremium(self):
        '''本次成交占用权利金'''
        return self.Premium

    def getPosition(self):
        '''持仓表今持仓量'''
        return self.Position

    def getPositionCost(self):
        '''持仓表今日持仓成本'''
        return self.PositionCost

    def getAvailable(self):
        '''资金表可用资金'''
        return self.Available

    def getMargin(self):
        '''资金表占用保证金'''
        return self.Margin

    def getFrozenMargin(self):
        '''资金表冻结的保证金'''
        return self.FrozenMargin

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getArbiInstrumentID(self):
        '''套利组合合约'''
        return str(self.ArbiInstrumentID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'TradingDay'={self.getTradingDay()}, 'ParticipantID'={self.getParticipantID()}, 'SeatID'={self.getSeatID()}, 'InvestorID'={self.getInvestorID()}, 'ClientID'={self.getClientID()}, 'UserID'={self.getUserID()}, 'OrderUserID'={self.getOrderUserID()}, 'TradeID'={self.getTradeID()}, 'OrderSysID'={self.getOrderSysID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'InstrumentID'={self.getInstrumentID()}, 'Direction'={self.getDirection()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'TradePrice'={self.getTradePrice()}, 'TradeVolume'={self.getTradeVolume()}, 'TradeTime'={self.getTradeTime()}, 'ClearingPartID'={self.getClearingPartID()}, 'UsedFee'={self.getUsedFee()}, 'UsedMargin'={self.getUsedMargin()}, 'Premium'={self.getPremium()}, 'Position'={self.getPosition()}, 'PositionCost'={self.getPositionCost()}, 'Available'={self.getAvailable()}, 'Margin'={self.getMargin()}, 'FrozenMargin'={self.getFrozenMargin()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'ActionDay'={self.getActionDay()}, 'ArbiType'={self.getArbiType()}, 'ArbiInstrumentID'={self.getArbiInstrumentID()}"


class CUstpFtdcOrderField(Structure):
    """报单"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("OrderSysID", c_char * 31),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("SeatNo", c_int32),
        ("InstrumentID", c_char * 31),
        ("UserOrderLocalID", c_char * 21),
        ("OrderPriceType", c_char),
        ("Direction", c_char),
        ("OffsetFlag", c_char),
        ("HedgeFlag", c_char),
        ("LimitPrice", c_double),
        ("Volume", c_int32),
        ("TimeCondition", c_char),
        ("GTDDate", c_char * 9),
        ("VolumeCondition", c_char),
        ("MinVolume", c_int32),
        ("StopPrice", c_double),
        ("ForceCloseReason", c_char),
        ("IsAutoSuspend", c_int32),
        ("BusinessUnit", c_char * 21),
        ("UserCustom", c_char * 65),
        ("BusinessLocalID", c_int32),
        ("ActionDay", c_char * 9),
        ("ArbiType", c_char),
        ("TradingDay", c_char * 9),
        ("ParticipantID", c_char * 11),
        ("OrderUserID", c_char * 16),
        ("ClientID", c_char * 19),
        ("SeatID", c_char * 13),
        ("InsertTime", c_char * 9),
        ("OrderLocalID", c_char * 13),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("CancelTime", c_char * 9),
        ("CancelUserID", c_char * 16),
        ("VolumeTraded", c_int32),
        ("VolumeRemain", c_int32),
        ("OrderType", c_char),
        ("DeliveryFlag", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getSeatNo(self):
        '''指定通过此席位序号下单'''
        return self.SeatNo

    def getInstrumentID(self):
        '''合约代码/套利组合合约号'''
        return str(self.InstrumentID, 'GBK')

    def getUserOrderLocalID(self):
        '''用户本地报单号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getOrderPriceType(self):
        '''报单类型'''
        return TUstpFtdcOrderPriceTypeType(ord(self.OrderPriceType)) if ord(self.OrderPriceType) in [e.value for e in list(TUstpFtdcOrderPriceTypeType)] else list(TUstpFtdcOrderPriceTypeType)[0]

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getOffsetFlag(self):
        '''开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.OffsetFlag)) if ord(self.OffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getLimitPrice(self):
        '''价格'''
        return self.LimitPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTimeCondition(self):
        '''有效期类型'''
        return TUstpFtdcTimeConditionType(ord(self.TimeCondition)) if ord(self.TimeCondition) in [e.value for e in list(TUstpFtdcTimeConditionType)] else list(TUstpFtdcTimeConditionType)[0]

    def getGTDDate(self):
        '''GTD日期'''
        return str(self.GTDDate, 'GBK')

    def getVolumeCondition(self):
        '''成交量类型'''
        return TUstpFtdcVolumeConditionType(ord(self.VolumeCondition)) if ord(self.VolumeCondition) in [e.value for e in list(TUstpFtdcVolumeConditionType)] else list(TUstpFtdcVolumeConditionType)[0]

    def getMinVolume(self):
        '''最小成交量'''
        return self.MinVolume

    def getStopPrice(self):
        '''止损价止赢价'''
        return self.StopPrice

    def getForceCloseReason(self):
        '''强平原因'''
        return TUstpFtdcForceCloseReasonType(ord(self.ForceCloseReason)) if ord(self.ForceCloseReason) in [e.value for e in list(TUstpFtdcForceCloseReasonType)] else list(TUstpFtdcForceCloseReasonType)[0]

    def getIsAutoSuspend(self):
        '''自动挂起标志'''
        return self.IsAutoSuspend

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getParticipantID(self):
        '''会员编号'''
        return str(self.ParticipantID, 'GBK')

    def getOrderUserID(self):
        '''最初下单用户编号'''
        return str(self.OrderUserID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getSeatID(self):
        '''下单席位号'''
        return str(self.SeatID, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getOrderSource(self):
        '''报单来源'''
        return TUstpFtdcOrderSourceType(ord(self.OrderSource)) if ord(self.OrderSource) in [e.value for e in list(TUstpFtdcOrderSourceType)] else list(TUstpFtdcOrderSourceType)[0]

    def getOrderStatus(self):
        '''报单状态'''
        return TUstpFtdcOrderStatusType(ord(self.OrderStatus)) if ord(self.OrderStatus) in [e.value for e in list(TUstpFtdcOrderStatusType)] else list(TUstpFtdcOrderStatusType)[0]

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getCancelUserID(self):
        '''撤单用户编号'''
        return str(self.CancelUserID, 'GBK')

    def getVolumeTraded(self):
        '''今成交数量'''
        return self.VolumeTraded

    def getVolumeRemain(self):
        '''剩余数量'''
        return self.VolumeRemain

    def getOrderType(self):
        '''委托类型'''
        return TUstpFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TUstpFtdcOrderTypeType)] else list(TUstpFtdcOrderTypeType)[0]

    def getDeliveryFlag(self):
        '''期权对冲标识'''
        return TUstpFtdcDeliveryFlagType(ord(self.DeliveryFlag)) if ord(self.DeliveryFlag) in [e.value for e in list(TUstpFtdcDeliveryFlagType)] else list(TUstpFtdcDeliveryFlagType)[0]

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'SeatNo'={self.getSeatNo()}, 'InstrumentID'={self.getInstrumentID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'OrderPriceType'={self.getOrderPriceType()}, 'Direction'={self.getDirection()}, 'OffsetFlag'={self.getOffsetFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LimitPrice'={self.getLimitPrice()}, 'Volume'={self.getVolume()}, 'TimeCondition'={self.getTimeCondition()}, 'GTDDate'={self.getGTDDate()}, 'VolumeCondition'={self.getVolumeCondition()}, 'MinVolume'={self.getMinVolume()}, 'StopPrice'={self.getStopPrice()}, 'ForceCloseReason'={self.getForceCloseReason()}, 'IsAutoSuspend'={self.getIsAutoSuspend()}, 'BusinessUnit'={self.getBusinessUnit()}, 'UserCustom'={self.getUserCustom()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'ActionDay'={self.getActionDay()}, 'ArbiType'={self.getArbiType()}, 'TradingDay'={self.getTradingDay()}, 'ParticipantID'={self.getParticipantID()}, 'OrderUserID'={self.getOrderUserID()}, 'ClientID'={self.getClientID()}, 'SeatID'={self.getSeatID()}, 'InsertTime'={self.getInsertTime()}, 'OrderLocalID'={self.getOrderLocalID()}, 'OrderSource'={self.getOrderSource()}, 'OrderStatus'={self.getOrderStatus()}, 'CancelTime'={self.getCancelTime()}, 'CancelUserID'={self.getCancelUserID()}, 'VolumeTraded'={self.getVolumeTraded()}, 'VolumeRemain'={self.getVolumeRemain()}, 'OrderType'={self.getOrderType()}, 'DeliveryFlag'={self.getDeliveryFlag()}"


class CUstpFtdcFlowMessageCancelField(Structure):
    """数据流回退"""
    _fields_ = [
        ("SequenceSeries", c_int32),
        ("TradingDay", c_char * 9),
        ("DataCenterID", c_int32),
        ("StartSequenceNo", c_int32),
        ("EndSequenceNo", c_int32),
    ]

    def getSequenceSeries(self):
        '''序列系列号'''
        return self.SequenceSeries

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getDataCenterID(self):
        '''数据中心代码'''
        return self.DataCenterID

    def getStartSequenceNo(self):
        '''回退起始序列号'''
        return self.StartSequenceNo

    def getEndSequenceNo(self):
        '''回退结束序列号'''
        return self.EndSequenceNo

    def __str__(self):  # 可以直接print
        return f"'SequenceSeries'={self.getSequenceSeries()}, 'TradingDay'={self.getTradingDay()}, 'DataCenterID'={self.getDataCenterID()}, 'StartSequenceNo'={self.getStartSequenceNo()}, 'EndSequenceNo'={self.getEndSequenceNo()}"


class CUstpFtdcDisseminationField(Structure):
    """信息分发"""
    _fields_ = [
        ("SequenceSeries", c_int32),
        ("SequenceNo", c_int32),
    ]

    def getSequenceSeries(self):
        '''序列系列号'''
        return self.SequenceSeries

    def getSequenceNo(self):
        '''序列号'''
        return self.SequenceNo

    def __str__(self):  # 可以直接print
        return f"'SequenceSeries'={self.getSequenceSeries()}, 'SequenceNo'={self.getSequenceNo()}"


class CUstpFtdcInvestorAccountDepositResField(Structure):
    """出入金结果"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("AccountID", c_char * 13),
        ("AccountSeqNo", c_char * 21),
        ("Amount", c_double),
        ("AmountDirection", c_char),
        ("Available", c_double),
        ("Balance", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getAccountID(self):
        '''资金帐号'''
        return str(self.AccountID, 'GBK')

    def getAccountSeqNo(self):
        '''资金流水号'''
        return str(self.AccountSeqNo, 'GBK')

    def getAmount(self):
        '''金额'''
        return self.Amount

    def getAmountDirection(self):
        '''出入金方向'''
        return TUstpFtdcAccountDirectionType(ord(self.AmountDirection)) if ord(self.AmountDirection) in [e.value for e in list(TUstpFtdcAccountDirectionType)] else list(TUstpFtdcAccountDirectionType)[0]

    def getAvailable(self):
        '''可用资金'''
        return self.Available

    def getBalance(self):
        '''结算准备金'''
        return self.Balance

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'AccountID'={self.getAccountID()}, 'AccountSeqNo'={self.getAccountSeqNo()}, 'Amount'={self.getAmount()}, 'AmountDirection'={self.getAmountDirection()}, 'Available'={self.getAvailable()}, 'Balance'={self.getBalance()}"


class CUstpFtdcInputQuoteField(Structure):
    """报价录入"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("InstrumentID", c_char * 31),
        ("Direction", c_char),
        ("QuoteSysID", c_char * 31),
        ("UserQuoteLocalID", c_char * 21),
        ("QuoteLocalID", c_char * 13),
        ("BidVolume", c_int32),
        ("BidOffsetFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("BidPrice", c_double),
        ("AskVolume", c_int32),
        ("AskOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("AskPrice", c_double),
        ("BusinessUnit", c_char * 21),
        ("UserCustom", c_char * 65),
        ("BidUserOrderLocalID", c_char * 21),
        ("AskUserOrderLocalID", c_char * 21),
        ("BidOrderLocalID", c_char * 13),
        ("AskOrderLocalID", c_char * 13),
        ("ReqForQuoteID", c_char * 31),
        ("StandByTime", c_int32),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getQuoteSysID(self):
        '''交易系统返回的系统报价编号'''
        return str(self.QuoteSysID, 'GBK')

    def getUserQuoteLocalID(self):
        '''用户设定的本地报价编号'''
        return str(self.UserQuoteLocalID, 'GBK')

    def getQuoteLocalID(self):
        '''飞马向交易系统报的本地报价编号'''
        return str(self.QuoteLocalID, 'GBK')

    def getBidVolume(self):
        '''买方买入数量'''
        return self.BidVolume

    def getBidOffsetFlag(self):
        '''买方开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.BidOffsetFlag)) if ord(self.BidOffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getBidHedgeFlag(self):
        '''买方投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.BidHedgeFlag)) if ord(self.BidHedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getBidPrice(self):
        '''买方买入价格'''
        return self.BidPrice

    def getAskVolume(self):
        '''卖方卖出数量'''
        return self.AskVolume

    def getAskOffsetFlag(self):
        '''卖方开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.AskOffsetFlag)) if ord(self.AskOffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getAskHedgeFlag(self):
        '''卖方投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.AskHedgeFlag)) if ord(self.AskHedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getAskPrice(self):
        '''卖方卖出价格'''
        return self.AskPrice

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getBidUserOrderLocalID(self):
        '''拆分出来的买方用户本地报单编号'''
        return str(self.BidUserOrderLocalID, 'GBK')

    def getAskUserOrderLocalID(self):
        '''拆分出来的卖方用户本地报单编号'''
        return str(self.AskUserOrderLocalID, 'GBK')

    def getBidOrderLocalID(self):
        '''拆分出来的买方本地报单编号'''
        return str(self.BidOrderLocalID, 'GBK')

    def getAskOrderLocalID(self):
        '''拆分出来的卖方本地报单编号'''
        return str(self.AskOrderLocalID, 'GBK')

    def getReqForQuoteID(self):
        '''询价编号'''
        return str(self.ReqForQuoteID, 'GBK')

    def getStandByTime(self):
        '''报价停留时间(秒)'''
        return self.StandByTime

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'InstrumentID'={self.getInstrumentID()}, 'Direction'={self.getDirection()}, 'QuoteSysID'={self.getQuoteSysID()}, 'UserQuoteLocalID'={self.getUserQuoteLocalID()}, 'QuoteLocalID'={self.getQuoteLocalID()}, 'BidVolume'={self.getBidVolume()}, 'BidOffsetFlag'={self.getBidOffsetFlag()}, 'BidHedgeFlag'={self.getBidHedgeFlag()}, 'BidPrice'={self.getBidPrice()}, 'AskVolume'={self.getAskVolume()}, 'AskOffsetFlag'={self.getAskOffsetFlag()}, 'AskHedgeFlag'={self.getAskHedgeFlag()}, 'AskPrice'={self.getAskPrice()}, 'BusinessUnit'={self.getBusinessUnit()}, 'UserCustom'={self.getUserCustom()}, 'BidUserOrderLocalID'={self.getBidUserOrderLocalID()}, 'AskUserOrderLocalID'={self.getAskUserOrderLocalID()}, 'BidOrderLocalID'={self.getBidOrderLocalID()}, 'AskOrderLocalID'={self.getAskOrderLocalID()}, 'ReqForQuoteID'={self.getReqForQuoteID()}, 'StandByTime'={self.getStandByTime()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcRtnQuoteField(Structure):
    """报价通知"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("InstrumentID", c_char * 31),
        ("Direction", c_char),
        ("QuoteSysID", c_char * 31),
        ("UserQuoteLocalID", c_char * 21),
        ("QuoteLocalID", c_char * 13),
        ("BidVolume", c_int32),
        ("BidOffsetFlag", c_char),
        ("BidHedgeFlag", c_char),
        ("BidPrice", c_double),
        ("AskVolume", c_int32),
        ("AskOffsetFlag", c_char),
        ("AskHedgeFlag", c_char),
        ("AskPrice", c_double),
        ("BusinessUnit", c_char * 21),
        ("UserCustom", c_char * 65),
        ("BidUserOrderLocalID", c_char * 21),
        ("AskUserOrderLocalID", c_char * 21),
        ("BidOrderLocalID", c_char * 13),
        ("AskOrderLocalID", c_char * 13),
        ("ReqForQuoteID", c_char * 31),
        ("StandByTime", c_int32),
        ("BidOrderSysID", c_char * 31),
        ("AskOrderSysID", c_char * 31),
        ("QuoteStatus", c_char),
        ("InsertTime", c_char * 9),
        ("CancelTime", c_char * 9),
        ("TradeTime", c_char * 9),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getQuoteSysID(self):
        '''交易系统返回的系统报价编号'''
        return str(self.QuoteSysID, 'GBK')

    def getUserQuoteLocalID(self):
        '''用户设定的本地报价编号'''
        return str(self.UserQuoteLocalID, 'GBK')

    def getQuoteLocalID(self):
        '''飞马向交易系统报的本地报价编号'''
        return str(self.QuoteLocalID, 'GBK')

    def getBidVolume(self):
        '''买方买入数量'''
        return self.BidVolume

    def getBidOffsetFlag(self):
        '''买方开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.BidOffsetFlag)) if ord(self.BidOffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getBidHedgeFlag(self):
        '''买方投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.BidHedgeFlag)) if ord(self.BidHedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getBidPrice(self):
        '''买方买入价格'''
        return self.BidPrice

    def getAskVolume(self):
        '''卖方卖出数量'''
        return self.AskVolume

    def getAskOffsetFlag(self):
        '''卖方开平标志'''
        return TUstpFtdcOffsetFlagType(ord(self.AskOffsetFlag)) if ord(self.AskOffsetFlag) in [e.value for e in list(TUstpFtdcOffsetFlagType)] else list(TUstpFtdcOffsetFlagType)[0]

    def getAskHedgeFlag(self):
        '''卖方投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.AskHedgeFlag)) if ord(self.AskHedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getAskPrice(self):
        '''卖方卖出价格'''
        return self.AskPrice

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getBidUserOrderLocalID(self):
        '''拆分出来的买方用户本地报单编号'''
        return str(self.BidUserOrderLocalID, 'GBK')

    def getAskUserOrderLocalID(self):
        '''拆分出来的卖方用户本地报单编号'''
        return str(self.AskUserOrderLocalID, 'GBK')

    def getBidOrderLocalID(self):
        '''拆分出来的买方本地报单编号'''
        return str(self.BidOrderLocalID, 'GBK')

    def getAskOrderLocalID(self):
        '''拆分出来的卖方本地报单编号'''
        return str(self.AskOrderLocalID, 'GBK')

    def getReqForQuoteID(self):
        '''询价编号'''
        return str(self.ReqForQuoteID, 'GBK')

    def getStandByTime(self):
        '''报价停留时间(秒)'''
        return self.StandByTime

    def getBidOrderSysID(self):
        '''买方系统报单编号'''
        return str(self.BidOrderSysID, 'GBK')

    def getAskOrderSysID(self):
        '''卖方系统报单编号'''
        return str(self.AskOrderSysID, 'GBK')

    def getQuoteStatus(self):
        '''报价单状态'''
        return TUstpFtdcQuoteStatusType(ord(self.QuoteStatus)) if ord(self.QuoteStatus) in [e.value for e in list(TUstpFtdcQuoteStatusType)] else list(TUstpFtdcQuoteStatusType)[0]

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getTradeTime(self):
        '''成交时间'''
        return str(self.TradeTime, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'InstrumentID'={self.getInstrumentID()}, 'Direction'={self.getDirection()}, 'QuoteSysID'={self.getQuoteSysID()}, 'UserQuoteLocalID'={self.getUserQuoteLocalID()}, 'QuoteLocalID'={self.getQuoteLocalID()}, 'BidVolume'={self.getBidVolume()}, 'BidOffsetFlag'={self.getBidOffsetFlag()}, 'BidHedgeFlag'={self.getBidHedgeFlag()}, 'BidPrice'={self.getBidPrice()}, 'AskVolume'={self.getAskVolume()}, 'AskOffsetFlag'={self.getAskOffsetFlag()}, 'AskHedgeFlag'={self.getAskHedgeFlag()}, 'AskPrice'={self.getAskPrice()}, 'BusinessUnit'={self.getBusinessUnit()}, 'UserCustom'={self.getUserCustom()}, 'BidUserOrderLocalID'={self.getBidUserOrderLocalID()}, 'AskUserOrderLocalID'={self.getAskUserOrderLocalID()}, 'BidOrderLocalID'={self.getBidOrderLocalID()}, 'AskOrderLocalID'={self.getAskOrderLocalID()}, 'ReqForQuoteID'={self.getReqForQuoteID()}, 'StandByTime'={self.getStandByTime()}, 'BidOrderSysID'={self.getBidOrderSysID()}, 'AskOrderSysID'={self.getAskOrderSysID()}, 'QuoteStatus'={self.getQuoteStatus()}, 'InsertTime'={self.getInsertTime()}, 'CancelTime'={self.getCancelTime()}, 'TradeTime'={self.getTradeTime()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcQuoteActionField(Structure):
    """报价操作"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("QuoteSysID", c_char * 31),
        ("UserQuoteLocalID", c_char * 21),
        ("UserQuoteActionLocalID", c_char * 21),
        ("ActionFlag", c_char),
        ("BusinessUnit", c_char * 21),
        ("UserCustom", c_char * 65),
        ("Direction", c_char),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getQuoteSysID(self):
        '''交易系统返回的系统报价编号'''
        return str(self.QuoteSysID, 'GBK')

    def getUserQuoteLocalID(self):
        '''用户设定的被撤的本地报价编号'''
        return str(self.UserQuoteLocalID, 'GBK')

    def getUserQuoteActionLocalID(self):
        '''用户向飞马报的本地撤消报价编号'''
        return str(self.UserQuoteActionLocalID, 'GBK')

    def getActionFlag(self):
        '''报单操作标志'''
        return TUstpFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TUstpFtdcActionFlagType)] else list(TUstpFtdcActionFlagType)[0]

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'QuoteSysID'={self.getQuoteSysID()}, 'UserQuoteLocalID'={self.getUserQuoteLocalID()}, 'UserQuoteActionLocalID'={self.getUserQuoteActionLocalID()}, 'ActionFlag'={self.getActionFlag()}, 'BusinessUnit'={self.getBusinessUnit()}, 'UserCustom'={self.getUserCustom()}, 'Direction'={self.getDirection()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcReqForQuoteField(Structure):
    """询价请求"""
    _fields_ = [
        ("ReqForQuoteID", c_char * 31),
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("InstrumentID", c_char * 31),
        ("Direction", c_char),
        ("TradingDay", c_char * 9),
        ("ReqForQuoteTime", c_char * 9),
        ("ClientID", c_char * 19),
    ]

    def getReqForQuoteID(self):
        '''询价编号'''
        return str(self.ReqForQuoteID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getReqForQuoteTime(self):
        '''询价时间'''
        return str(self.ReqForQuoteTime, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ReqForQuoteID'={self.getReqForQuoteID()}, 'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'InstrumentID'={self.getInstrumentID()}, 'Direction'={self.getDirection()}, 'TradingDay'={self.getTradingDay()}, 'ReqForQuoteTime'={self.getReqForQuoteTime()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcSyncMoneyTransferField(Structure):
    """资金同步通知"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("AccountID", c_char * 13),
        ("BankID", c_char * 10),
        ("BankAccount", c_char * 34),
        ("Currency", c_char * 5),
        ("Amount", c_double),
        ("SyncTransMoneyEvent", c_char),
        ("TradeCode", c_char * 10),
        ("TradeSource", c_char),
        ("TransSerialNo", c_char * 34),
        ("SerialNo", c_char * 34),
        ("UserID", c_char * 16),
        ("CommandDate", c_char * 9),
        ("CommandTime", c_char * 9),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getAccountID(self):
        '''资金帐号'''
        return str(self.AccountID, 'GBK')

    def getBankID(self):
        '''银行代码'''
        return str(self.BankID, 'GBK')

    def getBankAccount(self):
        '''银行帐号'''
        return str(self.BankAccount, 'GBK')

    def getCurrency(self):
        '''币种'''
        return str(self.Currency, 'GBK')

    def getAmount(self):
        '''金额'''
        return self.Amount

    def getSyncTransMoneyEvent(self):
        '''出入金事件通知'''
        return TUstpFtdcSyncDirectionType(ord(self.SyncTransMoneyEvent)) if ord(self.SyncTransMoneyEvent) in [e.value for e in list(TUstpFtdcSyncDirectionType)] else list(TUstpFtdcSyncDirectionType)[0]

    def getTradeCode(self):
        '''银期业务功能码'''
        return str(self.TradeCode, 'GBK')

    def getTradeSource(self):
        '''业务发起方'''
        return TUstpFtdcTradeSyncSourceType(ord(self.TradeSource)) if ord(self.TradeSource) in [e.value for e in list(TUstpFtdcTradeSyncSourceType)] else list(TUstpFtdcTradeSyncSourceType)[0]

    def getTransSerialNo(self):
        '''主席流水号'''
        return str(self.TransSerialNo, 'GBK')

    def getSerialNo(self):
        '''次席流水号'''
        return str(self.SerialNo, 'GBK')

    def getUserID(self):
        '''用户编号'''
        return str(self.UserID, 'GBK')

    def getCommandDate(self):
        '''日期'''
        return str(self.CommandDate, 'GBK')

    def getCommandTime(self):
        '''时间'''
        return str(self.CommandTime, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'AccountID'={self.getAccountID()}, 'BankID'={self.getBankID()}, 'BankAccount'={self.getBankAccount()}, 'Currency'={self.getCurrency()}, 'Amount'={self.getAmount()}, 'SyncTransMoneyEvent'={self.getSyncTransMoneyEvent()}, 'TradeCode'={self.getTradeCode()}, 'TradeSource'={self.getTradeSource()}, 'TransSerialNo'={self.getTransSerialNo()}, 'SerialNo'={self.getSerialNo()}, 'UserID'={self.getUserID()}, 'CommandDate'={self.getCommandDate()}, 'CommandTime'={self.getCommandTime()}"


class CUstpFtdcMarketDataBaseField(Structure):
    """行情基础属性"""
    _fields_ = [
        ("TradingDay", c_char * 9),
        ("SettlementGroupID", c_char * 9),
        ("SettlementID", c_int32),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("PreDelta", c_double),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementGroupID(self):
        '''结算组代码'''
        return str(self.SettlementGroupID, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getPreSettlementPrice(self):
        '''昨结算'''
        return self.PreSettlementPrice

    def getPreClosePrice(self):
        '''昨收盘'''
        return self.PreClosePrice

    def getPreOpenInterest(self):
        '''昨持仓量'''
        return self.PreOpenInterest

    def getPreDelta(self):
        '''昨虚实度'''
        return self.PreDelta

    def __str__(self):  # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'SettlementGroupID'={self.getSettlementGroupID()}, 'SettlementID'={self.getSettlementID()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'PreClosePrice'={self.getPreClosePrice()}, 'PreOpenInterest'={self.getPreOpenInterest()}, 'PreDelta'={self.getPreDelta()}"


class CUstpFtdcMarketDataStaticField(Structure):
    """行情静态属性"""
    _fields_ = [
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("ClosePrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("SettlementPrice", c_double),
        ("CurrDelta", c_double),
    ]

    def getOpenPrice(self):
        '''今开盘'''
        return self.OpenPrice

    def getHighestPrice(self):
        '''最高价'''
        return self.HighestPrice

    def getLowestPrice(self):
        '''最低价'''
        return self.LowestPrice

    def getClosePrice(self):
        '''今收盘'''
        return self.ClosePrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getSettlementPrice(self):
        '''今结算'''
        return self.SettlementPrice

    def getCurrDelta(self):
        '''今虚实度'''
        return self.CurrDelta

    def __str__(self):  # 可以直接print
        return f"'OpenPrice'={self.getOpenPrice()}, 'HighestPrice'={self.getHighestPrice()}, 'LowestPrice'={self.getLowestPrice()}, 'ClosePrice'={self.getClosePrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'CurrDelta'={self.getCurrDelta()}"


class CUstpFtdcMarketDataLastMatchField(Structure):
    """行情最新成交属性"""
    _fields_ = [
        ("LastPrice", c_double),
        ("Volume", c_int32),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
    ]

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTurnover(self):
        '''成交金额'''
        return self.Turnover

    def getOpenInterest(self):
        '''持仓量'''
        return self.OpenInterest

    def __str__(self):  # 可以直接print
        return f"'LastPrice'={self.getLastPrice()}, 'Volume'={self.getVolume()}, 'Turnover'={self.getTurnover()}, 'OpenInterest'={self.getOpenInterest()}"


class CUstpFtdcMarketDataBestPriceField(Structure):
    """行情最优价属性"""
    _fields_ = [
        ("BidPrice1", c_double),
        ("BidVolume1", c_int32),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int32),
    ]

    def getBidPrice1(self):
        '''申买价一'''
        return self.BidPrice1

    def getBidVolume1(self):
        '''申买量一'''
        return self.BidVolume1

    def getAskPrice1(self):
        '''申卖价一'''
        return self.AskPrice1

    def getAskVolume1(self):
        '''申卖量一'''
        return self.AskVolume1

    def __str__(self):  # 可以直接print
        return f"'BidPrice1'={self.getBidPrice1()}, 'BidVolume1'={self.getBidVolume1()}, 'AskPrice1'={self.getAskPrice1()}, 'AskVolume1'={self.getAskVolume1()}"


class CUstpFtdcMarketDataBid23Field(Structure):
    """行情申买二、三属性"""
    _fields_ = [
        ("BidPrice2", c_double),
        ("BidVolume2", c_int32),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int32),
    ]

    def getBidPrice2(self):
        '''申买价二'''
        return self.BidPrice2

    def getBidVolume2(self):
        '''申买量二'''
        return self.BidVolume2

    def getBidPrice3(self):
        '''申买价三'''
        return self.BidPrice3

    def getBidVolume3(self):
        '''申买量三'''
        return self.BidVolume3

    def __str__(self):  # 可以直接print
        return f"'BidPrice2'={self.getBidPrice2()}, 'BidVolume2'={self.getBidVolume2()}, 'BidPrice3'={self.getBidPrice3()}, 'BidVolume3'={self.getBidVolume3()}"


class CUstpFtdcMarketDataAsk23Field(Structure):
    """行情申卖二、三属性"""
    _fields_ = [
        ("AskPrice2", c_double),
        ("AskVolume2", c_int32),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int32),
    ]

    def getAskPrice2(self):
        '''申卖价二'''
        return self.AskPrice2

    def getAskVolume2(self):
        '''申卖量二'''
        return self.AskVolume2

    def getAskPrice3(self):
        '''申卖价三'''
        return self.AskPrice3

    def getAskVolume3(self):
        '''申卖量三'''
        return self.AskVolume3

    def __str__(self):  # 可以直接print
        return f"'AskPrice2'={self.getAskPrice2()}, 'AskVolume2'={self.getAskVolume2()}, 'AskPrice3'={self.getAskPrice3()}, 'AskVolume3'={self.getAskVolume3()}"


class CUstpFtdcMarketDataBid45Field(Structure):
    """行情申买四、五属性"""
    _fields_ = [
        ("BidPrice4", c_double),
        ("BidVolume4", c_int32),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int32),
    ]

    def getBidPrice4(self):
        '''申买价四'''
        return self.BidPrice4

    def getBidVolume4(self):
        '''申买量四'''
        return self.BidVolume4

    def getBidPrice5(self):
        '''申买价五'''
        return self.BidPrice5

    def getBidVolume5(self):
        '''申买量五'''
        return self.BidVolume5

    def __str__(self):  # 可以直接print
        return f"'BidPrice4'={self.getBidPrice4()}, 'BidVolume4'={self.getBidVolume4()}, 'BidPrice5'={self.getBidPrice5()}, 'BidVolume5'={self.getBidVolume5()}"


class CUstpFtdcMarketDataAsk45Field(Structure):
    """行情申卖四、五属性"""
    _fields_ = [
        ("AskPrice4", c_double),
        ("AskVolume4", c_int32),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int32),
    ]

    def getAskPrice4(self):
        '''申卖价四'''
        return self.AskPrice4

    def getAskVolume4(self):
        '''申卖量四'''
        return self.AskVolume4

    def getAskPrice5(self):
        '''申卖价五'''
        return self.AskPrice5

    def getAskVolume5(self):
        '''申卖量五'''
        return self.AskVolume5

    def __str__(self):  # 可以直接print
        return f"'AskPrice4'={self.getAskPrice4()}, 'AskVolume4'={self.getAskVolume4()}, 'AskPrice5'={self.getAskPrice5()}, 'AskVolume5'={self.getAskVolume5()}"


class CUstpFtdcMarketDataUpdateTimeField(Structure):
    """行情更新时间属性"""
    _fields_ = [
        ("InstrumentID", c_char * 31),
        ("UpdateTime", c_char * 9),
        ("UpdateMillisec", c_int32),
        ("ActionDay", c_char * 9),
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getUpdateMillisec(self):
        '''最后修改毫秒'''
        return self.UpdateMillisec

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'InstrumentID'={self.getInstrumentID()}, 'UpdateTime'={self.getUpdateTime()}, 'UpdateMillisec'={self.getUpdateMillisec()}, 'ActionDay'={self.getActionDay()}"


class CUstpFtdcDepthMarketDataField(Structure):
    """深度行情"""
    _fields_ = [
        ("TradingDay", c_char * 9),
        ("SettlementGroupID", c_char * 9),
        ("SettlementID", c_int32),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("PreDelta", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("ClosePrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("SettlementPrice", c_double),
        ("CurrDelta", c_double),
        ("LastPrice", c_double),
        ("Volume", c_int32),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("BidPrice1", c_double),
        ("BidVolume1", c_int32),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int32),
        ("BidPrice2", c_double),
        ("BidVolume2", c_int32),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int32),
        ("AskPrice2", c_double),
        ("AskVolume2", c_int32),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int32),
        ("BidPrice4", c_double),
        ("BidVolume4", c_int32),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int32),
        ("AskPrice4", c_double),
        ("AskVolume4", c_int32),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int32),
        ("InstrumentID", c_char * 31),
        ("UpdateTime", c_char * 9),
        ("UpdateMillisec", c_int32),
        ("ActionDay", c_char * 9),
        ("HisHighestPrice", c_double),
        ("HisLowestPrice", c_double),
        ("LatestVolume", c_int32),
        ("InitVolume", c_int32),
        ("ChangeVolume", c_int32),
        ("BidImplyVolume", c_int32),
        ("AskImplyVolume", c_int32),
        ("AvgPrice", c_double),
        ("ArbiType", c_char),
        ("InstrumentID_1", c_char * 31),
        ("InstrumentID_2", c_char * 31),
        ("InstrumentName", c_char * 31),
        ("TotalBidVolume", c_int32),
        ("TotalAskVolume", c_int32),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementGroupID(self):
        '''结算组代码'''
        return str(self.SettlementGroupID, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getPreSettlementPrice(self):
        '''昨结算'''
        return self.PreSettlementPrice

    def getPreClosePrice(self):
        '''昨收盘'''
        return self.PreClosePrice

    def getPreOpenInterest(self):
        '''昨持仓量'''
        return self.PreOpenInterest

    def getPreDelta(self):
        '''昨虚实度'''
        return self.PreDelta

    def getOpenPrice(self):
        '''今开盘'''
        return self.OpenPrice

    def getHighestPrice(self):
        '''最高价'''
        return self.HighestPrice

    def getLowestPrice(self):
        '''最低价'''
        return self.LowestPrice

    def getClosePrice(self):
        '''今收盘'''
        return self.ClosePrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getSettlementPrice(self):
        '''今结算'''
        return self.SettlementPrice

    def getCurrDelta(self):
        '''今虚实度'''
        return self.CurrDelta

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTurnover(self):
        '''成交金额'''
        return self.Turnover

    def getOpenInterest(self):
        '''持仓量'''
        return self.OpenInterest

    def getBidPrice1(self):
        '''申买价一'''
        return self.BidPrice1

    def getBidVolume1(self):
        '''申买量一'''
        return self.BidVolume1

    def getAskPrice1(self):
        '''申卖价一'''
        return self.AskPrice1

    def getAskVolume1(self):
        '''申卖量一'''
        return self.AskVolume1

    def getBidPrice2(self):
        '''申买价二'''
        return self.BidPrice2

    def getBidVolume2(self):
        '''申买量二'''
        return self.BidVolume2

    def getBidPrice3(self):
        '''申买价三'''
        return self.BidPrice3

    def getBidVolume3(self):
        '''申买量三'''
        return self.BidVolume3

    def getAskPrice2(self):
        '''申卖价二'''
        return self.AskPrice2

    def getAskVolume2(self):
        '''申卖量二'''
        return self.AskVolume2

    def getAskPrice3(self):
        '''申卖价三'''
        return self.AskPrice3

    def getAskVolume3(self):
        '''申卖量三'''
        return self.AskVolume3

    def getBidPrice4(self):
        '''申买价四'''
        return self.BidPrice4

    def getBidVolume4(self):
        '''申买量四'''
        return self.BidVolume4

    def getBidPrice5(self):
        '''申买价五'''
        return self.BidPrice5

    def getBidVolume5(self):
        '''申买量五'''
        return self.BidVolume5

    def getAskPrice4(self):
        '''申卖价四'''
        return self.AskPrice4

    def getAskVolume4(self):
        '''申卖量四'''
        return self.AskVolume4

    def getAskPrice5(self):
        '''申卖价五'''
        return self.AskPrice5

    def getAskVolume5(self):
        '''申卖量五'''
        return self.AskVolume5

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getUpdateMillisec(self):
        '''最后修改毫秒'''
        return self.UpdateMillisec

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getHisHighestPrice(self):
        '''历史最高价'''
        return self.HisHighestPrice

    def getHisLowestPrice(self):
        '''历史最低价'''
        return self.HisLowestPrice

    def getLatestVolume(self):
        '''最新成交量'''
        return self.LatestVolume

    def getInitVolume(self):
        '''初始持仓量'''
        return self.InitVolume

    def getChangeVolume(self):
        '''持仓量变化'''
        return self.ChangeVolume

    def getBidImplyVolume(self):
        '''申买推导量'''
        return self.BidImplyVolume

    def getAskImplyVolume(self):
        '''申卖推导量'''
        return self.AskImplyVolume

    def getAvgPrice(self):
        '''当日均价'''
        return self.AvgPrice

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getInstrumentID_1(self):
        '''第一腿合约代码'''
        return str(self.InstrumentID_1, 'GBK')

    def getInstrumentID_2(self):
        '''第二腿合约代码'''
        return str(self.InstrumentID_2, 'GBK')

    def getInstrumentName(self):
        '''合约名称'''
        return str(self.InstrumentName, 'GBK')

    def getTotalBidVolume(self):
        '''总买入量'''
        return self.TotalBidVolume

    def getTotalAskVolume(self):
        '''总卖出量'''
        return self.TotalAskVolume

    def __str__(self):  # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'SettlementGroupID'={self.getSettlementGroupID()}, 'SettlementID'={self.getSettlementID()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'PreClosePrice'={self.getPreClosePrice()}, 'PreOpenInterest'={self.getPreOpenInterest()}, 'PreDelta'={self.getPreDelta()}, 'OpenPrice'={self.getOpenPrice()}, 'HighestPrice'={self.getHighestPrice()}, 'LowestPrice'={self.getLowestPrice()}, 'ClosePrice'={self.getClosePrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'CurrDelta'={self.getCurrDelta()}, 'LastPrice'={self.getLastPrice()}, 'Volume'={self.getVolume()}, 'Turnover'={self.getTurnover()}, 'OpenInterest'={self.getOpenInterest()}, 'BidPrice1'={self.getBidPrice1()}, 'BidVolume1'={self.getBidVolume1()}, 'AskPrice1'={self.getAskPrice1()}, 'AskVolume1'={self.getAskVolume1()}, 'BidPrice2'={self.getBidPrice2()}, 'BidVolume2'={self.getBidVolume2()}, 'BidPrice3'={self.getBidPrice3()}, 'BidVolume3'={self.getBidVolume3()}, 'AskPrice2'={self.getAskPrice2()}, 'AskVolume2'={self.getAskVolume2()}, 'AskPrice3'={self.getAskPrice3()}, 'AskVolume3'={self.getAskVolume3()}, 'BidPrice4'={self.getBidPrice4()}, 'BidVolume4'={self.getBidVolume4()}, 'BidPrice5'={self.getBidPrice5()}, 'BidVolume5'={self.getBidVolume5()}, 'AskPrice4'={self.getAskPrice4()}, 'AskVolume4'={self.getAskVolume4()}, 'AskPrice5'={self.getAskPrice5()}, 'AskVolume5'={self.getAskVolume5()}, 'InstrumentID'={self.getInstrumentID()}, 'UpdateTime'={self.getUpdateTime()}, 'UpdateMillisec'={self.getUpdateMillisec()}, 'ActionDay'={self.getActionDay()}, 'HisHighestPrice'={self.getHisHighestPrice()}, 'HisLowestPrice'={self.getHisLowestPrice()}, 'LatestVolume'={self.getLatestVolume()}, 'InitVolume'={self.getInitVolume()}, 'ChangeVolume'={self.getChangeVolume()}, 'BidImplyVolume'={self.getBidImplyVolume()}, 'AskImplyVolume'={self.getAskImplyVolume()}, 'AvgPrice'={self.getAvgPrice()}, 'ArbiType'={self.getArbiType()}, 'InstrumentID_1'={self.getInstrumentID_1()}, 'InstrumentID_2'={self.getInstrumentID_2()}, 'InstrumentName'={self.getInstrumentName()}, 'TotalBidVolume'={self.getTotalBidVolume()}, 'TotalAskVolume'={self.getTotalAskVolume()}"


class CUstpFtdcSpecificInstrumentField(Structure):
    """订阅合约的相关信息"""
    _fields_ = [
        ("InstrumentID", c_char * 31),
    ]

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'InstrumentID'={self.getInstrumentID()}"


class CUstpFtdcMultiChannelHeartBeatField(Structure):
    """多播通道心跳"""
    _fields_ = [
        ("UstpMultiChannelHeartBeatTimeOut", c_int32),
    ]

    def getUstpMultiChannelHeartBeatTimeOut(self):
        '''心跳超时时间（秒）'''
        return self.UstpMultiChannelHeartBeatTimeOut

    def __str__(self):  # 可以直接print
        return f"'UstpMultiChannelHeartBeatTimeOut'={self.getUstpMultiChannelHeartBeatTimeOut()}"


class CUstpFtdcReqMarketTopicField(Structure):
    """获取行情订阅号请求"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}"


class CUstpFtdcRspMarketTopicField(Structure):
    """获取行情订阅号应答"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("TopicID", c_int32),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getTopicID(self):
        '''订阅号'''
        return self.TopicID

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'TopicID'={self.getTopicID()}"


class CUstpFtdcInputMarginCombActionField(Structure):
    """申请组合"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("UserID", c_char * 16),
        ("InvestorID", c_char * 19),
        ("HedgeFlag", c_char),
        ("UserActionLocalID", c_char * 21),
        ("CombInstrumentID", c_char * 41),
        ("CombVolume", c_int32),
        ("CombDirection", c_char),
        ("ActionLocalID", c_char * 13),
        ("Direction", c_char),
        ("OrderSysID", c_char * 31),
        ("CombActionStatus", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getUserID(self):
        '''交易用户代码'''
        return str(self.UserID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getUserActionLocalID(self):
        '''用户本地编号'''
        return str(self.UserActionLocalID, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getCombVolume(self):
        '''组合数量'''
        return self.CombVolume

    def getCombDirection(self):
        '''组合动作方向'''
        return TUstpFtdcCombDirectionType(ord(self.CombDirection)) if ord(self.CombDirection) in [e.value for e in list(TUstpFtdcCombDirectionType)] else list(TUstpFtdcCombDirectionType)[0]

    def getActionLocalID(self):
        '''本地编号'''
        return str(self.ActionLocalID, 'GBK')

    def getDirection(self):
        '''组合持仓方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getOrderSysID(self):
        '''系统编号'''
        return str(self.OrderSysID, 'GBK')

    def getCombActionStatus(self):
        '''组合操作状态'''
        return TUstpFtdcCombActionStatusType(ord(self.CombActionStatus)) if ord(self.CombActionStatus) in [e.value for e in list(TUstpFtdcCombActionStatusType)] else list(TUstpFtdcCombActionStatusType)[0]

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'UserID'={self.getUserID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'UserActionLocalID'={self.getUserActionLocalID()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'CombVolume'={self.getCombVolume()}, 'CombDirection'={self.getCombDirection()}, 'ActionLocalID'={self.getActionLocalID()}, 'Direction'={self.getDirection()}, 'OrderSysID'={self.getOrderSysID()}, 'CombActionStatus'={self.getCombActionStatus()}"


class CUstpFtdcQryInvestorCombPositionField(Structure):
    """投资者组合持仓查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("HedgeFlag", c_char),
        ("CombInstrumentID", c_char * 41),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcRspInvestorCombPositionField(Structure):
    """投资者组合持仓查询应答"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("Direction", c_char),
        ("InvestorID", c_char * 19),
        ("HedgeFlag", c_char),
        ("ClientID", c_char * 19),
        ("CombInstrumentID", c_char * 41),
        ("Leg1InstrumentID", c_char * 31),
        ("Leg2InstrumentID", c_char * 31),
        ("CombPosition", c_int32),
        ("CombFrozenPosition", c_int32),
        ("CombFreeMargin", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getDirection(self):
        '''持仓方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getLeg1InstrumentID(self):
        '''单腿1合约代码'''
        return str(self.Leg1InstrumentID, 'GBK')

    def getLeg2InstrumentID(self):
        '''单腿2合约代码'''
        return str(self.Leg2InstrumentID, 'GBK')

    def getCombPosition(self):
        '''组合持仓'''
        return self.CombPosition

    def getCombFrozenPosition(self):
        '''冻结组合持仓'''
        return self.CombFrozenPosition

    def getCombFreeMargin(self):
        '''组合一手释放的保证金'''
        return self.CombFreeMargin

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'Direction'={self.getDirection()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ClientID'={self.getClientID()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'Leg1InstrumentID'={self.getLeg1InstrumentID()}, 'Leg2InstrumentID'={self.getLeg2InstrumentID()}, 'CombPosition'={self.getCombPosition()}, 'CombFrozenPosition'={self.getCombFrozenPosition()}, 'CombFreeMargin'={self.getCombFreeMargin()}"


class CUstpFtdcMarginCombinationLegField(Structure):
    """组合规则"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("CombInstrumentID", c_char * 41),
        ("LegID", c_int32),
        ("LegInstrumentID", c_char * 31),
        ("Direction", c_char),
        ("LegMultiple", c_int32),
        ("Priority", c_int32),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getLegID(self):
        '''单腿编号'''
        return self.LegID

    def getLegInstrumentID(self):
        '''单腿合约代码'''
        return str(self.LegInstrumentID, 'GBK')

    def getDirection(self):
        '''买卖方向'''
        return TUstpFtdcDirectionType(ord(self.Direction)) if ord(self.Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getLegMultiple(self):
        '''单腿乘数'''
        return self.LegMultiple

    def getPriority(self):
        '''优先级'''
        return self.Priority

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'LegID'={self.getLegID()}, 'LegInstrumentID'={self.getLegInstrumentID()}, 'Direction'={self.getDirection()}, 'LegMultiple'={self.getLegMultiple()}, 'Priority'={self.getPriority()}"


class CUstpFtdcQryInvestorLegPositionField(Structure):
    """投资者单腿持仓查询"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("HedgeFlag", c_char),
        ("LegInstrumentID", c_char * 31),
        ("ClientID", c_char * 19),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getLegInstrumentID(self):
        '''单腿合约代码'''
        return str(self.LegInstrumentID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'LegInstrumentID'={self.getLegInstrumentID()}, 'ClientID'={self.getClientID()}"


class CUstpFtdcRspInvestorLegPositionField(Structure):
    """投资者单腿持仓查询应答"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("HedgeFlag", c_char),
        ("ClientID", c_char * 19),
        ("InstrumentID", c_char * 31),
        ("LongPosition", c_int32),
        ("ShortPosition", c_int32),
        ("LongMargin", c_double),
        ("ShortMargin", c_double),
        ("LongFrozenPosition", c_int32),
        ("ShortFrozenPosition", c_int32),
        ("LongFrozenMargin", c_double),
        ("ShortFrozenMargin", c_double),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getInstrumentID(self):
        '''单腿合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getLongPosition(self):
        '''多头持仓'''
        return self.LongPosition

    def getShortPosition(self):
        '''空头持仓'''
        return self.ShortPosition

    def getLongMargin(self):
        '''多头占用保证金'''
        return self.LongMargin

    def getShortMargin(self):
        '''空头占用保证金'''
        return self.ShortMargin

    def getLongFrozenPosition(self):
        '''多头冻结持仓'''
        return self.LongFrozenPosition

    def getShortFrozenPosition(self):
        '''空头冻结持仓'''
        return self.ShortFrozenPosition

    def getLongFrozenMargin(self):
        '''多头冻结保证金'''
        return self.LongFrozenMargin

    def getShortFrozenMargin(self):
        '''空头冻结保证金'''
        return self.ShortFrozenMargin

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'ClientID'={self.getClientID()}, 'InstrumentID'={self.getInstrumentID()}, 'LongPosition'={self.getLongPosition()}, 'ShortPosition'={self.getShortPosition()}, 'LongMargin'={self.getLongMargin()}, 'ShortMargin'={self.getShortMargin()}, 'LongFrozenPosition'={self.getLongFrozenPosition()}, 'ShortFrozenPosition'={self.getShortFrozenPosition()}, 'LongFrozenMargin'={self.getLongFrozenMargin()}, 'ShortFrozenMargin'={self.getShortFrozenMargin()}"


class CUstpFtdcQryUstpInstrumentGroupField(Structure):
    """查询合约组信息"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("BrokerID", c_char * 11),
        ("InstrumentID", c_char * 31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'BrokerID'={self.getBrokerID()}, 'InstrumentID'={self.getInstrumentID()}"


class CUstpFtdcRspInstrumentGroupField(Structure):
    """合约组信息查询应答"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("BrokerID", c_char * 11),
        ("InstrumentID", c_char * 31),
        ("InstrumentGroupID", c_char * 31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getInstrumentGroupID(self):
        '''合约组代码'''
        return str(self.InstrumentGroupID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'BrokerID'={self.getBrokerID()}, 'InstrumentID'={self.getInstrumentID()}, 'InstrumentGroupID'={self.getInstrumentGroupID()}"


class CUstpFtdcQryClientMarginCombTypeField(Structure):
    """查询组合保证金类型"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("BrokerID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("HedgeFlag", c_char),
        ("InstrumentGroupID", c_char * 31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getInstrumentGroupID(self):
        '''合约组代码'''
        return str(self.InstrumentGroupID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'HedgeFlag'={self.getHedgeFlag()}, 'InstrumentGroupID'={self.getInstrumentGroupID()}"


class CUstpFtdcRspClientMarginCombTypeField(Structure):
    """组合保证金类型查询应答"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("BrokerID", c_char * 11),
        ("ParticipantID", c_char * 11),
        ("ClientID", c_char * 19),
        ("InstrumentGroupID", c_char * 31),
        ("MarginCombType", c_char),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getParticipantID(self):
        '''会员代码'''
        return str(self.ParticipantID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getInstrumentGroupID(self):
        '''合约组代码'''
        return str(self.InstrumentGroupID, 'GBK')

    def getMarginCombType(self):
        '''保证金组合类型'''
        return TUstpFtdcClientMarginCombTypeType(ord(self.MarginCombType)) if ord(self.MarginCombType) in [e.value for e in list(TUstpFtdcClientMarginCombTypeType)] else list(TUstpFtdcClientMarginCombTypeType)[0]

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'BrokerID'={self.getBrokerID()}, 'ParticipantID'={self.getParticipantID()}, 'ClientID'={self.getClientID()}, 'InstrumentGroupID'={self.getInstrumentGroupID()}, 'MarginCombType'={self.getMarginCombType()}"


class CUstpFtdcReqQrySystemTimeField(Structure):
    """系统时间"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}"


class CUstpFtdcRspQrySystemTimeField(Structure):
    """系统时间"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("SystemTime", c_char * 9),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getSystemTime(self):
        '''系统时间'''
        return str(self.SystemTime, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'SystemTime'={self.getSystemTime()}"


class CUstpFtdcInputExecOrderField(Structure):
    """输入行权"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("OrderSysID", c_char * 31),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("InstrumentID", c_char * 31),
        ("UserOrderLocalID", c_char * 21),
        ("OrderType", c_char),
        ("DeliveryFlag", c_char),
        ("HedgeFlag", c_char),
        ("Volume", c_int32),
        ("UserCustom", c_char * 65),
        ("ActionDay", c_char * 9),
        ("BusinessLocalID", c_int32),
        ("BusinessUnit", c_char * 21),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getUserOrderLocalID(self):
        '''用户本地报单号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getOrderType(self):
        '''委托类型'''
        return TUstpFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TUstpFtdcOrderTypeType)] else list(TUstpFtdcOrderTypeType)[0]

    def getDeliveryFlag(self):
        '''期权对冲标识'''
        return TUstpFtdcDeliveryFlagType(ord(self.DeliveryFlag)) if ord(self.DeliveryFlag) in [e.value for e in list(TUstpFtdcDeliveryFlagType)] else list(TUstpFtdcDeliveryFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'InstrumentID'={self.getInstrumentID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'OrderType'={self.getOrderType()}, 'DeliveryFlag'={self.getDeliveryFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Volume'={self.getVolume()}, 'UserCustom'={self.getUserCustom()}, 'ActionDay'={self.getActionDay()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'BusinessUnit'={self.getBusinessUnit()}"


class CUstpFtdcInputExecOrderActionField(Structure):
    """输入行权操作"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("OrderSysID", c_char * 31),
        ("BrokerID", c_char * 11),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("UserOrderActionLocalID", c_char * 21),
        ("UserOrderLocalID", c_char * 21),
        ("ActionFlag", c_char),
        ("VolumeChange", c_int32),
        ("BusinessLocalID", c_int32),
        ("OrderType", c_char),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getUserOrderActionLocalID(self):
        '''本次撤单操作的本地编号'''
        return str(self.UserOrderActionLocalID, 'GBK')

    def getUserOrderLocalID(self):
        '''被撤订单的本地报单编号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getActionFlag(self):
        '''报单操作标志'''
        return TUstpFtdcActionFlagType(ord(self.ActionFlag)) if ord(self.ActionFlag) in [e.value for e in list(TUstpFtdcActionFlagType)] else list(TUstpFtdcActionFlagType)[0]

    def getVolumeChange(self):
        '''数量变化'''
        return self.VolumeChange

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getOrderType(self):
        '''委托类型'''
        return TUstpFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TUstpFtdcOrderTypeType)] else list(TUstpFtdcOrderTypeType)[0]

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'BrokerID'={self.getBrokerID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'UserOrderActionLocalID'={self.getUserOrderActionLocalID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'ActionFlag'={self.getActionFlag()}, 'VolumeChange'={self.getVolumeChange()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'OrderType'={self.getOrderType()}"


class CUstpFtdcExecOrderField(Structure):
    """行权通知"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("OrderSysID", c_char * 31),
        ("InvestorID", c_char * 19),
        ("UserID", c_char * 16),
        ("InstrumentID", c_char * 31),
        ("UserOrderLocalID", c_char * 21),
        ("OrderType", c_char),
        ("DeliveryFlag", c_char),
        ("HedgeFlag", c_char),
        ("Volume", c_int32),
        ("UserCustom", c_char * 65),
        ("ActionDay", c_char * 9),
        ("BusinessLocalID", c_int32),
        ("BusinessUnit", c_char * 21),
        ("TradingDay", c_char * 9),
        ("ParticipantID", c_char * 11),
        ("OrderUserID", c_char * 16),
        ("ClientID", c_char * 19),
        ("SeatID", c_char * 13),
        ("InsertTime", c_char * 9),
        ("OrderLocalID", c_char * 13),
        ("OrderSource", c_char),
        ("OrderStatus", c_char),
        ("CancelTime", c_char * 9),
        ("CancelUserID", c_char * 16),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getOrderSysID(self):
        '''系统报单编号'''
        return str(self.OrderSysID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getUserID(self):
        '''用户代码'''
        return str(self.UserID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getUserOrderLocalID(self):
        '''用户本地报单号'''
        return str(self.UserOrderLocalID, 'GBK')

    def getOrderType(self):
        '''委托类型'''
        return TUstpFtdcOrderTypeType(ord(self.OrderType)) if ord(self.OrderType) in [e.value for e in list(TUstpFtdcOrderTypeType)] else list(TUstpFtdcOrderTypeType)[0]

    def getDeliveryFlag(self):
        '''期权对冲标识'''
        return TUstpFtdcDeliveryFlagType(ord(self.DeliveryFlag)) if ord(self.DeliveryFlag) in [e.value for e in list(TUstpFtdcDeliveryFlagType)] else list(TUstpFtdcDeliveryFlagType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getUserCustom(self):
        '''用户自定义域'''
        return str(self.UserCustom, 'GBK')

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getBusinessLocalID(self):
        '''本地业务标识'''
        return self.BusinessLocalID

    def getBusinessUnit(self):
        '''业务单元'''
        return str(self.BusinessUnit, 'GBK')

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getParticipantID(self):
        '''会员编号'''
        return str(self.ParticipantID, 'GBK')

    def getOrderUserID(self):
        '''最初下单用户编号'''
        return str(self.OrderUserID, 'GBK')

    def getClientID(self):
        '''客户编码'''
        return str(self.ClientID, 'GBK')

    def getSeatID(self):
        '''下单席位号'''
        return str(self.SeatID, 'GBK')

    def getInsertTime(self):
        '''插入时间'''
        return str(self.InsertTime, 'GBK')

    def getOrderLocalID(self):
        '''本地报单编号'''
        return str(self.OrderLocalID, 'GBK')

    def getOrderSource(self):
        '''报单来源'''
        return TUstpFtdcOrderSourceType(ord(self.OrderSource)) if ord(self.OrderSource) in [e.value for e in list(TUstpFtdcOrderSourceType)] else list(TUstpFtdcOrderSourceType)[0]

    def getOrderStatus(self):
        '''报单状态'''
        return TUstpFtdcOrderStatusType(ord(self.OrderStatus)) if ord(self.OrderStatus) in [e.value for e in list(TUstpFtdcOrderStatusType)] else list(TUstpFtdcOrderStatusType)[0]

    def getCancelTime(self):
        '''撤销时间'''
        return str(self.CancelTime, 'GBK')

    def getCancelUserID(self):
        '''撤单用户编号'''
        return str(self.CancelUserID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'OrderSysID'={self.getOrderSysID()}, 'InvestorID'={self.getInvestorID()}, 'UserID'={self.getUserID()}, 'InstrumentID'={self.getInstrumentID()}, 'UserOrderLocalID'={self.getUserOrderLocalID()}, 'OrderType'={self.getOrderType()}, 'DeliveryFlag'={self.getDeliveryFlag()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Volume'={self.getVolume()}, 'UserCustom'={self.getUserCustom()}, 'ActionDay'={self.getActionDay()}, 'BusinessLocalID'={self.getBusinessLocalID()}, 'BusinessUnit'={self.getBusinessUnit()}, 'TradingDay'={self.getTradingDay()}, 'ParticipantID'={self.getParticipantID()}, 'OrderUserID'={self.getOrderUserID()}, 'ClientID'={self.getClientID()}, 'SeatID'={self.getSeatID()}, 'InsertTime'={self.getInsertTime()}, 'OrderLocalID'={self.getOrderLocalID()}, 'OrderSource'={self.getOrderSource()}, 'OrderStatus'={self.getOrderStatus()}, 'CancelTime'={self.getCancelTime()}, 'CancelUserID'={self.getCancelUserID()}"


class CUstpFtdcReqQryMarketDataField(Structure):
    """查询行情快照"""
    _fields_ = [
        ("ExchangeID", c_char * 11),
        ("InstrumentID", c_char * 31),
    ]

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'ExchangeID'={self.getExchangeID()}, 'InstrumentID'={self.getInstrumentID()}"


class CUstpFtdcRspDepthMarketDataField(Structure):
    """查询行情快应答"""
    _fields_ = [
        ("TradingDay", c_char * 9),
        ("SettlementGroupID", c_char * 9),
        ("SettlementID", c_int32),
        ("PreSettlementPrice", c_double),
        ("PreClosePrice", c_double),
        ("PreOpenInterest", c_double),
        ("PreDelta", c_double),
        ("OpenPrice", c_double),
        ("HighestPrice", c_double),
        ("LowestPrice", c_double),
        ("ClosePrice", c_double),
        ("UpperLimitPrice", c_double),
        ("LowerLimitPrice", c_double),
        ("SettlementPrice", c_double),
        ("CurrDelta", c_double),
        ("LastPrice", c_double),
        ("Volume", c_int32),
        ("Turnover", c_double),
        ("OpenInterest", c_double),
        ("BidPrice1", c_double),
        ("BidVolume1", c_int32),
        ("AskPrice1", c_double),
        ("AskVolume1", c_int32),
        ("BidPrice2", c_double),
        ("BidVolume2", c_int32),
        ("BidPrice3", c_double),
        ("BidVolume3", c_int32),
        ("AskPrice2", c_double),
        ("AskVolume2", c_int32),
        ("AskPrice3", c_double),
        ("AskVolume3", c_int32),
        ("BidPrice4", c_double),
        ("BidVolume4", c_int32),
        ("BidPrice5", c_double),
        ("BidVolume5", c_int32),
        ("AskPrice4", c_double),
        ("AskVolume4", c_int32),
        ("AskPrice5", c_double),
        ("AskVolume5", c_int32),
        ("InstrumentID", c_char * 31),
        ("UpdateTime", c_char * 9),
        ("UpdateMillisec", c_int32),
        ("ActionDay", c_char * 9),
        ("HisHighestPrice", c_double),
        ("HisLowestPrice", c_double),
        ("LatestVolume", c_int32),
        ("InitVolume", c_int32),
        ("ChangeVolume", c_int32),
        ("BidImplyVolume", c_int32),
        ("AskImplyVolume", c_int32),
        ("AvgPrice", c_double),
        ("ArbiType", c_char),
        ("InstrumentID_1", c_char * 31),
        ("InstrumentID_2", c_char * 31),
        ("InstrumentName", c_char * 31),
        ("TotalBidVolume", c_int32),
        ("TotalAskVolume", c_int32),
    ]

    def getTradingDay(self):
        '''交易日'''
        return str(self.TradingDay, 'GBK')

    def getSettlementGroupID(self):
        '''结算组代码'''
        return str(self.SettlementGroupID, 'GBK')

    def getSettlementID(self):
        '''结算编号'''
        return self.SettlementID

    def getPreSettlementPrice(self):
        '''昨结算'''
        return self.PreSettlementPrice

    def getPreClosePrice(self):
        '''昨收盘'''
        return self.PreClosePrice

    def getPreOpenInterest(self):
        '''昨持仓量'''
        return self.PreOpenInterest

    def getPreDelta(self):
        '''昨虚实度'''
        return self.PreDelta

    def getOpenPrice(self):
        '''今开盘'''
        return self.OpenPrice

    def getHighestPrice(self):
        '''最高价'''
        return self.HighestPrice

    def getLowestPrice(self):
        '''最低价'''
        return self.LowestPrice

    def getClosePrice(self):
        '''今收盘'''
        return self.ClosePrice

    def getUpperLimitPrice(self):
        '''涨停板价'''
        return self.UpperLimitPrice

    def getLowerLimitPrice(self):
        '''跌停板价'''
        return self.LowerLimitPrice

    def getSettlementPrice(self):
        '''今结算'''
        return self.SettlementPrice

    def getCurrDelta(self):
        '''今虚实度'''
        return self.CurrDelta

    def getLastPrice(self):
        '''最新价'''
        return self.LastPrice

    def getVolume(self):
        '''数量'''
        return self.Volume

    def getTurnover(self):
        '''成交金额'''
        return self.Turnover

    def getOpenInterest(self):
        '''持仓量'''
        return self.OpenInterest

    def getBidPrice1(self):
        '''申买价一'''
        return self.BidPrice1

    def getBidVolume1(self):
        '''申买量一'''
        return self.BidVolume1

    def getAskPrice1(self):
        '''申卖价一'''
        return self.AskPrice1

    def getAskVolume1(self):
        '''申卖量一'''
        return self.AskVolume1

    def getBidPrice2(self):
        '''申买价二'''
        return self.BidPrice2

    def getBidVolume2(self):
        '''申买量二'''
        return self.BidVolume2

    def getBidPrice3(self):
        '''申买价三'''
        return self.BidPrice3

    def getBidVolume3(self):
        '''申买量三'''
        return self.BidVolume3

    def getAskPrice2(self):
        '''申卖价二'''
        return self.AskPrice2

    def getAskVolume2(self):
        '''申卖量二'''
        return self.AskVolume2

    def getAskPrice3(self):
        '''申卖价三'''
        return self.AskPrice3

    def getAskVolume3(self):
        '''申卖量三'''
        return self.AskVolume3

    def getBidPrice4(self):
        '''申买价四'''
        return self.BidPrice4

    def getBidVolume4(self):
        '''申买量四'''
        return self.BidVolume4

    def getBidPrice5(self):
        '''申买价五'''
        return self.BidPrice5

    def getBidVolume5(self):
        '''申买量五'''
        return self.BidVolume5

    def getAskPrice4(self):
        '''申卖价四'''
        return self.AskPrice4

    def getAskVolume4(self):
        '''申卖量四'''
        return self.AskVolume4

    def getAskPrice5(self):
        '''申卖价五'''
        return self.AskPrice5

    def getAskVolume5(self):
        '''申卖量五'''
        return self.AskVolume5

    def getInstrumentID(self):
        '''合约代码'''
        return str(self.InstrumentID, 'GBK')

    def getUpdateTime(self):
        '''最后修改时间'''
        return str(self.UpdateTime, 'GBK')

    def getUpdateMillisec(self):
        '''最后修改毫秒'''
        return self.UpdateMillisec

    def getActionDay(self):
        '''业务发生日期'''
        return str(self.ActionDay, 'GBK')

    def getHisHighestPrice(self):
        '''历史最高价'''
        return self.HisHighestPrice

    def getHisLowestPrice(self):
        '''历史最低价'''
        return self.HisLowestPrice

    def getLatestVolume(self):
        '''最新成交量'''
        return self.LatestVolume

    def getInitVolume(self):
        '''初始持仓量'''
        return self.InitVolume

    def getChangeVolume(self):
        '''持仓量变化'''
        return self.ChangeVolume

    def getBidImplyVolume(self):
        '''申买推导量'''
        return self.BidImplyVolume

    def getAskImplyVolume(self):
        '''申卖推导量'''
        return self.AskImplyVolume

    def getAvgPrice(self):
        '''当日均价'''
        return self.AvgPrice

    def getArbiType(self):
        '''策略类别'''
        return TUstpFtdcArbiTypeType(ord(self.ArbiType)) if ord(self.ArbiType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getInstrumentID_1(self):
        '''第一腿合约代码'''
        return str(self.InstrumentID_1, 'GBK')

    def getInstrumentID_2(self):
        '''第二腿合约代码'''
        return str(self.InstrumentID_2, 'GBK')

    def getInstrumentName(self):
        '''合约名称'''
        return str(self.InstrumentName, 'GBK')

    def getTotalBidVolume(self):
        '''总买入量'''
        return self.TotalBidVolume

    def getTotalAskVolume(self):
        '''总卖出量'''
        return self.TotalAskVolume

    def __str__(self):  # 可以直接print
        return f"'TradingDay'={self.getTradingDay()}, 'SettlementGroupID'={self.getSettlementGroupID()}, 'SettlementID'={self.getSettlementID()}, 'PreSettlementPrice'={self.getPreSettlementPrice()}, 'PreClosePrice'={self.getPreClosePrice()}, 'PreOpenInterest'={self.getPreOpenInterest()}, 'PreDelta'={self.getPreDelta()}, 'OpenPrice'={self.getOpenPrice()}, 'HighestPrice'={self.getHighestPrice()}, 'LowestPrice'={self.getLowestPrice()}, 'ClosePrice'={self.getClosePrice()}, 'UpperLimitPrice'={self.getUpperLimitPrice()}, 'LowerLimitPrice'={self.getLowerLimitPrice()}, 'SettlementPrice'={self.getSettlementPrice()}, 'CurrDelta'={self.getCurrDelta()}, 'LastPrice'={self.getLastPrice()}, 'Volume'={self.getVolume()}, 'Turnover'={self.getTurnover()}, 'OpenInterest'={self.getOpenInterest()}, 'BidPrice1'={self.getBidPrice1()}, 'BidVolume1'={self.getBidVolume1()}, 'AskPrice1'={self.getAskPrice1()}, 'AskVolume1'={self.getAskVolume1()}, 'BidPrice2'={self.getBidPrice2()}, 'BidVolume2'={self.getBidVolume2()}, 'BidPrice3'={self.getBidPrice3()}, 'BidVolume3'={self.getBidVolume3()}, 'AskPrice2'={self.getAskPrice2()}, 'AskVolume2'={self.getAskVolume2()}, 'AskPrice3'={self.getAskPrice3()}, 'AskVolume3'={self.getAskVolume3()}, 'BidPrice4'={self.getBidPrice4()}, 'BidVolume4'={self.getBidVolume4()}, 'BidPrice5'={self.getBidPrice5()}, 'BidVolume5'={self.getBidVolume5()}, 'AskPrice4'={self.getAskPrice4()}, 'AskVolume4'={self.getAskVolume4()}, 'AskPrice5'={self.getAskPrice5()}, 'AskVolume5'={self.getAskVolume5()}, 'InstrumentID'={self.getInstrumentID()}, 'UpdateTime'={self.getUpdateTime()}, 'UpdateMillisec'={self.getUpdateMillisec()}, 'ActionDay'={self.getActionDay()}, 'HisHighestPrice'={self.getHisHighestPrice()}, 'HisLowestPrice'={self.getHisLowestPrice()}, 'LatestVolume'={self.getLatestVolume()}, 'InitVolume'={self.getInitVolume()}, 'ChangeVolume'={self.getChangeVolume()}, 'BidImplyVolume'={self.getBidImplyVolume()}, 'AskImplyVolume'={self.getAskImplyVolume()}, 'AvgPrice'={self.getAvgPrice()}, 'ArbiType'={self.getArbiType()}, 'InstrumentID_1'={self.getInstrumentID_1()}, 'InstrumentID_2'={self.getInstrumentID_2()}, 'InstrumentName'={self.getInstrumentName()}, 'TotalBidVolume'={self.getTotalBidVolume()}, 'TotalAskVolume'={self.getTotalAskVolume()}"


class CUstpFtdcDSUserInfoField(Structure):
    """穿透监管客户信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("AuthCode", c_char * 17),
        ("EncryptType", c_char),
    ]

    def getAppID(self):
        '''用户AppID'''
        return str(self.AppID, 'GBK')

    def getAuthCode(self):
        '''用户授权码'''
        return str(self.AuthCode, 'GBK')

    def getEncryptType(self):
        '''密钥加密类型'''
        return TUstpFtdcDSKeyEncryptType(ord(self.EncryptType)) if ord(self.EncryptType) in [e.value for e in list(TUstpFtdcDSKeyEncryptType)] else list(TUstpFtdcDSKeyEncryptType)[0]

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'AuthCode'={self.getAuthCode()}, 'EncryptType'={self.getEncryptType()}"


class CUstpFtdcDSUserCertReqDataField(Structure):
    """穿透监管客户认证请求信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("UserCertReqData", c_char * 801),
        ("TotalNum", c_int32),
        ("CurrentNum", c_int32),
    ]

    def getAppID(self):
        '''用户AppID'''
        return str(self.AppID, 'GBK')

    def getUserCertReqData(self):
        '''用户认证请求信息'''
        return str(self.UserCertReqData, 'GBK')

    def getTotalNum(self):
        '''用户证书信息分片的总片数'''
        return self.TotalNum

    def getCurrentNum(self):
        '''用户证书信息分片的第几片'''
        return self.CurrentNum

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'UserCertReqData'={self.getUserCertReqData()}, 'TotalNum'={self.getTotalNum()}, 'CurrentNum'={self.getCurrentNum()}"


class CUstpFtdcDSUserCertRspDataField(Structure):
    """穿透监管客户认证响应信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("AppIDType", c_char),
        ("UserCertRspData", c_char * 801),
        ("TotalNum", c_int32),
        ("CurrentNum", c_int32),
    ]

    def getAppID(self):
        '''AppID'''
        return str(self.AppID, 'GBK')

    def getAppIDType(self):
        '''AppID类型'''
        return TUstpFtdcDSAppIDTypeType(ord(self.AppIDType)) if ord(self.AppIDType) in [e.value for e in list(TUstpFtdcDSAppIDTypeType)] else list(TUstpFtdcDSAppIDTypeType)[0]

    def getUserCertRspData(self):
        '''用户认证返回信息'''
        return str(self.UserCertRspData, 'GBK')

    def getTotalNum(self):
        '''用户证书返回信息分片的总片数'''
        return self.TotalNum

    def getCurrentNum(self):
        '''用户证书返回信息分片的第几片'''
        return self.CurrentNum

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'AppIDType'={self.getAppIDType()}, 'UserCertRspData'={self.getUserCertRspData()}, 'TotalNum'={self.getTotalNum()}, 'CurrentNum'={self.getCurrentNum()}"


class CUstpFtdcDSLocalSystemDataField(Structure):
    """穿透监管客户信息采集信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("ExceptionFlag", c_char),
        ("LocalSystemData", c_char * 801),
    ]

    def getAppID(self):
        '''用户AppID'''
        return str(self.AppID, 'GBK')

    def getExceptionFlag(self):
        '''异常标识'''
        return TUstpFtdcDSExceptionFlagType(ord(self.ExceptionFlag)) if ord(self.ExceptionFlag) in [e.value for e in list(TUstpFtdcDSExceptionFlagType)] else list(TUstpFtdcDSExceptionFlagType)[0]

    def getLocalSystemData(self):
        '''用户信息采集结果'''
        return str(self.LocalSystemData, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'ExceptionFlag'={self.getExceptionFlag()}, 'LocalSystemData'={self.getLocalSystemData()}"


class CUstpFtdcDSProxyCheckUserInfoField(Structure):
    """穿透监管中继验证客户信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("AuthCode", c_char * 17),
        ("EncryptType", c_char),
    ]

    def getAppID(self):
        '''用户AppID'''
        return str(self.AppID, 'GBK')

    def getAuthCode(self):
        '''用户授权码'''
        return str(self.AuthCode, 'GBK')

    def getEncryptType(self):
        '''密钥加密类型'''
        return TUstpFtdcDSKeyEncryptType(ord(self.EncryptType)) if ord(self.EncryptType) in [e.value for e in list(TUstpFtdcDSKeyEncryptType)] else list(TUstpFtdcDSKeyEncryptType)[0]

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'AuthCode'={self.getAuthCode()}, 'EncryptType'={self.getEncryptType()}"


class CUstpFtdcDSProxyUserCertInField(Structure):
    """穿透监管中继处接收到的终端认证信息"""
    _fields_ = [
        ("UserCertReqInfo", c_char * 4097),
    ]

    def getUserCertReqInfo(self):
        '''穿透监管中继处接收到的终端认证信息'''
        return str(self.UserCertReqInfo, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'UserCertReqInfo'={self.getUserCertReqInfo()}"


class CUstpFtdcDSProxyUserCertOutField(Structure):
    """穿透监管中继处接终端认证返回信息"""
    _fields_ = [
        ("UserCertRspInfo", c_char * 4097),
        ("UserCertRspInfoLen", c_int32),
    ]

    def getUserCertRspInfo(self):
        '''穿透监管中继处证书认证的返回结果'''
        return str(self.UserCertRspInfo, 'GBK')

    def getUserCertRspInfoLen(self):
        '''中继处返回数据已使用长度信息'''
        return self.UserCertRspInfoLen

    def __str__(self):  # 可以直接print
        return f"'UserCertRspInfo'={self.getUserCertRspInfo()}, 'UserCertRspInfoLen'={self.getUserCertRspInfoLen()}"


class CUstpFtdcDSProxySubmitDataField(Structure):
    """穿透监管中继提交信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("TerminalPubNetIP", c_char * 40),
        ("TerminalPubNetPort", c_char * 6),
        ("TerminalLoginTime", c_char * 20),
        ("ExceptionFlag", c_char),
        ("RelayID", c_char * 31),
        ("TerminalSystemData", c_char * 801),
    ]

    def getAppID(self):
        '''AppID'''
        return str(self.AppID, 'GBK')

    def getTerminalPubNetIP(self):
        '''客户终端公网IP'''
        return str(self.TerminalPubNetIP, 'GBK')

    def getTerminalPubNetPort(self):
        '''客户终端公网端口号'''
        return str(self.TerminalPubNetPort, 'GBK')

    def getTerminalLoginTime(self):
        '''客户终端登入时间'''
        return str(self.TerminalLoginTime, 'GBK')

    def getExceptionFlag(self):
        '''异常标识'''
        return TUstpFtdcDSExceptionFlagType(ord(self.ExceptionFlag)) if ord(self.ExceptionFlag) in [e.value for e in list(TUstpFtdcDSExceptionFlagType)] else list(TUstpFtdcDSExceptionFlagType)[0]

    def getRelayID(self):
        '''RealyID'''
        return str(self.RelayID, 'GBK')

    def getTerminalSystemData(self):
        '''终端采集信息'''
        return str(self.TerminalSystemData, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'TerminalPubNetIP'={self.getTerminalPubNetIP()}, 'TerminalPubNetPort'={self.getTerminalPubNetPort()}, 'TerminalLoginTime'={self.getTerminalLoginTime()}, 'ExceptionFlag'={self.getExceptionFlag()}, 'RelayID'={self.getRelayID()}, 'TerminalSystemData'={self.getTerminalSystemData()}"


class CUstpFtdcDSOfflineInfoField(Structure):
    """穿透监管线下委托客户信息"""
    _fields_ = [
        ("AppID", c_char * 31),
        ("InvestorID", c_char * 19),
        ("InvestorTel", c_char * 21),
    ]

    def getAppID(self):
        '''AppID'''
        return str(self.AppID, 'GBK')

    def getInvestorID(self):
        '''投资者编号'''
        return str(self.InvestorID, 'GBK')

    def getInvestorTel(self):
        '''投资者手机号'''
        return str(self.InvestorTel, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'AppID'={self.getAppID()}, 'InvestorID'={self.getInvestorID()}, 'InvestorTel'={self.getInvestorTel()}"


class CUstpFtdcReqQryMarginPrefParamField(Structure):
    """查询保证金优惠参数请求"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("CombInstrumentID", c_char * 41),
        ("CombInstrumentName", c_char * 41),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getCombInstrumentName(self):
        '''组合合约名称'''
        return str(self.CombInstrumentName, 'GBK')

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'CombInstrumentName'={self.getCombInstrumentName()}"


class CUstpFtdcRspQryMarginPrefParamField(Structure):
    """查询保证金优惠参数应答"""
    _fields_ = [
        ("BrokerID", c_char * 11),
        ("ExchangeID", c_char * 11),
        ("CombInstrumentID", c_char * 41),
        ("CombInstrumentName", c_char * 41),
        ("CombType", c_char),
        ("HedgeFlag", c_char),
        ("Leg1InstrumentID", c_char * 31),
        ("Leg1ProductID", c_char * 13),
        ("Leg1Direction", c_char),
        ("Leg1HedgeFlag", c_char),
        ("Leg1SettlementPrice", c_double),
        ("Leg2InstrumentID", c_char * 31),
        ("Leg2ProductID", c_char * 13),
        ("Leg2Direction", c_char),
        ("Leg2HedgeFlag", c_char),
        ("Leg2SettlementPrice", c_double),
        ("Priority", c_int32),
        ("TradeEna", c_char),
    ]

    def getBrokerID(self):
        '''经纪公司编号'''
        return str(self.BrokerID, 'GBK')

    def getExchangeID(self):
        '''交易所代码'''
        return str(self.ExchangeID, 'GBK')

    def getCombInstrumentID(self):
        '''组合合约代码'''
        return str(self.CombInstrumentID, 'GBK')

    def getCombInstrumentName(self):
        '''组合合约名称'''
        return str(self.CombInstrumentName, 'GBK')

    def getCombType(self):
        '''组合类型'''
        return TUstpFtdcArbiTypeType(ord(self.CombType)) if ord(self.CombType) in [e.value for e in list(TUstpFtdcArbiTypeType)] else list(TUstpFtdcArbiTypeType)[0]

    def getHedgeFlag(self):
        '''投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.HedgeFlag)) if ord(self.HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getLeg1InstrumentID(self):
        '''腿1合约代码'''
        return str(self.Leg1InstrumentID, 'GBK')

    def getLeg1ProductID(self):
        '''腿1品种代码'''
        return str(self.Leg1ProductID, 'GBK')

    def getLeg1Direction(self):
        '''腿1方向'''
        return TUstpFtdcDirectionType(ord(self.Leg1Direction)) if ord(self.Leg1Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getLeg1HedgeFlag(self):
        '''腿1投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.Leg1HedgeFlag)) if ord(self.Leg1HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getLeg1SettlementPrice(self):
        '''腿1昨结算价'''
        return self.Leg1SettlementPrice

    def getLeg2InstrumentID(self):
        '''腿2合约代码'''
        return str(self.Leg2InstrumentID, 'GBK')

    def getLeg2ProductID(self):
        '''腿2品种代码'''
        return str(self.Leg2ProductID, 'GBK')

    def getLeg2Direction(self):
        '''腿2方向'''
        return TUstpFtdcDirectionType(ord(self.Leg2Direction)) if ord(self.Leg2Direction) in [e.value for e in list(TUstpFtdcDirectionType)] else list(TUstpFtdcDirectionType)[0]

    def getLeg2HedgeFlag(self):
        '''腿2投机套保标志'''
        return TUstpFtdcHedgeFlagType(ord(self.Leg2HedgeFlag)) if ord(self.Leg2HedgeFlag) in [e.value for e in list(TUstpFtdcHedgeFlagType)] else list(TUstpFtdcHedgeFlagType)[0]

    def getLeg2SettlementPrice(self):
        '''腿2昨结算价'''
        return self.Leg2SettlementPrice

    def getPriority(self):
        '''优先级'''
        return self.Priority

    def getTradeEna(self):
        '''是否交易期间优惠'''
        return TUstpFtdcIsActiveType(ord(self.TradeEna)) if ord(self.TradeEna) in [e.value for e in list(TUstpFtdcIsActiveType)] else list(TUstpFtdcIsActiveType)[0]

    def __str__(self):  # 可以直接print
        return f"'BrokerID'={self.getBrokerID()}, 'ExchangeID'={self.getExchangeID()}, 'CombInstrumentID'={self.getCombInstrumentID()}, 'CombInstrumentName'={self.getCombInstrumentName()}, 'CombType'={self.getCombType()}, 'HedgeFlag'={self.getHedgeFlag()}, 'Leg1InstrumentID'={self.getLeg1InstrumentID()}, 'Leg1ProductID'={self.getLeg1ProductID()}, 'Leg1Direction'={self.getLeg1Direction()}, 'Leg1HedgeFlag'={self.getLeg1HedgeFlag()}, 'Leg1SettlementPrice'={self.getLeg1SettlementPrice()}, 'Leg2InstrumentID'={self.getLeg2InstrumentID()}, 'Leg2ProductID'={self.getLeg2ProductID()}, 'Leg2Direction'={self.getLeg2Direction()}, 'Leg2HedgeFlag'={self.getLeg2HedgeFlag()}, 'Leg2SettlementPrice'={self.getLeg2SettlementPrice()}, 'Priority'={self.getPriority()}, 'TradeEna'={self.getTradeEna()}"
