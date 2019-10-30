using System.Runtime.InteropServices;


/// <summary>
/// 系统用户登录应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspUserLoginField
{
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 登录成功时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string LoginTime;
	/// <summary>
	/// 登录成功时的交易所时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ExchangeTime;
	/// <summary>
	/// 用户最大本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string MaxOrderLocalID;
	/// <summary>
	/// 交易系统名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=61)]
	public string TradingSystemName;
	/// <summary>
	/// 数据中心代码
	/// </summary>
	public int DataCenterID;
	/// <summary>
	/// 会员私有流当前长度
	/// </summary>
	public int PrivateFlowSize;
	/// <summary>
	/// 交易员私有流当前长度
	/// </summary>
	public int UserFlowSize;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 飞马版本号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string FemasVersion;
	/// <summary>
	/// 飞马生命周期号
	/// </summary>
	public int FemasLifeCycle;
}

/// <summary>
/// 用户登出请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqUserLogoutField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
}

/// <summary>
/// 用户登出响应
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspUserLogoutField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
}

/// <summary>
/// 强制用户退出
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcForceUserExitField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
}

/// <summary>
/// 用户口令修改
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcUserPasswordUpdateField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 旧密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string OldPassword;
	/// <summary>
	/// 新密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string NewPassword;
}

/// <summary>
/// 输入报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInputOrderField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 指定通过此席位序号下单
	/// </summary>
	public int SeatNo;
	/// <summary>
	/// 合约代码/套利组合合约号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 用户本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 报单类型
	/// </summary>
	public TUstpFtdcOrderPriceTypeType OrderPriceType;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType OffsetFlag;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 有效期类型
	/// </summary>
	public TUstpFtdcTimeConditionType TimeCondition;
	/// <summary>
	/// GTD日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string GTDDate;
	/// <summary>
	/// 成交量类型
	/// </summary>
	public TUstpFtdcVolumeConditionType VolumeCondition;
	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;
	/// <summary>
	/// 止损价止赢价
	/// </summary>
	public double StopPrice;
	/// <summary>
	/// 强平原因
	/// </summary>
	public TUstpFtdcForceCloseReasonType ForceCloseReason;
	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 报单操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcOrderActionField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 本次撤单操作的本地编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderActionLocalID;
	/// <summary>
	/// 被撤订单的本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 报单操作标志
	/// </summary>
	public TUstpFtdcActionFlagType ActionFlag;
	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;
	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 内存表导出
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMemDbField
{
	/// <summary>
	/// 内存表名
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=61)]
	public string MemTableName;
}

/// <summary>
/// 响应信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInfoField
{
	/// <summary>
	/// 错误代码
	/// </summary>
	public int ErrorID;
	/// <summary>
	/// 错误信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=81)]
	public string ErrorMsg;
}

/// <summary>
/// 报单查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryOrderField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 报单状态
	/// </summary>
	public TUstpFtdcOrderStatusType OrderStatus;
	/// <summary>
	/// 委托类型
	/// </summary>
	public TUstpFtdcOrderTypeType OrderType;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 成交查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryTradeField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 成交编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string TradeID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 合约查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInstrumentField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 产品代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string ProductID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
}

/// <summary>
/// 合约查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInstrumentField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 品种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string ProductID;
	/// <summary>
	/// 品种名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string ProductName;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 合约名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string InstrumentName;
	/// <summary>
	/// 交割年份
	/// </summary>
	public int DeliveryYear;
	/// <summary>
	/// 交割月
	/// </summary>
	public int DeliveryMonth;
	/// <summary>
	/// 限价单最大下单量
	/// </summary>
	public int MaxLimitOrderVolume;
	/// <summary>
	/// 限价单最小下单量
	/// </summary>
	public int MinLimitOrderVolume;
	/// <summary>
	/// 市价单最大下单量
	/// </summary>
	public int MaxMarketOrderVolume;
	/// <summary>
	/// 市价单最小下单量
	/// </summary>
	public int MinMarketOrderVolume;
	/// <summary>
	/// 数量乘数
	/// </summary>
	public int VolumeMultiple;
	/// <summary>
	/// 报价单位
	/// </summary>
	public double PriceTick;
	/// <summary>
	/// 币种
	/// </summary>
	public TUstpFtdcCurrencyType Currency;
	/// <summary>
	/// 多头限仓
	/// </summary>
	public int LongPosLimit;
	/// <summary>
	/// 空头限仓
	/// </summary>
	public int ShortPosLimit;
	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;
	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;
	/// <summary>
	/// 昨结算
	/// </summary>
	public double PreSettlementPrice;
	/// <summary>
	/// 合约交易状态
	/// </summary>
	public TUstpFtdcInstrumentStatusType InstrumentStatus;
	/// <summary>
	/// 创建日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CreateDate;
	/// <summary>
	/// 上市日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string OpenDate;
	/// <summary>
	/// 到期日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ExpireDate;
	/// <summary>
	/// 开始交割日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string StartDelivDate;
	/// <summary>
	/// 最后交割日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string EndDelivDate;
	/// <summary>
	/// 挂牌基准价
	/// </summary>
	public double BasisPrice;
	/// <summary>
	/// 当前是否交易
	/// </summary>
	public int IsTrading;
	/// <summary>
	/// 基础商品代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string UnderlyingInstrID;
	/// <summary>
	/// 基础商品乘数
	/// </summary>
	public int UnderlyingMultiple;
	/// <summary>
	/// 持仓类型
	/// </summary>
	public TUstpFtdcPositionTypeType PositionType;
	/// <summary>
	/// 执行价
	/// </summary>
	public double StrikePrice;
	/// <summary>
	/// 期权类型
	/// </summary>
	public TUstpFtdcOptionsTypeType OptionsType;
	/// <summary>
	/// 币种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=5)]
	public string CurrencyID;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 第一腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_1;
	/// <summary>
	/// 第一腿买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction_1;
	/// <summary>
	/// 第一腿数量比例
	/// </summary>
	public double Ratio_1;
	/// <summary>
	/// 第二腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_2;
	/// <summary>
	/// 第二腿买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction_2;
	/// <summary>
	/// 第二腿数量比例
	/// </summary>
	public double Ratio_2;
}

/// <summary>
/// 合约状态
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInstrumentStatusField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 品种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string ProductID;
	/// <summary>
	/// 品种名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string ProductName;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 合约名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string InstrumentName;
	/// <summary>
	/// 交割年份
	/// </summary>
	public int DeliveryYear;
	/// <summary>
	/// 交割月
	/// </summary>
	public int DeliveryMonth;
	/// <summary>
	/// 限价单最大下单量
	/// </summary>
	public int MaxLimitOrderVolume;
	/// <summary>
	/// 限价单最小下单量
	/// </summary>
	public int MinLimitOrderVolume;
	/// <summary>
	/// 市价单最大下单量
	/// </summary>
	public int MaxMarketOrderVolume;
	/// <summary>
	/// 市价单最小下单量
	/// </summary>
	public int MinMarketOrderVolume;
	/// <summary>
	/// 数量乘数
	/// </summary>
	public int VolumeMultiple;
	/// <summary>
	/// 报价单位
	/// </summary>
	public double PriceTick;
	/// <summary>
	/// 币种
	/// </summary>
	public TUstpFtdcCurrencyType Currency;
	/// <summary>
	/// 多头限仓
	/// </summary>
	public int LongPosLimit;
	/// <summary>
	/// 空头限仓
	/// </summary>
	public int ShortPosLimit;
	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;
	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;
	/// <summary>
	/// 昨结算
	/// </summary>
	public double PreSettlementPrice;
	/// <summary>
	/// 合约交易状态
	/// </summary>
	public TUstpFtdcInstrumentStatusType InstrumentStatus;
	/// <summary>
	/// 创建日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CreateDate;
	/// <summary>
	/// 上市日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string OpenDate;
	/// <summary>
	/// 到期日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ExpireDate;
	/// <summary>
	/// 开始交割日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string StartDelivDate;
	/// <summary>
	/// 最后交割日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string EndDelivDate;
	/// <summary>
	/// 挂牌基准价
	/// </summary>
	public double BasisPrice;
	/// <summary>
	/// 当前是否交易
	/// </summary>
	public int IsTrading;
	/// <summary>
	/// 基础商品代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string UnderlyingInstrID;
	/// <summary>
	/// 基础商品乘数
	/// </summary>
	public int UnderlyingMultiple;
	/// <summary>
	/// 持仓类型
	/// </summary>
	public TUstpFtdcPositionTypeType PositionType;
	/// <summary>
	/// 执行价
	/// </summary>
	public double StrikePrice;
	/// <summary>
	/// 期权类型
	/// </summary>
	public TUstpFtdcOptionsTypeType OptionsType;
	/// <summary>
	/// 币种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=5)]
	public string CurrencyID;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 第一腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_1;
	/// <summary>
	/// 第一腿买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction_1;
	/// <summary>
	/// 第一腿数量比例
	/// </summary>
	public double Ratio_1;
	/// <summary>
	/// 第二腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_2;
	/// <summary>
	/// 第二腿买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction_2;
	/// <summary>
	/// 第二腿数量比例
	/// </summary>
	public double Ratio_2;
	/// <summary>
	/// 进入本状态日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string EnterDate;
}

/// <summary>
/// 投资者资金查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInvestorAccountField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
}

/// <summary>
/// 投资者资金应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInvestorAccountField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 资金帐号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string AccountID;
	/// <summary>
	/// 上次结算准备金
	/// </summary>
	public double PreBalance;
	/// <summary>
	/// 入金金额
	/// </summary>
	public double Deposit;
	/// <summary>
	/// 出金金额
	/// </summary>
	public double Withdraw;
	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;
	/// <summary>
	/// 冻结手续费
	/// </summary>
	public double FrozenFee;
	/// <summary>
	/// 冻结权利金
	/// </summary>
	public double FrozenPremium;
	/// <summary>
	/// 手续费
	/// </summary>
	public double Fee;
	/// <summary>
	/// 平仓盈亏
	/// </summary>
	public double CloseProfit;
	/// <summary>
	/// 持仓盈亏
	/// </summary>
	public double PositionProfit;
	/// <summary>
	/// 可用资金
	/// </summary>
	public double Available;
	/// <summary>
	/// 多头冻结的保证金
	/// </summary>
	public double LongFrozenMargin;
	/// <summary>
	/// 空头冻结的保证金
	/// </summary>
	public double ShortFrozenMargin;
	/// <summary>
	/// 多头占用保证金
	/// </summary>
	public double LongMargin;
	/// <summary>
	/// 空头占用保证金
	/// </summary>
	public double ShortMargin;
	/// <summary>
	/// 当日释放保证金
	/// </summary>
	public double ReleaseMargin;
	/// <summary>
	/// 动态权益
	/// </summary>
	public double DynamicRights;
	/// <summary>
	/// 今日出入金
	/// </summary>
	public double TodayInOut;
	/// <summary>
	/// 占用保证金
	/// </summary>
	public double Margin;
	/// <summary>
	/// 期权权利金收支
	/// </summary>
	public double Premium;
	/// <summary>
	/// 风险度
	/// </summary>
	public double Risk;
}

/// <summary>
/// 可用投资者查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryUserInvestorField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
}

/// <summary>
/// 可用投资者
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspUserInvestorField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
}

/// <summary>
/// 交易编码查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryTradingCodeField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 交易编码查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspTradingCodeField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 客户编码权限
	/// </summary>
	public TUstpFtdcTradingRightType ClientRight;
	/// <summary>
	/// 客户保值类型
	/// </summary>
	public TUstpFtdcHedgeFlagType ClientHedgeFlag;
	/// <summary>
	/// 是否活跃
	/// </summary>
	public TUstpFtdcIsActiveType IsActive;
}

/// <summary>
/// 交易所查询请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryExchangeField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
}

/// <summary>
/// 交易所查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspExchangeField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 交易所名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string ExchangeName;
}

/// <summary>
/// 投资者持仓查询请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInvestorPositionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
}

/// <summary>
/// 投资者持仓查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInvestorPositionField
{
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 优惠前占用保证金
	/// </summary>
	public double UsedMargin;
	/// <summary>
	/// 今总持仓量
	/// </summary>
	public int Position;
	/// <summary>
	/// 今日持仓成本
	/// </summary>
	public double PositionCost;
	/// <summary>
	/// 昨持仓量
	/// </summary>
	public int YdPosition;
	/// <summary>
	/// 昨日持仓成本
	/// </summary>
	public double YdPositionCost;
	/// <summary>
	/// 冻结的保证金
	/// </summary>
	public double FrozenMargin;
	/// <summary>
	/// 开仓冻结持仓
	/// </summary>
	public int FrozenPosition;
	/// <summary>
	/// 平仓冻结持仓
	/// </summary>
	public int FrozenClosing;
	/// <summary>
	/// 平昨仓冻结持仓
	/// </summary>
	public int YdFrozenClosing;
	/// <summary>
	/// 冻结的权利金
	/// </summary>
	public double FrozenPremium;
	/// <summary>
	/// 最后一笔成交编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string LastTradeID;
	/// <summary>
	/// 最后一笔本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string LastOrderLocalID;
	/// <summary>
	/// 投机持仓量
	/// </summary>
	public int SpeculationPosition;
	/// <summary>
	/// 套利持仓量
	/// </summary>
	public int ArbitragePosition;
	/// <summary>
	/// 套保持仓量
	/// </summary>
	public int HedgePosition;
	/// <summary>
	/// 投机平仓冻结量
	/// </summary>
	public int SpecFrozenClosing;
	/// <summary>
	/// 套保平仓冻结量
	/// </summary>
	public int HedgeFrozenClosing;
	/// <summary>
	/// 币种
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=5)]
	public string Currency;
}

/// <summary>
/// 合规参数查询请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryComplianceParamField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 合规参数查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspComplianceParamField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 每日最大报单笔
	/// </summary>
	public int DailyMaxOrder;
	/// <summary>
	/// 每日最大撤单笔
	/// </summary>
	public int DailyMaxOrderAction;
	/// <summary>
	/// 每日最大错单笔
	/// </summary>
	public int DailyMaxErrorOrder;
	/// <summary>
	/// 每日最大报单手
	/// </summary>
	public int DailyMaxOrderVolume;
	/// <summary>
	/// 每日最大撤单手
	/// </summary>
	public int DailyMaxOrderActionVolume;
}

/// <summary>
/// 用户查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryUserField
{
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string StartUserID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string EndUserID;
}

/// <summary>
/// 用户
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcUserField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 用户登录密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string Password;
	/// <summary>
	/// 是否活跃
	/// </summary>
	public TUstpFtdcIsActiveType IsActive;
	/// <summary>
	/// 用户名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string UserName;
	/// <summary>
	/// 用户类型
	/// </summary>
	public TUstpFtdcUserTypeType UserType;
	/// <summary>
	/// 营业部
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string Department;
	/// <summary>
	/// 授权功能集
	/// </summary>
	public TUstpFtdcGrantFuncSetType GrantFuncSet;
	/// <summary>
	/// 修改用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string SetUserID;
	/// <summary>
	/// 操作日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CommandDate;
	/// <summary>
	/// 操作时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CommandTime;
}

/// <summary>
/// 投资者手续费率查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInvestorFeeField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 投资者手续费率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInvestorFeeField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 品种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string ProductID;
	/// <summary>
	/// 开仓手续费按比例
	/// </summary>
	public double OpenFeeRate;
	/// <summary>
	/// 开仓手续费按手数
	/// </summary>
	public double OpenFeeAmt;
	/// <summary>
	/// 平仓手续费按比例
	/// </summary>
	public double OffsetFeeRate;
	/// <summary>
	/// 平仓手续费按手数
	/// </summary>
	public double OffsetFeeAmt;
	/// <summary>
	/// 平今仓手续费按比例
	/// </summary>
	public double OTFeeRate;
	/// <summary>
	/// 平今仓手续费按手数
	/// </summary>
	public double OTFeeAmt;
	/// <summary>
	/// 行权手续费按比例
	/// </summary>
	public double ExecFeeRate;
	/// <summary>
	/// 行权手续费按手数
	/// </summary>
	public double ExecFeeAmt;
	/// <summary>
	/// 每笔委托申报费
	/// </summary>
	public double PerOrderAmt;
	/// <summary>
	/// 每笔撤单申报费
	/// </summary>
	public double PerCancelAmt;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
}

/// <summary>
/// 投资者保证金率查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInvestorMarginField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 投资者保证金率
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInvestorMarginField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 品种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string ProductID;
	/// <summary>
	/// 多头占用保证金按比例
	/// </summary>
	public double LongMarginRate;
	/// <summary>
	/// 多头保证金按手数
	/// </summary>
	public double LongMarginAmt;
	/// <summary>
	/// 空头占用保证金按比例
	/// </summary>
	public double ShortMarginRate;
	/// <summary>
	/// 空头保证金按手数
	/// </summary>
	public double ShortMarginAmt;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
}

/// <summary>
/// 系统用户登录请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqUserLoginField
{
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string Password;
	/// <summary>
	/// 用户端产品信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string UserProductInfo;
	/// <summary>
	/// 接口端产品信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string InterfaceProductInfo;
	/// <summary>
	/// 协议信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string ProtocolInfo;
	/// <summary>
	/// IP地址
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string IPAddress;
	/// <summary>
	/// Mac地址
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string MacAddress;
	/// <summary>
	/// 数据中心代码
	/// </summary>
	public int DataCenterID;
	/// <summary>
	/// 客户端运行文件大小
	/// </summary>
	public int UserProductFileSize;
	/// <summary>
	/// 客户认证类型
	/// </summary>
	public TUstpFtdcAuthenticate2TypeType Authenticate2Type;
	/// <summary>
	/// 客户认证密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string Authenticate2Password;
	/// <summary>
	/// 开发厂商终端编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string TerminalCode;
	/// <summary>
	/// 密码加密类型
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=3)]
	public string PasswordEncrypt;
}

/// <summary>
/// 用户请求出入金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcstpUserDepositField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 金额
	/// </summary>
	public double Amount;
	/// <summary>
	/// 出入金方向
	/// </summary>
	public TUstpFtdcAccountDirectionType AmountDirection;
	/// <summary>
	/// 用户本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
}

/// <summary>
/// 用户主次席出入金
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcstpTransferMoneyField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 金额
	/// </summary>
	public double Amount;
	/// <summary>
	/// 出入金方向
	/// </summary>
	public TUstpFtdcAccountDirectionType AmountDirection;
	/// <summary>
	/// 用户本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 银行机构代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BankID;
	/// <summary>
	/// 银行转账密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=36)]
	public string BankPasswd;
	/// <summary>
	/// 主席转账密码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=36)]
	public string AccountPasswd;
	/// <summary>
	/// 币种
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=5)]
	public string Currency;
	/// <summary>
	/// 次席资金流水号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=34)]
	public string SerialNo;
}

/// <summary>
/// 成交
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcTradeField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 会员编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ParticipantID;
	/// <summary>
	/// 下单席位号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string SeatID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 下单用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string OrderUserID;
	/// <summary>
	/// 成交编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string TradeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType OffsetFlag;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 成交价格
	/// </summary>
	public double TradePrice;
	/// <summary>
	/// 成交数量
	/// </summary>
	public int TradeVolume;
	/// <summary>
	/// 成交时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradeTime;
	/// <summary>
	/// 清算会员编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ClearingPartID;
	/// <summary>
	/// 本次成交手续费
	/// </summary>
	public double UsedFee;
	/// <summary>
	/// 本次成交占用保证金
	/// </summary>
	public double UsedMargin;
	/// <summary>
	/// 本次成交占用权利金
	/// </summary>
	public double Premium;
	/// <summary>
	/// 持仓表今持仓量
	/// </summary>
	public int Position;
	/// <summary>
	/// 持仓表今日持仓成本
	/// </summary>
	public double PositionCost;
	/// <summary>
	/// 资金表可用资金
	/// </summary>
	public double Available;
	/// <summary>
	/// 资金表占用保证金
	/// </summary>
	public double Margin;
	/// <summary>
	/// 资金表冻结的保证金
	/// </summary>
	public double FrozenMargin;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 套利组合合约
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string ArbiInstrumentID;
}

/// <summary>
/// 报单
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcOrderField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 指定通过此席位序号下单
	/// </summary>
	public int SeatNo;
	/// <summary>
	/// 合约代码/套利组合合约号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 用户本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 报单类型
	/// </summary>
	public TUstpFtdcOrderPriceTypeType OrderPriceType;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType OffsetFlag;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 价格
	/// </summary>
	public double LimitPrice;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 有效期类型
	/// </summary>
	public TUstpFtdcTimeConditionType TimeCondition;
	/// <summary>
	/// GTD日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string GTDDate;
	/// <summary>
	/// 成交量类型
	/// </summary>
	public TUstpFtdcVolumeConditionType VolumeCondition;
	/// <summary>
	/// 最小成交量
	/// </summary>
	public int MinVolume;
	/// <summary>
	/// 止损价止赢价
	/// </summary>
	public double StopPrice;
	/// <summary>
	/// 强平原因
	/// </summary>
	public TUstpFtdcForceCloseReasonType ForceCloseReason;
	/// <summary>
	/// 自动挂起标志
	/// </summary>
	public int IsAutoSuspend;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 会员编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ParticipantID;
	/// <summary>
	/// 最初下单用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string OrderUserID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 下单席位号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string SeatID;
	/// <summary>
	/// 插入时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string InsertTime;
	/// <summary>
	/// 本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string OrderLocalID;
	/// <summary>
	/// 报单来源
	/// </summary>
	public TUstpFtdcOrderSourceType OrderSource;
	/// <summary>
	/// 报单状态
	/// </summary>
	public TUstpFtdcOrderStatusType OrderStatus;
	/// <summary>
	/// 撤销时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CancelTime;
	/// <summary>
	/// 撤单用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string CancelUserID;
	/// <summary>
	/// 今成交数量
	/// </summary>
	public int VolumeTraded;
	/// <summary>
	/// 剩余数量
	/// </summary>
	public int VolumeRemain;
	/// <summary>
	/// 委托类型
	/// </summary>
	public TUstpFtdcOrderTypeType OrderType;
	/// <summary>
	/// 期权对冲标识
	/// </summary>
	public TUstpFtdcDeliveryFlagType DeliveryFlag;
}

/// <summary>
/// 数据流回退
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcFlowMessageCancelField
{
	/// <summary>
	/// 序列系列号
	/// </summary>
	public int SequenceSeries;
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 数据中心代码
	/// </summary>
	public int DataCenterID;
	/// <summary>
	/// 回退起始序列号
	/// </summary>
	public int StartSequenceNo;
	/// <summary>
	/// 回退结束序列号
	/// </summary>
	public int EndSequenceNo;
}

/// <summary>
/// 信息分发
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDisseminationField
{
	/// <summary>
	/// 序列系列号
	/// </summary>
	public int SequenceSeries;
	/// <summary>
	/// 序列号
	/// </summary>
	public int SequenceNo;
}

/// <summary>
/// 出入金结果
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInvestorAccountDepositResField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 资金帐号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string AccountID;
	/// <summary>
	/// 资金流水号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string AccountSeqNo;
	/// <summary>
	/// 金额
	/// </summary>
	public double Amount;
	/// <summary>
	/// 出入金方向
	/// </summary>
	public TUstpFtdcAccountDirectionType AmountDirection;
	/// <summary>
	/// 可用资金
	/// </summary>
	public double Available;
	/// <summary>
	/// 结算准备金
	/// </summary>
	public double Balance;
}

/// <summary>
/// 报价录入
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInputQuoteField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 交易系统返回的系统报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string QuoteSysID;
	/// <summary>
	/// 用户设定的本地报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserQuoteLocalID;
	/// <summary>
	/// 飞马向交易系统报的本地报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string QuoteLocalID;
	/// <summary>
	/// 买方买入数量
	/// </summary>
	public int BidVolume;
	/// <summary>
	/// 买方开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType BidOffsetFlag;
	/// <summary>
	/// 买方投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType BidHedgeFlag;
	/// <summary>
	/// 买方买入价格
	/// </summary>
	public double BidPrice;
	/// <summary>
	/// 卖方卖出数量
	/// </summary>
	public int AskVolume;
	/// <summary>
	/// 卖方开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType AskOffsetFlag;
	/// <summary>
	/// 卖方投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType AskHedgeFlag;
	/// <summary>
	/// 卖方卖出价格
	/// </summary>
	public double AskPrice;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 拆分出来的买方用户本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BidUserOrderLocalID;
	/// <summary>
	/// 拆分出来的卖方用户本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string AskUserOrderLocalID;
	/// <summary>
	/// 拆分出来的买方本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string BidOrderLocalID;
	/// <summary>
	/// 拆分出来的卖方本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string AskOrderLocalID;
	/// <summary>
	/// 询价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string ReqForQuoteID;
	/// <summary>
	/// 报价停留时间(秒)
	/// </summary>
	public int StandByTime;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 报价通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRtnQuoteField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 交易系统返回的系统报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string QuoteSysID;
	/// <summary>
	/// 用户设定的本地报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserQuoteLocalID;
	/// <summary>
	/// 飞马向交易系统报的本地报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string QuoteLocalID;
	/// <summary>
	/// 买方买入数量
	/// </summary>
	public int BidVolume;
	/// <summary>
	/// 买方开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType BidOffsetFlag;
	/// <summary>
	/// 买方投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType BidHedgeFlag;
	/// <summary>
	/// 买方买入价格
	/// </summary>
	public double BidPrice;
	/// <summary>
	/// 卖方卖出数量
	/// </summary>
	public int AskVolume;
	/// <summary>
	/// 卖方开平标志
	/// </summary>
	public TUstpFtdcOffsetFlagType AskOffsetFlag;
	/// <summary>
	/// 卖方投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType AskHedgeFlag;
	/// <summary>
	/// 卖方卖出价格
	/// </summary>
	public double AskPrice;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 拆分出来的买方用户本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BidUserOrderLocalID;
	/// <summary>
	/// 拆分出来的卖方用户本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string AskUserOrderLocalID;
	/// <summary>
	/// 拆分出来的买方本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string BidOrderLocalID;
	/// <summary>
	/// 拆分出来的卖方本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string AskOrderLocalID;
	/// <summary>
	/// 询价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string ReqForQuoteID;
	/// <summary>
	/// 报价停留时间(秒)
	/// </summary>
	public int StandByTime;
	/// <summary>
	/// 买方系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string BidOrderSysID;
	/// <summary>
	/// 卖方系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AskOrderSysID;
	/// <summary>
	/// 报价单状态
	/// </summary>
	public TUstpFtdcQuoteStatusType QuoteStatus;
	/// <summary>
	/// 插入时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string InsertTime;
	/// <summary>
	/// 撤销时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CancelTime;
	/// <summary>
	/// 成交时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradeTime;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 报价操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQuoteActionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 交易系统返回的系统报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string QuoteSysID;
	/// <summary>
	/// 用户设定的被撤的本地报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserQuoteLocalID;
	/// <summary>
	/// 用户向飞马报的本地撤消报价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserQuoteActionLocalID;
	/// <summary>
	/// 报单操作标志
	/// </summary>
	public TUstpFtdcActionFlagType ActionFlag;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 询价请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqForQuoteField
{
	/// <summary>
	/// 询价编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string ReqForQuoteID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 询价时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ReqForQuoteTime;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 资金同步通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcSyncMoneyTransferField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 资金帐号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string AccountID;
	/// <summary>
	/// 银行代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=10)]
	public string BankID;
	/// <summary>
	/// 银行帐号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=34)]
	public string BankAccount;
	/// <summary>
	/// 币种
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=5)]
	public string Currency;
	/// <summary>
	/// 金额
	/// </summary>
	public double Amount;
	/// <summary>
	/// 出入金事件通知
	/// </summary>
	public TUstpFtdcSyncDirectionType SyncTransMoneyEvent;
	/// <summary>
	/// 银期业务功能码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=10)]
	public string TradeCode;
	/// <summary>
	/// 业务发起方
	/// </summary>
	public TUstpFtdcTradeSyncSourceType TradeSource;
	/// <summary>
	/// 主席流水号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=34)]
	public string TransSerialNo;
	/// <summary>
	/// 次席流水号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=34)]
	public string SerialNo;
	/// <summary>
	/// 用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CommandDate;
	/// <summary>
	/// 时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CommandTime;
}

/// <summary>
/// 行情基础属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataBaseField
{
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 结算组代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string SettlementGroupID;
	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;
	/// <summary>
	/// 昨结算
	/// </summary>
	public double PreSettlementPrice;
	/// <summary>
	/// 昨收盘
	/// </summary>
	public double PreClosePrice;
	/// <summary>
	/// 昨持仓量
	/// </summary>
	public double PreOpenInterest;
	/// <summary>
	/// 昨虚实度
	/// </summary>
	public double PreDelta;
}

/// <summary>
/// 行情静态属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataStaticField
{
	/// <summary>
	/// 今开盘
	/// </summary>
	public double OpenPrice;
	/// <summary>
	/// 最高价
	/// </summary>
	public double HighestPrice;
	/// <summary>
	/// 最低价
	/// </summary>
	public double LowestPrice;
	/// <summary>
	/// 今收盘
	/// </summary>
	public double ClosePrice;
	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;
	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;
	/// <summary>
	/// 今结算
	/// </summary>
	public double SettlementPrice;
	/// <summary>
	/// 今虚实度
	/// </summary>
	public double CurrDelta;
}

/// <summary>
/// 行情最新成交属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataLastMatchField
{
	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 成交金额
	/// </summary>
	public double Turnover;
	/// <summary>
	/// 持仓量
	/// </summary>
	public double OpenInterest;
}

/// <summary>
/// 行情最优价属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataBestPriceField
{
	/// <summary>
	/// 申买价一
	/// </summary>
	public double BidPrice1;
	/// <summary>
	/// 申买量一
	/// </summary>
	public int BidVolume1;
	/// <summary>
	/// 申卖价一
	/// </summary>
	public double AskPrice1;
	/// <summary>
	/// 申卖量一
	/// </summary>
	public int AskVolume1;
}

/// <summary>
/// 行情申买二、三属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataBid23Field
{
	/// <summary>
	/// 申买价二
	/// </summary>
	public double BidPrice2;
	/// <summary>
	/// 申买量二
	/// </summary>
	public int BidVolume2;
	/// <summary>
	/// 申买价三
	/// </summary>
	public double BidPrice3;
	/// <summary>
	/// 申买量三
	/// </summary>
	public int BidVolume3;
}

/// <summary>
/// 行情申卖二、三属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataAsk23Field
{
	/// <summary>
	/// 申卖价二
	/// </summary>
	public double AskPrice2;
	/// <summary>
	/// 申卖量二
	/// </summary>
	public int AskVolume2;
	/// <summary>
	/// 申卖价三
	/// </summary>
	public double AskPrice3;
	/// <summary>
	/// 申卖量三
	/// </summary>
	public int AskVolume3;
}

/// <summary>
/// 行情申买四、五属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataBid45Field
{
	/// <summary>
	/// 申买价四
	/// </summary>
	public double BidPrice4;
	/// <summary>
	/// 申买量四
	/// </summary>
	public int BidVolume4;
	/// <summary>
	/// 申买价五
	/// </summary>
	public double BidPrice5;
	/// <summary>
	/// 申买量五
	/// </summary>
	public int BidVolume5;
}

/// <summary>
/// 行情申卖四、五属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataAsk45Field
{
	/// <summary>
	/// 申卖价四
	/// </summary>
	public double AskPrice4;
	/// <summary>
	/// 申卖量四
	/// </summary>
	public int AskVolume4;
	/// <summary>
	/// 申卖价五
	/// </summary>
	public double AskPrice5;
	/// <summary>
	/// 申卖量五
	/// </summary>
	public int AskVolume5;
}

/// <summary>
/// 行情更新时间属性
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarketDataUpdateTimeField
{
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 最后修改时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string UpdateTime;
	/// <summary>
	/// 最后修改毫秒
	/// </summary>
	public int UpdateMillisec;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
}

/// <summary>
/// 深度行情
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDepthMarketDataField
{
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 结算组代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string SettlementGroupID;
	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;
	/// <summary>
	/// 昨结算
	/// </summary>
	public double PreSettlementPrice;
	/// <summary>
	/// 昨收盘
	/// </summary>
	public double PreClosePrice;
	/// <summary>
	/// 昨持仓量
	/// </summary>
	public double PreOpenInterest;
	/// <summary>
	/// 昨虚实度
	/// </summary>
	public double PreDelta;
	/// <summary>
	/// 今开盘
	/// </summary>
	public double OpenPrice;
	/// <summary>
	/// 最高价
	/// </summary>
	public double HighestPrice;
	/// <summary>
	/// 最低价
	/// </summary>
	public double LowestPrice;
	/// <summary>
	/// 今收盘
	/// </summary>
	public double ClosePrice;
	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;
	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;
	/// <summary>
	/// 今结算
	/// </summary>
	public double SettlementPrice;
	/// <summary>
	/// 今虚实度
	/// </summary>
	public double CurrDelta;
	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 成交金额
	/// </summary>
	public double Turnover;
	/// <summary>
	/// 持仓量
	/// </summary>
	public double OpenInterest;
	/// <summary>
	/// 申买价一
	/// </summary>
	public double BidPrice1;
	/// <summary>
	/// 申买量一
	/// </summary>
	public int BidVolume1;
	/// <summary>
	/// 申卖价一
	/// </summary>
	public double AskPrice1;
	/// <summary>
	/// 申卖量一
	/// </summary>
	public int AskVolume1;
	/// <summary>
	/// 申买价二
	/// </summary>
	public double BidPrice2;
	/// <summary>
	/// 申买量二
	/// </summary>
	public int BidVolume2;
	/// <summary>
	/// 申买价三
	/// </summary>
	public double BidPrice3;
	/// <summary>
	/// 申买量三
	/// </summary>
	public int BidVolume3;
	/// <summary>
	/// 申卖价二
	/// </summary>
	public double AskPrice2;
	/// <summary>
	/// 申卖量二
	/// </summary>
	public int AskVolume2;
	/// <summary>
	/// 申卖价三
	/// </summary>
	public double AskPrice3;
	/// <summary>
	/// 申卖量三
	/// </summary>
	public int AskVolume3;
	/// <summary>
	/// 申买价四
	/// </summary>
	public double BidPrice4;
	/// <summary>
	/// 申买量四
	/// </summary>
	public int BidVolume4;
	/// <summary>
	/// 申买价五
	/// </summary>
	public double BidPrice5;
	/// <summary>
	/// 申买量五
	/// </summary>
	public int BidVolume5;
	/// <summary>
	/// 申卖价四
	/// </summary>
	public double AskPrice4;
	/// <summary>
	/// 申卖量四
	/// </summary>
	public int AskVolume4;
	/// <summary>
	/// 申卖价五
	/// </summary>
	public double AskPrice5;
	/// <summary>
	/// 申卖量五
	/// </summary>
	public int AskVolume5;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 最后修改时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string UpdateTime;
	/// <summary>
	/// 最后修改毫秒
	/// </summary>
	public int UpdateMillisec;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 历史最高价
	/// </summary>
	public double HisHighestPrice;
	/// <summary>
	/// 历史最低价
	/// </summary>
	public double HisLowestPrice;
	/// <summary>
	/// 最新成交量
	/// </summary>
	public int LatestVolume;
	/// <summary>
	/// 初始持仓量
	/// </summary>
	public int InitVolume;
	/// <summary>
	/// 持仓量变化
	/// </summary>
	public int ChangeVolume;
	/// <summary>
	/// 申买推导量
	/// </summary>
	public int BidImplyVolume;
	/// <summary>
	/// 申卖推导量
	/// </summary>
	public int AskImplyVolume;
	/// <summary>
	/// 当日均价
	/// </summary>
	public double AvgPrice;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 第一腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_1;
	/// <summary>
	/// 第二腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_2;
	/// <summary>
	/// 合约名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentName;
	/// <summary>
	/// 总买入量
	/// </summary>
	public int TotalBidVolume;
	/// <summary>
	/// 总卖出量
	/// </summary>
	public int TotalAskVolume;
}

/// <summary>
/// 订阅合约的相关信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcSpecificInstrumentField
{
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
}

/// <summary>
/// 多播通道心跳
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMultiChannelHeartBeatField
{
	/// <summary>
	/// 心跳超时时间（秒）
	/// </summary>
	public int UstpMultiChannelHeartBeatTimeOut;
}

/// <summary>
/// 获取行情订阅号请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqMarketTopicField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
}

/// <summary>
/// 获取行情订阅号应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspMarketTopicField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 订阅号
	/// </summary>
	public int TopicID;
}

/// <summary>
/// 申请组合
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInputMarginCombActionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 交易用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 用户本地编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserActionLocalID;
	/// <summary>
	/// 组合合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentID;
	/// <summary>
	/// 组合数量
	/// </summary>
	public int CombVolume;
	/// <summary>
	/// 组合动作方向
	/// </summary>
	public TUstpFtdcCombDirectionType CombDirection;
	/// <summary>
	/// 本地编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string ActionLocalID;
	/// <summary>
	/// 组合持仓方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 系统编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 组合操作状态
	/// </summary>
	public TUstpFtdcCombActionStatusType CombActionStatus;
}

/// <summary>
/// 投资者组合持仓查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInvestorCombPositionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 组合合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 投资者组合持仓查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInvestorCombPositionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 持仓方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 组合合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentID;
	/// <summary>
	/// 单腿1合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string Leg1InstrumentID;
	/// <summary>
	/// 单腿2合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string Leg2InstrumentID;
	/// <summary>
	/// 组合持仓
	/// </summary>
	public int CombPosition;
	/// <summary>
	/// 冻结组合持仓
	/// </summary>
	public int CombFrozenPosition;
	/// <summary>
	/// 组合一手释放的保证金
	/// </summary>
	public double CombFreeMargin;
}

/// <summary>
/// 组合规则
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcMarginCombinationLegField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 组合合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentID;
	/// <summary>
	/// 单腿编号
	/// </summary>
	public int LegID;
	/// <summary>
	/// 单腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string LegInstrumentID;
	/// <summary>
	/// 买卖方向
	/// </summary>
	public TUstpFtdcDirectionType Direction;
	/// <summary>
	/// 单腿乘数
	/// </summary>
	public int LegMultiple;
	/// <summary>
	/// 优先级
	/// </summary>
	public int Priority;
}

/// <summary>
/// 投资者单腿持仓查询
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryInvestorLegPositionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 单腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string LegInstrumentID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
}

/// <summary>
/// 投资者单腿持仓查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInvestorLegPositionField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 单腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 多头持仓
	/// </summary>
	public int LongPosition;
	/// <summary>
	/// 空头持仓
	/// </summary>
	public int ShortPosition;
	/// <summary>
	/// 多头占用保证金
	/// </summary>
	public double LongMargin;
	/// <summary>
	/// 空头占用保证金
	/// </summary>
	public double ShortMargin;
	/// <summary>
	/// 多头冻结持仓
	/// </summary>
	public int LongFrozenPosition;
	/// <summary>
	/// 空头冻结持仓
	/// </summary>
	public int ShortFrozenPosition;
	/// <summary>
	/// 多头冻结保证金
	/// </summary>
	public double LongFrozenMargin;
	/// <summary>
	/// 空头冻结保证金
	/// </summary>
	public double ShortFrozenMargin;
}

/// <summary>
/// 查询合约组信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryUstpInstrumentGroupField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
}

/// <summary>
/// 合约组信息查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspInstrumentGroupField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 合约组代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentGroupID;
}

/// <summary>
/// 查询组合保证金类型
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcQryClientMarginCombTypeField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 合约组代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentGroupID;
}

/// <summary>
/// 组合保证金类型查询应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspClientMarginCombTypeField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 会员代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ParticipantID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 合约组代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentGroupID;
	/// <summary>
	/// 保证金组合类型
	/// </summary>
	public TUstpFtdcClientMarginCombTypeType MarginCombType;
}

/// <summary>
/// 系统时间
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqQrySystemTimeField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
}

/// <summary>
/// 系统时间
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspQrySystemTimeField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string SystemTime;
}

/// <summary>
/// 输入行权
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInputExecOrderField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 用户本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 委托类型
	/// </summary>
	public TUstpFtdcOrderTypeType OrderType;
	/// <summary>
	/// 期权对冲标识
	/// </summary>
	public TUstpFtdcDeliveryFlagType DeliveryFlag;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
}

/// <summary>
/// 输入行权操作
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcInputExecOrderActionField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 本次撤单操作的本地编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderActionLocalID;
	/// <summary>
	/// 被撤订单的本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 报单操作标志
	/// </summary>
	public TUstpFtdcActionFlagType ActionFlag;
	/// <summary>
	/// 数量变化
	/// </summary>
	public int VolumeChange;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 委托类型
	/// </summary>
	public TUstpFtdcOrderTypeType OrderType;
}

/// <summary>
/// 行权通知
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcExecOrderField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 系统报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string OrderSysID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 用户代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string UserID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 用户本地报单号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string UserOrderLocalID;
	/// <summary>
	/// 委托类型
	/// </summary>
	public TUstpFtdcOrderTypeType OrderType;
	/// <summary>
	/// 期权对冲标识
	/// </summary>
	public TUstpFtdcDeliveryFlagType DeliveryFlag;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 用户自定义域
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=65)]
	public string UserCustom;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 本地业务标识
	/// </summary>
	public int BusinessLocalID;
	/// <summary>
	/// 业务单元
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string BusinessUnit;
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 会员编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ParticipantID;
	/// <summary>
	/// 最初下单用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string OrderUserID;
	/// <summary>
	/// 客户编码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string ClientID;
	/// <summary>
	/// 下单席位号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string SeatID;
	/// <summary>
	/// 插入时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string InsertTime;
	/// <summary>
	/// 本地报单编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string OrderLocalID;
	/// <summary>
	/// 报单来源
	/// </summary>
	public TUstpFtdcOrderSourceType OrderSource;
	/// <summary>
	/// 报单状态
	/// </summary>
	public TUstpFtdcOrderStatusType OrderStatus;
	/// <summary>
	/// 撤销时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string CancelTime;
	/// <summary>
	/// 撤单用户编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=16)]
	public string CancelUserID;
}

/// <summary>
/// 查询行情快照
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqQryMarketDataField
{
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
}

/// <summary>
/// 查询行情快应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspDepthMarketDataField
{
	/// <summary>
	/// 交易日
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string TradingDay;
	/// <summary>
	/// 结算组代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string SettlementGroupID;
	/// <summary>
	/// 结算编号
	/// </summary>
	public int SettlementID;
	/// <summary>
	/// 昨结算
	/// </summary>
	public double PreSettlementPrice;
	/// <summary>
	/// 昨收盘
	/// </summary>
	public double PreClosePrice;
	/// <summary>
	/// 昨持仓量
	/// </summary>
	public double PreOpenInterest;
	/// <summary>
	/// 昨虚实度
	/// </summary>
	public double PreDelta;
	/// <summary>
	/// 今开盘
	/// </summary>
	public double OpenPrice;
	/// <summary>
	/// 最高价
	/// </summary>
	public double HighestPrice;
	/// <summary>
	/// 最低价
	/// </summary>
	public double LowestPrice;
	/// <summary>
	/// 今收盘
	/// </summary>
	public double ClosePrice;
	/// <summary>
	/// 涨停板价
	/// </summary>
	public double UpperLimitPrice;
	/// <summary>
	/// 跌停板价
	/// </summary>
	public double LowerLimitPrice;
	/// <summary>
	/// 今结算
	/// </summary>
	public double SettlementPrice;
	/// <summary>
	/// 今虚实度
	/// </summary>
	public double CurrDelta;
	/// <summary>
	/// 最新价
	/// </summary>
	public double LastPrice;
	/// <summary>
	/// 数量
	/// </summary>
	public int Volume;
	/// <summary>
	/// 成交金额
	/// </summary>
	public double Turnover;
	/// <summary>
	/// 持仓量
	/// </summary>
	public double OpenInterest;
	/// <summary>
	/// 申买价一
	/// </summary>
	public double BidPrice1;
	/// <summary>
	/// 申买量一
	/// </summary>
	public int BidVolume1;
	/// <summary>
	/// 申卖价一
	/// </summary>
	public double AskPrice1;
	/// <summary>
	/// 申卖量一
	/// </summary>
	public int AskVolume1;
	/// <summary>
	/// 申买价二
	/// </summary>
	public double BidPrice2;
	/// <summary>
	/// 申买量二
	/// </summary>
	public int BidVolume2;
	/// <summary>
	/// 申买价三
	/// </summary>
	public double BidPrice3;
	/// <summary>
	/// 申买量三
	/// </summary>
	public int BidVolume3;
	/// <summary>
	/// 申卖价二
	/// </summary>
	public double AskPrice2;
	/// <summary>
	/// 申卖量二
	/// </summary>
	public int AskVolume2;
	/// <summary>
	/// 申卖价三
	/// </summary>
	public double AskPrice3;
	/// <summary>
	/// 申卖量三
	/// </summary>
	public int AskVolume3;
	/// <summary>
	/// 申买价四
	/// </summary>
	public double BidPrice4;
	/// <summary>
	/// 申买量四
	/// </summary>
	public int BidVolume4;
	/// <summary>
	/// 申买价五
	/// </summary>
	public double BidPrice5;
	/// <summary>
	/// 申买量五
	/// </summary>
	public int BidVolume5;
	/// <summary>
	/// 申卖价四
	/// </summary>
	public double AskPrice4;
	/// <summary>
	/// 申卖量四
	/// </summary>
	public int AskVolume4;
	/// <summary>
	/// 申卖价五
	/// </summary>
	public double AskPrice5;
	/// <summary>
	/// 申卖量五
	/// </summary>
	public int AskVolume5;
	/// <summary>
	/// 合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID;
	/// <summary>
	/// 最后修改时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string UpdateTime;
	/// <summary>
	/// 最后修改毫秒
	/// </summary>
	public int UpdateMillisec;
	/// <summary>
	/// 业务发生日期
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=9)]
	public string ActionDay;
	/// <summary>
	/// 历史最高价
	/// </summary>
	public double HisHighestPrice;
	/// <summary>
	/// 历史最低价
	/// </summary>
	public double HisLowestPrice;
	/// <summary>
	/// 最新成交量
	/// </summary>
	public int LatestVolume;
	/// <summary>
	/// 初始持仓量
	/// </summary>
	public int InitVolume;
	/// <summary>
	/// 持仓量变化
	/// </summary>
	public int ChangeVolume;
	/// <summary>
	/// 申买推导量
	/// </summary>
	public int BidImplyVolume;
	/// <summary>
	/// 申卖推导量
	/// </summary>
	public int AskImplyVolume;
	/// <summary>
	/// 当日均价
	/// </summary>
	public double AvgPrice;
	/// <summary>
	/// 策略类别
	/// </summary>
	public TUstpFtdcArbiTypeType ArbiType;
	/// <summary>
	/// 第一腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_1;
	/// <summary>
	/// 第二腿合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentID_2;
	/// <summary>
	/// 合约名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string InstrumentName;
	/// <summary>
	/// 总买入量
	/// </summary>
	public int TotalBidVolume;
	/// <summary>
	/// 总卖出量
	/// </summary>
	public int TotalAskVolume;
}

/// <summary>
/// 穿透监管客户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSUserInfoField
{
	/// <summary>
	/// 用户AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// 用户授权码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=17)]
	public string AuthCode;
	/// <summary>
	/// 密钥加密类型
	/// </summary>
	public TUstpFtdcDSKeyEncryptType EncryptType;
}

/// <summary>
/// 穿透监管客户认证请求信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSUserCertReqDataField
{
	/// <summary>
	/// 用户AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// 用户认证请求信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=801)]
	public string UserCertReqData;
	/// <summary>
	/// 用户证书信息分片的总片数
	/// </summary>
	public int TotalNum;
	/// <summary>
	/// 用户证书信息分片的第几片
	/// </summary>
	public int CurrentNum;
}

/// <summary>
/// 穿透监管客户认证响应信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSUserCertRspDataField
{
	/// <summary>
	/// AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// AppID类型
	/// </summary>
	public TUstpFtdcDSAppIDTypeType AppIDType;
	/// <summary>
	/// 用户认证返回信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=801)]
	public string UserCertRspData;
	/// <summary>
	/// 用户证书返回信息分片的总片数
	/// </summary>
	public int TotalNum;
	/// <summary>
	/// 用户证书返回信息分片的第几片
	/// </summary>
	public int CurrentNum;
}

/// <summary>
/// 穿透监管客户信息采集信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSLocalSystemDataField
{
	/// <summary>
	/// 用户AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// 异常标识
	/// </summary>
	public TUstpFtdcDSExceptionFlagType ExceptionFlag;
	/// <summary>
	/// 用户信息采集结果
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=801)]
	public string LocalSystemData;
}

/// <summary>
/// 穿透监管中继验证客户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSProxyCheckUserInfoField
{
	/// <summary>
	/// 用户AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// 用户授权码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=17)]
	public string AuthCode;
	/// <summary>
	/// 密钥加密类型
	/// </summary>
	public TUstpFtdcDSKeyEncryptType EncryptType;
}

/// <summary>
/// 穿透监管中继处接收到的终端认证信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSProxyUserCertInField
{
	/// <summary>
	/// 穿透监管中继处接收到的终端认证信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=4097)]
	public string UserCertReqInfo;
}

/// <summary>
/// 穿透监管中继处接终端认证返回信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSProxyUserCertOutField
{
	/// <summary>
	/// 穿透监管中继处证书认证的返回结果
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=4097)]
	public string UserCertRspInfo;
	/// <summary>
	/// 中继处返回数据已使用长度信息
	/// </summary>
	public int UserCertRspInfoLen;
}

/// <summary>
/// 穿透监管中继提交信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSProxySubmitDataField
{
	/// <summary>
	/// AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// 客户终端公网IP
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=40)]
	public string TerminalPubNetIP;
	/// <summary>
	/// 客户终端公网端口号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=6)]
	public string TerminalPubNetPort;
	/// <summary>
	/// 客户终端登入时间
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=20)]
	public string TerminalLoginTime;
	/// <summary>
	/// 异常标识
	/// </summary>
	public TUstpFtdcDSExceptionFlagType ExceptionFlag;
	/// <summary>
	/// RealyID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string RelayID;
	/// <summary>
	/// 终端采集信息
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=801)]
	public string TerminalSystemData;
}

/// <summary>
/// 穿透监管线下委托客户信息
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcDSOfflineInfoField
{
	/// <summary>
	/// AppID
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string AppID;
	/// <summary>
	/// 投资者编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=19)]
	public string InvestorID;
	/// <summary>
	/// 投资者手机号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=21)]
	public string InvestorTel;
}

/// <summary>
/// 查询保证金优惠参数请求
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcReqQryMarginPrefParamField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 组合合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentID;
	/// <summary>
	/// 组合合约名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentName;
}

/// <summary>
/// 查询保证金优惠参数应答
/// </summary>
[StructLayout(LayoutKind.Sequential)]
public struct  CUstpFtdcRspQryMarginPrefParamField
{
	/// <summary>
	/// 经纪公司编号
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string BrokerID;
	/// <summary>
	/// 交易所代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=11)]
	public string ExchangeID;
	/// <summary>
	/// 组合合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentID;
	/// <summary>
	/// 组合合约名称
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=41)]
	public string CombInstrumentName;
	/// <summary>
	/// 组合类型
	/// </summary>
	public TUstpFtdcArbiTypeType CombType;
	/// <summary>
	/// 投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType HedgeFlag;
	/// <summary>
	/// 腿1合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string Leg1InstrumentID;
	/// <summary>
	/// 腿1品种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string Leg1ProductID;
	/// <summary>
	/// 腿1方向
	/// </summary>
	public TUstpFtdcDirectionType Leg1Direction;
	/// <summary>
	/// 腿1投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType Leg1HedgeFlag;
	/// <summary>
	/// 腿1昨结算价
	/// </summary>
	public double Leg1SettlementPrice;
	/// <summary>
	/// 腿2合约代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=31)]
	public string Leg2InstrumentID;
	/// <summary>
	/// 腿2品种代码
	/// </summary>
	[MarshalAs(UnmanagedType.ByValTStr, SizeConst=13)]
	public string Leg2ProductID;
	/// <summary>
	/// 腿2方向
	/// </summary>
	public TUstpFtdcDirectionType Leg2Direction;
	/// <summary>
	/// 腿2投机套保标志
	/// </summary>
	public TUstpFtdcHedgeFlagType Leg2HedgeFlag;
	/// <summary>
	/// 腿2昨结算价
	/// </summary>
	public double Leg2SettlementPrice;
	/// <summary>
	/// 优先级
	/// </summary>
	public int Priority;
	/// <summary>
	/// 是否交易期间优惠
	/// </summary>
	public TUstpFtdcIsActiveType TradeEna;
}

