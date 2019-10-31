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
#include "../win32/USTPFtdcTraderApi.h"
#pragma comment(lib, "../win32/USTPtraderapiAF.lib")
#else
#define WINAPI      __stdcall
#include "../win64/USTPFtdcTraderApi.h"
#pragma comment(lib, "../win64/USTPtraderapiAF64.lib")
#endif
#else
#define WINAPI
#include "../lnx64/USTPFtdcTraderApi.h"
#endif

#include <string.h>

class Trade: CUstpFtdcTraderSpi
{
public:
    Trade(void);
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


	typedef int (WINAPI *QryFrontConnected)();
	void *_QryFrontConnected;
	virtual void OnQryFrontConnected(){if (_QryFrontConnected) ((QryFrontConnected)_QryFrontConnected)();}

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


	typedef int (WINAPI *QryFrontDisconnected)(int nReason);
	void *_QryFrontDisconnected;
	virtual void OnQryFrontDisconnected(int nReason){if (_QryFrontDisconnected) ((QryFrontDisconnected)_QryFrontDisconnected)(nReason);}

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

	///用户密码修改应答
	typedef int (WINAPI *RspUserPasswordUpdate)(CUstpFtdcUserPasswordUpdateField *pUserPasswordUpdate, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserPasswordUpdate;
	virtual void OnRspUserPasswordUpdate(CUstpFtdcUserPasswordUpdateField *pUserPasswordUpdate, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserPasswordUpdate)
        {
            if (pUserPasswordUpdate)
                ((RspUserPasswordUpdate)_RspUserPasswordUpdate)(pUserPasswordUpdate, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcUserPasswordUpdateField f = {};
                ((RspUserPasswordUpdate)_RspUserPasswordUpdate)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报单录入应答
	typedef int (WINAPI *RspOrderInsert)(CUstpFtdcInputOrderField *pInputOrder, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspOrderInsert;
	virtual void OnRspOrderInsert(CUstpFtdcInputOrderField *pInputOrder, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspOrderInsert)
        {
            if (pInputOrder)
                ((RspOrderInsert)_RspOrderInsert)(pInputOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInputOrderField f = {};
                ((RspOrderInsert)_RspOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报单操作应答
	typedef int (WINAPI *RspOrderAction)(CUstpFtdcOrderActionField *pOrderAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspOrderAction;
	virtual void OnRspOrderAction(CUstpFtdcOrderActionField *pOrderAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspOrderAction)
        {
            if (pOrderAction)
                ((RspOrderAction)_RspOrderAction)(pOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcOrderActionField f = {};
                ((RspOrderAction)_RspOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报价录入应答
	typedef int (WINAPI *RspQuoteInsert)(CUstpFtdcInputQuoteField *pInputQuote, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQuoteInsert;
	virtual void OnRspQuoteInsert(CUstpFtdcInputQuoteField *pInputQuote, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQuoteInsert)
        {
            if (pInputQuote)
                ((RspQuoteInsert)_RspQuoteInsert)(pInputQuote, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInputQuoteField f = {};
                ((RspQuoteInsert)_RspQuoteInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报价操作应答
	typedef int (WINAPI *RspQuoteAction)(CUstpFtdcQuoteActionField *pQuoteAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQuoteAction;
	virtual void OnRspQuoteAction(CUstpFtdcQuoteActionField *pQuoteAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQuoteAction)
        {
            if (pQuoteAction)
                ((RspQuoteAction)_RspQuoteAction)(pQuoteAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcQuoteActionField f = {};
                ((RspQuoteAction)_RspQuoteAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///询价请求应答
	typedef int (WINAPI *RspForQuote)(CUstpFtdcReqForQuoteField *pReqForQuote, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspForQuote;
	virtual void OnRspForQuote(CUstpFtdcReqForQuoteField *pReqForQuote, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspForQuote)
        {
            if (pReqForQuote)
                ((RspForQuote)_RspForQuote)(pReqForQuote, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcReqForQuoteField f = {};
                ((RspForQuote)_RspForQuote)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///客户申请组合应答
	typedef int (WINAPI *RspMarginCombAction)(CUstpFtdcInputMarginCombActionField *pInputMarginCombAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspMarginCombAction;
	virtual void OnRspMarginCombAction(CUstpFtdcInputMarginCombActionField *pInputMarginCombAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspMarginCombAction)
        {
            if (pInputMarginCombAction)
                ((RspMarginCombAction)_RspMarginCombAction)(pInputMarginCombAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInputMarginCombActionField f = {};
                ((RspMarginCombAction)_RspMarginCombAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///用户请求出入金应答
	typedef int (WINAPI *RspUserDeposit)(CUstpFtdcstpUserDepositField *pstpUserDeposit, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspUserDeposit;
	virtual void OnRspUserDeposit(CUstpFtdcstpUserDepositField *pstpUserDeposit, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspUserDeposit)
        {
            if (pstpUserDeposit)
                ((RspUserDeposit)_RspUserDeposit)(pstpUserDeposit, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcstpUserDepositField f = {};
                ((RspUserDeposit)_RspUserDeposit)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///数据流回退通知
	typedef int (WINAPI *RtnFlowMessageCancel)(CUstpFtdcFlowMessageCancelField *pFlowMessageCancel);
	void *_RtnFlowMessageCancel;
	virtual void OnRtnFlowMessageCancel(CUstpFtdcFlowMessageCancelField *pFlowMessageCancel)
    {
        if (_RtnFlowMessageCancel)
        {
            if (pFlowMessageCancel)
                ((RtnFlowMessageCancel)_RtnFlowMessageCancel)(pFlowMessageCancel);
            else
            {
                CUstpFtdcFlowMessageCancelField f = {};
                ((RtnFlowMessageCancel)_RtnFlowMessageCancel)(&f);
            }
        }
    }

	///成交回报
	typedef int (WINAPI *RtnTrade)(CUstpFtdcTradeField *pTrade);
	void *_RtnTrade;
	virtual void OnRtnTrade(CUstpFtdcTradeField *pTrade)
    {
        if (_RtnTrade)
        {
            if (pTrade)
                ((RtnTrade)_RtnTrade)(pTrade);
            else
            {
                CUstpFtdcTradeField f = {};
                ((RtnTrade)_RtnTrade)(&f);
            }
        }
    }

	///报单回报
	typedef int (WINAPI *RtnOrder)(CUstpFtdcOrderField *pOrder);
	void *_RtnOrder;
	virtual void OnRtnOrder(CUstpFtdcOrderField *pOrder)
    {
        if (_RtnOrder)
        {
            if (pOrder)
                ((RtnOrder)_RtnOrder)(pOrder);
            else
            {
                CUstpFtdcOrderField f = {};
                ((RtnOrder)_RtnOrder)(&f);
            }
        }
    }

	///报单录入错误回报
	typedef int (WINAPI *ErrRtnOrderInsert)(CUstpFtdcInputOrderField *pInputOrder, CUstpFtdcRspInfoField *pRspInfo);
	void *_ErrRtnOrderInsert;
	virtual void OnErrRtnOrderInsert(CUstpFtdcInputOrderField *pInputOrder, CUstpFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnOrderInsert)
        {
            if (pInputOrder)
                ((ErrRtnOrderInsert)_ErrRtnOrderInsert)(pInputOrder, repare(pRspInfo));
            else
            {
                CUstpFtdcInputOrderField f = {};
                ((ErrRtnOrderInsert)_ErrRtnOrderInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///报单操作错误回报
	typedef int (WINAPI *ErrRtnOrderAction)(CUstpFtdcOrderActionField *pOrderAction, CUstpFtdcRspInfoField *pRspInfo);
	void *_ErrRtnOrderAction;
	virtual void OnErrRtnOrderAction(CUstpFtdcOrderActionField *pOrderAction, CUstpFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnOrderAction)
        {
            if (pOrderAction)
                ((ErrRtnOrderAction)_ErrRtnOrderAction)(pOrderAction, repare(pRspInfo));
            else
            {
                CUstpFtdcOrderActionField f = {};
                ((ErrRtnOrderAction)_ErrRtnOrderAction)(&f, repare(pRspInfo));
            }
        }
    }

	///合约交易状态通知
	typedef int (WINAPI *RtnInstrumentStatus)(CUstpFtdcInstrumentStatusField *pInstrumentStatus);
	void *_RtnInstrumentStatus;
	virtual void OnRtnInstrumentStatus(CUstpFtdcInstrumentStatusField *pInstrumentStatus)
    {
        if (_RtnInstrumentStatus)
        {
            if (pInstrumentStatus)
                ((RtnInstrumentStatus)_RtnInstrumentStatus)(pInstrumentStatus);
            else
            {
                CUstpFtdcInstrumentStatusField f = {};
                ((RtnInstrumentStatus)_RtnInstrumentStatus)(&f);
            }
        }
    }

	///账户出入金回报
	typedef int (WINAPI *RtnInvestorAccountDeposit)(CUstpFtdcInvestorAccountDepositResField *pInvestorAccountDepositRes);
	void *_RtnInvestorAccountDeposit;
	virtual void OnRtnInvestorAccountDeposit(CUstpFtdcInvestorAccountDepositResField *pInvestorAccountDepositRes)
    {
        if (_RtnInvestorAccountDeposit)
        {
            if (pInvestorAccountDepositRes)
                ((RtnInvestorAccountDeposit)_RtnInvestorAccountDeposit)(pInvestorAccountDepositRes);
            else
            {
                CUstpFtdcInvestorAccountDepositResField f = {};
                ((RtnInvestorAccountDeposit)_RtnInvestorAccountDeposit)(&f);
            }
        }
    }

	///报价回报
	typedef int (WINAPI *RtnQuote)(CUstpFtdcRtnQuoteField *pRtnQuote);
	void *_RtnQuote;
	virtual void OnRtnQuote(CUstpFtdcRtnQuoteField *pRtnQuote)
    {
        if (_RtnQuote)
        {
            if (pRtnQuote)
                ((RtnQuote)_RtnQuote)(pRtnQuote);
            else
            {
                CUstpFtdcRtnQuoteField f = {};
                ((RtnQuote)_RtnQuote)(&f);
            }
        }
    }

	///报价录入错误回报
	typedef int (WINAPI *ErrRtnQuoteInsert)(CUstpFtdcInputQuoteField *pInputQuote, CUstpFtdcRspInfoField *pRspInfo);
	void *_ErrRtnQuoteInsert;
	virtual void OnErrRtnQuoteInsert(CUstpFtdcInputQuoteField *pInputQuote, CUstpFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnQuoteInsert)
        {
            if (pInputQuote)
                ((ErrRtnQuoteInsert)_ErrRtnQuoteInsert)(pInputQuote, repare(pRspInfo));
            else
            {
                CUstpFtdcInputQuoteField f = {};
                ((ErrRtnQuoteInsert)_ErrRtnQuoteInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///报价撤单错误回报
	typedef int (WINAPI *ErrRtnQuoteAction)(CUstpFtdcQuoteActionField *pQuoteAction, CUstpFtdcRspInfoField *pRspInfo);
	void *_ErrRtnQuoteAction;
	virtual void OnErrRtnQuoteAction(CUstpFtdcQuoteActionField *pQuoteAction, CUstpFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnQuoteAction)
        {
            if (pQuoteAction)
                ((ErrRtnQuoteAction)_ErrRtnQuoteAction)(pQuoteAction, repare(pRspInfo));
            else
            {
                CUstpFtdcQuoteActionField f = {};
                ((ErrRtnQuoteAction)_ErrRtnQuoteAction)(&f, repare(pRspInfo));
            }
        }
    }

	///询价回报
	typedef int (WINAPI *RtnForQuote)(CUstpFtdcReqForQuoteField *pReqForQuote);
	void *_RtnForQuote;
	virtual void OnRtnForQuote(CUstpFtdcReqForQuoteField *pReqForQuote)
    {
        if (_RtnForQuote)
        {
            if (pReqForQuote)
                ((RtnForQuote)_RtnForQuote)(pReqForQuote);
            else
            {
                CUstpFtdcReqForQuoteField f = {};
                ((RtnForQuote)_RtnForQuote)(&f);
            }
        }
    }

	///增加组合规则通知
	typedef int (WINAPI *RtnMarginCombinationLeg)(CUstpFtdcMarginCombinationLegField *pMarginCombinationLeg);
	void *_RtnMarginCombinationLeg;
	virtual void OnRtnMarginCombinationLeg(CUstpFtdcMarginCombinationLegField *pMarginCombinationLeg)
    {
        if (_RtnMarginCombinationLeg)
        {
            if (pMarginCombinationLeg)
                ((RtnMarginCombinationLeg)_RtnMarginCombinationLeg)(pMarginCombinationLeg);
            else
            {
                CUstpFtdcMarginCombinationLegField f = {};
                ((RtnMarginCombinationLeg)_RtnMarginCombinationLeg)(&f);
            }
        }
    }

	///客户申请组合确认
	typedef int (WINAPI *RtnMarginCombAction)(CUstpFtdcInputMarginCombActionField *pInputMarginCombAction);
	void *_RtnMarginCombAction;
	virtual void OnRtnMarginCombAction(CUstpFtdcInputMarginCombActionField *pInputMarginCombAction)
    {
        if (_RtnMarginCombAction)
        {
            if (pInputMarginCombAction)
                ((RtnMarginCombAction)_RtnMarginCombAction)(pInputMarginCombAction);
            else
            {
                CUstpFtdcInputMarginCombActionField f = {};
                ((RtnMarginCombAction)_RtnMarginCombAction)(&f);
            }
        }
    }

	///用户请求出入金
	typedef int (WINAPI *RtnUserDeposit)(CUstpFtdcstpUserDepositField *pstpUserDeposit);
	void *_RtnUserDeposit;
	virtual void OnRtnUserDeposit(CUstpFtdcstpUserDepositField *pstpUserDeposit)
    {
        if (_RtnUserDeposit)
        {
            if (pstpUserDeposit)
                ((RtnUserDeposit)_RtnUserDeposit)(pstpUserDeposit);
            else
            {
                CUstpFtdcstpUserDepositField f = {};
                ((RtnUserDeposit)_RtnUserDeposit)(&f);
            }
        }
    }

	///查询前置系统用户登录应答
	typedef int (WINAPI *RspQueryUserLogin)(CUstpFtdcRspUserLoginField *pRspUserLogin, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQueryUserLogin;
	virtual void OnRspQueryUserLogin(CUstpFtdcRspUserLoginField *pRspUserLogin, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQueryUserLogin)
        {
            if (pRspUserLogin)
                ((RspQueryUserLogin)_RspQueryUserLogin)(pRspUserLogin, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspUserLoginField f = {};
                ((RspQueryUserLogin)_RspQueryUserLogin)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///报单查询应答
	typedef int (WINAPI *RspQryOrder)(CUstpFtdcOrderField *pOrder, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryOrder;
	virtual void OnRspQryOrder(CUstpFtdcOrderField *pOrder, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryOrder)
        {
            if (pOrder)
                ((RspQryOrder)_RspQryOrder)(pOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcOrderField f = {};
                ((RspQryOrder)_RspQryOrder)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///成交单查询应答
	typedef int (WINAPI *RspQryTrade)(CUstpFtdcTradeField *pTrade, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTrade;
	virtual void OnRspQryTrade(CUstpFtdcTradeField *pTrade, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTrade)
        {
            if (pTrade)
                ((RspQryTrade)_RspQryTrade)(pTrade, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcTradeField f = {};
                ((RspQryTrade)_RspQryTrade)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///可用投资者账户查询应答
	typedef int (WINAPI *RspQryUserInvestor)(CUstpFtdcRspUserInvestorField *pRspUserInvestor, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryUserInvestor;
	virtual void OnRspQryUserInvestor(CUstpFtdcRspUserInvestorField *pRspUserInvestor, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryUserInvestor)
        {
            if (pRspUserInvestor)
                ((RspQryUserInvestor)_RspQryUserInvestor)(pRspUserInvestor, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspUserInvestorField f = {};
                ((RspQryUserInvestor)_RspQryUserInvestor)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///交易编码查询应答
	typedef int (WINAPI *RspQryTradingCode)(CUstpFtdcRspTradingCodeField *pRspTradingCode, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryTradingCode;
	virtual void OnRspQryTradingCode(CUstpFtdcRspTradingCodeField *pRspTradingCode, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryTradingCode)
        {
            if (pRspTradingCode)
                ((RspQryTradingCode)_RspQryTradingCode)(pRspTradingCode, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspTradingCodeField f = {};
                ((RspQryTradingCode)_RspQryTradingCode)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者资金账户查询应答
	typedef int (WINAPI *RspQryInvestorAccount)(CUstpFtdcRspInvestorAccountField *pRspInvestorAccount, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorAccount;
	virtual void OnRspQryInvestorAccount(CUstpFtdcRspInvestorAccountField *pRspInvestorAccount, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorAccount)
        {
            if (pRspInvestorAccount)
                ((RspQryInvestorAccount)_RspQryInvestorAccount)(pRspInvestorAccount, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInvestorAccountField f = {};
                ((RspQryInvestorAccount)_RspQryInvestorAccount)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///合约查询应答
	typedef int (WINAPI *RspQryInstrument)(CUstpFtdcRspInstrumentField *pRspInstrument, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInstrument;
	virtual void OnRspQryInstrument(CUstpFtdcRspInstrumentField *pRspInstrument, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInstrument)
        {
            if (pRspInstrument)
                ((RspQryInstrument)_RspQryInstrument)(pRspInstrument, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInstrumentField f = {};
                ((RspQryInstrument)_RspQryInstrument)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///交易所查询应答
	typedef int (WINAPI *RspQryExchange)(CUstpFtdcRspExchangeField *pRspExchange, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryExchange;
	virtual void OnRspQryExchange(CUstpFtdcRspExchangeField *pRspExchange, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryExchange)
        {
            if (pRspExchange)
                ((RspQryExchange)_RspQryExchange)(pRspExchange, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspExchangeField f = {};
                ((RspQryExchange)_RspQryExchange)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者持仓查询应答
	typedef int (WINAPI *RspQryInvestorPosition)(CUstpFtdcRspInvestorPositionField *pRspInvestorPosition, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorPosition;
	virtual void OnRspQryInvestorPosition(CUstpFtdcRspInvestorPositionField *pRspInvestorPosition, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorPosition)
        {
            if (pRspInvestorPosition)
                ((RspQryInvestorPosition)_RspQryInvestorPosition)(pRspInvestorPosition, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInvestorPositionField f = {};
                ((RspQryInvestorPosition)_RspQryInvestorPosition)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///合规参数查询应答
	typedef int (WINAPI *RspQryComplianceParam)(CUstpFtdcRspComplianceParamField *pRspComplianceParam, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryComplianceParam;
	virtual void OnRspQryComplianceParam(CUstpFtdcRspComplianceParamField *pRspComplianceParam, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryComplianceParam)
        {
            if (pRspComplianceParam)
                ((RspQryComplianceParam)_RspQryComplianceParam)(pRspComplianceParam, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspComplianceParamField f = {};
                ((RspQryComplianceParam)_RspQryComplianceParam)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者手续费率查询应答
	typedef int (WINAPI *RspQryInvestorFee)(CUstpFtdcInvestorFeeField *pInvestorFee, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorFee;
	virtual void OnRspQryInvestorFee(CUstpFtdcInvestorFeeField *pInvestorFee, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorFee)
        {
            if (pInvestorFee)
                ((RspQryInvestorFee)_RspQryInvestorFee)(pInvestorFee, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInvestorFeeField f = {};
                ((RspQryInvestorFee)_RspQryInvestorFee)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者保证金率查询应答
	typedef int (WINAPI *RspQryInvestorMargin)(CUstpFtdcInvestorMarginField *pInvestorMargin, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorMargin;
	virtual void OnRspQryInvestorMargin(CUstpFtdcInvestorMarginField *pInvestorMargin, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorMargin)
        {
            if (pInvestorMargin)
                ((RspQryInvestorMargin)_RspQryInvestorMargin)(pInvestorMargin, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInvestorMarginField f = {};
                ((RspQryInvestorMargin)_RspQryInvestorMargin)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者组合持仓查询应答
	typedef int (WINAPI *RspQryInvestorCombPosition)(CUstpFtdcRspInvestorCombPositionField *pRspInvestorCombPosition, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorCombPosition;
	virtual void OnRspQryInvestorCombPosition(CUstpFtdcRspInvestorCombPositionField *pRspInvestorCombPosition, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorCombPosition)
        {
            if (pRspInvestorCombPosition)
                ((RspQryInvestorCombPosition)_RspQryInvestorCombPosition)(pRspInvestorCombPosition, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInvestorCombPositionField f = {};
                ((RspQryInvestorCombPosition)_RspQryInvestorCombPosition)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///投资者单腿持仓查询应答
	typedef int (WINAPI *RspQryInvestorLegPosition)(CUstpFtdcRspInvestorLegPositionField *pRspInvestorLegPosition, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInvestorLegPosition;
	virtual void OnRspQryInvestorLegPosition(CUstpFtdcRspInvestorLegPositionField *pRspInvestorLegPosition, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInvestorLegPosition)
        {
            if (pRspInvestorLegPosition)
                ((RspQryInvestorLegPosition)_RspQryInvestorLegPosition)(pRspInvestorLegPosition, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInvestorLegPositionField f = {};
                ((RspQryInvestorLegPosition)_RspQryInvestorLegPosition)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///合约组信息查询应答
	typedef int (WINAPI *RspQryInstrumentGroup)(CUstpFtdcRspInstrumentGroupField *pRspInstrumentGroup, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryInstrumentGroup;
	virtual void OnRspQryInstrumentGroup(CUstpFtdcRspInstrumentGroupField *pRspInstrumentGroup, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryInstrumentGroup)
        {
            if (pRspInstrumentGroup)
                ((RspQryInstrumentGroup)_RspQryInstrumentGroup)(pRspInstrumentGroup, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInstrumentGroupField f = {};
                ((RspQryInstrumentGroup)_RspQryInstrumentGroup)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///组合保证金类型查询应答
	typedef int (WINAPI *RspQryClientMarginCombType)(CUstpFtdcRspClientMarginCombTypeField *pRspClientMarginCombType, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryClientMarginCombType;
	virtual void OnRspQryClientMarginCombType(CUstpFtdcRspClientMarginCombTypeField *pRspClientMarginCombType, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryClientMarginCombType)
        {
            if (pRspClientMarginCombType)
                ((RspQryClientMarginCombType)_RspQryClientMarginCombType)(pRspClientMarginCombType, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspClientMarginCombTypeField f = {};
                ((RspQryClientMarginCombType)_RspQryClientMarginCombType)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///行权录入应答
	typedef int (WINAPI *RspExecOrderInsert)(CUstpFtdcInputExecOrderField *pInputExecOrder, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspExecOrderInsert;
	virtual void OnRspExecOrderInsert(CUstpFtdcInputExecOrderField *pInputExecOrder, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspExecOrderInsert)
        {
            if (pInputExecOrder)
                ((RspExecOrderInsert)_RspExecOrderInsert)(pInputExecOrder, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInputExecOrderField f = {};
                ((RspExecOrderInsert)_RspExecOrderInsert)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///行权操作应答
	typedef int (WINAPI *RspExecOrderAction)(CUstpFtdcInputExecOrderActionField *pInputExecOrderAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspExecOrderAction;
	virtual void OnRspExecOrderAction(CUstpFtdcInputExecOrderActionField *pInputExecOrderAction, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspExecOrderAction)
        {
            if (pInputExecOrderAction)
                ((RspExecOrderAction)_RspExecOrderAction)(pInputExecOrderAction, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcInputExecOrderActionField f = {};
                ((RspExecOrderAction)_RspExecOrderAction)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///行权通知
	typedef int (WINAPI *RtnExecOrder)(CUstpFtdcExecOrderField *pExecOrder);
	void *_RtnExecOrder;
	virtual void OnRtnExecOrder(CUstpFtdcExecOrderField *pExecOrder)
    {
        if (_RtnExecOrder)
        {
            if (pExecOrder)
                ((RtnExecOrder)_RtnExecOrder)(pExecOrder);
            else
            {
                CUstpFtdcExecOrderField f = {};
                ((RtnExecOrder)_RtnExecOrder)(&f);
            }
        }
    }

	///行权录入错误回报
	typedef int (WINAPI *ErrRtnExecOrderInsert)(CUstpFtdcInputExecOrderField *pInputExecOrder, CUstpFtdcRspInfoField *pRspInfo);
	void *_ErrRtnExecOrderInsert;
	virtual void OnErrRtnExecOrderInsert(CUstpFtdcInputExecOrderField *pInputExecOrder, CUstpFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnExecOrderInsert)
        {
            if (pInputExecOrder)
                ((ErrRtnExecOrderInsert)_ErrRtnExecOrderInsert)(pInputExecOrder, repare(pRspInfo));
            else
            {
                CUstpFtdcInputExecOrderField f = {};
                ((ErrRtnExecOrderInsert)_ErrRtnExecOrderInsert)(&f, repare(pRspInfo));
            }
        }
    }

	///行权操作错误回报
	typedef int (WINAPI *ErrRtnExecOrderAction)(CUstpFtdcInputExecOrderActionField *pInputExecOrderAction, CUstpFtdcRspInfoField *pRspInfo);
	void *_ErrRtnExecOrderAction;
	virtual void OnErrRtnExecOrderAction(CUstpFtdcInputExecOrderActionField *pInputExecOrderAction, CUstpFtdcRspInfoField *pRspInfo)
    {
        if (_ErrRtnExecOrderAction)
        {
            if (pInputExecOrderAction)
                ((ErrRtnExecOrderAction)_ErrRtnExecOrderAction)(pInputExecOrderAction, repare(pRspInfo));
            else
            {
                CUstpFtdcInputExecOrderActionField f = {};
                ((ErrRtnExecOrderAction)_ErrRtnExecOrderAction)(&f, repare(pRspInfo));
            }
        }
    }

	///主次席资金同步通知
	typedef int (WINAPI *RtnTransferMoney)(CUstpFtdcSyncMoneyTransferField *pSyncMoneyTransfer);
	void *_RtnTransferMoney;
	virtual void OnRtnTransferMoney(CUstpFtdcSyncMoneyTransferField *pSyncMoneyTransfer)
    {
        if (_RtnTransferMoney)
        {
            if (pSyncMoneyTransfer)
                ((RtnTransferMoney)_RtnTransferMoney)(pSyncMoneyTransfer);
            else
            {
                CUstpFtdcSyncMoneyTransferField f = {};
                ((RtnTransferMoney)_RtnTransferMoney)(&f);
            }
        }
    }

	///系统时间查询应答
	typedef int (WINAPI *RspQrySystemTime)(CUstpFtdcRspQrySystemTimeField *pRspQrySystemTime, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQrySystemTime;
	virtual void OnRspQrySystemTime(CUstpFtdcRspQrySystemTimeField *pRspQrySystemTime, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQrySystemTime)
        {
            if (pRspQrySystemTime)
                ((RspQrySystemTime)_RspQrySystemTime)(pRspQrySystemTime, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspQrySystemTimeField f = {};
                ((RspQrySystemTime)_RspQrySystemTime)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///查询保证金优惠参数响应
	typedef int (WINAPI *RspQryMarginPrefParam)(CUstpFtdcRspQryMarginPrefParamField *pRspQryMarginPrefParam, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspQryMarginPrefParam;
	virtual void OnRspQryMarginPrefParam(CUstpFtdcRspQryMarginPrefParamField *pRspQryMarginPrefParam, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspQryMarginPrefParam)
        {
            if (pRspQryMarginPrefParam)
                ((RspQryMarginPrefParam)_RspQryMarginPrefParam)(pRspQryMarginPrefParam, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspQryMarginPrefParamField f = {};
                ((RspQryMarginPrefParam)_RspQryMarginPrefParam)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///穿透监管客户认证应答
	typedef int (WINAPI *RspDSUserCertification)(CUstpFtdcDSUserCertRspDataField *pDSUserCertRspData, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspDSUserCertification;
	virtual void OnRspDSUserCertification(CUstpFtdcDSUserCertRspDataField *pDSUserCertRspData, CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspDSUserCertification)
        {
            if (pDSUserCertRspData)
                ((RspDSUserCertification)_RspDSUserCertification)(pDSUserCertRspData, repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcDSUserCertRspDataField f = {};
                ((RspDSUserCertification)_RspDSUserCertification)(&f, repare(pRspInfo), nRequestID, bIsLast);
            }
        }
    }

	///穿透监管信息采集中继上传信息响应
	typedef int (WINAPI *RspDSProxySubmitInfo)(CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast);
	void *_RspDSProxySubmitInfo;
	virtual void OnRspDSProxySubmitInfo(CUstpFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast)
    {
        if (_RspDSProxySubmitInfo)
        {
            if (pRspInfo)
                ((RspDSProxySubmitInfo)_RspDSProxySubmitInfo)(repare(pRspInfo), nRequestID, bIsLast);
            else
            {
                CUstpFtdcRspInfoField f = {};
                ((RspDSProxySubmitInfo)_RspDSProxySubmitInfo)(repare(&f), nRequestID, bIsLast);
            }
        }
    }
};
