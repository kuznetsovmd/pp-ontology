/*
 *
 * render help menu
 * 
 */
$(function () {
	var menuData = [{"id":"compute","icon":"../images/help/compute-icon.svg","label":{"zh-cn":"计算","en-us":"Compute"},"items":[{"id":"ecs","help-url":"/ecs/index.html","url":"http://www.huaweicloud.com/product/ecs.html","label":"弹性云服务器","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"cce","help-url":"/cce/index.html","url":"http://www.huaweicloud.com/product/cce.html","label":"云容器引擎","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"bms","help-url":"/bms/index.html","url":"http://www.huaweicloud.com/product/bms.html","label":"裸金属服务器","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"as","help-url":"/as/index.html","url":"http://www.huaweicloud.com/product/as.html","label":"弹性伸缩","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"functionstage","help-url":"/functionstage/index.html","url":"http://www.huaweicloud.com/product/functionstage.html","label":"函数服务","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"ims","help-url":"/ims/index.html","url":"http://www.huaweicloud.com/product/ims.html","label":"镜像服务","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"deh","help-url":"/deh_dld/index.html","url":"http://www.huaweicloud.com/product/deh.html","label":"专属主机","icon":"xxx/yyy/icon.png","tag":"compute"},{"id":"cci","help-url":"/cci_dld/index.html","url":"http://www.huaweicloud.com/product/cci.html","label":"云容器实例","icon":"xxx/yyy/icon.png","tag":"compute"}]},{"id":"storage","icon":"../images/help/storage-icon.svg","label":{"zh-cn":"存储","en-us":"Storage"},"items":[{"id":"csbs","help-url":"/csbs/index.html","url":"http://www.huaweicloud.com/product/csbs.html","label":"云服务器备份","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"evs","help-url":"/evs/index.html","url":"http://www.huaweicloud.com/product/evs.html","label":"云硬盘","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"vbs","help-url":"/vbs/index.html","url":"http://www.huaweicloud.com/product/vbs.html","label":"云硬盘备份","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"dss","help-url":"/dss_dld/index.html","url":"http://www.huaweicloud.com/product/dss.html","label":"专属分布式存储服务","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"obs","help-url":"/obs/index.html","url":"http://www.huaweicloud.com/product/obs.html","label":"对象存储服务","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"sdrs","help-url":"/sdrs_dld/index.html","url":"http://www.huaweicloud.com/product/sdrs.html","label":"存储容灾服务","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"cdn","help-url":"/cdn/index.html","url":"http://www.huaweicloud.com/product/cdn.html","label":"CDN","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"lsa","help-url":"/lsa_dld/index.html#","url":"http://www.huaweicloud.com/product/lsa.html","label":"直播加速","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"sfs","help-url":"/sfs/index.html","url":"http://www.huaweicloud.com/product/sfs.html","label":"弹性文件服务","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"des","help-url":"/des/index.html","url":"http://www.huaweicloud.com/product/des.html","label":"数据快递服务","icon":"xxx/yyy/icon.png","tag":"storage"},{"id":"dess","help-url":"/dess_dld/index.html","url":"http://www.huaweicloud.com/product/dess.html","label":"专属企业存储服务","icon":"xxx/yyy/icon.png","tag":"storage"}]},{"id":"network","icon":"../images/help/network-icon.svg","label":{"zh-cn":"网络","en-us":"Network"},"items":[{"id":"vpc","help-url":"/vpc/index.html","url":"http://www.huaweicloud.com/product/vpc.html","label":"虚拟私有云","icon":"xxx/yyy/icon.png","tag":"network"},{"id":"elb","help-url":"/elb/index.html","url":"http://www.huaweicloud.com/product/elb.html","label":"弹性负载均衡","icon":"xxx/yyy/icon.png","tag":"network"},{"id":"natgateway","help-url":"/natgateway_gls/index.html","url":"http://www.huaweicloud.com/product/nat.html","label":"NAT网关","icon":"xxx/yyy/icon.png","tag":"network"},{"id":"dc","help-url":"/dc/index.html","url":"http://www.huaweicloud.com/product/dc.html","label":"云专线","icon":"xxx/yyy/icon.png","tag":"network"},{"id":"vpn","help-url":"/vpn/index.html","url":"http://www.huaweicloud.com/product/vpn.html","label":"虚拟专用网络","icon":"xxx/yyy/icon.png","tag":"network"},{"id":"dns","help-url":"/dns/index.html","url":"http://www.huaweicloud.com/product/dns.html","label":"云解析服务","icon":"xxx/yyy/icon.png","tag":"network"}]},{"id":"security","icon":"../images/help/security-icon.svg","label":{"zh-cn":"安全","en-us":"Security"},"items":[{"id":"antiddos","help-url":"/antiddos/index.html","url":"http://www.huaweicloud.com/product/antiddos.html","label":"Anti-DDoS流量清洗","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"cad","help-url":"/cad/index.html","url":"http://www.huaweicloud.com/product/cad.html","label":"DDoS高防IP","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"vss","help-url":"/vss_dld/index.html","url":"http://www.huaweicloud.com/product/vss.html","label":"漏洞扫描服务","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"hss","help-url":"/hss_gls/glossary.html","url":"http://www.huaweicloud.com/product/hss.html","label":"企业主机安全","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"dbss","help-url":"/dbss_gls/glossary.html","url":"http://www.huaweicloud.com/product/dbss.html","label":"数据库安全服务","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"dew","help-url":"/dew_gls/index.html","url":"http://www.huaweicloud.com/product/dew.html","label":"数据加密服务","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"ses","help-url":"/ses_dld/index.html","url":"http://www.huaweicloud.com/product/ses.html","label":"安全专家服务","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"waf","help-url":"/waf_gls/glossary.html","url":"http://www.huaweicloud.com/product/waf.html","label":"Web应用防火墙","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"sa","help-url":"/sa/index.html","url":"http://www.huaweicloud.com/product/ssa.html","label":"态势感知","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"cbh","help-url":"/cbh_dld/index.html","url":"http://www.huaweicloud.com/product/cbh.html","label":"云堡垒机","icon":"xxx/yyy/icon.png","tag":"security"},{"id":"scm","help-url":"/scm_dld/index.html","url":"http://www.huaweicloud.com/product/scm.html","label":"SSL证书管理","icon":"xxx/yyy/icon.png","tag":"security"}]},{"id":"management-deployment","icon":"../images/help/management-deployment-icon.svg","label":{"zh-cn":"管理与部署","en-us":"Management and Deployment"},"items":[{"id":"ces","help-url":"/ces/index.html","url":"http://www.huaweicloud.com/product/ces.html","label":"云监控服务","icon":"xxx/yyy/icon.png","tag":"management-deployment"},{"id":"iam","help-url":"/iam/index.html","url":"http://www.huaweicloud.com/product/iam.html","label":"统一身份认证服务","icon":"xxx/yyy/icon.png","tag":"management-deployment"},{"id":"cts","help-url":"/cts/index.html","url":"http://www.huaweicloud.com/product/cts.html","label":"云审计服务","icon":"xxx/yyy/icon.png","tag":"management-deployment"},{"id":"lts","help-url":"/lts_dld/index.html","url":"http://www.huaweicloud.com/product/lts.html","label":"云日志服务","icon":"xxx/yyy/icon.png","tag":"management-deployment"},{"id":"tms","help-url":"/tms/index.html","url":"http://www.huaweicloud.com/product/tms.html","label":"标签管理服务","icon":"xxx/yyy/icon.png","tag":"management-deployment"},{"id":"rts","label":"资源模板服务","help-url":"/rts_dld/index.html","tag":"management-deployment"}]},{"id":"application","icon":"../images/help/application-icon.svg","label":{"zh-cn":"应用服务","en-us":"Application"},"items":[{"id":"servicestage","help-url":"/usermanual-servicestage/zh-cn_topic_0053812706.html ","url":"http://www.huaweicloud.com/product/servicestage.html","label":"微服务云应用平台","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"dms","help-url":"/dms/index.html","url":"http://www.huaweicloud.com/product/dms.html","label":"分布式消息服务","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"smn","help-url":"/smn/index.html","url":"http://www.huaweicloud.com/product/smn.html","label":"消息通知服务","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"cse","help-url":"/cse_dld/index.html","url":"http://www.huaweicloud.com/product/cse.html","label":"微服务引擎","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"functiongraph","help-url":"/functiongraph_dld/index.html","url":"http://www.huaweicloud.com/product/functionGraph.html","label":"函数工作流","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"apm","help-url":"/productdesc-apm/apm_06_0006.html","url":"http://www.huaweicloud.com/product/apm.html","label":"应用性能管理","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"aom","label":"应用运维管理","icon":"xxx/yyy/icon.svg","tag":"application","help-url":"/productdesc-aom/aom_06_0006.html"},{"id":"cpts","help-url":"/productdesc-cpts/cpts_productdesc_0001.html","url":"http://www.huaweicloud.com/product/cpts.html","label":"云性能测试服务","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"bcs","help-url":"/bcs_dld/index.html","url":"http://www.huaweicloud.com/product/bcs.html","label":"区块链服务 BCS","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"apig","help-url":"/apig_gls/index.html","url":"http://www.huaweicloud.com/product/apig.html","label":"API网关","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"aos","help-url":"/usermanual-aos/aos_01_0000.html","url":"http://www.huaweicloud.com/product/aos.html","label":"应用编排服务","icon":"xxx/yyy/icon.png","tag":"application"},{"id":"swr","help-url":"/usermanual-swr/swr_01_0001.html","url":"http://www.huaweicloud.com/product/swr.html","label":"容器镜像服务","icon":"xxx/yyy/icon.png","tag":"application"}]},{"id":"dedicated cloud","icon":"../images/help/dedicated cloud-icon.svg","label":{"zh-cn":"专属云","en-us":"Dedicated Cloud"},"items":[{"id":"dcc","help-url":"/dcc_dld/index.html","url":"http://www.huaweicloud.com/product/dcc.html","label":"专属计算集群","icon":"xxx/yyy/icon.png","tag":"dedicated cloud"}]},{"id":"database","label":{"zh-cn":"数据库","en-us":"Database"},"icon":"../images/help/database-icon.svg","items":[{"id":"rds","label":"关系型数据库","icon":"xxx/yyy/icon.svg","tag":"database","help-url":"/rds/index.html"},{"id":"dds","help-url":"/dds/index.html","url":"http://www.huaweicloud.com/product/dds.html","label":"文档数据库服务","icon":"xxx/yyy/icon.png","tag":"database"},{"id":"dcs","help-url":"/dcs/index.html","url":"http://www.huaweicloud.com/product/dcs.html","label":"分布式缓存服务","icon":"xxx/yyy/icon.png","tag":"database"},{"id":"ddm","help-url":"/ddm_gls/index.html","url":"http://www.huaweicloud.com/product/ddm.html","label":"分布式数据库中间件","icon":"xxx/yyy/icon.png","tag":"database"},{"id":"drs","help-url":"/drs_gls/index.html","url":"http://www.huaweicloud.com/product/drs.html","label":"数据复制服务","icon":"xxx/yyy/icon.png","tag":"database"},{"id":"das","help-url":"/das_dld/index.html","url":"http://www.huaweicloud.com/product/das.html","label":"数据管理服务","icon":"xxx/yyy/icon.png","tag":"database"}]},{"id":"migration","icon":"../images/help/migration-icon.svg","label":{"zh-cn":"迁移","en-us":"Migration"},"items":[{"id":"cmc","help-url":"/productdesc-cmc/zh-cn_topic_0113554842.html","url":"http://www.huaweicloud.com/product/cmc.html","label":"云迁移中心","icon":"xxx/yyy/icon.png","tag":"migration"},{"id":"sms","help-url":"/productdesc-sms/sms_01_0002.html","url":"http://www.huaweicloud.com/product/sms.html","label":"主机迁移服务","icon":"xxx/yyy/icon.png","tag":"migration"},{"id":"oms","help-url":"/oms/index.html","url":"http://www.huaweicloud.com/product/oms.html","label":"对象存储迁移服务","icon":"xxx/yyy/icon.png","tag":"migration"},{"id":"cdm","help-url":"/cdm/index.html","url":"http://www.huaweicloud.com/product/cdm.html","label":"云数据迁移","icon":"xxx/yyy/icon.png","tag":"migration"}]},{"id":"EI","icon":"../images/help/EI-icon.svg","label":{"zh-cn":"EI 企业智能","en-us":""},"items":[{"id":"dis","help-url":"/dis/index.html","tag":"EI","url":"http://www.huaweicloud.com/product/dis.html","label":"数据接入服务","icon":"xxx/yyy/icon.png"},{"id":"mrs","help-url":"/mrs/index.html","url":"http://www.huaweicloud.com/product/mrs.html","label":"MapReduce服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"cs","help-url":"/cs/index.html","url":"http://www.huaweicloud.com/product/cs.html","label":"实时流计算服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"dws","help-url":"/dws/index.html","url":"http://www.huaweicloud.com/product/dws.html","label":"数据仓库服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"mls","help-url":"/mls/index.html","url":"http://www.huaweicloud.com/product/mls.html","label":"机器学习服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"ges","help-url":"/ges_dld/index.html","url":"http://www.huaweicloud.com/product/ges.html","label":"图引擎服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"batch","help-url":"/batch_dld/index.html","url":"http://www.huaweicloud.com/product/batch.html","label":"批处理服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"uquery","help-url":"/uquery/index.html","url":"http://www.huaweicloud.com/product/uquery.html","label":"数据湖探索","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"es","help-url":"/es/index.html","url":"http://www.huaweicloud.com/product/es.html","label":"云搜索服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"res","help-url":"/usermanual-res/res_01_0001.html","url":"http://www.huaweicloud.com/product/res.html","label":"推荐引擎服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"cloudtable","help-url":"/cloudtable/index.html","url":"http://www.huaweicloud.com/product/cloudtable.html","label":"表格存储服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"ocr","help-url":"/ocr_gls/index.html","url":"http://www.huaweicloud.com/product/ocr.html","label":"文字识别","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"ils","help-url":"/ils_gls/index.html","url":"http://www.huaweicloud.com/product/ils.html","label":"智能物流","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"dls","help-url":"/dls_gls/index.html","url":"http://www.huaweicloud.com/product/dls.html","label":"深度学习服务","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"moderation","help-url":"/moderation_gls/index.html","tag":"EI","url":"http://www.huaweicloud.com/product/moderation.html","label":"内容检测","icon":"xxx/yyy/icon.png"},{"id":"image","help-url":"/image_gls/index.html","url":"http://www.huaweicloud.com/product/image.html","label":"图像识别","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"imagesearch","help-url":"/productdesc-imagesearch/imagesearch_01_0001.html","url":"http://www.huaweicloud.com/product/imagesearch.html","label":"图像搜索","icon":"xxx/yyy/icon.png","tag":"EI"},{"id":"face","help-url":"/face_dld/index.html","label":" 人脸识别","tag":"EI","url":"http://www.huaweicloud.com/product/face.html","icon":"xxx/yyy/icon.png"},{"id":"asr","help-url":"/asr_gls/index.html","tag":"EI","url":"http://www.huaweicloud.com/product/asr.html","label":"语音识别","icon":"xxx/yyy/icon.png"},{"id":"tts","help-url":"/tts_gls/index.html","label":"语音合成","tag":"EI","url":"http://www.huaweicloud.com/product/tts.html","icon":"xxx/yyy/icon.png"},{"id":"cbs","help-url":"/cbs_dld/index.html","label":" 对话机器人服务","tag":"EI"},{"id":"dlf","help-url":"/dlf/index.html","label":" 数据湖工厂","tag":"EI"}]},{"id":"devcloud","icon":"../images/help/devcloud-icon.svg","label":{"zh-cn":"软件开发服务","en-us":""},"items":[{"id":"projectman","help-url":"/devcloud/1479456954745.html","url":"http://www.huaweicloud.com/product/projectman.html","label":"项目管理","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"codehub","help-url":"/devcloud/1479457012211.html","url":"http://www.huaweicloud.com/product/codehub.html","label":"代码托管","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"pipeline","help-url":"/devcloud/1492767016468.html","url":"http://www.huaweicloud.com/product/pipeline.html","label":"流水线","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"codecheck","help-url":"/devcloud/1479457040846.html","url":"http://www.huaweicloud.com/product/codecheck.html","label":"代码检查","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"codeci","help-url":"/devcloud/1479457068315.html","url":"http://www.huaweicloud.com/product/codeci.html","label":"编译构建","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"deployman","help-url":"/devcloud/1492767785690.html","url":"http://www.huaweicloud.com/product/deployman.html","label":"部署","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"testman","help-url":"/devcloud/1479457091347.html","url":"http://www.huaweicloud.com/product/testman.html","label":"测试管理","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"releaseman","help-url":"/devcloud/1479457111259.html","url":"http://www.huaweicloud.com/product/releaseman.html","label":"发布","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"mobiletest","help-url":"/devcloud/1496648313109.html","url":"http://www.huaweicloud.com/product/mobiletest.html","label":"移动应用测试","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"cloudide","help-url":"/devcloud/1500256562906.html","url":"http://www.huaweicloud.com/product/cloudide.html","label":"CloudIDE","icon":"xxx/yyy/icon.png","tag":"devcloud"},{"id":"classroom","help-url":"/productdesc-classroom/classroom_pdtd_1000.html","url":"http://www.huaweicloud.com/product/classroom.html","label":"Classroom","icon":"xxx/yyy/icon.png","tag":"devcloud"}]},{"id":"enterprise-applications","icon":"../images/help/enterprise-applications-icon.svg","label":{"zh-cn":"企业应用","en-us":"Enterprise Applications"},"items":[{"id":"workspace","help-url":"/workspace/index.html","url":"http://www.huaweicloud.com/product/workspace.html","label":"云桌面","icon":"xxx/yyy/icon.png","tag":"enterprise-applications"}]},{"id":"communications","icon":"../images/help/communications-icon.svg","label":{"zh-cn":"云通信","en-us":""},"items":[{"id":"cloudvc","help-url":"/cloudvc/index.html","url":"http://www.huaweicloud.com/product/cloudvc.html","label":"会议","icon":"xxx/yyy/icon.png","tag":"communications"},{"id":"msgsms","help-url":"/msgsms_dld/index.html","url":"http://www.huaweicloud.com/product/msgsms.html","label":"消息&短信","icon":"xxx/yyy/icon.png","tag":"communications"},{"id":"cloudipcc","help-url":"/cloudipcc_faq/index.html","url":"http://www.huaweicloud.com/product/cloudcc.html","label":"联络中心","icon":"xxx/yyy/icon.png","tag":"communications"},{"id":"voice","help-url":"/voice_gls/index.html","url":"http://www.huaweicloud.com/product/voice.html","label":"语音通话","icon":"xxx/yyy/icon.png","tag":"communications"},{"id":"PrivateNumber","help-url":"/PrivateNumber_dld/index.html","url":"http://www.huaweicloud.com/product/privatenumber.html","label":"隐私保护通话","icon":"xxx/yyy/icon.png","tag":"communications"}]},{"id":"IOT","icon":"../images/help/IOT-icon.svg","label":{"zh-cn":"物联网","en-us":"Internet of Things"},"items":[{"id":"iot","help-url":"/usermanual-IoT/iot_01_0024.html","url":"http://www.huaweicloud.com/product/iot.html","label":"IoT平台","icon":"xxx/yyy/icon.png","tag":"IOT"},{"id":"ief","label":"智能边缘平台","icon":"xxx/yyy/icon.svg","tag":"IOT","help-url":"http://support.huaweicloud.com/productdesc-ief/ief_productdesc_0001.html"}]},{"id":"solutions","label":{"zh-cn":"解决方案","en-us":"Solutions"},"icon":"../images/help/solutions-icon.svg","items":[{"id":"highperformance","help-url":"http://support.huaweicloud.com/usermanual-hpc/zh-cn_topic_0062552886.html","tag":"solutions","url":"http://www.huaweicloud.com/solution/highperformance/","label":"高性能计算","icon":"xxx/yyy/icon.png"},{"id":"sap","help-url":"http://support.huaweicloud.com/sap_dld/index.html","tag":"solutions","url":"http://www.huaweicloud.com/solution/sap/","label":"SAP","icon":"xxx/yyy/icon.png"},{"id":"gc","label":"游戏云","icon":"xxx/yyy/icon.svg","tag":"solutions","help-url":"http://support.huaweicloud.com/gc_faq/index.html"},{"id":"webmobile","label":"移动互联解决方案","icon":"xxx/yyy/icon.svg","tag":"solutions","help-url":"http://support.huaweicloud.com/webmobile_dld/index.html","url":"http://www.huaweicloud.com/solution/webmobile/"},{"id":"ivs","label":"人证核身","icon":"xxx/yyy/icon.svg","tag":"solutions","help-url":"http://support.huaweicloud.com/ivs_dld/index.html"}]},{"id":"devtool","label":{"zh-cn":"开发者工具","en-us":"develop tool"},"icon":"../images/help/devtool-icon.svg","items":[{"id":"sdk","label":"SDK开发指南","icon":"xxx/yyy/icon.svg","tag":"devtool","help-url":"http://support.huaweicloud.com/devg-sdk/zh-cn_topic_0070637169.html"},{"id":"sdk_cli","label":"CLI开发指南","icon":"xxx/yyy/icon.svg","tag":"devtool","help-url":"http://support.huaweicloud.com/devg-sdk_cli/zh-cn_topic_0070637155.html"},{"id":"apilist","label":"API列表","icon":"xxx/yyy/icon.svg","tag":"devtool","help-url":"http://support.huaweicloud.com/api_list/index.html"}]},{"id":"video","label":{"zh-cn":"视频","en-us":"Video"},"icon":"../images/help/video-icon.svg","items":[{"id":"mpc","help-url":"/mpc_dld/index.html","tag":"video","label":"媒体转码","url":"http://www.huaweicloud.com/product/mpc.html","icon":"xxx/yyy/icon.png"},{"id":"vod","help-url":"/productdesc-vod/vod030001.html","tag":"video","label":"视频点播"},{"id":"live","help-url":"/live_dld/index.html","tag":"video","label":"视频直播"}]},{"id":"price","label":{"zh-cn":"价格","en-us":"price"},"icon":"../images/help/price-icon.svg","items":[{"id":"principle","label":"价格原则","icon":"xxx/yyy/icon.svg","tag":"price","help-url":"http://support.huaweicloud.com/price-principle/zh-cn_topic_0088492731.html"},{"id":"bestpract","label":"成本优化最佳实践","icon":"xxx/yyy/icon.svg","tag":"price","help-url":"http://support.huaweicloud.com/price-bestpract/zh-cn_topic_0088404785.html"},{"id":"bizlogic","label":"云和托管的商业逻辑","icon":"xxx/yyy/icon.svg","tag":"price","help-url":"http://support.huaweicloud.com/price-bizlogic/zh-cn_topic_0088407240.html"},{"id":"fcslogic","label":"FCS商业逻辑","icon":"xxx/yyy/icon.svg","tag":"price","help-url":"http://support.huaweicloud.com/price-fcslogic/zh-cn_topic_0094669296.html"},{"id":"declogic","label":"专属云商业逻辑","icon":"xxx/yyy/icon.svg","tag":"price","help-url":"http://support.huaweicloud.com/price-declogic/zh-cn_topic_0101321604.html"}]},{"id":"others","label":{"zh-cn":"其他","en-us":"others"},"icon":"../images/help/others-icon.svg","items":[{"id":"consolehome","label":"管理控制台","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/qs-consolehome/zh-cn_topic_0016739341.html"},{"id":"mc","label":"消息中心","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/mc_faq/index.html"},{"id":"pro_price","label":"产品价格详情","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/pro_price/index.html"},{"id":"pro_features","label":"产品新特性","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/pro_features/features_1.html"},{"id":"permissions","label":"权限说明","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/usermanual-permissions/zh-cn_topic_0063498930.html"},{"id":"ca","label":"我的凭证","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/usermanual-ca/zh-cn_topic_0046606215.html"},{"id":"bp_usernotice","label":"客户绑定华为云合作伙伴须知","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/bp_usernotice/index.html"},{"id":"iaas","label":"公共问题","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/usermanual-iaas/zh-cn_topic_0040259342.html"},{"id":"compliance","label":"合规中心","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/compliance/1486968407000.html"},{"id":"period","label":"宽限期保留期","icon":"xxx/yyy/icon.svg","tag":"others","help-url":"http://support.huaweicloud.com/usermanual-period/zh-cn_topic_0086671074.html"}]},{"id":"closedeconomy","label":{"zh-cn":"云生态","en-us":"closedeconomy"},"icon":"../images/help/closedeconomy -icon.svg","items":[{"id":"marketplace","label":"云市场","icon":"xxx/yyy/icon.svg","tag":"closedeconomy","help-url":"https://support.huaweicloud.com/mpintro-marketplace/zh-cn_topic_0105864564.html"},{"id":"bpconsole","label":"合作伙伴中心","icon":"xxx/yyy/icon.svg","tag":"closedeconomy","help-url":"http://support.huaweicloud.com/usermanual-bpconsole/zh-cn_topic_0071293240.html"},{"id":"edu","label":"华为云学院","icon":"xxx/yyy/icon.svg","tag":"closedeconomy","help-url":"http://support.huaweicloud.com/usermanual-edu/zh-cn_topic_0104702228.html"}]},{"id":"UserSupport","label":{"zh-cn":"用户服务","en-us":"UserSupport"},"icon":"../images/help/UserSupport-icon.svg","items":[{"id":"account","label":"账号中心","icon":"xxx/yyy/icon.svg","tag":"UserSupport","help-url":"http://support.huaweicloud.com/usermanual-account/zh-cn_topic_0031285551.html"},{"id":"billing","label":"费用中心","icon":"xxx/yyy/icon.svg","tag":"UserSupport","help-url":"http://support.huaweicloud.com/usermanual-billing/zh-cn_topic_0081343161.html"},{"id":"support","label":"服务支持中心","icon":"xxx/yyy/icon.svg","tag":"UserSupport","help-url":"http://support.huaweicloud.com/usermanual-support/zh-cn_topic_0065264094.html"},{"id":"em","label":"企业管理","icon":"xxx/yyy/icon.svg","tag":"UserSupport","help-url":"https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0108744739.html"},{"id":"oce","label":"运营能力开放","icon":"xxx/yyy/icon.svg","tag":"UserSupport","help-url":"http://support.huaweicloud.com/api-oce/zh-cn_topic_0075195195.html"},{"id":"intl","label":"国际站常见问题","icon":"xxx/yyy/icon.svg","tag":"UserSupport","help-url":"https://support.huaweicloud.com/intl_faq/zh-cn_topic_0115884691.html"}]}];
	var winWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
	var tagInfos = ['compute', 'storage', 'network', 'database', 'application', 'dedicated cloud', 'security', 'management-deployment', 'migration', 'EI', 'devcloud', 'enterprise-applications', 'communications', 'closedeconomy', 'IOT', 'solutions', 'devtool', 'price', 'others', 'video', 'UserSupport'];
	var colInfo = [
	  ['compute', 'application', 'dedicated cloud', 'enterprise-applications', 'price'],
	  ['storage', 'management-deployment', 'communications', 'video', 'devtool'],
	  ['network', 'migration', 'closedeconomy', 'IOT', 'others', 'UserSupport'],
	  ['database', 'EI'],
	  ['security', 'devcloud', 'solutions']
	];
	var colInAccordion = [
	  ['compute', 'network', 'security', 'management-deployment', 'EI', 'enterprise-applications', 'closedeconomy', 'IOT', 'devtool', 'price'],
	  ['storage', 'database', 'application', 'dedicated cloud', 'migration', 'devcloud', 'communications', 'solutions', 'video', 'others', 'UserSupport']
	];
  
	if (!$('.help-cen').children().length) {
	  initMenuMap(menuData, winWidth, tagInfos, colInfo);
	}
	var win_width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
	  win_height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
  
	//子元素滚动父元素不滚动
	$(".side-nav-menu .inner").scrollUnique();
  
	//tab  切换
	$(".help-tab-al ul li").click(function () {
	  if ($(".help-cen .tabbox").length <= 1) {
		return;
	  }
	  $(".help-tab-al ul li").removeClass("active");
	  $(this).addClass('active');
	  $(".help-cen .tabbox").css("display", "none");
	  var cal = $(this).attr('data-name');
	  var e = $(".help-cen").find("." + cal + "");
	  e.css("display", "block");
	})
	/*hover切换*/
	$(".left li").hover(function () {
	  $(".left li").removeClass("active");
	  $(this).addClass('active');
	  $(".center-partner .right > div").css("display", "none");
	  var cal = $(this).attr('data-name');
	  var e = $(".center-partner .right").find("." + cal + "");
	  e.css("display", "block");
	})
  
	//移动端产品文档下拉
	if (win_width < 1024) {
  
	  $(".tooled .help-title").click(function () {
		$(this).toggleClass("unfile");
		$(this).next(".item").slideToggle();
	  })
	  $(".help-menu-panel .help-title").click(function () {
		$(this).toggleClass("unfile");
		if ($(this).hasClass("unfile")) {
		  $(this).parent().next().slideDown();
		} else {
		  $(this).parent().next().slideUp();
		}
	  })
  
  
	}
  
	if ($("#ratingBox").length > 0) {
	  $('#ratingBox').barrating({
		wrapperClass: 'br-wrapper-f',
		showSelectedRating: false,
		onSelect: function (value, text) {
		  $(".fb-hint").fadeIn();
		}
	  });
	}
  
	//  帮助中心左侧菜单
	if ($(".help-side").length > 0) {
	  initAccordionMenu(function () {
		var $frame = $("body");
		if (win_width > 1024) {
		  $(".menu-box").click(function () {
			$(this).toggleClass("active");
			var con = $(this).closest(".prod-name").find(".side-nav-menu");
			con.toggle();
		  })
		  $(document).on("click", function (e) {
			var e = e || window.event;
			var target = e.target || e.srcElement;
			if ($(target).closest(".menu-box").length > 0 || $(target).closest(".side-nav-menu").length > 0) {
			  //$(".side-nav-menu").hide();
			} else {
			  $(".side-nav-menu").hide();
			  $(".menu-box").removeClass("active");
			}
		  })
		  $(".side-nav .nav-item>i").click(function (e) {
			var navItem = $(this).parent(".nav-item"),
			  sidenav = navItem.closest(".side-nav"),
			  subUl = navItem.find("ul");
			if (subUl.length > 0) {
			  navItem.toggleClass("active");
			} else {
			  sidenav.find(".nav-item").removeClass("selected");
			  navItem.toggleClass("selected");
			}
		  })
		  $(".sear-nav .nav-item .text").click(function (e) {
			var navItem = $(this).parent(".nav-item"),
			  subUl = navItem.find("ul");
			if (subUl.length > 0) {
			  navItem.toggleClass("active");
			}
		  })
		} else {
		  $(".help-side .prod-name .caption>a").removeAttr('href');
		  var sideHei = $(".banner-box").outerHeight() + $(".prod-name").height() + 10;
		  $(".help-side .prod-name").click(function (e) {
			if ($(e.target).hasClass('menu-btn')) {
			  var sideNav = $(this).closest(".help-side").find(".side-nav");
			  sideNav.toggleClass('show');
			  if (sideNav.hasClass('show')) {
				sideNav.show().width("100%").height(win_height - sideHei - $("#header .wrapper").outerHeight());
				$frame.height(win_height).addClass('overflow-hide');
			  } else {
				sideNav.height("0").width("0").hide();
				$frame.height("auto").removeClass('overflow-hide');
			  }
			} else {
			  var $foldIcon = $(this).find('.foldIcon');
			  var con = $foldIcon.closest(".prod-name").find(".side-nav-menu");
			  if (!$foldIcon.hasClass("active")) {
				$foldIcon.addClass('active');
				con.addClass("show");
				con.height(win_height - sideHei - $("#header .wrapper").outerHeight());
				$frame.height(win_height).addClass('overflow-hide');
			  } else {
				$foldIcon.removeClass('active');
				$frame.height("auto").removeClass('overflow-hide');
				con.height(0);
				// con.removeClass("show").addClass("hide");
				// setTimeout(function() {
				//     con.removeClass("hide");
				// }, 300)
			  }
			}
  
		  });
		  // $(".prod-name .caption").click(function() {
		  //   var con = $(this).closest(".prod-name").find(".side-nav-menu");
		  //   if (!$(this).hasClass("active")) {
		  //     $(this).addClass("active");
		  //     con.addClass("show");
		  //     con.height(win_height - sideHei - $("#header .wrapper").outerHeight());
		  //     $frame.height(win_height).addClass('overflow-hide');
		  //   } else {
		  //     $(this).removeClass("active");
		  //     $frame.height("auto").removeClass('overflow-hide');
		  //     con.removeClass("show").addClass("hide");
		  //     setTimeout(function() {
		  //       con.removeClass("hide");
		  //     }, 300)
		  //   }
		  // });
		  //
		  // $(".menu-box").click(function() {
		  //   var sideNav = $(this).closest(".help-side").find(".side-nav");
		  //   sideNav.toggleClass('show');
		  //   if (sideNav.hasClass('show')) {
		  //     sideNav.show().height(win_height - sideHei - $("#header .wrapper").outerHeight());
		  //     $frame.height(win_height).addClass('overflow-hide');
		  //   } else {
		  //     $frame.height("auto").removeClass('overflow-hide');
		  //     sideNav.height("0").hide();
		  //   }
		  // });
  
		  $(".side-nav .nav-item>i").click(function (e) {
			var navItem = $(this).parent(".nav-item"),
			  sidenav = navItem.closest(".side-nav"),
			  subUl = navItem.find("ul");
			if (subUl.length > 0) {
			  navItem.toggleClass("active");
			} else {
			  sidenav.find(".nav-item").removeClass("selected");
			  navItem.toggleClass("selected");
			  sidenav.height("0").removeClass('show').hide();
			  $frame.height("auto").removeClass('overflow-hide');
			}
		  })
  
		  $(".filterIcon").click(function () {
			var sideNav = $(".help-side.search");
			if (!$(this).hasClass("active")) {
			  var Hei = $(".banner-box").outerHeight() + $(".search-crumbs").height() + 20 + $("#header .wrapper").outerHeight();
			  $(this).addClass("active");
			  sideNav.addClass("show").css("top", Hei + 2);
			  sideNav.height(win_height - sideHei - $("#header .wrapper").outerHeight());
			  $frame.height(win_height).addClass('overflow-hide');
			} else {
			  $(this).removeClass("active");
			  $frame.height("auto").removeClass('overflow-hide');
			  sideNav.removeClass("show").addClass("hide");
			  setTimeout(function () {
				sideNav.removeClass("hide");
			  }, 300)
			}
		  });
		  $(".sear-nav .nav-item .text").click(function (e) {
			var navItem = $(this).parent(".nav-item"),
			  subUl = navItem.find("ul");
			if (subUl.length > 0) {
			  navItem.toggleClass("active");
			}
		  })
		}
	  });
  
	}
  
	function checkContentLength() {
	  var value = $('#helpContent').val(); // 获取值
	  value = $.trim(value);
	  if (value.length > 0) {
		$('#submitHelp').removeClass("disable");
		$('#submitHelp').removeAttr('disabled');
	  } else {
		$('#submitHelp').addClass("disable");
		$('#submitHelp').attr('disabled', true);
	  }
	  if (value.length > 100) {
		$("#helpContent").val(value.substring(0, 100));
		ui.error('字符长度不能超过100', '');
	  }
	}
  
	function getCookie(name) {
	  if (document.cookie.length > 0) {
		start = document.cookie.indexOf(name + "=");
		if (start !== -1) {
		  start = start + name.length + 1;
		  end = document.cookie.indexOf(";", start);
		  if (end === -1) end = document.cookie.length;
		  return unescape(document.cookie.substring(start, end))
		}
	  }
	  return null;
	}
  
	$('#helpContent').focus(function () {
	  checkContentLength()
	});
  
	$('#helpContent').blur(function () {
	  checkContentLength()
	});
	$('#helpContent').keyup(function () {
	  checkContentLength()
	});
	$('#helpContent').keydown(function () {
	  checkContentLength()
	});
	$("#submitHelp").click(function () {
	  var value = $('#helpContent').val(); // 获取值
	  value = $.trim(value);
	  if (value == '') {
		ui.error('反馈内容不能为空！', '');
		return false;
	  }
	  var e = {};
	  e.fb = $.base64.encode($('#helpContent').val(), true);
	  e.ih = $('a.br-current').data("rating-value");
	  e.ty = $('#help_type').val();
	  e.ti = $.base64.encode($("#help_title").val(), true);
	  var a = window.feedback_ajax_url || "https://portal.huaweicloud.com/feedback/ajaxsumbit";
	  // get csrf token from cookie
	  var csrf = getCookie('csrf') || '';
	  a = a + '?csrf=' + csrf;
	  var userAgent = navigator.userAgent;
	  var isOpera = userAgent.indexOf("Opera") > -1;
	  if (userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1 && !isOpera) {
		$.getJSON(a, e, function (data) {
		  $('#helpContent').val('');
		  switch (data.data.result) {
			case 1:
			  ui.success('反馈成功！', data)
			  break;
			default:
			  ui.error(data.data.info, data)
		  }
  
  
		});
	  } else {
		$.ajax({
		  type: "post",
		  async: false,
		  url: a,
		  data: e,
		  dataType: "json",
		  timeout: 30000,
		  xhrFields: {
			withCredentials: true
		  },
		  success: function (e) {
			if (e.data) {
			  e = e.data;
			}
			$('#helpContent').val('');
			switch (e.result) {
			  case 1:
				ui.success('反馈成功！', e)
				break;
			  default:
				ui.error(e.info, e)
			}
		  },
		  error: function (e) {
			$('#helpContent').val('');
			ui.error('反馈失败，请联系客服！', e);
		  }
		})
	  }
	})
	window.ui = (function () {
	  var template = '<div class="modal modal-s" >\
	  <div class="modal-header">\
		  <div class="modal-close state-close"></div>\
		  <h3>温馨提示</h3>\
	  </div>\
	  <div class="modal-body">\
		  <p class="modal-title"><span></span></p>\
		  <p class="modal-detail"></p>\
	  </div>\
	  <div class="modal-footer">\
		  <div class="act-modal-btn act-btn-red state-close">确定</div>\
		</div>\
		</div><div class="shade">\
		  </div>';
	  var _default_options = {
  
	  };
	  return {
		dialog: function (message, options, icon) {
		  options = options || {};
		  var dialog = $('.modal');
		  if (dialog.length == 0) {
			$('body').append(template);
			dialog = $('.modal');
		  }
		  dialog.find('.modal-title').removeClass('');
		  dialog.find('.modal-title').addClass(icon);
		  dialog.find('.modal-detail').html(message);
		  $(".shade").fadeIn();
		  dialog.fadeIn();
		  dialog.unbind().on('click', '.state-close', function (event) {
			$(".shade").fadeOut();
			$(this).parents(".modal").fadeOut();
		  });
		},
		warn: function (message, options) {
		  return this.dialog(message, options, 'warn');
		},
		success: function (message, options) {
		  return this.dialog(message, options, 'success');
		},
		error: function (message, options) {
		  return this.dialog(message, options, 'error');
		}
	  };
	})();
  
	function getHotSearchWord() {
	  var domain_pre = window.location.host;
	  var e = {};
	  e.tmp = Math.random();
	  var a = window.hot_ajax_url || "https://portal.huaweicloud.com/api/search/hot";
	  var s = window.site_search_url + "/s/" || "https://www.huaweicloud.com/s/";
	  $.ajax({
		type: "get",
		async: false,
		url: a,
		data: e,
		dataType: "jsonp",
		jsonp: "ca",
		jsonpCallback: "as",
		timeout: 30000,
		success: function (data) {
		  var str1 = '';
		  var str2 = '<h2>最近大家都在搜</h2>';
		  var str3 = '';
		  for (var i = 0, len = data.length; i < len; i++) {
			str1 = str1 + "<li><a mate_data_ts='portal_v3_search.click.q_" + data[i].question + "_20171201' href='" + s + $.base64.urlSafeEncode(data[i].question, true) + "'>" + data[i].question + "</a></li>";
			str2 = str2 + "<p><a mate_data_ts='portal_v3_search.click.q_" + data[i].question + "_20171201' href='" + s + $.base64.urlSafeEncode(data[i].question, true) + "'>" + data[i].question + "</a></p>";
			str3 = str3 + "<li onclick='gotoSelect()'>" + data[i].question + "</li>";
		  }
		  $('ul.search-items').html(str1);
		  //关键词添加
		  $('.search-keylist ul').html(str1);
		  //$('div.search-hot').html(str2);
		  // $('.search-droplist ul').html(str3);
		}
	  })
	}
	//getHotSearchWord();
  
  
	function gotoSelect() {
	  return false;
	}
  
	function initMenuMap(menuData, winWidth, tagInfos, colInfo) {
	  // 渲染菜单数据
	  var containerTmpl = '' + '<div class="tabbox file tab1">' + '  <div class="AGrid-row sen-row">' + '  </div>' + '</div>';
	  var colTmpl = '<div class=" col-pd-3 help-menu-col col-mb-12 flid"></div>';
	  var panelTmpl = '' + '<div class="help-menu-panel">' + '  <div><p class="help-title"><i class="help-icon"></i><span></span><i class="foldIcon file-icon"></i></p></div>' + '  <ul class="item"></ul>' + '</div>'
	  var itemTmpl = '<li><a target="_blank"></a></li>';
  
	  // 生成panel list
	  // panel list与排序无关
	  var tagArray = [];
	  tagInfos.forEach(function (el) {
		// 每个生成一个panel
		var $panelTmpl = $(panelTmpl);
		var hasItem = false;
		menuData.forEach(function (items) {
		  // id 匹配上，进行menu填充
		  if (items.id === el) {
			items.items && items.items.forEach(function (el) {
			  hasItem = true;
			  var $itemTmpl = $(itemTmpl);
			  $itemTmpl.find('a').attr('href', el['help-url']);
			  $itemTmpl.find('a').attr('mate_data_ts', 'support_china_zh-cn_v3_supportIndex.click.' + el.label);
			  $itemTmpl.find('a').text(el.label);
			  $panelTmpl.find('.item').append($itemTmpl);
			});
			$panelTmpl.find('.help-title span').text(items.label && items.label['zh-cn']);
			$panelTmpl.find('.help-icon').css('background-image', 'url(//img.huaweicloud.com/static/v2_resources/css/' + items.icon + ')');
		  }
		});
		if (hasItem) {
		  var obj = {};
		  obj.id = el;
		  obj.$dom = $panelTmpl;
		  tagArray.push(obj);
		}
	  });
  
	  var $containerTmpl = $(containerTmpl);
	  if (winWidth > 1023) {
		// pc端，按五列装箱
		// 为了达到最好的展示效果，按指定tag布局装箱
		colInfo.forEach(function (col) {
		  var $colTmpl = $(colTmpl);
		  col.forEach(function (tag) {
			tagArray.forEach(function (el) {
			  if (el.id === tag) {
				$colTmpl.append(el.$dom);
			  }
			})
		  })
		  $containerTmpl.find('.AGrid-row').append($colTmpl);
		})
	  } else {
		// 移动端，按一列装箱
		tagArray.forEach(function (el) {
		  $containerTmpl.find('.AGrid-row').append($(colTmpl).append(el.$dom));
		})
	  }
	  $('.help-cen').append($containerTmpl);
	}
  
	function initAccordionMenu(bindEvent) {
	  var path = window.location.pathname && window.location.pathname.split('/')[1];
  
	  if ($('.m_all_classz').length) {
		render({ handbooks: JSON.parse($('.m_all_classz').val()), item: JSON.parse($('.m_item').val()) });
	  } else {
		var $menuDom = getMenuDom();
		$('.side-nav-menu').remove();
		$('.prod-name').append($menuDom);
	  }
	  if ($.isFunction(bindEvent)) {
		bindEvent.apply();
	  }
  
	  if ($('.m_handbook').length) {
		var _handbook = JSON.parse($('.m_handbook').val());
		if (_handbook.download_uri) {
		  $('.help-main .helpContent').prepend('<div class="help-view-pdf"><a target="_blank" href="' + _handbook.download_uri + '"><i></i><span>查看PDF</span></a></div>');
		}
	  }
	}
  
	function getMenuDom() {
	  var menuContainerTmpl = '<div class="side-nav-menu"><div class="inner"></div></div>';
	  var menuPanelTmpl = '<div class="item"></div>';
	  var menuItemListTmpl = '<dl class="side-menu-list"><dt></dt></dl>';
	  var menuItemTmpl = '<dd title=""><a href="" target="_self"></a></dd>';
	  var $menuContainerTmpl = $(menuContainerTmpl);
	  var cols = colInfo;
	  if (win_width < 768) {
		cols = colInAccordion;
	  }
	  cols.forEach(function (tags) {
		var $menuPanelTmpl = $(menuPanelTmpl);
		tags.forEach(function (tag) {
		  menuData.forEach(function (menuList) {
			if (menuList.id === tag) {
			  var $menuItemListTmpl = $(menuItemListTmpl);
			  $menuItemListTmpl.find('dt').text(menuList.label['zh-cn']);
			  menuList.items.forEach(function (item) {
				var $menuItemTmpl = $(menuItemTmpl);
				$menuItemTmpl.attr('title', item.label)
				$menuItemTmpl.find('a').attr('href', item['help-url']).text(item.label);
				$menuItemListTmpl.append($menuItemTmpl);
			  })
			  $menuPanelTmpl.append($menuItemListTmpl);
			}
		  })
		});
		$menuContainerTmpl.find('.inner').append($menuPanelTmpl);
	  });
	  return $menuContainerTmpl;
	}
  
	function render(data) {
	  // TODO: check
	  var currentTopic = window.location.pathname && window.location.pathname.split('/')[window.location.pathname.split('/').length - 1];
  
	  var $accordionMenuContainer = $('<div><div class="prod-name"></div><ul class="side-nav"></ul></div>');
	  var headTmpl = '' + '<div class="menu-box">' + '<p class="title">全部文档</p>' + '<i class="menu-btn"></i>' + '</div>' + '<em class="icons-product-md"></em>' + '<p class="caption">' + '<a target="_self"></a>' + '<i class="foldIcon"></i>' + '</p>';
	  var navContainerTmpl = '<ul class="side-nav"></div>';
	  var handbookTmpl = '' + '<li class="nav-item level1 ">' + '<a target="_self"></a>' + '<ul>' + '</ul>' + '</li>';
	  var classTmpl = '' + '<li class="nav-item level2 ">' + '<a  target="_self"></a>' + '<ul>';
	  var childrenContainerTmpl = '';
	  var childrenTmlp = '' + '<li class="nav-item">' + '<a target="_self"></a>' + '<ul>' + '</ul>' + '</li>';
	  var level4ChildrenTmlp = '' + '<li class="nav-item level4 ">' + '<a target="_self"></a>' + '<ul>' + '</ul>' + '</li>';
	  var level5ChildrenTmlp = '' + '<li class="nav-item level5 ">' + '<a target="_self"></a>' + '<ul>' + '</ul>' + '</li>';
	  var flodIconTmpl = '<i class="foldIcon"></i>';
  
	  function loop($parent, children, pathPrefix, level) {
		children.forEach(function (child) {
		  var $childrenTmlp = $(childrenTmlp);
		  $childrenTmlp.addClass('level' + level);
		  $childrenTmlp.find('a')
			.attr('title', child.title)
			.text(child.title)
			.attr('href', pathPrefix + child.uri)
			.attr('meta-uri', child.uri);
		  if ($.isArray(child.children)) {
			$(flodIconTmpl).insertBefore($childrenTmlp.find('ul'));
			loop($childrenTmlp.find('ul'), child.children, pathPrefix, level + 1);
		  }
		  $parent.append($childrenTmlp);
		})
	  }
	  // render header 
	  var headData = data.item,
		$headTmpl = $(headTmpl);
	  // TODO: 需要变化？
	  // $headTmpl.find('.menu-box .title').text('全部文档');
	  $headTmpl.find('a').attr('href', headData['help-url']);
	  $headTmpl.find('a').text(headData.label);
  
	  // render menu items
	  var $navContainerTmpl = $(navContainerTmpl);
	  var handbooks = data.handbooks;
	  handbooks.forEach(function (el) {
		var $handbookTmpl = $(handbookTmpl);
		$handbookTmpl.find('a')
		  .attr('title', el.title)
		  .attr('href', el.index)
		  .text(el.title);
		var pathPrefix = '/' + el.path + '/';
		if ($.isArray(el.class_data) && el.class_data.length) {
		  $(flodIconTmpl).insertBefore($handbookTmpl.find('ul'));
		  el.class_data.forEach(function (classData) {
			var $classTmpl = $(classTmpl);
			$classTmpl.find('a')
			  .attr('title', classData.title)
			  .text(classData.title)
			  .attr('href', pathPrefix + classData.uri)
			  .attr('meta-uri', classData.uri);
  
			if ($.isArray(classData.children)) {
			  $(flodIconTmpl).insertBefore($classTmpl.find('ul'));
			  loop($classTmpl.find('ul'), classData.children, pathPrefix, 3);
			}
			$handbookTmpl.append($classTmpl);
		  })
		} else {
		  $handbookTmpl.addClass('no-item');
		}
		$navContainerTmpl.append($handbookTmpl);
	  });
	  // render menu in accordion
	  var $hoverMenu = getMenuDom();
  
	  $accordionMenuContainer.find('.prod-name').append($headTmpl).append($hoverMenu);
	  $accordionMenuContainer.find('.side-nav').append($navContainerTmpl);
  
	  // class 需要append之后加
	  $('.help-side').append($accordionMenuContainer)
		.find('.icons-product-md').addClass(headData.id);
	  // 展开默认选中的手风琴
	  var $selected = $('[href="' + location.pathname + '"]').last().closest('.nav-item');
  
	  if (!$selected.length) {
		$selected = $('[href="' + window.location.pathname + '"]').closest('.nav-item');
	  }
	  if (!$selected.length) {
		var tmpArray = window.location.pathname.split('/');
		tmpArray.pop();
		var tmpPath = tmpArray.join('/');
		$('.side-nav').find('a').each(function (idx, el) {
		  //if ($(el).attr('href') && $(el).attr('href').startsWith && $(el).attr('href').startsWith(tmpPath)) {
		  if ($(el).attr('href') && ($(el).attr('href').indexOf(tmpPath)) == 0 ) {
			$selected = $(el).closest('.nav-item');
		  }
		});
	  }
	  var activeItem = function ($dom) {
		var $nextDom = $dom.parent().closest('.nav-item');
		if ($nextDom.length) {
		  $nextDom.addClass('active');
		  activeItem($nextDom);
		}
	  }
	  $selected.addClass('selected');
	  activeItem($selected);
	  setTimeout(function () {
		$selected.children('.foldIcon').click();
	  }, 0);
	  // 生成面包屑
	  var crumbObj = [];
	  crumbObj.push({ 'href': '/index.html', 'label': '帮助中心' });
	  if (headData.label) {
		crumbObj.push({ 'href': headData['help-url'], 'label': headData.label });
	  }
	  $('.help-side .active>a').each(function (idx, el) {
		crumbObj.push({ 'href': $(el).attr('href'), 'label': $(el).text() });
	  })
	  crumbObj.push({ 'label': $selected.find('a').eq(0).text() });
  
	  var crumbItemStr = '';
	  crumbObj.forEach(function (el, idx) {
		if (idx !== 0) {
		  crumbItemStr += '&gt;'
		}
		if (el.href) {
		  crumbItemStr = crumbItemStr + "<a class='link help-link' href='" + el.href + "'>" + el.label + "</a>"
		} else {
		  crumbItemStr = crumbItemStr + "<span class='text'>" + el.label + "</span>"
		}
	  })
	  $('.help-main .crumbs').empty().append(crumbItemStr);
	}
  })
  
  /* 工具：函数节流
   ==============*/
  !function ($) {
	'use strict';
  
	$.throttle = function (fn, interval) {
	  var __self = fn, // 保存需要被延迟执行的函数引用
		timer, // 定时器
		firstTime = true; // 是否是第一次调用
	  interval = interval || 150;
	  return function () {
		var args = arguments,
		  __me = this;
		if (firstTime) { // 如果是第一次调用，不需延迟执行
		  __self.apply(__me, args);
		  return firstTime = false;
		}
		if (timer) { // 如果定时器还在，说明前一次延迟执行还没有完成
		  return false;
		}
		timer = setTimeout(function () { // 延迟一段时间执行
		  clearTimeout(timer);
		  timer = null;
		  __self.apply(__me, args);
		}, interval);
	  };
	};
  
  }(jQuery);
  
  /* region text guide */
  $(function () {
	/*
	 * 生成dom
	 */
	var textGuide = $('<div class="text-guide-container">\n    <div class="text-guide-head">本文导读</div>\n    <div class="text-guide-body">\n        <ul class="tex-guide-list">\n        </ul>\n    </div>\n</div>');
	var textGuideList = textGuide.find('.tex-guide-list');
	var $sectiontitle = $('.sectiontitle');
  
	if ($sectiontitle.length === 0) return;
  
	$('.help-main').addClass('has-guide');
  
	$sectiontitle.each(function (index) {
	  var $this = $(this);
	  var textGuideItem = '<li><a href="#section' + index + '">' + $this.text() + '</a></li>';
	  textGuideList.append(textGuideItem);
	  $this.attr('id', 'section' + index);
	});
  
	$('.help-body').append(textGuide);
  
  
	syncGuide();
  
	/* 同步文本导读激活项 */
	function syncGuide() {
	  var scrollTop = $(window).scrollTop();
	  var offsetTop = 0;
	  var $section;
	  var flag_set = false;
  
	  for (var i = $sectiontitle.length - 1; i >= 0; i--) {
		$section = $sectiontitle.eq(i);
		offsetTop = $section.offset().top;
		if (scrollTop + 46 + 10 >= offsetTop) {
		  textGuideList.find('a[href="#' + $section.attr('id') + '"]').parent().addClass('active').siblings().removeClass('active');
		  flag_set = true;
		  break
		}
	  }
  
	  if (!flag_set) {
		textGuideList.find('li').first().addClass('active').siblings().removeClass('active');
	  }
  
	}
  
	$(window).scroll($.throttle(syncGuide));
  
	/* 固定在顶部 */
	var textGuideOffsetTop = textGuide.offset().top;
  
	function setGuideFixed() {
	  var scrollTop = $(window).scrollTop();
  
	  textGuide.toggleClass('fixed', scrollTop + 46 + 10 >= textGuideOffsetTop);
	}
  
	$(window).scroll($.throttle(setGuideFixed));
  
	/* 固定在顶部后，控制距窗口右边的距离 */
	setGuideFixedRight();
	function setGuideFixedRight() {
	  var right = ($('body').width() - $('.help-body').width()) / 2;
  
	  textGuide.css('right', right);
	}
	$(window).resize($.throttle(setGuideFixedRight));
  });
  /* endregion text guide */
//   $(function () {
// 	function addCopy(className) {
// 	  var target = null;
// 	  $(className).not('[codetype]').append('<button class="btnCP" style="outline:none;border:none;background-color:transparent;"></button>');
// 	  $(className).not('[codetype]').append('<div class="btnCC"></div>');
// 	  $(".btnCC").on("click", function () {
// 		$(className).not('[codetype]').toggleClass("ctnc");
// 		if ($(className).not('[codetype]').hasClass("ctnc")) {
// 		  $(className).not('[codetype]').css({ "color": "rgba(0,0,0)", "background-color": "rgba(241,241,241,1)" });
// 		} else {
// 		  $(className).not('[codetype]').css({ "color": "rgba(255,255,255,1)", "background-color": "#666666" });
// 		}
// 	  })
// 	  $(".btnCC").eq(0).trigger("click");
// 	  $(".btnCP").on("click", function () {
// 		if ($(this).parent().hasClass("ctnc")) {
// 		  $(this).parent().css({ "background-color": "rgba(241,241,241,0.5)", "color": "rgba(0,0,0,0.5)" });
// 		  target = $(this).parent();
// 		  var timeout1 = setTimeout(function () {
// 			target.css({ "background-color": "rgba(241,241,241,1)", "color": "rgba(0,0,0,1)" });
// 		  }, 200);
// 		} else {
// 		  $(this).parent().css({ "background-color": "#000000", "color": "rgba(255,255,255,0.8)" });
// 		  target = $(this).parent();
// 		  var timeout = setTimeout(function () {
// 			target.css({ "background-color": "#666666", "color": "rgba(255,255,255,1)" });
// 		  }, 200);
// 		}
// 	  })
  
// 	  var clipboard = new Clipboard('.btnCP', {
// 		// 通过target指定要复印的节点
// 		target: function (trigger) {
// 		  return trigger.parentNode;
// 		}
// 	  });
  
// 	  clipboard.on('success', function (e) {
// 		e.clearSelection();
// 	  });
  
// 	  clipboard.on('error', function (e) {
// 		e.clearSelection();
// 	  });
// 	}
// 	addCopy(".screen,.codeblock");
//   })
  
  
  $(document).ready(function () {
	setTimeout(function () {
	  document.documentElement.scrollTop = 0;
	  var hashId = window.location.hash;
	  window.location.hash = "";
	  var divId = hashId.substring(1);
	  if (hashId) {
		var prefix = $("*[name=" + divId + "]").offset().top - 60;
		console.log(prefix)
		document.documentElement.scrollTop = prefix;
	  }
	}, 0)
  })