#include "quote.h"
#include <string.h>
int nReq;

Quote::Quote(void)
{	
	_FrontConnected = NULL;
	_FrontDisconnected = NULL;
	_HeartBeatWarning = NULL;
	_PackageStart = NULL;
	_PackageEnd = NULL;
	_RspError = NULL;
	_RspUserLogin = NULL;
	_RspUserLogout = NULL;
	_RtnDepthMarketData = NULL;
	_RspSubMarketData = NULL;
	_RspUnSubMarketData = NULL;
	_RspGetMarketTopic = NULL;
	_RspGetMarketData = NULL;
}

DLL_EXPORT_C_DECL void WINAPI SetOnFrontConnected(Quote* spi, void* func){spi->_FrontConnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnFrontDisconnected(Quote* spi, void* func){spi->_FrontDisconnected = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnHeartBeatWarning(Quote* spi, void* func){spi->_HeartBeatWarning = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnPackageStart(Quote* spi, void* func){spi->_PackageStart = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnPackageEnd(Quote* spi, void* func){spi->_PackageEnd = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspError(Quote* spi, void* func){spi->_RspError = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogin(Quote* spi, void* func){spi->_RspUserLogin = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUserLogout(Quote* spi, void* func){spi->_RspUserLogout = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRtnDepthMarketData(Quote* spi, void* func){spi->_RtnDepthMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspSubMarketData(Quote* spi, void* func){spi->_RspSubMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspUnSubMarketData(Quote* spi, void* func){spi->_RspUnSubMarketData = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspGetMarketTopic(Quote* spi, void* func){spi->_RspGetMarketTopic = func;}
DLL_EXPORT_C_DECL void WINAPI SetOnRspGetMarketData(Quote* spi, void* func){spi->_RspGetMarketData = func;}

DLL_EXPORT_C_DECL void* WINAPI CreateApi(){return CUstpFtdcMduserApi::CreateFtdcMduserApi("./log/");}
DLL_EXPORT_C_DECL void* WINAPI CreateSpi(){return new Quote();}
DLL_EXPORT_C_DECL void* WINAPI Release(CUstpFtdcMduserApi *api){api->Release(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Init(CUstpFtdcMduserApi *api){api->Init(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI Join(CUstpFtdcMduserApi *api){api->Join(); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SetUseMultiChannel(CUstpFtdcMduserApi *api, bool bUseMulti = false){api->SetUseMultiChannel(bUseMulti); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterMultiChannel(CUstpFtdcMduserApi *api, const char *pMultiChannel){api->RegisterMultiChannel(pMultiChannel); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterFront(CUstpFtdcMduserApi *api, char *pszFrontAddress){api->RegisterFront(pszFrontAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterNameServer(CUstpFtdcMduserApi *api, char *pszNsAddress){api->RegisterNameServer(pszNsAddress); return 0;}
DLL_EXPORT_C_DECL void* WINAPI RegisterSpi(CUstpFtdcMduserApi *api, CUstpFtdcMduserSpi *pSpi){api->RegisterSpi(pSpi); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubscribeMarketDataTopic(CUstpFtdcMduserApi *api, int nTopicID, USTP_TE_RESUME_TYPE nResumeType){api->SubscribeMarketDataTopic(nTopicID, nResumeType); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SubMarketData(CUstpFtdcMduserApi *api, char *ppInstrumentID[], int nCount){api->SubMarketData(ppInstrumentID, nCount); return 0;}
DLL_EXPORT_C_DECL void* WINAPI UnSubMarketData(CUstpFtdcMduserApi *api, char *ppInstrumentID[], int nCount){api->UnSubMarketData(ppInstrumentID, nCount); return 0;}
DLL_EXPORT_C_DECL void* WINAPI GetMarketTopic(CUstpFtdcMduserApi *api, char *pExchangeID){api->GetMarketTopic(pExchangeID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI GetMarketData(CUstpFtdcMduserApi *api, char *pExchangeID, char *pInstrumentID){api->GetMarketData(pExchangeID, pInstrumentID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI SetHeartbeatTimeout(CUstpFtdcMduserApi *api, unsigned int timeout){api->SetHeartbeatTimeout(timeout); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogin(CUstpFtdcMduserApi *api, CUstpFtdcReqUserLoginField *pReqUserLogin, int nRequestID){api->ReqUserLogin(pReqUserLogin, nRequestID); return 0;}
DLL_EXPORT_C_DECL void* WINAPI ReqUserLogout(CUstpFtdcMduserApi *api, CUstpFtdcReqUserLogoutField *pReqUserLogout, int nRequestID){api->ReqUserLogout(pReqUserLogout, nRequestID); return 0;}