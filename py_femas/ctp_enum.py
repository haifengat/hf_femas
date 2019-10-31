#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class USTP_TE_RESUME_TYPE(Enum):
    USTP_TERT_RESTART = 0
    USTP_TERT_RESUME = 1
    USTP_TERT_QUICK = 2


class TUstpFtdcDSKeyEncryptType(Enum):
    """密钥加密类型类型"""
    Normal = 49  # 特别添加,原文件此枚举无内容


class TUstpFtdcDSAppIDTypeType(Enum):
    """AppID和RelayID类型类型"""
    USTP_FTDC_DSID_PC = 49
    """PC终端"""
    USTP_FTDC_DSID_App = 50
    """IOS或安卓app"""
    USTP_FTDC_DSID_ProxyNoOperator = 51
    """中继转发模式，即多对多模式"""
    USTP_FTDC_DSID_ProxyOperator = 52
    """中继操作员模式，即多对一模式"""


class TUstpFtdcDSExceptionFlagType(Enum):
    """异常标识类型"""
    Normal = 49


class TUstpFtdcVolumeConditionType(Enum):
    """成交量类型类型"""
    USTP_FTDC_VC_AV = 49
    """任何数量"""
    USTP_FTDC_VC_MV = 50
    """最小数量"""
    USTP_FTDC_VC_CV = 51
    """全部数量"""


class TUstpFtdcForceCloseReasonType(Enum):
    """强平原因类型"""
    USTP_FTDC_FCR_NotForceClose = 48
    """非强平"""
    USTP_FTDC_FCR_LackDeposit = 49
    """资金不足"""
    USTP_FTDC_FCR_ClientOverPositionLimit = 50
    """客户超仓"""
    USTP_FTDC_FCR_MemberOverPositionLimit = 51
    """会员超仓"""
    USTP_FTDC_FCR_NotMultiple = 52
    """持仓非整数倍"""
    USTP_FTDC_FCR_Violation = 53
    """违规"""
    USTP_FTDC_FCR_Other = 54
    """其他"""
    USTP_FTDC_FCR_PersonDeliv = 55
    """自然人临近交割"""
    USTP_FTDC_FCR_HedgeOverPositionLimit = 56
    """客户套保超仓"""


class TUstpFtdcInstrumentStatusType(Enum):
    """合约交易状态类型"""
    USTP_FTDC_IS_BeforeTrading = 48
    """开盘前"""
    USTP_FTDC_IS_NoTrading = 49
    """非交易"""
    USTP_FTDC_IS_Continous = 50
    """连续交易"""
    USTP_FTDC_IS_AuctionOrdering = 51
    """集合竞价报单"""
    USTP_FTDC_IS_AuctionBalance = 52
    """集合竞价价格平衡"""
    USTP_FTDC_IS_AuctionMatch = 53
    """集合竞价撮合"""
    USTP_FTDC_IS_Closed = 54
    """收盘"""


class TUstpFtdcOffsetFlagType(Enum):
    """开平标志类型"""
    USTP_FTDC_OF_Open = 48
    """开仓"""
    USTP_FTDC_OF_Close = 49
    """平仓"""
    USTP_FTDC_OF_ForceClose = 50
    """强平"""
    USTP_FTDC_OF_CloseToday = 51
    """平今"""
    USTP_FTDC_OF_CloseYesterday = 52
    """平昨"""
    USTP_FTDC_OF_ALL = 57
    """ALL"""


class TUstpFtdcOrderPriceTypeType(Enum):
    """报单价格条件类型"""
    USTP_FTDC_OPT_AnyPrice = 49
    """任意价"""
    USTP_FTDC_OPT_LimitPrice = 50
    """限价"""
    USTP_FTDC_OPT_BestPrice = 51
    """最优价"""
    USTP_FTDC_OPT_FiveLevelPrice = 52
    """五档价"""
    USTP_FTDC_OPT_StopLosPrice = 53
    """止损定单"""
    USTP_FTDC_OPT_StopProfitPrice = 54
    """止盈定单"""
    USTP_FTDC_OPT_LimitStopLosPrice = 55
    """限价止损定单"""
    USTP_FTDC_OPT_LimitStopProfitPrice = 56
    """限价止盈定单"""


class TUstpFtdcOrderStatusType(Enum):
    """报单状态类型"""
    USTP_FTDC_OS_AllTraded = 48
    """全部成交"""
    USTP_FTDC_OS_PartTradedQueueing = 49
    """部分成交还在队列中"""
    USTP_FTDC_OS_PartTradedNotQueueing = 50
    """部分成交不在队列中"""
    USTP_FTDC_OS_NoTradeQueueing = 51
    """未成交还在队列中"""
    USTP_FTDC_OS_NoTradeNotQueueing = 52
    """未成交不在队列中"""
    USTP_FTDC_OS_Canceled = 53
    """撤单"""
    USTP_FTDC_OS_AcceptedNoReply = 54
    """订单已报入交易所未应答"""


class TUstpFtdcUserTypeType(Enum):
    """用户类型类型"""
    USTP_FTDC_UT_Person = 49
    """自然人"""
    USTP_FTDC_UT_Product = 50
    """理财产品"""
    USTP_FTDC_UT_Manager = 51
    """期货公司管理员"""
    USTP_FTDC_UT_Seat = 52
    """席位"""


class TUstpFtdcTradingRightType(Enum):
    """交易权限类型"""
    USTP_FTDC_TR_Allow = 48
    """可以交易"""
    USTP_FTDC_TR_CloseOnly = 49
    """只能平仓"""
    USTP_FTDC_TR_Forbidden = 50
    """不能交易"""


class TUstpFtdcTimeConditionType(Enum):
    """有效期类型类型"""
    USTP_FTDC_TC_IOC = 49
    """立即完成，否则撤销"""
    USTP_FTDC_TC_GFS = 50
    """本节有效"""
    USTP_FTDC_TC_GFD = 51
    """当日有效"""
    USTP_FTDC_TC_GTD = 52
    """指定日期前有效"""
    USTP_FTDC_TC_GTC = 53
    """撤销前有效"""
    USTP_FTDC_TC_GFA = 54
    """集合竞价有效"""


class TUstpFtdcOrderSourceType(Enum):
    """报单来源类型"""
    USTP_FTDC_OS_Participant = 48
    """来自参与者"""
    USTP_FTDC_OS_Administrator = 49
    """来自管理员"""
    USTP_FTDC_OS_QuoteSplit = 50
    """报价单拆分出来的买单或卖单"""
    USTP_FTDC_OS_ForceLower = 51
    """强减单"""


class TUstpFtdcDirectionType(Enum):
    """买卖方向类型"""
    USTP_FTDC_D_Buy = 48
    """买"""
    USTP_FTDC_D_Sell = 49
    """卖"""
    USTP_FTDC_D_ALL = 57
    """ALL"""


class TUstpFtdcCurrencyType(Enum):
    """币种类型"""
    USTP_FTDC_C_RMB = 49
    """人民币"""
    USTP_FTDC_C_UDOLLAR = 50
    """美元"""


class TUstpFtdcAccountDirectionType(Enum):
    """出入金方向类型"""
    USTP_FTDC_AD_In = 49
    """入金"""
    USTP_FTDC_AD_Out = 50
    """出金"""


class TUstpFtdcSyncDirectionType(Enum):
    """出入金通知类型"""
    USTP_FTDC_AD_In = 49
    """入金通知"""
    USTP_FTDC_AD_Out = 50
    """出金通知"""
    USTP_FTDC_AD_InReserval = 51
    """入金冲销通知"""
    USTP_FTDC_AD_OutReserval = 52
    """出金冲销通知"""
    USTP_FTDC_AD_PreOut = 53
    """预出金通知"""
    USTP_FTDC_AD_PreOutSuccess = 54
    """预出金成功通知"""
    USTP_FTDC_AD_PreOutFailed = 55
    """预出金失败通知"""
    USTP_FTDC_AD_PreIn = 56
    """待入金"""


class TUstpFtdcTradeSyncSourceType(Enum):
    """同步请求发起方类型"""
    USTP_FTDC_TSS_Terminal = 49
    """终端"""
    USTP_FTDC_TSS_Terminal_Second = 50
    """次席终端"""
    USTP_FTDC_TSS_Bank = 51
    """银行"""
    USTP_FTDC_TSS_Settle = 52
    """结算"""


class TUstpFtdcHedgeFlagType(Enum):
    """投机套保标志类型"""
    USTP_FTDC_CHF_Speculation = 49
    """交易/投机"""
    USTP_FTDC_CHF_Arbitrage = 50
    """套利"""
    USTP_FTDC_CHF_Hedge = 51
    """套保"""
    USTP_FTDC_CHF_MarketMaker = 52
    """做市商"""
    USTP_FTDC_CHF_SpecHedge = 53
    """投机-套保"""
    USTP_FTDC_CHF_HedgeSpec = 54
    """套保-投机"""
    USTP_FTDC_CHF_AllValue = 57
    """匹配所有的值"""


class TUstpFtdcActionFlagType(Enum):
    """操作标志类型"""
    USTP_FTDC_AF_Delete = 48
    """删除"""
    USTP_FTDC_AF_Suspend = 49
    """挂起"""
    USTP_FTDC_AF_Active = 50
    """激活"""
    USTP_FTDC_AF_Modify = 51
    """修改"""


class TUstpFtdcPositionTypeType(Enum):
    """持仓类型类型"""
    USTP_FTDC_PT_Net = 49
    """净持仓"""
    USTP_FTDC_PT_Gross = 50
    """综合持仓"""


class TUstpFtdcOptionsTypeType(Enum):
    """期权类型类型"""
    USTP_FTDC_OT_NotOptions = 48
    """非期权"""
    USTP_FTDC_OT_CallOptions = 49
    """看涨"""
    USTP_FTDC_OT_PutOptions = 50
    """看跌"""
    USTP_FTDC_OT_ALL = 57
    """全部"""


class TUstpFtdcIsActiveType(Enum):
    """是否活跃类型"""
    USTP_FTDC_UIA_NoActive = 48
    """不活跃"""
    USTP_FTDC_UIA_Active = 49
    """活跃"""


class TUstpFtdcClientMarginCombTypeType(Enum):
    """组合保证金类型类型"""
    USTP_FTDC_MCT_SingleLeg = 48
    """单腿保证金组合"""
    USTP_FTDC_MCT_BigLeg = 49
    """合约组大边保证金组合"""
    USTP_FTDC_MCT_StrategyManual = 50
    """手动策略保证金组合"""
    USTP_FTDC_MCT_StrategyAuto = 51
    """自动策略保证金组合"""
    USTP_FTDC_MCT_StrategyBigLegManual = 52
    """手动策略大边保证金组合"""
    USTP_FTDC_MCT_StrategyBigLegAuto = 53
    """自动策略大边保证金组合"""


class TUstpFtdcGrantFuncSetType(Enum):
    """授权功能号类型"""
    USTP_FTDC_FUNC_Trading = 48
    """正常交易"""
    USTP_FTDC_FUNC_CloseOnly = 49
    """只能平仓"""
    USTP_FTDC_FUNC_CanotTrade = 50
    """禁止交易"""


class TUstpFtdcQuoteStatusType(Enum):
    """报价单状态类型类型"""
    USTP_FTDC_QS_Inited_InFEMAS = 48
    """在飞马中还未进入交易系统"""
    USTP_FTDC_QS_Accepted_InTradingSystem = 49
    """已经报入交易系统中"""
    USTP_FTDC_QS_Canceled_SingleLeg = 50
    """已经撤掉单腿"""
    USTP_FTDC_QS_Canceled_All = 51
    """已经全部撤掉"""
    USTP_FTDC_QS_Traded_SingleLeg = 52
    """已经有单腿成交"""
    USTP_FTDC_QS_Traded_All = 53
    """已经全部成交"""
    USTP_FTDC_QS_Error_QuoteAction = 54
    """错误的撤消报价请求"""


class TUstpFtdcCombDirectionType(Enum):
    """申请保证金组合指令方向类型"""
    USTP_FTDC_CA_Combine = 48
    """申请组合"""
    USTP_FTDC_CA_UnCombine = 49
    """申请拆分组合"""


class TUstpFtdcArbiTypeType(Enum):
    """策略类别类型"""
    USTP_FTDC_AT_Basic = 48
    """基本"""
    USTP_FTDC_AT_SP = 49
    """跨期套利"""
    USTP_FTDC_AT_SPC = 50
    """两腿跨品种套利"""
    USTP_FTDC_AT_SPX = 51
    """压榨套利"""
    USTP_FTDC_AT_Combo = 52
    """组合"""
    USTP_FTDC_AT_Strip = 53
    """批量"""
    USTP_FTDC_AT_Exec = 54
    """期权执行申请"""
    USTP_FTDC_AT_Both = 55
    """双边报价"""
    USTP_FTDC_AT_Swap = 56
    """互换"""
    USTP_FTDC_AT_Other = 57
    """其他策略"""
    USTP_FTDC_AT_BUL = 97
    """看涨期权垂直价差"""
    USTP_FTDC_AT_BER = 98
    """看跌期权垂直价差"""
    USTP_FTDC_AT_BLT = 99
    """看涨期权水平价差"""
    USTP_FTDC_AT_BRT = 100
    """看跌期权水平价差"""
    USTP_FTDC_AT_STD = 101
    """跨式"""
    USTP_FTDC_AT_STG = 102
    """宽跨式"""
    USTP_FTDC_AT_PRT = 103
    """备兑"""
    USTP_FTDC_AT_LOC = 104
    """对锁"""


class TUstpFtdcOrderTypeType(Enum):
    """委托类型类型"""
    USTP_FTDC_OT_Common = 48
    """普通委托"""
    USTP_FTDC_OT_OptExec = 49
    """期权执行"""
    USTP_FTDC_OT_OptAbandon = 50
    """放弃执行"""
    USTP_FTDC_OT_OTCDerived = 51
    """OTC衍生"""
    USTP_FTDC_OT_EFPDerived = 52
    """期转现衍生"""


class TUstpFtdcDeliveryFlagType(Enum):
    """执行类型类型"""
    USTP_FTDC_DF_ExecOpen = 48
    """不对冲"""
    USTP_FTDC_DF_Delivery = 49
    """对冲(期货)"""
    USTP_FTDC_DF_OptDelivery = 50
    """对冲(期权)"""
    USTP_FTDC_DF_OptHold = 51
    """保留持仓"""
    USTP_FTDC_DF_SellDelivery = 52
    """履约后对冲"""
    USTP_FTDC_DF_SellNoDelivery = 53
    """履约后不对冲"""


class TUstpFtdcCombActionStatusType(Enum):
    """组合操作状态类型"""
    USTP_FTDC_CAS_Submitted = 49
    """已提交"""
    USTP_FTDC_CAS_Accepted = 50
    """已接收"""
    USTP_FTDC_CAS_Rejected = 51
    """已拒绝"""


class TUstpFtdcAuthenticate2TypeType(Enum):
    """客户认证类型类型"""
    USTP_FTDC_A2T_Blank = 48
    """初始值，空，表示未设口令。即不需要进行口令验证"""
    USTP_FTDC_A2T_ShortMessage = 49
    """短信验证码"""
    USTP_FTDC_A2T_DynamicToken = 50
    """动态令牌"""
    USTP_FTDC_A2T_GraphicVerificationCode = 51
    """图形验证码"""
