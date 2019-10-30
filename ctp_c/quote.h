#pragma once
#ifdef _WINDOWS  //64位系统没有预定义 WIN32
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C" __declspec(dllexport)
#else
#define DLL_EXPORT_DECL __declspec(dllexport)
#endif
#else
#ifdef __cplusplus
#define DLL_EXPORT_C_DECL extern "C"
#else
#define DLL_EXPORT_DECL extern
#endif
#endif

#ifdef _WINDOWS
#define WIN32_LEAN_AND_MEAN             //  从 Windows 头文件中排除极少使用的信息
#include "stddef.h"
#ifdef WIN32
#define WINAPI      __cdecl
#include "../win32/USTPFtdcMduserApi.h"
#pragma comment(lib, "../win32/USTPmduserapiAF.lib")
#else
#define WINAPI      __stdcall
#include "../win64/USTPFtdcMduserApi.h"
#pragma comment(lib, "../win64/USTPmduserapiAF64.lib")
#endif
#else
#define WINAPI
#include "../lnx64/USTPFtdcMduserApi.h"
#endif

#include <string.h>

class Quote: CUstpFtdcMduserSpi
{
public:
    Quote(void);
    //针对收到空反馈的处理
    CUstpFtdcRspInfoField rif;
    CUstpFtdcRspInfoField* repare(CUstpFtdcRspInfoField *pRspInfo)
    {
        if (pRspInfo == NULL)
        {
            memset(&rif, 0, sizeof(rif));
            return &rif;
        }
        else
            return pRspInfo;
    }

	///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
	typedef int (WINAPI *FrontConnected)();
	void *_FrontConnected;
	virtual void OnFrontConnected(){if (_FrontConnected) ((FrontConnected)_FrontConnected)();}

	///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
		///@param nReason 错误原因
		///        0x1001 网络读失败
		///        0x1002 网络写失败
		///        0x2001 接收心跳超时
		///        0x2002 发送心跳失败
		///        0x2003 收到错误报文
	typedef int (WINAPI *FrontDisconnected)(int nReason);
	void *_FrontDisconnected;
	virtual void OnFrontDisconnected(int nReason){if (_FrontDisconnected) ((FrontDisconnected)_FrontDisconnected)(nReason);}

	///心跳超时警告。当长时间未收到报文时，该方法被调用。
		///@param nTimeLapse 距离上次接收报文的时间
	typedef int (WINAPI *HeartBeatWarning)(int nTimeLapse);
	void *_HeartBeatWarning;
	virtual void OnHeartBeatWarning(int nTimeLapse){if (_HeartBeatWarning) ((HeartBeatWarning)_HeartBeatWarning)(nTimeLapse);}

	///报文回调开始通知。当API收到一个报文后，首先调用本方法，然后是各数据域的回调，最后是报文回调结束通知。
		///@param nTopicID 主题代码（如私有流、公共流、行情流等）
		///@param nSequenceNo 报文序号
	typedef int (WINAPI *PackageStart)(int nTopicID, int nSequenceNo);
	void *_PackageStart;
	virtual void OnPackageStart(int nTopicID, int nSequenceNo){if (_PackageStart) ((PackageStart)_PackageStart)(nTopicID, nSequenceNo);}

	///报文回调结束通知。当API收到一个报文后，首先调用报文回调开始通知，然后是各数据域的回调，最后调用本方法。
		///@param nTopicID 主题代码（如私有流、公共流、行情流等）
		///@param nSequenceNo 报文序号
	typedef int (WINAPI *PackageEnd)(int nTopicID, int nSequenceNo);
	void *_PackageEnd;
	virtual void OnPackageEnd(int nTopicID, int nSequenceNo){if (_PackageEnd) ((PackageEnd)_PackageEnd)(nTopicID, nSequenceNo);}

	///错误应答
	typedef int (WINAPI *RspError)(CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspError;
	virtual void OnRspError(CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspError)
        {
            if (pRspInfo)
                ((RspError)_RspError)(repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInfoField f = {};
                ((RspError)_RspError)(repare(&f), nRequestID, bIsLast);
            }
        }
    }

	///风控前置系统用户登录应答
	typedef int (WINAPI *RspUserLogin)(CUstpFtdcRspUserLoginField *pRspUserLogin, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserLogin;
	virtual void OnRspUserLogin(CUstpFtdcRspUserLoginField *pRspUserLogin, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserLogin)
        {
            if (pRspUserLogin)
                ((RspUserLogin)_RspUserLogin)(pRspUserLogin, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspUserLoginField f = {};
                ((RspUserLogin)_RspUserLogin)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///用户退出应答
	typedef int (WINAPI *RspUserLogout)(CUstpFtdcRspUserLogoutField *pRspUserLogout, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserLogout;
	virtual void OnRspUserLogout(CUstpFtdcRspUserLogoutField *pRspUserLogout, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserLogout)
        {
            if (pRspUserLogout)
                ((RspUserLogout)_RspUserLogout)(pRspUserLogout, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspUserLogoutField f = {};
                ((RspUserLogout)_RspUserLogout)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///深度行情通知
	typedef int (WINAPI *RtnDepthMarketData)(CUstpFtdcDepthMarketDataField *pDepthMarketData);
	void *_RtnDepthMarketData;
	virtual void OnRtnDepthMarketData(CUstpFtdcDepthMarketDataField *pDepthMarketData)
    {
        if (_RtnDepthMarketData)
        {
            if (pDepthMarketData)
                ((RtnDepthMarketData)_RtnDepthMarketData)(pDepthMarketData);
            else
            {
                CUstpFtdcDepthMarketDataField f = {};
                ((RtnDepthMarketData)_RtnDepthMarketData)(&f);
            }
        }
    }

	///订阅合约的相关信息
	typedef int (WINAPI *RspSubMarketData)(CUstpFtdcSpecificInstrumentField *pSpecificInstrument, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspSubMarketData;
	virtual void OnRspSubMarketData(CUstpFtdcSpecificInstrumentField *pSpecificInstrument, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspSubMarketData)
        {
            if (pSpecificInstrument)
                ((RspSubMarketData)_RspSubMarketData)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcSpecificInstrumentField f = {};
                ((RspSubMarketData)_RspSubMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///退订合约的相关信息
	typedef int (WINAPI *RspUnSubMarketData)(CUstpFtdcSpecificInstrumentField *pSpecificInstrument, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUnSubMarketData;
	virtual void OnRspUnSubMarketData(CUstpFtdcSpecificInstrumentField *pSpecificInstrument, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUnSubMarketData)
        {
            if (pSpecificInstrument)
                ((RspUnSubMarketData)_RspUnSubMarketData)(pSpecificInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcSpecificInstrumentField f = {};
                ((RspUnSubMarketData)_RspUnSubMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///获取行情主题信息应答
	typedef int (WINAPI *RspGetMarketTopic)(CUstpFtdcRspMarketTopicField *pRspMarketTopic, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspGetMarketTopic;
	virtual void OnRspGetMarketTopic(CUstpFtdcRspMarketTopicField *pRspMarketTopic, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspGetMarketTopic)
        {
            if (pRspMarketTopic)
                ((RspGetMarketTopic)_RspGetMarketTopic)(pRspMarketTopic, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspMarketTopicField f = {};
                ((RspGetMarketTopic)_RspGetMarketTopic)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///获取行情快照应答
	typedef int (WINAPI *RspGetMarketData)(CUstpFtdcRspDepthMarketDataField *pRspDepthMarketData, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspGetMarketData;
	virtual void OnRspGetMarketData(CUstpFtdcRspDepthMarketDataField *pRspDepthMarketData, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspGetMarketData)
        {
            if (pRspDepthMarketData)
                ((RspGetMarketData)_RspGetMarketData)(pRspDepthMarketData, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspDepthMarketDataField f = {};
                ((RspGetMarketData)_RspGetMarketData)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }
};
