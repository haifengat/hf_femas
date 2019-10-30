using System;
using System.IO;
using System.Runtime.InteropServices;
using System.IO.Compression;

namespace HaiFeng
{
	public class ctp_trade
	{
		#region Dll Load /UnLoad
		/// <summary>
		/// 原型是 :HMODULE LoadLibrary(LPCTSTR lpFileName);
		/// </summary>
		/// <param name="lpFileName"> DLL 文件名 </param>
		/// <returns> 函数库模块的句柄 </returns>
		[DllImport("kernel32.dll")]
		private static extern IntPtr LoadLibrary(string lpFileName);

		/// <summary>
		/// 原型是 : FARPROC GetProcAddress(HMODULE hModule, LPCWSTR lpProcName);
		/// </summary>
		/// <param name="hModule"> 包含需调用函数的函数库模块的句柄 </param>
		/// <param name="lpProcName"> 调用函数的名称 </param>
		/// <returns> 函数指针 </returns>
		[DllImport("kernel32.dll")]
		private static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);

		/// <summary>
		/// 原型是 : BOOL FreeLibrary(HMODULE hModule);
		/// </summary>
		/// <param name="hModule"> 需释放的函数库模块的句柄 </param>
		/// <returns> 是否已释放指定的 Dll </returns>
		[DllImport("kernel32", EntryPoint = "FreeLibrary", SetLastError = true)]
		private static extern bool FreeLibrary(IntPtr hModule);

		/// <summary>
		///
		/// </summary>
		/// <param name="pHModule"></param>
		/// <param name="lpProcName"></param>
		/// <param name="t"></param>
		/// <returns></returns>
		/// <exception cref="Exception"></exception>
		private static Delegate Invoke(IntPtr pHModule, string lpProcName, Type t)
		{
			// 若函数库模块的句柄为空，则抛出异常
			if (pHModule == IntPtr.Zero)
			{
				throw (new Exception(" 函数库模块的句柄为空 , 请确保已进行 LoadDll 操作 !"));
			}
			// 取得函数指针
			IntPtr farProc = GetProcAddress(pHModule, lpProcName);
			// 若函数指针，则抛出异常
			if (farProc == IntPtr.Zero)
			{
				throw (new Exception(" 没有找到 :" + lpProcName + " 这个函数的入口点 "));
			}
			return Marshal.GetDelegateForFunctionPointer(farProc, t);
		}
		#endregion

		IntPtr _handle = IntPtr.Zero, _api = IntPtr.Zero, _spi = IntPtr.Zero;
		private int nRequestID = 0;
		delegate IntPtr Create();
		
		public ctp_trade()
		{
			string curPath = Environment.CurrentDirectory;
            var dll_path = new FileInfo(this.GetType().Assembly.Location).DirectoryName;
            Environment.CurrentDirectory = dll_path;
            dll_path = Path.Combine(dll_path, "lib" + (Environment.Is64BitProcess ? "64" : "32"));
            if (!Directory.Exists(dll_path))
            {
                File.WriteAllBytes("lib.zip", Properties.Resources.lib);
                ZipFile.ExtractToDirectory("lib.zip", ".");
                File.Delete("lib.zip");
            }
			Environment.CurrentDirectory = dll_path;
			_handle = LoadLibrary(Path.Combine(dll_path, "ctp_trade.dll"));
			if (_handle == IntPtr.Zero)
			{
				throw (new Exception(String.Format("没有找到:", dll_path)));
			}
			Environment.CurrentDirectory = curPath;
			Directory.CreateDirectory("log");

			_api = (Invoke(_handle, "CreateApi", typeof(Create)) as Create)();
			_spi = (Invoke(_handle, "CreateSpi", typeof(Create)) as Create)();
			this.RegisterSpi(_spi);
		}
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRelease(IntPtr api);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleInit(IntPtr api);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleJoin(IntPtr api);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterFront(IntPtr api, string pszFrontAddress);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterQryFront(IntPtr api, string pszFrontAddress);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterNameServer(IntPtr api, string pszNsAddress);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterSpi(IntPtr api, IntPtr pSpi);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribePrivateTopic(IntPtr api, USTP_TE_RESUME_TYPE nResumeType);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribePublicTopic(IntPtr api, USTP_TE_RESUME_TYPE nResumeType);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribeUserTopic(IntPtr api, USTP_TE_RESUME_TYPE nResumeType);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSubscribeForQuote(IntPtr api, USTP_TE_RESUME_TYPE nResumeType);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleSetHeartbeatTimeout(IntPtr api, unsigned int);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleOpenRequestLog(IntPtr api, const char);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleOpenResponseLog(IntPtr api, const char);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleRegisterDSProxyUserCert(IntPtr api, ref CUstpFtdcDSProxyCheckUserInfoField pDSProxyUserUserInfo, ref CUstpFtdcDSProxyUserCertInField pDSProxyUserCertIn, ref CUstpFtdcDSProxyUserCertOutField pDProxyUserCertOut, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogin(IntPtr api, ref CUstpFtdcReqUserLoginField pReqUserLogin, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserLogout(IntPtr api, ref CUstpFtdcReqUserLogoutField pReqUserLogout, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserPasswordUpdate(IntPtr api, ref CUstpFtdcUserPasswordUpdateField pUserPasswordUpdate, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOrderInsert(IntPtr api, ref CUstpFtdcInputOrderField pInputOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqOrderAction(IntPtr api, ref CUstpFtdcOrderActionField pOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQuoteInsert(IntPtr api, ref CUstpFtdcInputQuoteField pInputQuote, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQuoteAction(IntPtr api, ref CUstpFtdcQuoteActionField pQuoteAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqForQuote(IntPtr api, ref CUstpFtdcReqForQuoteField pReqForQuote, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqMarginCombAction(IntPtr api, ref CUstpFtdcInputMarginCombActionField pInputMarginCombAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqUserDeposit(IntPtr api, ref CUstpFtdcstpUserDepositField pstpUserDeposit, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryOrder(IntPtr api, ref CUstpFtdcQryOrderField pQryOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTrade(IntPtr api, ref CUstpFtdcQryTradeField pQryTrade, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryUserInvestor(IntPtr api, ref CUstpFtdcQryUserInvestorField pQryUserInvestor, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryTradingCode(IntPtr api, ref CUstpFtdcQryTradingCodeField pQryTradingCode, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorAccount(IntPtr api, ref CUstpFtdcQryInvestorAccountField pQryInvestorAccount, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrument(IntPtr api, ref CUstpFtdcQryInstrumentField pQryInstrument, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryExchange(IntPtr api, ref CUstpFtdcQryExchangeField pQryExchange, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorPosition(IntPtr api, ref CUstpFtdcQryInvestorPositionField pQryInvestorPosition, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryComplianceParam(IntPtr api, ref CUstpFtdcQryComplianceParamField pQryComplianceParam, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorFee(IntPtr api, ref CUstpFtdcQryInvestorFeeField pQryInvestorFee, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorMargin(IntPtr api, ref CUstpFtdcQryInvestorMarginField pQryInvestorMargin, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorCombPosition(IntPtr api, ref CUstpFtdcQryInvestorCombPositionField pQryInvestorCombPosition, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInvestorLegPosition(IntPtr api, ref CUstpFtdcQryInvestorLegPositionField pQryInvestorLegPosition, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryInstrumentGroup(IntPtr api, ref CUstpFtdcQryUstpInstrumentGroupField pQryUstpInstrumentGroup, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryClientMarginCombType(IntPtr api, ref CUstpFtdcQryClientMarginCombTypeField pQryClientMarginCombType, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqExecOrderInsert(IntPtr api, ref CUstpFtdcInputExecOrderField pInputExecOrder, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqExecOrderAction(IntPtr api, ref CUstpFtdcInputExecOrderActionField pInputExecOrderAction, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQrySystemTime(IntPtr api, ref CUstpFtdcReqQrySystemTimeField pReqQrySystemTime, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqQryMarginPrefParam(IntPtr api, ref CUstpFtdcReqQryMarginPrefParamField pReqQryMarginPrefParam, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqDSUserCertification(IntPtr api, ref CUstpFtdcDSUserInfoField pDSUserInfo, int nRequestID);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate IntPtr DeleReqDSProxySubmitInfo(IntPtr api, ref CUstpFtdcDSProxySubmitDataField pDSProxySubmitData, int nRequestID);
        public IntPtr Release()
        {
            return (Invoke(_handle, "Release", typeof(DeleRelease)) as DeleRelease)(_api);
        }
                    

        public IntPtr Init()
        {
            return (Invoke(_handle, "Init", typeof(DeleInit)) as DeleInit)(_api);
        }
                    

        public IntPtr Join()
        {
            return (Invoke(_handle, "Join", typeof(DeleJoin)) as DeleJoin)(_api);
        }
                    

        public IntPtr RegisterFront(string pszFrontAddress)
        {
            return (Invoke(_handle, "RegisterFront", typeof(DeleRegisterFront)) as DeleRegisterFront)(_api, pszFrontAddress);
        }
                    

        public IntPtr RegisterQryFront(string pszFrontAddress)
        {
            return (Invoke(_handle, "RegisterQryFront", typeof(DeleRegisterQryFront)) as DeleRegisterQryFront)(_api, pszFrontAddress);
        }
                    

        public IntPtr RegisterNameServer(string pszNsAddress)
        {
            return (Invoke(_handle, "RegisterNameServer", typeof(DeleRegisterNameServer)) as DeleRegisterNameServer)(_api, pszNsAddress);
        }
                    

        public IntPtr RegisterSpi(IntPtr pSpi)
        {
            return (Invoke(_handle, "RegisterSpi", typeof(DeleRegisterSpi)) as DeleRegisterSpi)(_api, pSpi);
        }
                    

        public IntPtr SubscribePrivateTopic(USTP_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribePrivateTopic", typeof(DeleSubscribePrivateTopic)) as DeleSubscribePrivateTopic)(_api, nResumeType);
        }
                    

        public IntPtr SubscribePublicTopic(USTP_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribePublicTopic", typeof(DeleSubscribePublicTopic)) as DeleSubscribePublicTopic)(_api, nResumeType);
        }
                    

        public IntPtr SubscribeUserTopic(USTP_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribeUserTopic", typeof(DeleSubscribeUserTopic)) as DeleSubscribeUserTopic)(_api, nResumeType);
        }
                    

        public IntPtr SubscribeForQuote(USTP_TE_RESUME_TYPE nResumeType)
        {
            return (Invoke(_handle, "SubscribeForQuote", typeof(DeleSubscribeForQuote)) as DeleSubscribeForQuote)(_api, nResumeType);
        }
                    

        public IntPtr SetHeartbeatTimeout(unsigned int)
        {
            return (Invoke(_handle, "SetHeartbeatTimeout", typeof(DeleSetHeartbeatTimeout)) as DeleSetHeartbeatTimeout)(_api, int);
        }
                    

        public IntPtr OpenRequestLog(const char)
        {
            return (Invoke(_handle, "OpenRequestLog", typeof(DeleOpenRequestLog)) as DeleOpenRequestLog)(_api, char);
        }
                    

        public IntPtr OpenResponseLog(const char)
        {
            return (Invoke(_handle, "OpenResponseLog", typeof(DeleOpenResponseLog)) as DeleOpenResponseLog)(_api, char);
        }
                    

        public IntPtr RegisterDSProxyUserCert(string AppID = "",string AuthCode = "",TUstpFtdcDSKeyEncryptType EncryptType = TUstpFtdcDSKeyEncryptType.Normal,string UserCertReqInfo = "",string UserCertRspInfo = "",int UserCertRspInfoLen = 1)
        {
			CUstpFtdcDSProxyCheckUserInfoField pDSProxyUserUserInfo = new CUstpFtdcDSProxyCheckUserInfoField
			{
				AppID = AppID,
				AuthCode = AuthCode,
				EncryptType = EncryptType,
			};
			CUstpFtdcDSProxyUserCertInField pDSProxyUserCertIn = new CUstpFtdcDSProxyUserCertInField
			{
				UserCertReqInfo = UserCertReqInfo,
			};
			CUstpFtdcDSProxyUserCertOutField pDProxyUserCertOut = new CUstpFtdcDSProxyUserCertOutField
			{
				UserCertRspInfo = UserCertRspInfo,
				UserCertRspInfoLen = UserCertRspInfoLen,
			};
            return (Invoke(_handle, "RegisterDSProxyUserCert", typeof(DeleRegisterDSProxyUserCert)) as DeleRegisterDSProxyUserCert)(_api, ref pDSProxyUserUserInfo, ref pDSProxyUserCertIn, ref pDProxyUserCertOut, this.nRequestID++);
        }
                    

        public IntPtr ReqUserLogin(string TradingDay = "",string UserID = "",string BrokerID = "",string Password = "",string UserProductInfo = "",string InterfaceProductInfo = "",string ProtocolInfo = "",string IPAddress = "",string MacAddress = "",int DataCenterID = 1,int UserProductFileSize = 1,TUstpFtdcAuthenticate2TypeType Authenticate2Type = TUstpFtdcAuthenticate2TypeType.USTP_FTDC_A2T_Blank,string Authenticate2Password = "",string TerminalCode = "",string PasswordEncrypt = "")
        {
			CUstpFtdcReqUserLoginField pReqUserLogin = new CUstpFtdcReqUserLoginField
			{
				TradingDay = TradingDay,
				UserID = UserID,
				BrokerID = BrokerID,
				Password = Password,
				UserProductInfo = UserProductInfo,
				InterfaceProductInfo = InterfaceProductInfo,
				ProtocolInfo = ProtocolInfo,
				IPAddress = IPAddress,
				MacAddress = MacAddress,
				DataCenterID = DataCenterID,
				UserProductFileSize = UserProductFileSize,
				Authenticate2Type = Authenticate2Type,
				Authenticate2Password = Authenticate2Password,
				TerminalCode = TerminalCode,
				PasswordEncrypt = PasswordEncrypt,
			};
            return (Invoke(_handle, "ReqUserLogin", typeof(DeleReqUserLogin)) as DeleReqUserLogin)(_api, ref pReqUserLogin, this.nRequestID++);
        }
                    

        public IntPtr ReqUserLogout(string BrokerID = "",string UserID = "")
        {
			CUstpFtdcReqUserLogoutField pReqUserLogout = new CUstpFtdcReqUserLogoutField
			{
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqUserLogout", typeof(DeleReqUserLogout)) as DeleReqUserLogout)(_api, ref pReqUserLogout, this.nRequestID++);
        }
                    

        public IntPtr ReqUserPasswordUpdate(string BrokerID = "",string UserID = "",string OldPassword = "",string NewPassword = "")
        {
			CUstpFtdcUserPasswordUpdateField pUserPasswordUpdate = new CUstpFtdcUserPasswordUpdateField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				OldPassword = OldPassword,
				NewPassword = NewPassword,
			};
            return (Invoke(_handle, "ReqUserPasswordUpdate", typeof(DeleReqUserPasswordUpdate)) as DeleReqUserPasswordUpdate)(_api, ref pUserPasswordUpdate, this.nRequestID++);
        }
                    

        public IntPtr ReqOrderInsert(string BrokerID = "",string ExchangeID = "",string OrderSysID = "",string InvestorID = "",string UserID = "",int SeatNo = 1,string InstrumentID = "",string UserOrderLocalID = "",TUstpFtdcOrderPriceTypeType OrderPriceType = TUstpFtdcOrderPriceTypeType.USTP_FTDC_OPT_AnyPrice,TUstpFtdcDirectionType Direction = TUstpFtdcDirectionType.USTP_FTDC_D_Buy,TUstpFtdcOffsetFlagType OffsetFlag = TUstpFtdcOffsetFlagType.USTP_FTDC_OF_Open,TUstpFtdcHedgeFlagType HedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,double LimitPrice = 0.0,int Volume = 1,TUstpFtdcTimeConditionType TimeCondition = TUstpFtdcTimeConditionType.USTP_FTDC_TC_IOC,string GTDDate = "",TUstpFtdcVolumeConditionType VolumeCondition = TUstpFtdcVolumeConditionType.USTP_FTDC_VC_AV,int MinVolume = 1,double StopPrice = 0.0,TUstpFtdcForceCloseReasonType ForceCloseReason = TUstpFtdcForceCloseReasonType.USTP_FTDC_FCR_NotForceClose,int IsAutoSuspend = 1,string BusinessUnit = "",string UserCustom = "",int BusinessLocalID = 1,string ActionDay = "",TUstpFtdcArbiTypeType ArbiType = TUstpFtdcArbiTypeType.USTP_FTDC_AT_Basic,string ClientID = "")
        {
			CUstpFtdcInputOrderField pInputOrder = new CUstpFtdcInputOrderField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				InvestorID = InvestorID,
				UserID = UserID,
				SeatNo = SeatNo,
				InstrumentID = InstrumentID,
				UserOrderLocalID = UserOrderLocalID,
				OrderPriceType = OrderPriceType,
				Direction = Direction,
				OffsetFlag = OffsetFlag,
				HedgeFlag = HedgeFlag,
				LimitPrice = LimitPrice,
				Volume = Volume,
				TimeCondition = TimeCondition,
				GTDDate = GTDDate,
				VolumeCondition = VolumeCondition,
				MinVolume = MinVolume,
				StopPrice = StopPrice,
				ForceCloseReason = ForceCloseReason,
				IsAutoSuspend = IsAutoSuspend,
				BusinessUnit = BusinessUnit,
				UserCustom = UserCustom,
				BusinessLocalID = BusinessLocalID,
				ActionDay = ActionDay,
				ArbiType = ArbiType,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqOrderInsert", typeof(DeleReqOrderInsert)) as DeleReqOrderInsert)(_api, ref pInputOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqOrderAction(string ExchangeID = "",string OrderSysID = "",string BrokerID = "",string InvestorID = "",string UserID = "",string UserOrderActionLocalID = "",string UserOrderLocalID = "",TUstpFtdcActionFlagType ActionFlag = TUstpFtdcActionFlagType.USTP_FTDC_AF_Delete,double LimitPrice = 0.0,int VolumeChange = 1,int BusinessLocalID = 1,string ClientID = "")
        {
			CUstpFtdcOrderActionField pOrderAction = new CUstpFtdcOrderActionField
			{
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				UserID = UserID,
				UserOrderActionLocalID = UserOrderActionLocalID,
				UserOrderLocalID = UserOrderLocalID,
				ActionFlag = ActionFlag,
				LimitPrice = LimitPrice,
				VolumeChange = VolumeChange,
				BusinessLocalID = BusinessLocalID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqOrderAction", typeof(DeleReqOrderAction)) as DeleReqOrderAction)(_api, ref pOrderAction, this.nRequestID++);
        }
                    

        public IntPtr ReqQuoteInsert(string BrokerID = "",string ExchangeID = "",string InvestorID = "",string UserID = "",string InstrumentID = "",TUstpFtdcDirectionType Direction = TUstpFtdcDirectionType.USTP_FTDC_D_Buy,string QuoteSysID = "",string UserQuoteLocalID = "",string QuoteLocalID = "",int BidVolume = 1,TUstpFtdcOffsetFlagType BidOffsetFlag = TUstpFtdcOffsetFlagType.USTP_FTDC_OF_Open,TUstpFtdcHedgeFlagType BidHedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,double BidPrice = 0.0,int AskVolume = 1,TUstpFtdcOffsetFlagType AskOffsetFlag = TUstpFtdcOffsetFlagType.USTP_FTDC_OF_Open,TUstpFtdcHedgeFlagType AskHedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,double AskPrice = 0.0,string BusinessUnit = "",string UserCustom = "",string BidUserOrderLocalID = "",string AskUserOrderLocalID = "",string BidOrderLocalID = "",string AskOrderLocalID = "",string ReqForQuoteID = "",int StandByTime = 1,string ClientID = "")
        {
			CUstpFtdcInputQuoteField pInputQuote = new CUstpFtdcInputQuoteField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				UserID = UserID,
				InstrumentID = InstrumentID,
				Direction = Direction,
				QuoteSysID = QuoteSysID,
				UserQuoteLocalID = UserQuoteLocalID,
				QuoteLocalID = QuoteLocalID,
				BidVolume = BidVolume,
				BidOffsetFlag = BidOffsetFlag,
				BidHedgeFlag = BidHedgeFlag,
				BidPrice = BidPrice,
				AskVolume = AskVolume,
				AskOffsetFlag = AskOffsetFlag,
				AskHedgeFlag = AskHedgeFlag,
				AskPrice = AskPrice,
				BusinessUnit = BusinessUnit,
				UserCustom = UserCustom,
				BidUserOrderLocalID = BidUserOrderLocalID,
				AskUserOrderLocalID = AskUserOrderLocalID,
				BidOrderLocalID = BidOrderLocalID,
				AskOrderLocalID = AskOrderLocalID,
				ReqForQuoteID = ReqForQuoteID,
				StandByTime = StandByTime,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQuoteInsert", typeof(DeleReqQuoteInsert)) as DeleReqQuoteInsert)(_api, ref pInputQuote, this.nRequestID++);
        }
                    

        public IntPtr ReqQuoteAction(string BrokerID = "",string ExchangeID = "",string InvestorID = "",string UserID = "",string QuoteSysID = "",string UserQuoteLocalID = "",string UserQuoteActionLocalID = "",TUstpFtdcActionFlagType ActionFlag = TUstpFtdcActionFlagType.USTP_FTDC_AF_Delete,string BusinessUnit = "",string UserCustom = "",TUstpFtdcDirectionType Direction = TUstpFtdcDirectionType.USTP_FTDC_D_Buy,string ClientID = "")
        {
			CUstpFtdcQuoteActionField pQuoteAction = new CUstpFtdcQuoteActionField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				UserID = UserID,
				QuoteSysID = QuoteSysID,
				UserQuoteLocalID = UserQuoteLocalID,
				UserQuoteActionLocalID = UserQuoteActionLocalID,
				ActionFlag = ActionFlag,
				BusinessUnit = BusinessUnit,
				UserCustom = UserCustom,
				Direction = Direction,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQuoteAction", typeof(DeleReqQuoteAction)) as DeleReqQuoteAction)(_api, ref pQuoteAction, this.nRequestID++);
        }
                    

        public IntPtr ReqForQuote(string ReqForQuoteID = "",string BrokerID = "",string ExchangeID = "",string InvestorID = "",string UserID = "",string InstrumentID = "",TUstpFtdcDirectionType Direction = TUstpFtdcDirectionType.USTP_FTDC_D_Buy,string TradingDay = "",string ReqForQuoteTime = "",string ClientID = "")
        {
			CUstpFtdcReqForQuoteField pReqForQuote = new CUstpFtdcReqForQuoteField
			{
				ReqForQuoteID = ReqForQuoteID,
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				UserID = UserID,
				InstrumentID = InstrumentID,
				Direction = Direction,
				TradingDay = TradingDay,
				ReqForQuoteTime = ReqForQuoteTime,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqForQuote", typeof(DeleReqForQuote)) as DeleReqForQuote)(_api, ref pReqForQuote, this.nRequestID++);
        }
                    

        public IntPtr ReqMarginCombAction(string BrokerID = "",string ExchangeID = "",string UserID = "",string InvestorID = "",TUstpFtdcHedgeFlagType HedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,string UserActionLocalID = "",string CombInstrumentID = "",int CombVolume = 1,TUstpFtdcCombDirectionType CombDirection = TUstpFtdcCombDirectionType.USTP_FTDC_CA_Combine,string ActionLocalID = "",TUstpFtdcDirectionType Direction = TUstpFtdcDirectionType.USTP_FTDC_D_Buy,string OrderSysID = "",TUstpFtdcCombActionStatusType CombActionStatus = TUstpFtdcCombActionStatusType.USTP_FTDC_CAS_Submitted)
        {
			CUstpFtdcInputMarginCombActionField pInputMarginCombAction = new CUstpFtdcInputMarginCombActionField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				UserID = UserID,
				InvestorID = InvestorID,
				HedgeFlag = HedgeFlag,
				UserActionLocalID = UserActionLocalID,
				CombInstrumentID = CombInstrumentID,
				CombVolume = CombVolume,
				CombDirection = CombDirection,
				ActionLocalID = ActionLocalID,
				Direction = Direction,
				OrderSysID = OrderSysID,
				CombActionStatus = CombActionStatus,
			};
            return (Invoke(_handle, "ReqMarginCombAction", typeof(DeleReqMarginCombAction)) as DeleReqMarginCombAction)(_api, ref pInputMarginCombAction, this.nRequestID++);
        }
                    

        public IntPtr ReqUserDeposit(string BrokerID = "",string UserID = "",string InvestorID = "",double Amount = 0.0,TUstpFtdcAccountDirectionType AmountDirection = TUstpFtdcAccountDirectionType.USTP_FTDC_AD_In,string UserOrderLocalID = "")
        {
			CUstpFtdcstpUserDepositField pstpUserDeposit = new CUstpFtdcstpUserDepositField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				InvestorID = InvestorID,
				Amount = Amount,
				AmountDirection = AmountDirection,
				UserOrderLocalID = UserOrderLocalID,
			};
            return (Invoke(_handle, "ReqUserDeposit", typeof(DeleReqUserDeposit)) as DeleReqUserDeposit)(_api, ref pstpUserDeposit, this.nRequestID++);
        }
                    

        public IntPtr ReqQryOrder(string BrokerID = "",string UserID = "",string ExchangeID = "",string InvestorID = "",string OrderSysID = "",string InstrumentID = "",TUstpFtdcOrderStatusType OrderStatus = TUstpFtdcOrderStatusType.USTP_FTDC_OS_AllTraded,TUstpFtdcOrderTypeType OrderType = TUstpFtdcOrderTypeType.USTP_FTDC_OT_Common,string ClientID = "")
        {
			CUstpFtdcQryOrderField pQryOrder = new CUstpFtdcQryOrderField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				OrderSysID = OrderSysID,
				InstrumentID = InstrumentID,
				OrderStatus = OrderStatus,
				OrderType = OrderType,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryOrder", typeof(DeleReqQryOrder)) as DeleReqQryOrder)(_api, ref pQryOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqQryTrade(string BrokerID = "",string UserID = "",string ExchangeID = "",string InvestorID = "",string TradeID = "",string InstrumentID = "",string ClientID = "")
        {
			CUstpFtdcQryTradeField pQryTrade = new CUstpFtdcQryTradeField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				TradeID = TradeID,
				InstrumentID = InstrumentID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryTrade", typeof(DeleReqQryTrade)) as DeleReqQryTrade)(_api, ref pQryTrade, this.nRequestID++);
        }
                    

        public IntPtr ReqQryUserInvestor(string BrokerID = "",string UserID = "")
        {
			CUstpFtdcQryUserInvestorField pQryUserInvestor = new CUstpFtdcQryUserInvestorField
			{
				BrokerID = BrokerID,
				UserID = UserID,
			};
            return (Invoke(_handle, "ReqQryUserInvestor", typeof(DeleReqQryUserInvestor)) as DeleReqQryUserInvestor)(_api, ref pQryUserInvestor, this.nRequestID++);
        }
                    

        public IntPtr ReqQryTradingCode(string BrokerID = "",string UserID = "",string InvestorID = "",string ExchangeID = "",string ClientID = "")
        {
			CUstpFtdcQryTradingCodeField pQryTradingCode = new CUstpFtdcQryTradingCodeField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryTradingCode", typeof(DeleReqQryTradingCode)) as DeleReqQryTradingCode)(_api, ref pQryTradingCode, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorAccount(string BrokerID = "",string UserID = "",string InvestorID = "")
        {
			CUstpFtdcQryInvestorAccountField pQryInvestorAccount = new CUstpFtdcQryInvestorAccountField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				InvestorID = InvestorID,
			};
            return (Invoke(_handle, "ReqQryInvestorAccount", typeof(DeleReqQryInvestorAccount)) as DeleReqQryInvestorAccount)(_api, ref pQryInvestorAccount, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInstrument(string ExchangeID = "",string ProductID = "",string InstrumentID = "")
        {
			CUstpFtdcQryInstrumentField pQryInstrument = new CUstpFtdcQryInstrumentField
			{
				ExchangeID = ExchangeID,
				ProductID = ProductID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInstrument", typeof(DeleReqQryInstrument)) as DeleReqQryInstrument)(_api, ref pQryInstrument, this.nRequestID++);
        }
                    

        public IntPtr ReqQryExchange(string ExchangeID = "")
        {
			CUstpFtdcQryExchangeField pQryExchange = new CUstpFtdcQryExchangeField
			{
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQryExchange", typeof(DeleReqQryExchange)) as DeleReqQryExchange)(_api, ref pQryExchange, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorPosition(string BrokerID = "",string UserID = "",string ExchangeID = "",string InvestorID = "",string InstrumentID = "")
        {
			CUstpFtdcQryInvestorPositionField pQryInvestorPosition = new CUstpFtdcQryInvestorPositionField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInvestorPosition", typeof(DeleReqQryInvestorPosition)) as DeleReqQryInvestorPosition)(_api, ref pQryInvestorPosition, this.nRequestID++);
        }
                    

        public IntPtr ReqQryComplianceParam(string BrokerID = "",string UserID = "",string InvestorID = "",string ExchangeID = "",string ClientID = "")
        {
			CUstpFtdcQryComplianceParamField pQryComplianceParam = new CUstpFtdcQryComplianceParamField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryComplianceParam", typeof(DeleReqQryComplianceParam)) as DeleReqQryComplianceParam)(_api, ref pQryComplianceParam, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorFee(string BrokerID = "",string UserID = "",string InvestorID = "",string ExchangeID = "",string InstrumentID = "",string ClientID = "")
        {
			CUstpFtdcQryInvestorFeeField pQryInvestorFee = new CUstpFtdcQryInvestorFeeField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryInvestorFee", typeof(DeleReqQryInvestorFee)) as DeleReqQryInvestorFee)(_api, ref pQryInvestorFee, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorMargin(string BrokerID = "",string UserID = "",string InvestorID = "",string ExchangeID = "",string InstrumentID = "",string ClientID = "")
        {
			CUstpFtdcQryInvestorMarginField pQryInvestorMargin = new CUstpFtdcQryInvestorMarginField
			{
				BrokerID = BrokerID,
				UserID = UserID,
				InvestorID = InvestorID,
				ExchangeID = ExchangeID,
				InstrumentID = InstrumentID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryInvestorMargin", typeof(DeleReqQryInvestorMargin)) as DeleReqQryInvestorMargin)(_api, ref pQryInvestorMargin, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorCombPosition(string BrokerID = "",string ExchangeID = "",string InvestorID = "",TUstpFtdcHedgeFlagType HedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,string CombInstrumentID = "",string ClientID = "")
        {
			CUstpFtdcQryInvestorCombPositionField pQryInvestorCombPosition = new CUstpFtdcQryInvestorCombPositionField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				HedgeFlag = HedgeFlag,
				CombInstrumentID = CombInstrumentID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryInvestorCombPosition", typeof(DeleReqQryInvestorCombPosition)) as DeleReqQryInvestorCombPosition)(_api, ref pQryInvestorCombPosition, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInvestorLegPosition(string BrokerID = "",string ExchangeID = "",string InvestorID = "",TUstpFtdcHedgeFlagType HedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,string LegInstrumentID = "",string ClientID = "")
        {
			CUstpFtdcQryInvestorLegPositionField pQryInvestorLegPosition = new CUstpFtdcQryInvestorLegPositionField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				InvestorID = InvestorID,
				HedgeFlag = HedgeFlag,
				LegInstrumentID = LegInstrumentID,
				ClientID = ClientID,
			};
            return (Invoke(_handle, "ReqQryInvestorLegPosition", typeof(DeleReqQryInvestorLegPosition)) as DeleReqQryInvestorLegPosition)(_api, ref pQryInvestorLegPosition, this.nRequestID++);
        }
                    

        public IntPtr ReqQryInstrumentGroup(string ExchangeID = "",string BrokerID = "",string InstrumentID = "")
        {
			CUstpFtdcQryUstpInstrumentGroupField pQryUstpInstrumentGroup = new CUstpFtdcQryUstpInstrumentGroupField
			{
				ExchangeID = ExchangeID,
				BrokerID = BrokerID,
				InstrumentID = InstrumentID,
			};
            return (Invoke(_handle, "ReqQryInstrumentGroup", typeof(DeleReqQryInstrumentGroup)) as DeleReqQryInstrumentGroup)(_api, ref pQryUstpInstrumentGroup, this.nRequestID++);
        }
                    

        public IntPtr ReqQryClientMarginCombType(string ExchangeID = "",string BrokerID = "",string InvestorID = "",TUstpFtdcHedgeFlagType HedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,string InstrumentGroupID = "")
        {
			CUstpFtdcQryClientMarginCombTypeField pQryClientMarginCombType = new CUstpFtdcQryClientMarginCombTypeField
			{
				ExchangeID = ExchangeID,
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				HedgeFlag = HedgeFlag,
				InstrumentGroupID = InstrumentGroupID,
			};
            return (Invoke(_handle, "ReqQryClientMarginCombType", typeof(DeleReqQryClientMarginCombType)) as DeleReqQryClientMarginCombType)(_api, ref pQryClientMarginCombType, this.nRequestID++);
        }
                    

        public IntPtr ReqExecOrderInsert(string BrokerID = "",string ExchangeID = "",string OrderSysID = "",string InvestorID = "",string UserID = "",string InstrumentID = "",string UserOrderLocalID = "",TUstpFtdcOrderTypeType OrderType = TUstpFtdcOrderTypeType.USTP_FTDC_OT_Common,TUstpFtdcDeliveryFlagType DeliveryFlag = TUstpFtdcDeliveryFlagType.USTP_FTDC_DF_ExecOpen,TUstpFtdcHedgeFlagType HedgeFlag = TUstpFtdcHedgeFlagType.USTP_FTDC_CHF_Speculation,int Volume = 1,string UserCustom = "",string ActionDay = "",int BusinessLocalID = 1,string BusinessUnit = "")
        {
			CUstpFtdcInputExecOrderField pInputExecOrder = new CUstpFtdcInputExecOrderField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				InvestorID = InvestorID,
				UserID = UserID,
				InstrumentID = InstrumentID,
				UserOrderLocalID = UserOrderLocalID,
				OrderType = OrderType,
				DeliveryFlag = DeliveryFlag,
				HedgeFlag = HedgeFlag,
				Volume = Volume,
				UserCustom = UserCustom,
				ActionDay = ActionDay,
				BusinessLocalID = BusinessLocalID,
				BusinessUnit = BusinessUnit,
			};
            return (Invoke(_handle, "ReqExecOrderInsert", typeof(DeleReqExecOrderInsert)) as DeleReqExecOrderInsert)(_api, ref pInputExecOrder, this.nRequestID++);
        }
                    

        public IntPtr ReqExecOrderAction(string ExchangeID = "",string OrderSysID = "",string BrokerID = "",string InvestorID = "",string UserID = "",string UserOrderActionLocalID = "",string UserOrderLocalID = "",TUstpFtdcActionFlagType ActionFlag = TUstpFtdcActionFlagType.USTP_FTDC_AF_Delete,int VolumeChange = 1,int BusinessLocalID = 1,TUstpFtdcOrderTypeType OrderType = TUstpFtdcOrderTypeType.USTP_FTDC_OT_Common)
        {
			CUstpFtdcInputExecOrderActionField pInputExecOrderAction = new CUstpFtdcInputExecOrderActionField
			{
				ExchangeID = ExchangeID,
				OrderSysID = OrderSysID,
				BrokerID = BrokerID,
				InvestorID = InvestorID,
				UserID = UserID,
				UserOrderActionLocalID = UserOrderActionLocalID,
				UserOrderLocalID = UserOrderLocalID,
				ActionFlag = ActionFlag,
				VolumeChange = VolumeChange,
				BusinessLocalID = BusinessLocalID,
				OrderType = OrderType,
			};
            return (Invoke(_handle, "ReqExecOrderAction", typeof(DeleReqExecOrderAction)) as DeleReqExecOrderAction)(_api, ref pInputExecOrderAction, this.nRequestID++);
        }
                    

        public IntPtr ReqQrySystemTime(string ExchangeID = "")
        {
			CUstpFtdcReqQrySystemTimeField pReqQrySystemTime = new CUstpFtdcReqQrySystemTimeField
			{
				ExchangeID = ExchangeID,
			};
            return (Invoke(_handle, "ReqQrySystemTime", typeof(DeleReqQrySystemTime)) as DeleReqQrySystemTime)(_api, ref pReqQrySystemTime, this.nRequestID++);
        }
                    

        public IntPtr ReqQryMarginPrefParam(string BrokerID = "",string ExchangeID = "",string CombInstrumentID = "",string CombInstrumentName = "")
        {
			CUstpFtdcReqQryMarginPrefParamField pReqQryMarginPrefParam = new CUstpFtdcReqQryMarginPrefParamField
			{
				BrokerID = BrokerID,
				ExchangeID = ExchangeID,
				CombInstrumentID = CombInstrumentID,
				CombInstrumentName = CombInstrumentName,
			};
            return (Invoke(_handle, "ReqQryMarginPrefParam", typeof(DeleReqQryMarginPrefParam)) as DeleReqQryMarginPrefParam)(_api, ref pReqQryMarginPrefParam, this.nRequestID++);
        }
                    

        public IntPtr ReqDSUserCertification(string AppID = "",string AuthCode = "",TUstpFtdcDSKeyEncryptType EncryptType = TUstpFtdcDSKeyEncryptType.Normal)
        {
			CUstpFtdcDSUserInfoField pDSUserInfo = new CUstpFtdcDSUserInfoField
			{
				AppID = AppID,
				AuthCode = AuthCode,
				EncryptType = EncryptType,
			};
            return (Invoke(_handle, "ReqDSUserCertification", typeof(DeleReqDSUserCertification)) as DeleReqDSUserCertification)(_api, ref pDSUserInfo, this.nRequestID++);
        }
                    

        public IntPtr ReqDSProxySubmitInfo(string AppID = "",string TerminalPubNetIP = "",string TerminalPubNetPort = "",string TerminalLoginTime = "",TUstpFtdcDSExceptionFlagType ExceptionFlag = TUstpFtdcDSExceptionFlagType.Normal,string RelayID = "",string TerminalSystemData = "")
        {
			CUstpFtdcDSProxySubmitDataField pDSProxySubmitData = new CUstpFtdcDSProxySubmitDataField
			{
				AppID = AppID,
				TerminalPubNetIP = TerminalPubNetIP,
				TerminalPubNetPort = TerminalPubNetPort,
				TerminalLoginTime = TerminalLoginTime,
				ExceptionFlag = ExceptionFlag,
				RelayID = RelayID,
				TerminalSystemData = TerminalSystemData,
			};
            return (Invoke(_handle, "ReqDSProxySubmitInfo", typeof(DeleReqDSProxySubmitInfo)) as DeleReqDSProxySubmitInfo)(_api, ref pDSProxySubmitData, this.nRequestID++);
        }
                    
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		delegate void DeleSet(IntPtr spi, Delegate func);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnFrontConnected();
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnQryFrontConnected();
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnFrontDisconnected(int nReason);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnQryFrontDisconnected(int nReason);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnHeartBeatWarning(int nTimeLapse);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnPackageStart(int nTopicID,int nSequenceNo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnPackageEnd(int nTopicID,int nSequenceNo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspError(ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogin(ref CUstpFtdcRspUserLoginField pRspUserLogin,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserLogout(ref CUstpFtdcRspUserLogoutField pRspUserLogout,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserPasswordUpdate(ref CUstpFtdcUserPasswordUpdateField pUserPasswordUpdate,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOrderInsert(ref CUstpFtdcInputOrderField pInputOrder,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspOrderAction(ref CUstpFtdcOrderActionField pOrderAction,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQuoteInsert(ref CUstpFtdcInputQuoteField pInputQuote,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQuoteAction(ref CUstpFtdcQuoteActionField pQuoteAction,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspForQuote(ref CUstpFtdcReqForQuoteField pReqForQuote,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspMarginCombAction(ref CUstpFtdcInputMarginCombActionField pInputMarginCombAction,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspUserDeposit(ref CUstpFtdcstpUserDepositField pstpUserDeposit,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnFlowMessageCancel(ref CUstpFtdcFlowMessageCancelField pFlowMessageCancel);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnTrade(ref CUstpFtdcTradeField pTrade);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnOrder(ref CUstpFtdcOrderField pOrder);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOrderInsert(ref CUstpFtdcInputOrderField pInputOrder,ref CUstpFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnOrderAction(ref CUstpFtdcOrderActionField pOrderAction,ref CUstpFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnInstrumentStatus(ref CUstpFtdcInstrumentStatusField pInstrumentStatus);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnInvestorAccountDeposit(ref CUstpFtdcInvestorAccountDepositResField pInvestorAccountDepositRes);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnQuote(ref CUstpFtdcRtnQuoteField pRtnQuote);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQuoteInsert(ref CUstpFtdcInputQuoteField pInputQuote,ref CUstpFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnQuoteAction(ref CUstpFtdcQuoteActionField pQuoteAction,ref CUstpFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnForQuote(ref CUstpFtdcReqForQuoteField pReqForQuote);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnMarginCombinationLeg(ref CUstpFtdcMarginCombinationLegField pMarginCombinationLeg);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnMarginCombAction(ref CUstpFtdcInputMarginCombActionField pInputMarginCombAction);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnUserDeposit(ref CUstpFtdcstpUserDepositField pstpUserDeposit);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQueryUserLogin(ref CUstpFtdcRspUserLoginField pRspUserLogin,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryOrder(ref CUstpFtdcOrderField pOrder,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTrade(ref CUstpFtdcTradeField pTrade,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryUserInvestor(ref CUstpFtdcRspUserInvestorField pRspUserInvestor,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryTradingCode(ref CUstpFtdcRspTradingCodeField pRspTradingCode,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorAccount(ref CUstpFtdcRspInvestorAccountField pRspInvestorAccount,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrument(ref CUstpFtdcRspInstrumentField pRspInstrument,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryExchange(ref CUstpFtdcRspExchangeField pRspExchange,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorPosition(ref CUstpFtdcRspInvestorPositionField pRspInvestorPosition,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryComplianceParam(ref CUstpFtdcRspComplianceParamField pRspComplianceParam,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorFee(ref CUstpFtdcInvestorFeeField pInvestorFee,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorMargin(ref CUstpFtdcInvestorMarginField pInvestorMargin,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorCombPosition(ref CUstpFtdcRspInvestorCombPositionField pRspInvestorCombPosition,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInvestorLegPosition(ref CUstpFtdcRspInvestorLegPositionField pRspInvestorLegPosition,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryInstrumentGroup(ref CUstpFtdcRspInstrumentGroupField pRspInstrumentGroup,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryClientMarginCombType(ref CUstpFtdcRspClientMarginCombTypeField pRspClientMarginCombType,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspExecOrderInsert(ref CUstpFtdcInputExecOrderField pInputExecOrder,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspExecOrderAction(ref CUstpFtdcInputExecOrderActionField pInputExecOrderAction,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnExecOrder(ref CUstpFtdcExecOrderField pExecOrder);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnExecOrderInsert(ref CUstpFtdcInputExecOrderField pInputExecOrder,ref CUstpFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnErrRtnExecOrderAction(ref CUstpFtdcInputExecOrderActionField pInputExecOrderAction,ref CUstpFtdcRspInfoField pRspInfo);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRtnTransferMoney(ref CUstpFtdcSyncMoneyTransferField pSyncMoneyTransfer);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQrySystemTime(ref CUstpFtdcRspQrySystemTimeField pRspQrySystemTime,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspQryMarginPrefParam(ref CUstpFtdcRspQryMarginPrefParamField pRspQryMarginPrefParam,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspDSUserCertification(ref CUstpFtdcDSUserCertRspDataField pDSUserCertRspData,ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		[UnmanagedFunctionPointer(CallingConvention.Cdecl, CharSet = CharSet.Ansi, SetLastError = true)]
		public delegate void DeleOnRspDSProxySubmitInfo(ref CUstpFtdcRspInfoField pRspInfo,int nRequestID,bool bIsLast);
		public void SetOnFrontConnected(DeleOnFrontConnected func) {(Invoke(_handle, "SetOnFrontConnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnQryFrontConnected(DeleOnQryFrontConnected func) {(Invoke(_handle, "SetOnQryFrontConnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnFrontDisconnected(DeleOnFrontDisconnected func) {(Invoke(_handle, "SetOnFrontDisconnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnQryFrontDisconnected(DeleOnQryFrontDisconnected func) {(Invoke(_handle, "SetOnQryFrontDisconnected", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnHeartBeatWarning(DeleOnHeartBeatWarning func) {(Invoke(_handle, "SetOnHeartBeatWarning", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnPackageStart(DeleOnPackageStart func) {(Invoke(_handle, "SetOnPackageStart", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnPackageEnd(DeleOnPackageEnd func) {(Invoke(_handle, "SetOnPackageEnd", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspError(DeleOnRspError func) {(Invoke(_handle, "SetOnRspError", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserLogin(DeleOnRspUserLogin func) {(Invoke(_handle, "SetOnRspUserLogin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserLogout(DeleOnRspUserLogout func) {(Invoke(_handle, "SetOnRspUserLogout", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserPasswordUpdate(DeleOnRspUserPasswordUpdate func) {(Invoke(_handle, "SetOnRspUserPasswordUpdate", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspOrderInsert(DeleOnRspOrderInsert func) {(Invoke(_handle, "SetOnRspOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspOrderAction(DeleOnRspOrderAction func) {(Invoke(_handle, "SetOnRspOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQuoteInsert(DeleOnRspQuoteInsert func) {(Invoke(_handle, "SetOnRspQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQuoteAction(DeleOnRspQuoteAction func) {(Invoke(_handle, "SetOnRspQuoteAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspForQuote(DeleOnRspForQuote func) {(Invoke(_handle, "SetOnRspForQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspMarginCombAction(DeleOnRspMarginCombAction func) {(Invoke(_handle, "SetOnRspMarginCombAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspUserDeposit(DeleOnRspUserDeposit func) {(Invoke(_handle, "SetOnRspUserDeposit", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnFlowMessageCancel(DeleOnRtnFlowMessageCancel func) {(Invoke(_handle, "SetOnRtnFlowMessageCancel", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnTrade(DeleOnRtnTrade func) {(Invoke(_handle, "SetOnRtnTrade", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnOrder(DeleOnRtnOrder func) {(Invoke(_handle, "SetOnRtnOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnOrderInsert(DeleOnErrRtnOrderInsert func) {(Invoke(_handle, "SetOnErrRtnOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnOrderAction(DeleOnErrRtnOrderAction func) {(Invoke(_handle, "SetOnErrRtnOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnInstrumentStatus(DeleOnRtnInstrumentStatus func) {(Invoke(_handle, "SetOnRtnInstrumentStatus", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnInvestorAccountDeposit(DeleOnRtnInvestorAccountDeposit func) {(Invoke(_handle, "SetOnRtnInvestorAccountDeposit", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnQuote(DeleOnRtnQuote func) {(Invoke(_handle, "SetOnRtnQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnQuoteInsert(DeleOnErrRtnQuoteInsert func) {(Invoke(_handle, "SetOnErrRtnQuoteInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnQuoteAction(DeleOnErrRtnQuoteAction func) {(Invoke(_handle, "SetOnErrRtnQuoteAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnForQuote(DeleOnRtnForQuote func) {(Invoke(_handle, "SetOnRtnForQuote", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnMarginCombinationLeg(DeleOnRtnMarginCombinationLeg func) {(Invoke(_handle, "SetOnRtnMarginCombinationLeg", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnMarginCombAction(DeleOnRtnMarginCombAction func) {(Invoke(_handle, "SetOnRtnMarginCombAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnUserDeposit(DeleOnRtnUserDeposit func) {(Invoke(_handle, "SetOnRtnUserDeposit", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQueryUserLogin(DeleOnRspQueryUserLogin func) {(Invoke(_handle, "SetOnRspQueryUserLogin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryOrder(DeleOnRspQryOrder func) {(Invoke(_handle, "SetOnRspQryOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTrade(DeleOnRspQryTrade func) {(Invoke(_handle, "SetOnRspQryTrade", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryUserInvestor(DeleOnRspQryUserInvestor func) {(Invoke(_handle, "SetOnRspQryUserInvestor", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryTradingCode(DeleOnRspQryTradingCode func) {(Invoke(_handle, "SetOnRspQryTradingCode", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorAccount(DeleOnRspQryInvestorAccount func) {(Invoke(_handle, "SetOnRspQryInvestorAccount", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInstrument(DeleOnRspQryInstrument func) {(Invoke(_handle, "SetOnRspQryInstrument", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryExchange(DeleOnRspQryExchange func) {(Invoke(_handle, "SetOnRspQryExchange", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorPosition(DeleOnRspQryInvestorPosition func) {(Invoke(_handle, "SetOnRspQryInvestorPosition", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryComplianceParam(DeleOnRspQryComplianceParam func) {(Invoke(_handle, "SetOnRspQryComplianceParam", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorFee(DeleOnRspQryInvestorFee func) {(Invoke(_handle, "SetOnRspQryInvestorFee", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorMargin(DeleOnRspQryInvestorMargin func) {(Invoke(_handle, "SetOnRspQryInvestorMargin", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorCombPosition(DeleOnRspQryInvestorCombPosition func) {(Invoke(_handle, "SetOnRspQryInvestorCombPosition", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInvestorLegPosition(DeleOnRspQryInvestorLegPosition func) {(Invoke(_handle, "SetOnRspQryInvestorLegPosition", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryInstrumentGroup(DeleOnRspQryInstrumentGroup func) {(Invoke(_handle, "SetOnRspQryInstrumentGroup", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryClientMarginCombType(DeleOnRspQryClientMarginCombType func) {(Invoke(_handle, "SetOnRspQryClientMarginCombType", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspExecOrderInsert(DeleOnRspExecOrderInsert func) {(Invoke(_handle, "SetOnRspExecOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspExecOrderAction(DeleOnRspExecOrderAction func) {(Invoke(_handle, "SetOnRspExecOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnExecOrder(DeleOnRtnExecOrder func) {(Invoke(_handle, "SetOnRtnExecOrder", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnExecOrderInsert(DeleOnErrRtnExecOrderInsert func) {(Invoke(_handle, "SetOnErrRtnExecOrderInsert", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnErrRtnExecOrderAction(DeleOnErrRtnExecOrderAction func) {(Invoke(_handle, "SetOnErrRtnExecOrderAction", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRtnTransferMoney(DeleOnRtnTransferMoney func) {(Invoke(_handle, "SetOnRtnTransferMoney", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQrySystemTime(DeleOnRspQrySystemTime func) {(Invoke(_handle, "SetOnRspQrySystemTime", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspQryMarginPrefParam(DeleOnRspQryMarginPrefParam func) {(Invoke(_handle, "SetOnRspQryMarginPrefParam", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspDSUserCertification(DeleOnRspDSUserCertification func) {(Invoke(_handle, "SetOnRspDSUserCertification", typeof(DeleSet)) as DeleSet)(_spi, func);}
		public void SetOnRspDSProxySubmitInfo(DeleOnRspDSProxySubmitInfo func) {(Invoke(_handle, "SetOnRspDSProxySubmitInfo", typeof(DeleSet)) as DeleSet)(_spi, func);}
	}
}