#include "trade.h"
#include <string.h>
int nReq;

Trade::Trade(void)
{	
	_FrontConnected = NULL;
	_QryFrontConnected = NULL;
	_FrontDisconnected = NULL;
	_QryFrontDisconnected = NULL;
	_HeartBeatWarning = NULL;
	_PackageStart = NULL;
	_PackageEnd = NULL;
	_RspError = NULL;
	_RspUserLogin = NULL;
	_RspUserLogout = NULL;
	_RspUserPasswordUpdate = NULL;
	_RspOrderInsert = NULL;
	_RspOrderAction = NULL;
	_RspQuoteInsert = NULL;
	_RspQuoteAction = NULL;
	_RspForQuote = NULL;
	_RspMarginCombAction = NULL;
	_RspUserDeposit = NULL;
	_RtnFlowMessageCancel = NULL;
	_RtnTrade = NULL;
	_RtnOrder = NULL;
	_ErrRtnOrderInsert = NULL;
	_ErrRtnOrderAction = NULL;
	_RtnInstrumentStatus = NULL;
	_RtnInvestorAccountDeposit = NULL;
	_RtnQuote = NULL;
	_ErrRtnQuoteInsert = NULL;
	_ErrRtnQuoteAction = NULL;
	_RtnForQuote = NULL;
	_RtnMarginCombinationLeg = NULL;
	_RtnMarginCombAction = NULL;
	_RtnUserDeposit = NULL;
	_RspQueryUserLogin = NULL;
	_RspQryOrder = NULL;
	_RspQryTrade = NULL;
	_RspQryUserInvestor = NULL;
	_RspQryTradingCode = NULL;
	_RspQryInvestorAccount = NULL;
	_RspQryInstrument = NULL;
	_RspQryExchange = NULL;
	_RspQryInvestorPosition = NULL;
	_RspQryComplianceParam = NULL;
	_RspQryInvestorFee = NULL;
	_RspQryInvestorMargin = NULL;
	_RspQryInvestorCombPosition = NULL;
	_RspQryInvestorLegPosition = NULL;
	_RspQryInstrumentGroup = NULL;
	_RspQryClientMarginCombType = NULL;
	_RspExecOrderInsert = NULL;
	_RspExecOrderAction = NULL;
	_RtnExecOrder = NULL;
	_ErrRtnExecOrderInsert = NULL;
	_ErrRtnExecOrderAction = NULL;
	_RtnTransferMoney = NULL;
	_RspQrySystemTime = NULL;
	_RspQryMarginPrefParam = NULL;
	_RspDSUserCertification = NULL;
	_RspDSProxySubmitInfo = NULL;
}

DLL_EXPORT_C_DECL void WINAPI SetOnFrontConnected(Trade* spi, void* func){spi->_FrontConnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnQryFrontConnected(Trade* spi, void* func){spi->_QryFrontConnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnFrontDisconnected(Trade* spi, void* func){spi->_FrontDisconnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnQryFrontDisconnected(Trade* spi, void* func){spi->_QryFrontDisconnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnHeartBeatWarning(Trade* spi, void* func){spi->_HeartBeatWarning = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnPackageStart(Trade* spi, void* func){spi->_PackageStart = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnPackageEnd(Trade* spi, void* func){spi->_PackageEnd = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspError(Trade* spi, void* func){spi->_RspError = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogin(Trade* spi, void* func){spi->_RspUserLogin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogout(Trade* spi, void* func){spi->_RspUserLogout = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserPasswordUpdate(Trade* spi, void* func){spi->_RspUserPasswordUpdate = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspOrderInsert(Trade* spi, void* func){spi->_RspOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspOrderAction(Trade* spi, void* func){spi->_RspOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQuoteInsert(Trade* spi, void* func){spi->_RspQuoteInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQuoteAction(Trade* spi, void* func){spi->_RspQuoteAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspForQuote(Trade* spi, void* func){spi->_RspForQuote = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspMarginCombAction(Trade* spi, void* func){spi->_RspMarginCombAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserDeposit(Trade* spi, void* func){spi->_RspUserDeposit = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnFlowMessageCancel(Trade* spi, void* func){spi->_RtnFlowMessageCancel = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnTrade(Trade* spi, void* func){spi->_RtnTrade = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnOrder(Trade* spi, void* func){spi->_RtnOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnOrderInsert(Trade* spi, void* func){spi->_ErrRtnOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnOrderAction(Trade* spi, void* func){spi->_ErrRtnOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnInstrumentStatus(Trade* spi, void* func){spi->_RtnInstrumentStatus = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnInvestorAccountDeposit(Trade* spi, void* func){spi->_RtnInvestorAccountDeposit = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnQuote(Trade* spi, void* func){spi->_RtnQuote = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnQuoteInsert(Trade* spi, void* func){spi->_ErrRtnQuoteInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnQuoteAction(Trade* spi, void* func){spi->_ErrRtnQuoteAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnForQuote(Trade* spi, void* func){spi->_RtnForQuote = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnMarginCombinationLeg(Trade* spi, void* func){spi->_RtnMarginCombinationLeg = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnMarginCombAction(Trade* spi, void* func){spi->_RtnMarginCombAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnUserDeposit(Trade* spi, void* func){spi->_RtnUserDeposit = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQueryUserLogin(Trade* spi, void* func){spi->_RspQueryUserLogin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryOrder(Trade* spi, void* func){spi->_RspQryOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTrade(Trade* spi, void* func){spi->_RspQryTrade = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryUserInvestor(Trade* spi, void* func){spi->_RspQryUserInvestor = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryTradingCode(Trade* spi, void* func){spi->_RspQryTradingCode = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorAccount(Trade* spi, void* func){spi->_RspQryInvestorAccount = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInstrument(Trade* spi, void* func){spi->_RspQryInstrument = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryExchange(Trade* spi, void* func){spi->_RspQryExchange = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorPosition(Trade* spi, void* func){spi->_RspQryInvestorPosition = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryComplianceParam(Trade* spi, void* func){spi->_RspQryComplianceParam = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorFee(Trade* spi, void* func){spi->_RspQryInvestorFee = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorMargin(Trade* spi, void* func){spi->_RspQryInvestorMargin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorCombPosition(Trade* spi, void* func){spi->_RspQryInvestorCombPosition = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInvestorLegPosition(Trade* spi, void* func){spi->_RspQryInvestorLegPosition = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryInstrumentGroup(Trade* spi, void* func){spi->_RspQryInstrumentGroup = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryClientMarginCombType(Trade* spi, void* func){spi->_RspQryClientMarginCombType = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspExecOrderInsert(Trade* spi, void* func){spi->_RspExecOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspExecOrderAction(Trade* spi, void* func){spi->_RspExecOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnExecOrder(Trade* spi, void* func){spi->_RtnExecOrder = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnExecOrderInsert(Trade* spi, void* func){spi->_ErrRtnExecOrderInsert = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnErrRtnExecOrderAction(Trade* spi, void* func){spi->_ErrRtnExecOrderAction = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnTransferMoney(Trade* spi, void* func){spi->_RtnTransferMoney = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQrySystemTime(Trade* spi, void* func){spi->_RspQrySystemTime = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspQryMarginPrefParam(Trade* spi, void* func){spi->_RspQryMarginPrefParam = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspDSUserCertification(Trade* spi, void* func){spi->_RspDSUserCertification = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspDSProxySubmitInfo(Trade* spi, void* func){spi->_RspDSProxySubmitInfo = func;}

DLL_EXPORT_C_DECL void* WINAPI CreateApi(){return CUstpFtdcTraderApi::CreateFtdcTraderApi("./log/");}
DLL_EXPORT_C_DECL void* WINAPI CreateSpi(){return new Trade();}
DLL_EXPORT_C_DECL void* WINAPI Release(CUstpFtdcTraderApi *api){api->Release(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Init(CUstpFtdcTraderApi *api){api->Init(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Join(CUstpFtdcTraderApi *api){api->Join(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterFront(CUstpFtdcTraderApi *api, char *pszFrontAddress){api->RegisterFront(pszFrontAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterQryFront(CUstpFtdcTraderApi *api, char *pszFrontAddress){api->RegisterQryFront(pszFrontAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterNameServer(CUstpFtdcTraderApi *api, char *pszNsAddress){api->RegisterNameServer(pszNsAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterSpi(CUstpFtdcTraderApi *api, CUstpFtdcTraderSpi *pSpi){api->RegisterSpi(pSpi); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribePrivateTopic(CUstpFtdcTraderApi *api, USTP_TE_RESUME_TYPE nResumeType){api->SubscribePrivateTopic(nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribePublicTopic(CUstpFtdcTraderApi *api, USTP_TE_RESUME_TYPE nResumeType){api->SubscribePublicTopic(nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribeUserTopic(CUstpFtdcTraderApi *api, USTP_TE_RESUME_TYPE nResumeType){api->SubscribeUserTopic(nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribeForQuote(CUstpFtdcTraderApi *api, USTP_TE_RESUME_TYPE nResumeType){api->SubscribeForQuote(nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SetHeartbeatTimeout(CUstpFtdcTraderApi *api, unsigned int timeout){api->SetHeartbeatTimeout(timeout); return 0;}
DLL_EXPORT_C_DECL void* WINAPI OpenRequestLog(CUstpFtdcTraderApi *api, const char *pszReqLogFileName){api->OpenRequestLog(pszReqLogFileName); return 0;}
DLL_EXPORT_C_DECL void* WINAPI OpenResponseLog(CUstpFtdcTraderApi *api, const char *pszRspLogFileName){api->OpenResponseLog(pszRspLogFileName); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterDSProxyUserCert(CUstpFtdcTraderApi *api, CUstpFtdcDSProxyCheckUserInfoField *pDSProxyUserUserInfo, CUstpFtdcDSProxyUserCertInField *pDSProxyUserCertIn, CUstpFtdcDSProxyUserCertOutField *pDProxyUserCertOut, int nRequestID){api->RegisterDSProxyUserCert(pDSProxyUserUserInfo, pDSProxyUserCertIn, pDProxyUserCertOut, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogin(CUstpFtdcTraderApi *api, CUstpFtdcReqUserLoginField *pReqUserLogin, int nRequestID){api->ReqUserLogin(pReqUserLogin, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogout(CUstpFtdcTraderApi *api, CUstpFtdcReqUserLogoutField *pReqUserLogout, int nRequestID){api->ReqUserLogout(pReqUserLogout, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserPasswordUpdate(CUstpFtdcTraderApi *api, CUstpFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID){api->ReqUserPasswordUpdate(pUserPasswordUpdate, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqOrderInsert(CUstpFtdcTraderApi *api, CUstpFtdcInputOrderField *pInputOrder, int nRequestID){api->ReqOrderInsert(pInputOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqOrderAction(CUstpFtdcTraderApi *api, CUstpFtdcOrderActionField *pOrderAction, int nRequestID){api->ReqOrderAction(pOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQuoteInsert(CUstpFtdcTraderApi *api, CUstpFtdcInputQuoteField *pInputQuote, int nRequestID){api->ReqQuoteInsert(pInputQuote, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQuoteAction(CUstpFtdcTraderApi *api, CUstpFtdcQuoteActionField *pQuoteAction, int nRequestID){api->ReqQuoteAction(pQuoteAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqForQuote(CUstpFtdcTraderApi *api, CUstpFtdcReqForQuoteField *pReqForQuote, int nRequestID){api->ReqForQuote(pReqForQuote, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqMarginCombAction(CUstpFtdcTraderApi *api, CUstpFtdcInputMarginCombActionField *pInputMarginCombAction, int nRequestID){api->ReqMarginCombAction(pInputMarginCombAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserDeposit(CUstpFtdcTraderApi *api, CUstpFtdcstpUserDepositField *pstpUserDeposit, int nRequestID){api->ReqUserDeposit(pstpUserDeposit, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryOrder(CUstpFtdcTraderApi *api, CUstpFtdcQryOrderField *pQryOrder, int nRequestID){api->ReqQryOrder(pQryOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTrade(CUstpFtdcTraderApi *api, CUstpFtdcQryTradeField *pQryTrade, int nRequestID){api->ReqQryTrade(pQryTrade, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryUserInvestor(CUstpFtdcTraderApi *api, CUstpFtdcQryUserInvestorField *pQryUserInvestor, int nRequestID){api->ReqQryUserInvestor(pQryUserInvestor, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryTradingCode(CUstpFtdcTraderApi *api, CUstpFtdcQryTradingCodeField *pQryTradingCode, int nRequestID){api->ReqQryTradingCode(pQryTradingCode, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorAccount(CUstpFtdcTraderApi *api, CUstpFtdcQryInvestorAccountField *pQryInvestorAccount, int nRequestID){api->ReqQryInvestorAccount(pQryInvestorAccount, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInstrument(CUstpFtdcTraderApi *api, CUstpFtdcQryInstrumentField *pQryInstrument, int nRequestID){api->ReqQryInstrument(pQryInstrument, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryExchange(CUstpFtdcTraderApi *api, CUstpFtdcQryExchangeField *pQryExchange, int nRequestID){api->ReqQryExchange(pQryExchange, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorPosition(CUstpFtdcTraderApi *api, CUstpFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID){api->ReqQryInvestorPosition(pQryInvestorPosition, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryComplianceParam(CUstpFtdcTraderApi *api, CUstpFtdcQryComplianceParamField *pQryComplianceParam, int nRequestID){api->ReqQryComplianceParam(pQryComplianceParam, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorFee(CUstpFtdcTraderApi *api, CUstpFtdcQryInvestorFeeField *pQryInvestorFee, int nRequestID){api->ReqQryInvestorFee(pQryInvestorFee, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorMargin(CUstpFtdcTraderApi *api, CUstpFtdcQryInvestorMarginField *pQryInvestorMargin, int nRequestID){api->ReqQryInvestorMargin(pQryInvestorMargin, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorCombPosition(CUstpFtdcTraderApi *api, CUstpFtdcQryInvestorCombPositionField *pQryInvestorCombPosition, int nRequestID){api->ReqQryInvestorCombPosition(pQryInvestorCombPosition, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInvestorLegPosition(CUstpFtdcTraderApi *api, CUstpFtdcQryInvestorLegPositionField *pQryInvestorLegPosition, int nRequestID){api->ReqQryInvestorLegPosition(pQryInvestorLegPosition, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryInstrumentGroup(CUstpFtdcTraderApi *api, CUstpFtdcQryUstpInstrumentGroupField *pQryUstpInstrumentGroup, int nRequestID){api->ReqQryInstrumentGroup(pQryUstpInstrumentGroup, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryClientMarginCombType(CUstpFtdcTraderApi *api, CUstpFtdcQryClientMarginCombTypeField *pQryClientMarginCombType, int nRequestID){api->ReqQryClientMarginCombType(pQryClientMarginCombType, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqExecOrderInsert(CUstpFtdcTraderApi *api, CUstpFtdcInputExecOrderField *pInputExecOrder, int nRequestID){api->ReqExecOrderInsert(pInputExecOrder, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqExecOrderAction(CUstpFtdcTraderApi *api, CUstpFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID){api->ReqExecOrderAction(pInputExecOrderAction, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQrySystemTime(CUstpFtdcTraderApi *api, CUstpFtdcReqQrySystemTimeField *pReqQrySystemTime, int nRequestID){api->ReqQrySystemTime(pReqQrySystemTime, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqQryMarginPrefParam(CUstpFtdcTraderApi *api, CUstpFtdcReqQryMarginPrefParamField *pReqQryMarginPrefParam, int nRequestID){api->ReqQryMarginPrefParam(pReqQryMarginPrefParam, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqDSUserCertification(CUstpFtdcTraderApi *api, CUstpFtdcDSUserInfoField *pDSUserInfo, int nRequestID){api->ReqDSUserCertification(pDSUserInfo, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqDSProxySubmitInfo(CUstpFtdcTraderApi *api, CUstpFtdcDSProxySubmitDataField *pDSProxySubmitData, int nRequestID){api->ReqDSProxySubmitInfo(pDSProxySubmitData, nRequestID); return 0;}