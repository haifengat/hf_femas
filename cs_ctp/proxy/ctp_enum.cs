
/// <summary>
/// 
/// </summary>
public enum THOST_TE_RESUME_TYPE
{
    /// <summary>
    /// 
    /// </summary>
	THOST_TERT_RESTART = 0,
	/// <summary>
    /// 
    /// </summary>
	THOST_TERT_RESUME,
	/// <summary>
    /// 
    /// </summary>
	THOST_TERT_QUICK
}

/// <summary>
/// 密钥加密类型类型
///</summary>
public enum TUstpFtdcDSKeyEncryptType : byte
{
}

/// <summary>
/// AppID和RelayID类型类型
///</summary>
public enum TUstpFtdcDSAppIDTypeType : byte
{
	/// <summary>
	/// 中继操作员模式，即多对一模式
	///</summary>
	USTP_FTDC_DSID_ProxyOperator = (byte)'4',
	/// <summary>
	/// 中继转发模式，即多对多模式
	///</summary>
	USTP_FTDC_DSID_ProxyNoOperator = (byte)'3',
	/// <summary>
	/// IOS或安卓app
	///</summary>
	USTP_FTDC_DSID_App = (byte)'2',
	/// <summary>
	/// PC终端
	///</summary>
	USTP_FTDC_DSID_PC = (byte)'1',
}

/// <summary>
/// 异常标识类型
///</summary>
public enum TUstpFtdcDSExceptionFlagType : byte
{
}

/// <summary>
/// 成交量类型类型
///</summary>
public enum TUstpFtdcVolumeConditionType : byte
{
	/// <summary>
	/// 全部数量
	///</summary>
	USTP_FTDC_VC_CV = (byte)'3',
	/// <summary>
	/// 最小数量
	///</summary>
	USTP_FTDC_VC_MV = (byte)'2',
	/// <summary>
	/// 任何数量
	///</summary>
	USTP_FTDC_VC_AV = (byte)'1',
}

/// <summary>
/// 强平原因类型
///</summary>
public enum TUstpFtdcForceCloseReasonType : byte
{
	/// <summary>
	/// 客户套保超仓
	///</summary>
	USTP_FTDC_FCR_HedgeOverPositionLimit = (byte)'8',
	/// <summary>
	/// 自然人临近交割
	///</summary>
	USTP_FTDC_FCR_PersonDeliv = (byte)'7',
	/// <summary>
	/// 其他
	///</summary>
	USTP_FTDC_FCR_Other = (byte)'6',
	/// <summary>
	/// 违规
	///</summary>
	USTP_FTDC_FCR_Violation = (byte)'5',
	/// <summary>
	/// 持仓非整数倍
	///</summary>
	USTP_FTDC_FCR_NotMultiple = (byte)'4',
	/// <summary>
	/// 会员超仓
	///</summary>
	USTP_FTDC_FCR_MemberOverPositionLimit = (byte)'3',
	/// <summary>
	/// 客户超仓
	///</summary>
	USTP_FTDC_FCR_ClientOverPositionLimit = (byte)'2',
	/// <summary>
	/// 资金不足
	///</summary>
	USTP_FTDC_FCR_LackDeposit = (byte)'1',
	/// <summary>
	/// 非强平
	///</summary>
	USTP_FTDC_FCR_NotForceClose = (byte)'0',
}

/// <summary>
/// 合约交易状态类型
///</summary>
public enum TUstpFtdcInstrumentStatusType : byte
{
	/// <summary>
	/// 收盘
	///</summary>
	USTP_FTDC_IS_Closed = (byte)'6',
	/// <summary>
	/// 集合竞价撮合
	///</summary>
	USTP_FTDC_IS_AuctionMatch = (byte)'5',
	/// <summary>
	/// 集合竞价价格平衡
	///</summary>
	USTP_FTDC_IS_AuctionBalance = (byte)'4',
	/// <summary>
	/// 集合竞价报单
	///</summary>
	USTP_FTDC_IS_AuctionOrdering = (byte)'3',
	/// <summary>
	/// 连续交易
	///</summary>
	USTP_FTDC_IS_Continous = (byte)'2',
	/// <summary>
	/// 非交易
	///</summary>
	USTP_FTDC_IS_NoTrading = (byte)'1',
	/// <summary>
	/// 开盘前
	///</summary>
	USTP_FTDC_IS_BeforeTrading = (byte)'0',
}

/// <summary>
/// 开平标志类型
///</summary>
public enum TUstpFtdcOffsetFlagType : byte
{
	/// <summary>
	/// ALL
	///</summary>
	USTP_FTDC_OF_ALL = (byte)'9',
	/// <summary>
	/// 平昨
	///</summary>
	USTP_FTDC_OF_CloseYesterday = (byte)'4',
	/// <summary>
	/// 平今
	///</summary>
	USTP_FTDC_OF_CloseToday = (byte)'3',
	/// <summary>
	/// 强平
	///</summary>
	USTP_FTDC_OF_ForceClose = (byte)'2',
	/// <summary>
	/// 平仓
	///</summary>
	USTP_FTDC_OF_Close = (byte)'1',
	/// <summary>
	/// 开仓
	///</summary>
	USTP_FTDC_OF_Open = (byte)'0',
}

/// <summary>
/// 报单价格条件类型
///</summary>
public enum TUstpFtdcOrderPriceTypeType : byte
{
	/// <summary>
	/// 限价止盈定单
	///</summary>
	USTP_FTDC_OPT_LimitStopProfitPrice = (byte)'8',
	/// <summary>
	/// 限价止损定单
	///</summary>
	USTP_FTDC_OPT_LimitStopLosPrice = (byte)'7',
	/// <summary>
	/// 止盈定单
	///</summary>
	USTP_FTDC_OPT_StopProfitPrice = (byte)'6',
	/// <summary>
	/// 止损定单
	///</summary>
	USTP_FTDC_OPT_StopLosPrice = (byte)'5',
	/// <summary>
	/// 五档价
	///</summary>
	USTP_FTDC_OPT_FiveLevelPrice = (byte)'4',
	/// <summary>
	/// 最优价
	///</summary>
	USTP_FTDC_OPT_BestPrice = (byte)'3',
	/// <summary>
	/// 限价
	///</summary>
	USTP_FTDC_OPT_LimitPrice = (byte)'2',
	/// <summary>
	/// 任意价
	///</summary>
	USTP_FTDC_OPT_AnyPrice = (byte)'1',
}

/// <summary>
/// 报单状态类型
///</summary>
public enum TUstpFtdcOrderStatusType : byte
{
	/// <summary>
	/// 订单已报入交易所未应答
	///</summary>
	USTP_FTDC_OS_AcceptedNoReply = (byte)'6',
	/// <summary>
	/// 撤单
	///</summary>
	USTP_FTDC_OS_Canceled = (byte)'5',
	/// <summary>
	/// 未成交不在队列中
	///</summary>
	USTP_FTDC_OS_NoTradeNotQueueing = (byte)'4',
	/// <summary>
	/// 未成交还在队列中
	///</summary>
	USTP_FTDC_OS_NoTradeQueueing = (byte)'3',
	/// <summary>
	/// 部分成交不在队列中
	///</summary>
	USTP_FTDC_OS_PartTradedNotQueueing = (byte)'2',
	/// <summary>
	/// 部分成交还在队列中
	///</summary>
	USTP_FTDC_OS_PartTradedQueueing = (byte)'1',
	/// <summary>
	/// 全部成交
	///</summary>
	USTP_FTDC_OS_AllTraded = (byte)'0',
}

/// <summary>
/// 用户类型类型
///</summary>
public enum TUstpFtdcUserTypeType : byte
{
	/// <summary>
	/// 席位
	///</summary>
	USTP_FTDC_UT_Seat = (byte)'4',
	/// <summary>
	/// 期货公司管理员
	///</summary>
	USTP_FTDC_UT_Manager = (byte)'3',
	/// <summary>
	/// 理财产品
	///</summary>
	USTP_FTDC_UT_Product = (byte)'2',
	/// <summary>
	/// 自然人
	///</summary>
	USTP_FTDC_UT_Person = (byte)'1',
}

/// <summary>
/// 交易权限类型
///</summary>
public enum TUstpFtdcTradingRightType : byte
{
	/// <summary>
	/// 不能交易
	///</summary>
	USTP_FTDC_TR_Forbidden = (byte)'2',
	/// <summary>
	/// 只能平仓
	///</summary>
	USTP_FTDC_TR_CloseOnly = (byte)'1',
	/// <summary>
	/// 可以交易
	///</summary>
	USTP_FTDC_TR_Allow = (byte)'0',
}

/// <summary>
/// 有效期类型类型
///</summary>
public enum TUstpFtdcTimeConditionType : byte
{
	/// <summary>
	/// 集合竞价有效
	///</summary>
	USTP_FTDC_TC_GFA = (byte)'6',
	/// <summary>
	/// 撤销前有效
	///</summary>
	USTP_FTDC_TC_GTC = (byte)'5',
	/// <summary>
	/// 指定日期前有效
	///</summary>
	USTP_FTDC_TC_GTD = (byte)'4',
	/// <summary>
	/// 当日有效
	///</summary>
	USTP_FTDC_TC_GFD = (byte)'3',
	/// <summary>
	/// 本节有效
	///</summary>
	USTP_FTDC_TC_GFS = (byte)'2',
	/// <summary>
	/// 立即完成，否则撤销
	///</summary>
	USTP_FTDC_TC_IOC = (byte)'1',
}

/// <summary>
/// 报单来源类型
///</summary>
public enum TUstpFtdcOrderSourceType : byte
{
	/// <summary>
	/// 强减单
	///</summary>
	USTP_FTDC_OS_ForceLower = (byte)'3',
	/// <summary>
	/// 报价单拆分出来的买单或卖单
	///</summary>
	USTP_FTDC_OS_QuoteSplit = (byte)'2',
	/// <summary>
	/// 来自管理员
	///</summary>
	USTP_FTDC_OS_Administrator = (byte)'1',
	/// <summary>
	/// 来自参与者
	///</summary>
	USTP_FTDC_OS_Participant = (byte)'0',
}

/// <summary>
/// 买卖方向类型
///</summary>
public enum TUstpFtdcDirectionType : byte
{
	/// <summary>
	/// ALL
	///</summary>
	USTP_FTDC_D_ALL = (byte)'9',
	/// <summary>
	/// 卖
	///</summary>
	USTP_FTDC_D_Sell = (byte)'1',
	/// <summary>
	/// 买
	///</summary>
	USTP_FTDC_D_Buy = (byte)'0',
}

/// <summary>
/// 币种类型
///</summary>
public enum TUstpFtdcCurrencyType : byte
{
	/// <summary>
	/// 美元
	///</summary>
	USTP_FTDC_C_UDOLLAR = (byte)'2',
	/// <summary>
	/// 人民币
	///</summary>
	USTP_FTDC_C_RMB = (byte)'1',
}

/// <summary>
/// 出入金方向类型
///</summary>
public enum TUstpFtdcAccountDirectionType : byte
{
	/// <summary>
	/// 出金
	///</summary>
	USTP_FTDC_AD_Out = (byte)'2',
	/// <summary>
	/// 入金
	///</summary>
	USTP_FTDC_AD_In = (byte)'1',
}

/// <summary>
/// 出入金通知类型
///</summary>
public enum TUstpFtdcSyncDirectionType : byte
{
	/// <summary>
	/// 待入金
	///</summary>
	USTP_FTDC_AD_PreIn = (byte)'8',
	/// <summary>
	/// 预出金失败通知
	///</summary>
	USTP_FTDC_AD_PreOutFailed = (byte)'7',
	/// <summary>
	/// 预出金成功通知
	///</summary>
	USTP_FTDC_AD_PreOutSuccess = (byte)'6',
	/// <summary>
	/// 预出金通知
	///</summary>
	USTP_FTDC_AD_PreOut = (byte)'5',
	/// <summary>
	/// 出金冲销通知
	///</summary>
	USTP_FTDC_AD_OutReserval = (byte)'4',
	/// <summary>
	/// 入金冲销通知
	///</summary>
	USTP_FTDC_AD_InReserval = (byte)'3',
	/// <summary>
	/// 出金通知
	///</summary>
	USTP_FTDC_AD_Out = (byte)'2',
	/// <summary>
	/// 入金通知
	///</summary>
	USTP_FTDC_AD_In = (byte)'1',
}

/// <summary>
/// 同步请求发起方类型
///</summary>
public enum TUstpFtdcTradeSyncSourceType : byte
{
	/// <summary>
	/// 结算
	///</summary>
	USTP_FTDC_TSS_Settle = (byte)'4',
	/// <summary>
	/// 银行
	///</summary>
	USTP_FTDC_TSS_Bank = (byte)'3',
	/// <summary>
	/// 次席终端
	///</summary>
	USTP_FTDC_TSS_Terminal_Second = (byte)'2',
	/// <summary>
	/// 终端
	///</summary>
	USTP_FTDC_TSS_Terminal = (byte)'1',
}

/// <summary>
/// 投机套保标志类型
///</summary>
public enum TUstpFtdcHedgeFlagType : byte
{
	/// <summary>
	/// 匹配所有的值
	///</summary>
	USTP_FTDC_CHF_AllValue = (byte)'9',
	/// <summary>
	/// 套保-投机
	///</summary>
	USTP_FTDC_CHF_HedgeSpec = (byte)'6',
	/// <summary>
	/// 投机-套保
	///</summary>
	USTP_FTDC_CHF_SpecHedge = (byte)'5',
	/// <summary>
	/// 做市商
	///</summary>
	USTP_FTDC_CHF_MarketMaker = (byte)'4',
	/// <summary>
	/// 套保
	///</summary>
	USTP_FTDC_CHF_Hedge = (byte)'3',
	/// <summary>
	/// 套利
	///</summary>
	USTP_FTDC_CHF_Arbitrage = (byte)'2',
	/// <summary>
	/// 交易/投机
	///</summary>
	USTP_FTDC_CHF_Speculation = (byte)'1',
}

/// <summary>
/// 操作标志类型
///</summary>
public enum TUstpFtdcActionFlagType : byte
{
	/// <summary>
	/// 修改
	///</summary>
	USTP_FTDC_AF_Modify = (byte)'3',
	/// <summary>
	/// 激活
	///</summary>
	USTP_FTDC_AF_Active = (byte)'2',
	/// <summary>
	/// 挂起
	///</summary>
	USTP_FTDC_AF_Suspend = (byte)'1',
	/// <summary>
	/// 删除
	///</summary>
	USTP_FTDC_AF_Delete = (byte)'0',
}

/// <summary>
/// 持仓类型类型
///</summary>
public enum TUstpFtdcPositionTypeType : byte
{
	/// <summary>
	/// 综合持仓
	///</summary>
	USTP_FTDC_PT_Gross = (byte)'2',
	/// <summary>
	/// 净持仓
	///</summary>
	USTP_FTDC_PT_Net = (byte)'1',
}

/// <summary>
/// 期权类型类型
///</summary>
public enum TUstpFtdcOptionsTypeType : byte
{
	/// <summary>
	/// 全部
	///</summary>
	USTP_FTDC_OT_ALL = (byte)'9',
	/// <summary>
	/// 看跌
	///</summary>
	USTP_FTDC_OT_PutOptions = (byte)'2',
	/// <summary>
	/// 看涨
	///</summary>
	USTP_FTDC_OT_CallOptions = (byte)'1',
	/// <summary>
	/// 非期权
	///</summary>
	USTP_FTDC_OT_NotOptions = (byte)'0',
}

/// <summary>
/// 是否活跃类型
///</summary>
public enum TUstpFtdcIsActiveType : byte
{
	/// <summary>
	/// 活跃
	///</summary>
	USTP_FTDC_UIA_Active = (byte)'1',
	/// <summary>
	/// 不活跃
	///</summary>
	USTP_FTDC_UIA_NoActive = (byte)'0',
}

/// <summary>
/// 组合保证金类型类型
///</summary>
public enum TUstpFtdcClientMarginCombTypeType : byte
{
	/// <summary>
	/// 自动策略大边保证金组合
	///</summary>
	USTP_FTDC_MCT_StrategyBigLegAuto = (byte)'5',
	/// <summary>
	/// 手动策略大边保证金组合
	///</summary>
	USTP_FTDC_MCT_StrategyBigLegManual = (byte)'4',
	/// <summary>
	/// 自动策略保证金组合
	///</summary>
	USTP_FTDC_MCT_StrategyAuto = (byte)'3',
	/// <summary>
	/// 手动策略保证金组合
	///</summary>
	USTP_FTDC_MCT_StrategyManual = (byte)'2',
	/// <summary>
	/// 合约组大边保证金组合
	///</summary>
	USTP_FTDC_MCT_BigLeg = (byte)'1',
	/// <summary>
	/// 单腿保证金组合
	///</summary>
	USTP_FTDC_MCT_SingleLeg = (byte)'0',
}

/// <summary>
/// 授权功能号类型
///</summary>
public enum TUstpFtdcGrantFuncSetType : byte
{
	/// <summary>
	/// 禁止交易
	///</summary>
	USTP_FTDC_FUNC_CanotTrade = (byte)'2',
	/// <summary>
	/// 只能平仓
	///</summary>
	USTP_FTDC_FUNC_CloseOnly = (byte)'1',
	/// <summary>
	/// 正常交易
	///</summary>
	USTP_FTDC_FUNC_Trading = (byte)'0',
}

/// <summary>
/// 报价单状态类型类型
///</summary>
public enum TUstpFtdcQuoteStatusType : byte
{
	/// <summary>
	/// 错误的撤消报价请求
	///</summary>
	USTP_FTDC_QS_Error_QuoteAction = (byte)'6',
	/// <summary>
	/// 已经全部成交
	///</summary>
	USTP_FTDC_QS_Traded_All = (byte)'5',
	/// <summary>
	/// 已经有单腿成交
	///</summary>
	USTP_FTDC_QS_Traded_SingleLeg = (byte)'4',
	/// <summary>
	/// 已经全部撤掉
	///</summary>
	USTP_FTDC_QS_Canceled_All = (byte)'3',
	/// <summary>
	/// 已经撤掉单腿
	///</summary>
	USTP_FTDC_QS_Canceled_SingleLeg = (byte)'2',
	/// <summary>
	/// 已经报入交易系统中
	///</summary>
	USTP_FTDC_QS_Accepted_InTradingSystem = (byte)'1',
	/// <summary>
	/// 在飞马中还未进入交易系统
	///</summary>
	USTP_FTDC_QS_Inited_InFEMAS = (byte)'0',
}

/// <summary>
/// 申请保证金组合指令方向类型
///</summary>
public enum TUstpFtdcCombDirectionType : byte
{
	/// <summary>
	/// 申请拆分组合
	///</summary>
	USTP_FTDC_CA_UnCombine = (byte)'1',
	/// <summary>
	/// 申请组合
	///</summary>
	USTP_FTDC_CA_Combine = (byte)'0',
}

/// <summary>
/// 策略类别类型
///</summary>
public enum TUstpFtdcArbiTypeType : byte
{
	/// <summary>
	/// 对锁
	///</summary>
	USTP_FTDC_AT_LOC = (byte)'h',
	/// <summary>
	/// 备兑
	///</summary>
	USTP_FTDC_AT_PRT = (byte)'g',
	/// <summary>
	/// 宽跨式
	///</summary>
	USTP_FTDC_AT_STG = (byte)'f',
	/// <summary>
	/// 跨式
	///</summary>
	USTP_FTDC_AT_STD = (byte)'e',
	/// <summary>
	/// 看跌期权水平价差
	///</summary>
	USTP_FTDC_AT_BRT = (byte)'d',
	/// <summary>
	/// 看涨期权水平价差
	///</summary>
	USTP_FTDC_AT_BLT = (byte)'c',
	/// <summary>
	/// 看跌期权垂直价差
	///</summary>
	USTP_FTDC_AT_BER = (byte)'b',
	/// <summary>
	/// 看涨期权垂直价差
	///</summary>
	USTP_FTDC_AT_BUL = (byte)'a',
	/// <summary>
	/// 其他策略
	///</summary>
	USTP_FTDC_AT_Other = (byte)'9',
	/// <summary>
	/// 互换
	///</summary>
	USTP_FTDC_AT_Swap = (byte)'8',
	/// <summary>
	/// 双边报价
	///</summary>
	USTP_FTDC_AT_Both = (byte)'7',
	/// <summary>
	/// 期权执行申请
	///</summary>
	USTP_FTDC_AT_Exec = (byte)'6',
	/// <summary>
	/// 批量
	///</summary>
	USTP_FTDC_AT_Strip = (byte)'5',
	/// <summary>
	/// 组合
	///</summary>
	USTP_FTDC_AT_Combo = (byte)'4',
	/// <summary>
	/// 压榨套利
	///</summary>
	USTP_FTDC_AT_SPX = (byte)'3',
	/// <summary>
	/// 两腿跨品种套利
	///</summary>
	USTP_FTDC_AT_SPC = (byte)'2',
	/// <summary>
	/// 跨期套利
	///</summary>
	USTP_FTDC_AT_SP = (byte)'1',
	/// <summary>
	/// 基本
	///</summary>
	USTP_FTDC_AT_Basic = (byte)'0',
}

/// <summary>
/// 委托类型类型
///</summary>
public enum TUstpFtdcOrderTypeType : byte
{
	/// <summary>
	/// 期转现衍生
	///</summary>
	USTP_FTDC_OT_EFPDerived = (byte)'4',
	/// <summary>
	/// OTC衍生
	///</summary>
	USTP_FTDC_OT_OTCDerived = (byte)'3',
	/// <summary>
	/// 放弃执行
	///</summary>
	USTP_FTDC_OT_OptAbandon = (byte)'2',
	/// <summary>
	/// 期权执行
	///</summary>
	USTP_FTDC_OT_OptExec = (byte)'1',
	/// <summary>
	/// 普通委托
	///</summary>
	USTP_FTDC_OT_Common = (byte)'0',
}

/// <summary>
/// 执行类型类型
///</summary>
public enum TUstpFtdcDeliveryFlagType : byte
{
	/// <summary>
	/// 履约后不对冲
	///</summary>
	USTP_FTDC_DF_SellNoDelivery = (byte)'5',
	/// <summary>
	/// 履约后对冲
	///</summary>
	USTP_FTDC_DF_SellDelivery = (byte)'4',
	/// <summary>
	/// 保留持仓
	///</summary>
	USTP_FTDC_DF_OptHold = (byte)'3',
	/// <summary>
	/// 对冲(期权)
	///</summary>
	USTP_FTDC_DF_OptDelivery = (byte)'2',
	/// <summary>
	/// 对冲(期货)
	///</summary>
	USTP_FTDC_DF_Delivery = (byte)'1',
	/// <summary>
	/// 不对冲
	///</summary>
	USTP_FTDC_DF_ExecOpen = (byte)'0',
}

/// <summary>
/// 组合操作状态类型
///</summary>
public enum TUstpFtdcCombActionStatusType : byte
{
	/// <summary>
	/// 已拒绝
	///</summary>
	USTP_FTDC_CAS_Rejected = (byte)'3',
	/// <summary>
	/// 已接收
	///</summary>
	USTP_FTDC_CAS_Accepted = (byte)'2',
	/// <summary>
	/// 已提交
	///</summary>
	USTP_FTDC_CAS_Submitted = (byte)'1',
}

/// <summary>
/// 客户认证类型类型
///</summary>
public enum TUstpFtdcAuthenticate2TypeType : byte
{
	/// <summary>
	/// 图形验证码
	///</summary>
	USTP_FTDC_A2T_GraphicVerificationCode = (byte)'3',
	/// <summary>
	/// 动态令牌
	///</summary>
	USTP_FTDC_A2T_DynamicToken = (byte)'2',
	/// <summary>
	/// 短信验证码
	///</summary>
	USTP_FTDC_A2T_ShortMessage = (byte)'1',
	/// <summary>
	/// 初始值，空，表示未设口令。即不需要进行口令验证
	///</summary>
	USTP_FTDC_A2T_Blank = (byte)'0',
}

