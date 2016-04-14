#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
alibaba 模型列表复制后生成对应属性语句.
"""
import re
s='''
instantPay(stepOrder)	String	否	是否允许即时到帐（分阶段订单）	
needSellerCallNext(stepOrder)	String	否	是否需要卖家推进（分阶段订单）	
transferAfterConfirm(stepOrder)	String	否	阶段结束是否打款（分阶段订单）	
needSellerAction(stepOrder)	String	否	是否需要卖家操作和买家确认（分阶段订单）	
needLogistics(stepOrder)	String	否	是否需要物流（分阶段订单）	
buyerConfirmTimeout(stepOrder)	String	否	买家不确认的超时时间（分阶段订单）	
buyerPayTimeout(stepOrder)	String	否	买家不付款的超时时间(秒)（分阶段订单）	
sellerActionName(stepOrder)	String	否	卖家操作名称（分阶段订单）	
Price	double	是	商品信息数组-商品单价，单位：分	
actualPayFee(stepOrder)	String	否	应付款（含运费）（分阶段订单）	
adjustFee(stepOrder)	String	否	修改价格修改的金额（分阶段订单）	
alipayTradeId	Integer	是	支付宝交易号	2010120200901808
amount(stepOrder)	String	否	购买数量（分阶段订单）	
bankAndAccount	String	是	发票信息数组-银行及账户	
buyerAlipayId	String	是	买家支付宝ID	
buyerCompanyName	String	是	买家公司名	
buyerFeedback	String	是	买家留言	
buyerMemberId	String	是	买家会员登录名，即会员id	alibuyer
buyerMobile	String	是	买家手机号	
buyerPhone	String	是	买家电话	
buyerRateStatus	String	是	4-已经评价，5-没有评价	
carriage	String	是	运费，单位：分	
closeReason	String	是	关闭交易理由	
codActualFee	String	否	cod交易的实付款，单位：分（货到付款订单）	
codAudit	String	否	是否COD订单并且清算成功（货到付款订单）	
codBuyerFee	String	否	买家承担的服务费（货到付款订单）	
codBuyerInitFee	String	否	买家承担的服务费初始值，单位：分（货到付款订单）	
codFee	String	否	cod服务费，单位：分（货到付款订单）	
codFeeDividend	String	否	cod三家分润（货到付款订单）	
codGmtSign	String	否	买家签收时间（货到付款订单）	
codInitFee	String	否	cod服务费初始值，单位：分（货到付款订单）	
codSellerFee	String	否	卖家承担的服务费，单位：分（货到付款订单）	
codStatus	String	否	COD物流状态，取值范围：0(初始值),20(接单),-20(不接单),2(接单超时),30(揽收成功),-30(揽收失败),3(揽收超时),100(签收成功),-100(签收失败),10(订单等候发送给物流公司),-1(用户取消物流订单)（货到付款订单）	
discount	String	是	卖家修改价格的金额。是discountFee的总和 涨价或折扣，折扣为负数（单位:分）	
discountFee(stepOrder)	String	否	明细被修改的价格。 本阶段分摊的店铺优惠（分阶段订单）	
endTime(stepOrder)	String	否	本阶段结束时间（分阶段订单）	
enterTime(stepOrder)	String	否	开始时间（分阶段订单）	
entryCodStatus	String	否	订单明细货到付款状态，取值范围同订单codStatus	
entryDiscount	String	否	订单明细折扣	
entryStatus	String	否	订单明细状态，取值范围同订单status	
fromAddress	String	否	发货街道地址	
fromArea	String	否	发货区	
fromCity	String	否	发货市	
fromContact	String	否	发货联系人	
fromMobile	String	否	发货联系手机	
fromPhone	String	否	发货联系电话	
fromPost	String	否	发货地址邮编	
fromProvince	String	否	发货省	
gmtCompleted	String	是	交易完成时间	
gmtCreate	String	是	买家下单时间，即订单创建时间	
gmtGoodsSend	String	是	卖家发货时间	
gmtModified	String	是	交易最后修改时间	
gmtPayment	String	是	买家付款时间	
gmtSend	String	否	发货时间	
hasDisbursed(stepOrder)	String	否	是否已打款给卖家（分阶段订单）	
id	Integer	是	订单ID	
invoiceCompanyName	String	是	发票信息数组-购货公司名称	
invoiceId	String	是	发票信息数组-发票ID（订单中买家购买的发票信息，包括发票ID，购货公司名称、纳税人识别码、地址、电话。下同）	
itemDiscountFee(stepOrder)	String	否	本阶段分摊的单品优惠（分阶段订单）	
lastStep(stepOrder)	String	否	是否最后一个阶段（分阶段订单）	
logistics	String[]	是	订单中买家购买的物流信息	
logisticsBillNo	String	否	物流公司运单号	
logisticsCompanyName	String	否	快递公司名	
logisticsCompanyNo	String	否	物流公司编号	
logisticsId	String	否	物流编号	
logisticsOrderNo	String	否	物流单号	
message(stepOrder)	String	否	卖家操作留言（分阶段订单）	
messagePath(stepOrder)	String	否	卖家操作留言路径（分阶段订单）	
offerSnapshotImageUrl	String	否	产品图片/快照图片	
payFee(stepOrder)	String	否	创建时需要付款的金额，不含运费（分阶段订单）	
picturePath(stepOrder)	String	否	卖家上传图片凭据路径（分阶段订单）	
postFee(stepOrder)	String	否	运费（分阶段订单）	
price(stepOrder)	String	否	本阶段分摊的单价（分阶段订单）	
productName	Integer	是	商品信息数组-商品名称	
productPic	String[]	是	商品信息数组-商品所有图片的URL地址	
quantity	double	是	商品信息数组-订单中该商品的购买数量	
receiveAddress	String	是	发票信息数组-地址	
receivePhone	String	是	发票信息数组-电话	
refundId	String	否	退款单ID	
refundPayment	String	是	退款金额，单位：分	
refundStatus	String	是	退款状态，取值范围：waitselleragree(等待卖家同意),refundsuccess(退款成功),refundclose(退款关闭),waitbuyermodify(待买家修改),waitbuyersend(等待买家退货),waitsellerreceive(等待卖家确认收货)	
remark	String	否	备注内容	
remarkIcon	String	否	备注标识，取值范围：1(红),2(蓝),3(绿),4(黄)	
sellerActionTime(stepOrder)	String	否	卖家操作时间（分阶段订单）	
sellerAlipayId	String	是	卖家支付宝ID	
sellerCompanyName	String	是	卖家公司名	
sellerEmail	String	是	卖家邮箱	
sellerMemberId	String	是	卖家会员登录名，即会员id	aliseller
sellerMobile	String	是	卖家手机号	
sellerPhone	String	是	卖家电话	
sellerRateStatus	String	是	4-已经评价，5-没有评价	
sourceId	Integer	是	商品信息数组-商品ID(订单中买家购买的商品信息，包括商品ID，图片URL、名称、单价、购买数量，下同)	
specId	String	是	一个sku的唯一编码	
specInfo	String[]	是	属性信息	
specName	String	是	属性名称	冠幅
specUnit	String	是	属性单位	cm
specValue	String	是	属性值	22
status	String	是	订单状态，取值范围：waitbuyerpay（等待买家付款），waitsellersend（等待卖家发货），waitbuyerreceive（等待买家确认收货），success（交易成功），cancel（交易关闭），waitbuyerconfirm（分队段等待买家确认，waitselleract（分阶段等待卖家处理），waitbuyerconfirmaction（分阶段等待买家确认动作），waitsellerpush（分阶段卖家推进），waitlogisticstakein（等待物流公司揽件），waitbuyersign（等待买家签收），signinsuccess（买家已签收），signinfailed（签收失败）	waitbuyerpay
status(logistics)	String	否	发货状态，取值范围：waitsend(等待发货),alreadysend(已发货)	
stepAgreementPath	String	否	分阶段协议地址URL	
stepName(stepOrder)	String	否	当前步骤的名称（分阶段订单）	
stepNo(stepOrder)	String	否	分阶段子订单阶段序列（分阶段订单）	
stepOrderId(stepOrder)	String	否	分阶段子订单阶段id（分阶段订单）	
stepOrderStatus(stepOrder)	String	否	支付状态，取值范围：1(未付款),2(已付款),4(已退款),6(交易成功),8(交易未付款被关闭)（分阶段订单）	
stepPayAll	String	否	是否一次性付款	
sumPayment	String	是	货品总价+运费=实付款（单位:分）	
taxpayerIdentity	String	是	发票信息数组-纳税人识别码	
templateId(stepOrder)	String	否	使用的模板id（分阶段订单）	
toAddress	String	否	收货街道地址	
toArea	String	否	收货区	
toCity	String	否	收货市	
toContact	String	否	收货联系人	
toMobile	String	否	收货联系手机	
toPhone	String	否	收货联系电话	
toPost	String	否	收货地址邮编	
toProvince	String	否	收货省	
tradeType	Integer	是	1：担保交易，2：预付款交易，3：ETC境外收单交易，4：及时到账交易，5：保障金安全交易，6：统一交易流程，7：分阶段交易，8：货到付款交易，9：信用凭证支付交易	1
'''
ss=s.split("\n")
print(len(ss))
function get():
    for c in ss:
     cc=c.split('\t')
     if len(cc)>=3:
         p=cc[0].findall
         print("private %s %s;"%(cc[1],cc[0]))
#get()

p=re.compile(r'(\(\w*)/?(\w*)')
s='/wiki/a;sdfs/wiki/b/c'
def func(m):
    print(m.groups())
    if(m.group(2)!=''):
        return m.group(1)+'.'+m.group(2)+'.html'
    else:
        return m.group(1)+'.html'

ss=p.sub(func,s)
print(ss)
c='sd(sds)'
dd=re.findall
订单-(新)查询订单列表接口编写
