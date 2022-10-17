if(typeof hpeuck_loaded === 'undefined') {
	var hpeuck_loaded = false;
}

if(!hpeuck_loaded) {

	//create the reverse function for strings
	String.prototype.reverse = function(){
		return this.split("").reverse().join("");
	}

	/* set the hpeuck_loaded loaded flag to true */
	hpeuck_loaded = true;


	/*
	 * Privacy Banner Configuration object
	 */
	HPEPRIVACYBANNER_CFG = {
		'supportedLocales': [
			{ 'cc': 'at', 'll': 'de', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Austria/German */
			{ 'cc': 'be', 'll': 'fr', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Belgium/French */
			{ 'cc': 'be', 'll': 'en', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Belgium/English */
			{ 'cc': 'ch', 'll': 'de', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Switzerland/German */
			{ 'cc': 'ch', 'll': 'fr', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Switzerland/French */
			{ 'cc': 'cz', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Czech Republic/English */
			{ 'cc': 'de', 'll': 'de', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Germany/German */
			{ 'cc': 'dk', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Denmark/English */
			{ 'cc': 'emea_europe', 'll': 'en', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },	/* Other Europe/English */
			{ 'cc': 'es', 'll': 'es', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Spain/Spanish */
			{ 'cc': 'fi', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Finland/English */
			{ 'cc': 'fr', 'll': 'fr', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* France/French */
			{ 'cc': 'ie', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Ireland/English */
			{ 'cc': 'it', 'll': 'it', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Italy/Italian */
			{ 'cc': 'nl', 'll': 'en', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Netherlands/English */
			{ 'cc': 'no', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Norway/English */
			{ 'cc': 'pl', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': true, 'ccpa': false },	/* Poland/English */
			{ 'cc': 'pt', 'll': 'en', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Portugal/English */
			{ 'cc': 'se', 'll': 'en', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* Sweden/English */
			{ 'cc': 'uk', 'll': 'en', 'optIn': true, 'defaultAnswer': 'no', 'gdpr': true, 'ccpa': false },		/* United Kingdom/English */
			{ 'cc': 'us', 'll': 'en', 'optIn': false, 'defaultAnswer': 'yes', 'gdpr': false, 'ccpa': true }		/* United States */
		],

		/* countryToLocaleMap can be used to find out what banner supported locale to use, if we could detect only the country, or we detected cc and ll not on supported list */
		'countryToLocaleMap': [
			{ 'cc': 'at', 'useLocale': { 'cc': 'at', 'll': 'de' } },
			{ 'cc': 'be', 'useLocale': { 'cc': 'be', 'll': 'en' } },
			{ 'cc': 'bg', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'hr', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'cy', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'cz', 'useLocale': { 'cc': 'cz', 'll': 'en' } },
			{ 'cc': 'dk', 'useLocale': { 'cc': 'dk', 'll': 'en' } },
			{ 'cc': 'ee', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'fi', 'useLocale': { 'cc': 'fi', 'll': 'en' } },
			{ 'cc': 'fr', 'useLocale': { 'cc': 'fr', 'll': 'fr' } },
			{ 'cc': 'de', 'useLocale': { 'cc': 'de', 'll': 'de' } },
			{ 'cc': 'gr', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'hu', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'ie', 'useLocale': { 'cc': 'ie', 'll': 'en' } },
			{ 'cc': 'it', 'useLocale': { 'cc': 'it', 'll': 'it' } },
			{ 'cc': 'lv', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'lt', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'nl', 'useLocale': { 'cc': 'nl', 'll': 'en' } },
			{ 'cc': 'no', 'useLocale': { 'cc': 'no', 'll': 'en' } },
			{ 'cc': 'pl', 'useLocale': { 'cc': 'pl', 'll': 'en' } },
			{ 'cc': 'pt', 'useLocale': { 'cc': 'pt', 'll': 'en' } },
			{ 'cc': 'ro', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'sk', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'si', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'es', 'useLocale': { 'cc': 'es', 'll': 'es' } },
			{ 'cc': 'se', 'useLocale': { 'cc': 'se', 'll': 'en' } },
			{ 'cc': 'uk', 'useLocale': { 'cc': 'uk', 'll': 'en' } },
			{ 'cc': 'gb', 'useLocale': { 'cc': 'uk', 'll': 'en' } },
			{ 'cc': 'us', 'useLocale': { 'cc': 'us', 'll': 'en' } }
		],

		/* languageToLocaleMap can be used to find out what banner supported locale to use, if we could detect only the language, or we detected cc and ll not on supported list */
		'languageToLocaleMap': [
			{ 'll': 'bg', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'hr', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'el', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'cs', 'useLocale': { 'cc': 'cz', 'll': 'en' } },
			{ 'll': 'da', 'useLocale': { 'cc': 'dk', 'll': 'en' } },
			{ 'll': 'et', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'fi', 'useLocale': { 'cc': 'fi', 'll': 'en' } },
			{ 'll': 'hu', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'it', 'useLocale': { 'cc': 'it', 'll': 'it' } },
			{ 'll': 'lv', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'lt', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'pl', 'useLocale': { 'cc': 'pl', 'll': 'en' } },
			{ 'll': 'ro', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'sk', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'sl', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'll': 'sv', 'useLocale': { 'cc': 'se', 'll': 'en' } },
			{ 'll': 'no', 'useLocale': { 'cc': 'no', 'll': 'en' } }
		],

		/* excludeDomains is array containing list of domains where privacy banner should not be shown */
		'excludeDomains': [],

		/* Arrays containing list of technical, tracking, personalization and ccpa cookies */
		'technical_cookies': ['hpe_theme','SplitTestGroup','discover_session_banner','kndctr_56B5A25055667EED7F000101_AdobeOrg_identity','proposalweb.it.hpe.com-FedAuth','[]proposalweb.it.hpe.com/houston-UserContext','_ntv_uid','hpe_mn_nn','LithiumCookiesAccepted','itg-proposalweb.it.hpe.com-FedAuth','infosight_iam','h30674.www3.hpe.com.ost','h30674.www3.hpe.com.wwwwebshowmanagementcom','Dashboard','iam_dce_state_[]','iam_dce_session','dce.auth.source','test_cookie','language','dnn_IsMobile','__RequestVerificationToken','sessionCookie_SNR','autolaunch_triggered','srefresh','enduser_version','DT','t','proximity_[]','113962-HPE-OT','HPPF','IdentifierFirst.previous.subjects','PF','ccs-pf-id','ccs-old-style-pf-id','ccs-csrftoken','ccs-session','__coveo.analytics.history','CKPT_JSESSIONID','VISITORID','LiSESSIONID','takeover','__d_pardot','__d_eloqua','__d_hsutk','__d_mkto','dextp','demdex','DST','okta-oauth-redirect-params','okta-oauth-state','ln','okta-oauth-nonce','hva.sign-in.success','WOPISessionContext','cookietest','sj_ubid','sessionid','csrftoken','fcs','token','adminToken','AWSALB', 'AWSALBCORS','auth.unattended','ApplicationGatewayAffinityCORS','GordonUserType','hpe-nxt-subscribe-close','hpe-newsroom-banner-close','PicassoLanguage[]','dce.logout.return','cookieKey','userAccount','userPartnerType','unreadMessages','accessLevel','smbgProgram','storageRangerProgram','LSKey[c]DCE_NOTIFICATIONS','HPEITGUID','WSS_FullScreenMode','PWebopportunityID','PWebMobileApprove','stsSyncIconPath','stsSyncAppName','[]proposalweb.ext.hpe.com/houston-UserContex','ckAccessToken','ckRefreshToken','roles','itg.proposalweb.ext.hpe.com-FedAuth','proposalweb.ext.hpe.com-FedAuth','hpe-cpt-welcome-closed','hpe-cpt-welcome-hide','RetURL2','RRetURL','rsid2','rsid','idccsrf','sid_Client','QCQQ','force-proxy-stream','sfdc-stream','force-stream','pctrk','renderCtx','spock2_groups_cookie2','spock2_id_cookie2','spock2_roles_cookie2','hybris-store-logged-in','bizaddrarea','bizaddrcity','bizaddrline1','bizaddrline2','bizcountry','companyname','bizfax','bizphonecitycode','email','bizfaxcityareacode','bizphonextn','firstname','bizfaxextn','hppprofileid','bizpostalcode','lastname','bizphone','bizstate','DealSource','SM_USER','SM_UNIVERSALID','Local storage','MetStamp','LinkCR','AMCV_[]','AMCVS_[]','AuthenticationStateToken-[]','userid-[]','login_assetRec','hpeVST','session','tzoffset','snfversion','NewRecSolution','LinkCase','NewRecCR','USERTOKEN','USERLOGONID','NewRecCase','TIS_REDIRECT','LOGONMECHANISMUSED','DesktopCont','DesktopRefresh','EditRecent','GenWEBV','LMWritten','LMStamp','_gcl_aw','DSS%5FTOKEN','_gcl_dc','_gac_UA-136618955-1','_cs_id','pwalandingpage','bRedirect','migrated','CPQGLTOKEN','[]-HPE-IOT','glo_cookie_struct_def','ROUTEID','TIS_COOKIE','.ASPXANONYMOUS','.ASPXAUTH','__atuvc','__CSRFCOOKIE','__CT_Data','__Secure-3PAPISID','__Secure-3PSID','__Secure-APISID','__Secure-HSID','__Secure-SSID','__utma','__utmb','__utmc','__utmt','__utmz','_cs_c','_cs_ex','_csrf','_CT_RS_','_gat','_gid','_opHistory','[]-OT','[]-IOT','1P_JAR','acceleratorSecureGUID','AgentSales','ak_bmsc','AKA_A2','ANID','anonymous-consents','apiPath','APISID','AppKey','ApplicationGatewayAffinity','area','ASP.NET_SessionId','ASP.NET_SessionID','assistant.[]','assistant1.[]','Authsite','authuser','AWSELB','BCHPPSESSION','BENCHMARK','bkreqmade','bm_mi','bm_sv','browser','browserupdateorg','c_u','cbSessionId','cc','ChatOpen','cid','CL_Cookie','Compare[]','connect.sid','COOKIE_SUPPORT','cookie-notification','COUNTRY%5FCOOKIE','COUNTRY_COOKIE','cpcLang','CSUserProfile','ctm','D41ID','ddj','discoverVisited','displayName','dnb_sent','DSS%5FTICKET','DWF-HF-ROUTE','DWF-PROXY-SESSION-ID','eg[]','EG_ALL_SEC','EG_CUST_SEC','egcb[]','egChatStateBeforeUnload','egofr[]','EG-SEQ-ID','EG-S-ID','egSSTabOpen','EG-U-ID','EG-U-ID','EndTime','FE_Subscription_Bar','FeedbackCaptchaCode','fe-popoup-exit','FEWarnMissingParts','FONT_CHOICE','GLO_USER','gpv_pn','gss.api.gsid','GUEST_LANGUAGE_ID','homepageUrl','HP_EBUS','HP_LB','HP_SPF_LOCALE','HP_SPF_SID','HP_SPF_SITE','HPE_ELOQUA_PRE','hpe_is_partner','hpe_locale','hpealert_answ[]','hpefhlc','hpefhsn','HPEMyRoomWeb.LangDefaultCountry','HPEMyRoomWeb.Language','HPESC_NOTIF','hpeuck_answ','hpeuck_cktst','hpeuck_prefs','hpeUSSiteB2C-cart','HPPFEDIDENTITY','HPPFEDSESSION','HPPIDENTITY','HPPSESSION','HSID','HTMLClientBlocked','is','IsChecked','IsExstream','iv','jscr','JSESSIONID','lang','laravel_session','lastAccessedProfile','LastInteractionDate','LastInvite','lastTab','lastuser','lia.anon.profile.language','LithiumUserInfo','locale','login','LoginURL','logontarget','mainWindowName','mboxEdgeCluster','MyProcurve_Auth','NID','ocps_session','OneUid','OneUid','OUTAGE_DEBUG','parentPage','platform_cookie partitionID','PCCInfo','PF_AUTH_uid','PFTime','PHPSESSID','pid','pp','PSTOP','QuestionID','QuestionString','RELAYSTATE','REMEMBER','Roles','route','RT','s_fid','sa_session_id','sa_user_tracking_id','SAPISID','ScriptDebuggerDisabled','SEARCH_SAMESITE','Security_level','selectedProfile','selectedTab','sessionId','SessionID','SIDCC','SimpleSAMLAuthToken','SMSESSION','SpinCompany','Spoofed','SRID','StartTime','surveysnow-auth','TimezoneOffset','TIS_BACK_OVER','TIS_LOGON_ID','treeview','u_d','uid','UIDCSNSESSION','UNIQUE_USER_ID','user','userCulture','user-has-cart','userid','UserID','username','utag_main','utag_opt_out','vendor','vendorid','W2GISM','WRUIDAWS','XSRF-TOKEN','session_id','Remember_me','Interworks.Cloud Platform Cookies','GLCSESSION','sid'],

		'tracking_cookies': ['LSKey[CoveoV2]coveo_visitorId','drift_conversation_id','HPEITGICCUID','AMCV_56B5A25055667EED7F000101%40AdobeOrg','AMCVS_56B5A25055667EED7F000101%40AdobeOrg','!lithiumSSO:{hpeb.prod}','!lithiumSSO:{hpeb.stage}','coveo_visitorId','[CoveoV2]coveo_visitorId','LithiumVisitor','driftt_aaid','drift_ujwt','drift_eid','driftt_eid','DRIFT_ALWAYS_SEND_IDS','DRIFT_SESSION_STARTED','DRIFT_SESSION_ID','DRIFT_openTabs','DRIFT_visitCounts','Drift.Targeting.referrerDomain','Drift.Targeting.searchTerm','Drift.Targeting.currentReferrer','Drift.Targeting.previousPage','Drift.Targeting.originalReferrer','Drift.Targeting.activeSessionStartedAt','Drift.Targeting.previousSessionEndedAt','Drift.Targeting.previousSessionStartedAt','Drift.Targeting.currentSessionStartedAt','Drift.Targeting.currentPageViewStarted','Drift.Targeting.numberOfSessions','Drift.Targeting.numberOfVisits','Drift.Targeting.lastVisit','Drift.Targeting.firstVisit','DFTT_LEAD_HAS_PREV_IDENTIFIED','DFTT_END_USER_PREV_BOOTSTRAPPED','driftt_wmd','drift_campaign_refresh','driftt_sid','drift_aid','driftt_aid','_cs_mk','fs_uid','s_tp','s_ips','liked_articles','disliked_articles','expid_connect','oid','disco','inst','autocomplete','oinfo','clientSrc','alohaEpt','BrowserId','BrowserId_sec','session id','hpechatpp','hpeppn','hpaaeid','_pg_ses.11.6fd8','_pk_id.11.6fd8','CT_RS','gglck','HPE_ELOQUA_90','HPEProICCUID','HPEProUID','LastVisit','passWindowOpen','s_prevPage','sessionStartTime','signalSession','signalUser','UserID-HPE','UserID-HPEROI','ValueSurveyParticipation','vid','VISITOR_BEACON','buy_loggedin'],

		'personalization_cookies': ['_mkto_trk','dpm','IDE','TDID','TDCPM','personalization_id','ELQSTATUS','_gat_gtag_UA_136618955_1','guest_id','AnalyticsSyncHistory','bcookie','UserMatchHistory','li_sugr','_twitter_sess','s_ppv','userCountry','uuuid','_ga','.sbc.hpe.com','aam_uuid','BKUT','cq-authoring-mode','cq-editor-layer.page','ELOQUA','elqAdID','elqDebug','ev_sync_ax','ev_sync_dd','ev_sync_yh','everest_g_v2','everest_session_v2','HPE_ELOQUA','hpe-aid','HPELOQUA','languagePre_cookie','ll','mbox','s_cc','s_ecid','s_sq','wcmmode','web_templates_personalization_cookie','WebcastExperience'],

		'ccpa_cookies': ['BKUT'],

		/* Below is HTML template for privacy banner with radio buttons */
		'template': '<div id="hpe_privacy_banner"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg><div class="hpe_privacy_banner_main_text"><span>____message____</span></div><div class="hpe_privacy_banner_radio_buttons"><span id="hpe_privacy_banner_alert_message">____optionalCookies____</span><div class="hpe_control-group"><label class="hpe_control hpe_control-radio">____yes____<input type="radio" name="hpe_privacy_answer" class="hpe_privacy_answer" value="1" ___checked_yes___ /><div class="hpe_control_indicator"></div></label><label class="hpe_control hpe_control-radio">____no____<input type="radio" name="hpe_privacy_answer" class="hpe_privacy_answer" value="0" ___checked_no___ /><div class="hpe_control_indicator"></div></label></div></div><a href="#" id="hpe_privacy_banner_close" class="hpe_privacy_banner_close" ___hpe_privacy_banner_close_style___ title="____close____" ><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a></div>',

		/* Below is HTML template for privacy banner without radio buttons */
		'template_no_radio_buttons': '<div id="hpe_privacy_banner"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg><div class="hpe_privacy_banner_main_text"><span>____message_no_radio____</span></div><a href="#" id="hpe_privacy_banner_close" class="hpe_privacy_banner_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a></div>',

		/* Below is HTML template for CCPA opt-out form */
		'template_ccpa_form': '<div id="hpe_privacy_ccpa"><div class="hpe_privacy_ccpa_radio_buttons"><h4 id="hpe_privacy_ccpa_alert_message">Do you want to opt-out from optional <a href="/content/hpe/base/blueprint/privacy.html#datacollection">Automatic Data Collection Tools</a>?</h4><div class="hpe_control-group"><label id="ccpa_label_yes" class="hpe_control hpe_control-radio">Yes<input type="radio" name="hpe_ccpa_answer" class="hpe_ccpa_answer" id="ccpa_yes" value="1" Yes /><div class="hpe_control_indicator"></div></label><label id="ccpa_label_no" class="hpe_control hpe_control-radio">No<input type="radio" name="hpe_ccpa_answer" class="hpe_ccpa_answer" id="ccpa_no" value="0" No /><div class="hpe_control_indicator"></div></label><a href="#ccpaoptout" id="hpe_privacy_ccpa_save" class="hpe_privacy_ccpa_save" title="Submit">Submit</a></div></div><div id="hpe_privacy_ccpa_confirm_text" class="hpe_privacy_ccpa_confirm_text"><span>Your configuration had been saved</span></div></div>',

		/* CSS for banner */
		'css_font': '@font-face{font-family:MetricReg;src:url(https://h50007.www5.hpe.com/caas-static/fonts/metric/latin-e-regular-woff.woff) format("woff")} @font-face{font-family:MetricBold;src:url(https://h50007.www5.hpe.com/hfws-static/fonts/metric-hpe/MetricHPE-Web-Bold.woff) format("woff");font-weight:700} @font-face{font-family:MetricSemibold;src:url(https://h50007.www5.hpe.com/caas-static/fonts/metric/latin-e-semibold-woff.woff) format("woff");font-weight:600} @font-face{font-family:MetricLight;src:url(https://h50007.www5.hpe.com/caas-static/fonts/metric/latin-e-light-woff.woff) format("woff");font-weight:100}',
		'css': ' #hpe_privacy_banner_container { background-color: #624768; border-bottom: 2px solid #2bc5bd; } #hpe_privacy_banner { display: flex; position: relative; left: 0px; top: 0px; width: 100%; max-width: 1530px; margin: 0px auto; padding: 15px 0px 15px 0px; background-color: #624768; } #hpe_privacy_banner .hpe_privacy_banner_main_text { display: block; float: left; width: 100%; color: #fff; font-family: MetricReg,\'Metric Regular\',HPEMetricRegular,Arial,sans-serif; font-size: 17px; line-height: 18px; margin: 0px 0px 0px 64px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons { display: block; float: left; max-width: 250px; min-width: 150px; color: #fff; font-family: MetricReg,\'Metric Regular\',HPEMetricRegular,Arial,sans-serif; font-size: 18px; margin: 0px 0px 0px 60px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons .spaced { margin: 5px 10px 0 20px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons span { display: block; line-height: 16px; font-family: MetricSemibold,\'Metric Semibold\',HPEMetricSemiBold,Arial,sans-serif; font-weight: bold; padding-bottom: 4px; } #hpe_privacy_banner .hpe_control { display: table-cell; font-family: MetricReg,\'Metric Regular\',HPEMetricRegular,Arial,sans-serif; color: #fff; display: table-cell; position: relative; padding: 3px 20px 0 30px; margin: 5px 0 0 30px; cursor: pointer; font-size: 17px; font-weight: normal; line-height: 19px; } label.hpe_control.hpe_control-radio { color: #fff; } .hpe_control input { position: absolute; z-index: -1; opacity: 0; } .hpe_control_indicator { position: absolute; top: 5px; left: 0; height: 15px; width: 15px; background: #fff; border: 2px solid #c0c4c3; box-sizing: border-box; } .hpe_control-radio .hpe_control_indicator { border-radius: 50%; } .hpe_control:hover input ~ .hpe_control_indicator, .hpe_control input:focus ~ .hpe_control_indicator { background: #cccccc; } .hpe_control input:checked ~ .hpe_control_indicator { background: #fff; } .hpe_control:hover input:not([disabled]):checked ~ .hpe_control_indicator, .hpe_control input:checked:focus ~ .hpe_control_indicator { background: #0e6647d; } .hpe_control input:disabled ~ .hpe_control_indicator { background: #e6e6e6; opacity: 0.6; pointer-events: none; } .hpe_control_indicator:after { box-sizing: unset; content: \'\'; position: absolute; display: none; } .hpe_control input:checked ~ .hpe_control_indicator:after { display: block; } .hpe_control-radio .hpe_control_indicator:after { left: 2px; top: 2px; height: 7px; width: 7px; border-radius: 50%; background: #01a982; } .hpe_control-radio input:disabled ~ .hpe_control_indicator:after { background: #7b7b7b; } #hpe_privacy_banner .hpe_privacy_banner_main_text a { color: #fff; font-family: MetricReg,\'Metric Regular\',HPEMetricRegular,Arial,sans-serif; text-decoration: underline; } #hpe_privacy_banner .hpe_privacy_banner_main_text a:hover { color: #fff; text-decoration: none; } #hpe_privacy_banner .hpe_privacy_banner_main_text a:after { color: #fff; text-decoration: none; } #hpe_privacy_banner .hpe_privacy_banner_close { display: flex; display: -ms-grid; height: auto; float: right; margin: auto 64px auto 60px; } #hpe_privacy_banner .hpe_privacy_banner_close .icon { width: 20px; height: 20px; } @media only screen and (max-width: 991px) { #hpe_privacy_banner .hpe_privacy_banner_main_text { font-size: 16px; line-height: 17px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons { font-size: 17px; } #hpe_privacy_banner .hpe_control { font-size: 16px; line-height: 18px; } } @media only screen and (max-width: 767px) { #hpe_privacy_banner { display: inline-block; } #hpe_privacy_banner .hpe_control { font-size: 15px; line-height: 17px; } #hpe_privacy_banner .hpe_privacy_banner_main_text { position: relative; left: inherit; width: auto; width: -webkit-fill-available; width: -moz-fit-content; height: content; margin: 0 50px 0 15px; font-size: 15px; line-height: 16px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons { display: table-row; max-width: 100%; margin: 20px 15px 0 15px; font-size: 16px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons span { line-height: 22px; display: table-cell; padding: 0 20px 0 0; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons div { display: table-cell; vertical-align: middle; } #hpe_privacy_banner .hpe_privacy_banner_close { position: absolute; top: 15px; right: 0px; margin: 0px 15px 0px 0px; color: #fff; } } @media only screen and (max-width: 400px) { #hpe_privacy_banner { display: flow-root; } #hpe_privacy_banner .hpe_privacy_banner_main_text { position: relative; left: inherit; width: auto; width: -webkit-fill-available; width: -moz-fit-content; height: content; margin: 0 50px 0 15px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons { display: table-row; max-width: 100%; margin: 20px 15px 0 15px; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons span { display: table-row; margin: 0 20px 0 0; } #hpe_privacy_banner .hpe_privacy_banner_radio_buttons div { display: block; } #hpe_privacy_banner .hpe_privacy_banner_close { position: absolute; top: 15px; right: 0px; margin: 0px 15px 0px 0px; } }',

		/* CSS for CCPA opt-out form */
		'ccpa_css': '#hpe_privacy_ccpa_radio_buttons {display: block;float: left;max-width: 250px;min-width: 150px;color: #fff;font-family: MetricReg,\'Metric Regular\',HPEMetricRegular,Arial,sans-serif;font-size: 18px;margin: 0px 0px 0px 60px;}#hpe_privacy_ccpa_alert_message {font-family: \'Metric Semibold\',Arial,sans-serif;font-size:22px;text-align: center;}#hpe_privacy_ccpa_alert_message a, a:hover {color: #000;}.hpe_control-group {display: table;height: 60px;margin: 65px auto 20px;}#hpe_privacy_ccpa .hpe_control {display: inline-flex;font-family: \'Metric Light\',Arial,sans-serif;font-size:22px;color: #000;position: relative;padding: 3px 20px 0 30px;cursor: pointer;font-size: 17px;font-weight: normal;line-height: 19px;}label.hpe_control.hpe_control-radio {color: #000;}.hpe_control input {position: absolute;z-index: -1;opacity: 0;}.hpe_control_indicator {position: absolute;top: 5px;left: 0;height: 15px;width: 15px;background: #fff;border: 2px solid #c0c4c3;box-sizing: border-box;}.hpe_control-radio .hpe_control_indicator {border-radius: 50%;}.hpe_control:hover input ~ .hpe_control_indicator,.hpe_control input:focus ~ .hpe_control_indicator {background: #cccccc;}.hpe_control input:checked ~ .hpe_control_indicator {background: #fff;}.hpe_control_indicator:after {box-sizing: unset;content: \'\'; position: absolute; display: none; }.hpe_control input:checked ~ .hpe_control_indicator:after {display: block;}.hpe_control-radio .hpe_control_indicator:after {left: 2px;top: 2px;height: 7px;width: 7px;border-radius: 50%;background: #01a982;}.hpe_privacy_ccpa_save:hover{background:0 0;box-shadow:none;color:#000;outline:#01A982 solid 2px}.hpe_privacy_ccpa_save {background: 0 0;color: #000;outline: 0;border: 2px solid #01A982;font-family: MetricReg, \'Metric Regular\',HPEMetricRegular,Arial,sans-serif;font-weight: bold;font-size: 14px;text-transform: uppercase;text-decoration: none;padding: 10px 50px;}.hpe_privacy_ccpa_confirm_text {text-align: center; display: none;}',

		/* Below we're storing translations for privacy banner */
		'translation': {
			'en': {
				'message_no_radio': 'We use data collection tools to personalize your experience. By continuing to browse the site, you are agreeing to our use of cookies. To learn more, please visit our <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Privacy Statement</a>.',
				'message': 'This site uses cookies. While some cookies are required for the site to function, you can enable other non-essential cookies that will personalize and enhance your experience. To learn more, please visit our <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Privacy Statement</a>.',
				'close': 'close',
				'optionalCookies': 'Optional Cookies',
				'yes': 'Yes',
				'no': 'No'
				},
			'de': {
				'message_no_radio': 'Wir verwenden Tools f&uuml;r die Datenerfassung, um Ihr Erlebnis zu personalisieren. Indem Sie die Website weiter nutzen, erkl&auml;ren Sie sich mit der Verwendung von Cookies einverstanden. Weitere Informationen hierzu finden Sie in unserer <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Datenschutzerkl&auml;rung</a>.',
				'message': 'Diese Website verwendet Cookies. W&auml;hrend einige Cookies f&uuml;r die Funktionsf&auml;higkeit der Website ben&ouml;tigt werden, k&ouml;nnen Sie weitere nicht-wesentliche Cookies aktivieren, die Ihr Erlebnis personalisieren und verbessern. Weitere Informationen hierzu finden Sie in unserer <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Datenschutzerkl&auml;rung</a>.',
				'close': 'Schlie&szlig;en',
				'optionalCookies': 'Optionale Cookies',
				'yes': 'Ja',
				'no': 'Nein'
				},
			'es': {
				'message_no_radio': 'Usamos herramientas de recopilaci&oacute;n de datos para personalizar su experiencia. Al seguir navegando por el sitio, confirma que est&aacute; de acuerdo con el uso de cookies. Para m&aacute;s informaci&oacute;n consulte nuestra <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Declaraci&oacute;n de privacidad</a>.',
				'message': 'Este sitio usa cookies. Si bien algunas cookies son necesarias para el funcionamiento del sitio, puede habilitar otras cookies que le permitir&aacute;n personalizar y mejorar su experiencia. Para m&aacute;s informaci&oacute;n consulte nuestra <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Declaraci&oacute;n de privacidad</a>.',
				'close': 'Cerrar',
				'optionalCookies': 'Cookies opcionales',
				'yes': 'S&iacute;',
				'no': 'No'
				},
			'fr': {
				'message_no_radio': 'Nous utilisons des outils de collecte de donn&eacute;es pour personnaliser votre exp&eacute;rience. En poursuivant votre navigation sur le site, vous acceptez notre utilisation des cookies. Pour en savoir plus, veuillez consulter notre <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">D&eacute;claration de confidentialit&eacute;</a>.',
				'message': 'Ce site utilise des cookies. Si certains cookies sont n&eacute;cessaires au fonctionnement du site, vous pouvez toutefois activer d&apos;autres cookies non essentiels pour personnaliser et am&eacute;liorer votre exp&eacute;rience. Pour en savoir plus, veuillez consulter notre <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">D&eacute;claration de confidentialit&eacute;</a>.',
				'close': 'Fermer',
				'optionalCookies': 'Cookies optionnels',
				'yes': 'Oui',
				'no': 'Non'
				},
			'it': {
				'message_no_radio': 'Utilizziamo strumenti di raccolta dati che consentono di personalizzare l&apos;esperienza dell&apos;utente. Continuando a navigare nel sito, acconsenti all&apos;utilizzo dei cookie. Per ulteriori informazioni, consulta la nostra <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Informativa sulla privacy</a>.',
				'message': 'Questo sito utilizza cookie. Alcuni cookie sono indispensabili per il funzionamento del sito, ma puoi attivarne altri per personalizzare e migliorare la tua esperienza. Per ulteriori informazioni, consulta la nostra <a href="https://www.hpe.com/____cc____/____ll____/legal/privacy.html">Informativa sulla privacy</a>.',
				'close': 'Chiudi',
				'optionalCookies': 'Cookie facoltativi',
				'yes': 'S&igrave;',
				'no': 'No'
				},
			}
	};


	/*
	 * Privacy Banner object
	 */
	HPEPRIVACYBANNER = {
		cfg: null,
		cc: null,
		ll: null,
		bannerCssInserted: false,
		bannerHtmlInserted: false,
		bannerVisible: false,
		cookieDomain: '',
		bannerEventPrefix: 'HPEPRIVACYBANNER.',
		bannerReadyEvent: null,
		bannerOpenEvent: null,
		bannerCloseEvent: null,
		bannerConfigReadyEvent: null,
		footerLinkID: 'hpe-footer-privacy-cookie-link',
		bannerHTMLContainter: 'hpe_privacy_banner_container',
		bannerHTMLClose: 'hpe_privacy_banner_close',
		bannerAnswerCookie: 'hpeuck_answ',
		bannerPrefsCookie: 'hpeuck_prefs',
		bannerCookieLifeDays: 365,
		ccpaOptout: '#ccpaoptout',


		/*
		 * log(logStr) - our own log method; it checks if console exists, to make it safe to execute on older browsers
		 */
		log: function(logStr) {
			if ( (typeof console != 'undefined') && (typeof console.log != 'undefined') ) {
				console.log(logStr);
			}
		},


		/*
		 * isExcludedDomain() - checks if domain privacy banner script is included on, is on list of excluded domains; returns true if yes, and false if no
		 */
		isExcludedDomain: function() {
			var loc = window.location.href;
			for (var key in this.cfg.excludeDomains) {
				if ( loc.indexOf(this.cfg.excludeDomains[key]) > -1 ) {
					return true;
				}
			}
			return false;
		},


		/*
		 * isBannerAnswered() - returns true if banner was already answered and closed by user. In that case, we do not have to show banner again to user.
		 */
		isBannerAnswered: function() {
			if ( this.readCookie(this.bannerAnswerCookie) === '1' ) {
				return true;
			}
			return false;
		},


		/*
		 * isNoRadioButtonsTemplate(): - returns true if we should render banner template without radio buttons
		 */
		isNoRadioButtonsTemplate: function() {
			/* Check if we're called to force "no radio buttons" template */
			if ( document.location.href.indexOf("privacytemplatenoradiobuttons=1") != -1 ) {
				this.log('isNoRadioButtonsTemplate(): forced true');
				return true;
			}

			/* Check for existence of Slim/Full HFWS, or AEM HF on non-.hpe.com domains, to determine when to use no radio buttons template.
			   The "no radio buttons" template should be used on non-.hpe.com sites where we cannot "hijack" the footer cookies link to
			   allow user change preferences after banner close.
			*/
			if ( (this.getCookieDomain() != '.hpe.com') && ( !this.isFooterCookiesLinkAvailable() ) ) {
				this.log('isNoRadioButtonsTemplate(): true');
				return true;
			}

			this.log('isNoRadioButtonsTemplate(): false');
			return false;
		},


		/*
		 * isScriptInIframe() - returns true if privacy banner script is executed inside an iframe
		 */
		isScriptInIframe: function() {
			try {
				return window.self !== window.top;
			} catch(e) {
				return true;
			}
		},


		/*
		 * isBannerVisible() - returns true if privacy banner is visible
		 */
		isBannerVisible: function() {
			return this.bannerVisible;
		},


		/*
		 * isFooterCookiesLinkAvailable() - hijacks footer cookies link to relaunch the banner
		 */
		isFooterCookiesLinkAvailable: function() {
			if ( document.getElementById(this.footerLinkID) != null ) {
				return true;
			}
			return false;
		},


		/*
		 * isFontAvailable(font) - returns true if provided font name is available
		 */
		isFontAvailable: function (font) {
			var container = document.createElement('span');
			container.innerHTML = Array(100).join('wi');
			container.style.cssText = [
				'position:absolute',
				'width:auto',
				'font-size:128px',
				'left:-99999px'
					].join(' !important;');

			var monoWidth  = this.getContainerWidthForFont(container, 'monospace');
			var serifWidth = this.getContainerWidthForFont(container, 'serif');
			var sansWidth  = this.getContainerWidthForFont(container, 'sans-serif');

			return ( monoWidth !== this.getContainerWidthForFont(container, font + ',monospace') ||
				sansWidth !== this.getContainerWidthForFont(container, font + ',sans-serif') ||
				serifWidth !== this.getContainerWidthForFont(container, font + ',serif') );
		},


		/*
		 * isCookieToBeDeleted(cookie_name, allowed_cookies) - returns true cookie_name is not on the allowed_cookies list
		 */
		isCookieToBeDeleted: function(cookie_name, allowed_cookies) {
			var result = true;
			var cookie_allowed = "";
			var reversed_cookie_name = "";
			for(var j=0; j < allowed_cookies.length; j++) {
				if(cookie_name == allowed_cookies[j]) { //simple cookie
					result = false;
				}
				else if(allowed_cookies[j].indexOf("[]") > 0) { //wildcard is at the end of the cookie name
					cookie_allowed = allowed_cookies[j];
					var pos = cookie_allowed.indexOf("[]");
					cookie_allowed = cookie_allowed.substring(0, pos);
					if(cookie_name.indexOf(cookie_allowed) == 0) {
						result = false;
					}
				}
				else if(allowed_cookies[j].indexOf("[]") == 0){ //wildcard is at the begining of the cookie name
					cookie_allowed = allowed_cookies[j];
					var pos = cookie_allowed.indexOf("[]");
					cookie_allowed = cookie_allowed.substring(2, cookie_allowed.length);
					cookie_allowed = cookie_allowed.reverse();
					reversed_cookie_name = cookie_name.reverse();
					if(reversed_cookie_name.indexOf(cookie_allowed) > -1) {
						result = false;
					}
				}
			}
			return result;
		},


		/*
		* getCCPAAllowedCookies(hpeuck_prefs) - returns list of ccpa allowed cookies based on hpeuck_prefs cookie value
		*/
		getCCPAAllowedCookies: function(hpeuck_prefs) {
			var result = new Array();
			if(hpeuck_prefs.charAt(4) == "1" || hpeuck_prefs.length == 4) {
				result = result.concat(this.cfg.ccpa_cookies);
			}
			//this.log(" |=> " + result.length + " ccpa cookies allowed");
			return result;
		},


		/*
		* getGDPRAllowedCookies(hpeuck_prefs) - returns list of GDPR allowed cookies based on hpeuck_prefs cookie value
		*/
		getGDPRAllowedCookies: function(hpeuck_prefs) {
			var result = new Array();
			for (i=0; i<hpeuck_prefs.length; i++) {
				if (hpeuck_prefs.charAt(i) == "1") {
					switch(i) {
						case 0 :
							result = result.concat(this.cfg.technical_cookies);
							break;
						case 1 :
							result = result.concat(this.cfg.tracking_cookies);
							break;
						case 2 :
							result = result.concat(this.cfg.personalization_cookies);
							break;
						default:
							result = result.concat(this.cfg.technical_cookies);
					}
				}
			}
			//this.log(" |=> " + result.length + " GDPR cookies allowed");
			return result;
		},


		/*
		 * getContainerWidthForFont(container, fontFamily) - calculates the width of provided container with text styled for provided fontFamily.
		 *    (method used by isFontAvailable())
		 */
		getContainerWidthForFont: function (container, fontFamily) {
			var width;
			var body = document.body;

			container.style.fontFamily = fontFamily;

			body.appendChild(container);
			width = container.clientWidth;
			body.removeChild(container);

			return width;
		},


		/*
		 * getLocaleConfigByCCLL(cc, ll) - searches for and returns locale config for cc and ll. In case locale is not found, returns null.
		 */
		getLocaleConfigByCCLL: function(cc, ll) {
			for (var key in this.cfg.supportedLocales) {
				if ( (cc === this.cfg.supportedLocales[key].cc) && (ll === this.cfg.supportedLocales[key].ll) ) {
					return this.cfg.supportedLocales[key];
				}
			}
			return null;
		},


		/*
		 * getLocaleConfigByCC(cc) - searches for and returns locale config for the provided CC country code. In case locale is not found, returns null.
		 */
		getLocaleConfigByCC: function(cc) {
			for (var key in this.cfg.countryToLocaleMap) {
				if ( cc === this.cfg.countryToLocaleMap[key].cc ) {
					return this.getLocaleConfigByCCLL(this.cfg.countryToLocaleMap[key].useLocale.cc, this.cfg.countryToLocaleMap[key].useLocale.ll);
				}
			}
			return null;
		},


		/*
		 * getLocaleConfigByLL(ll) - searches for and returns locale config for the provided LL language code. In case locale is not found, returns null.
		 */
		getLocaleConfigByLL: function(ll) {
			for (var key in this.cfg.languageToLocaleMap) {
				if ( ll === this.cfg.languageToLocaleMap[key].ll ) {
					return this.getLocaleConfigByCCLL(this.cfg.languageToLocaleMap[key].useLocale.cc, this.cfg.languageToLocaleMap[key].useLocale.ll);
				}
			}
			return null;
		},


		/*
		 * getBannerHeight() - returns banner's height. If banner is closed, returns 0. This is used by AEM for some templates.
		 */
		getBannerHeight: function() {
			if ( !this.isBannerVisible() ) {
				return 0;
			}
			return document.getElementById(this.bannerHTMLContainter).offsetHeight;
		},


		/*
		 * getMetaTagContent(name) - returns content of meta tag identified by name, or null if unable to find it
		 */
		getMetaTagContent: function(name) {
			var m = document.getElementsByTagName('meta');
			for(var i in m) {
				if (m[i].name == name) {
					return m[i].content;
					break;
				}
			}
			return null;
		},


		/*
		 * getCookieDomain() - get the domain under which we should be saving the cookies
		 */
		getCookieDomain: function() {

			/* check if we already found and cached domain - then return it */
			if (this.cookieDomain != '') {
				return this.cookieDomain;
			}

			var href = window.location.href;

			if ( href.indexOf('http://') > -1 || href.indexOf('https://') > -1 ) { /* if cookie domain can be detected */
				var domain = href.split('/');
				var domain_name = domain[2];
				if( domain_name.indexOf(':') > 0 ) { /* check if we have port number in the domain name */
					var tmp = domain_name.split(':');
					domain_name = tmp[0];
				}
				var bits = domain_name.split('.');
				if(bits.length > 1) { /* if there are subdomains */
					this.log(bits);
					var cookie_domain = '.' + bits[bits.length - 1];
					var accept_cookie = '0';
					for(i=bits.length-1; i>0; i--) {
						cookie_domain = '.' + bits[i-1] + cookie_domain;
						this.writeCookie(cookie_domain, 'hpeuck_cktst', '1');
						accept_cookie = this.readCookie('hpeuck_cktst');
						this.eraseCookie(cookie_domain, 'hpeuck_cktst');
						if (accept_cookie === '1') { break }
						this.log(cookie_domain);
					}
					if(accept_cookie === '0') {
						cookie_domain = false;
					}
				}
				else {
					this.writeCookie(domain_name, 'hpeuck_cktst','1');
					accept_cookie = this.readCookie('hpeuck_cktst');
					this.eraseCookie(domain_name, 'hpeuck_cktst');
					if (accept_cookie === '1') { cookie_domain = domain_name }
					else { cookie_domain = false }
				}
			}
			else { /* the cookie domain is not detected */
				cookie_domain = 'localhost';
			}

			this.log(href + ' | ' + cookie_domain);

			this.cookieDomain = cookie_domain;

			return cookie_domain;
		},


		/*
		 * getLocaleOptIn() - returns optIn value from config, based on current object's locale
		 */
		getLocaleOptIn: function() {
			var tmpLoc = null;

			if ( (tmpLoc = this.getLocaleConfigByCCLL(this.cc, this.ll)) != null ) {
				return tmpLoc.optIn;
			}

			return null;
		},


		/*
		 * getLocaleDefaultAnswer() - returns defaultAnswer value from config, based on current object's locale
		 */
		getLocaleDefaultAnswer: function() {
			var tmpLoc = null;

			if ( (tmpLoc = this.getLocaleConfigByCCLL(this.cc, this.ll)) != null ) {
				return tmpLoc.defaultAnswer;
			}

			return null;
		},


		/*
		 * getCookiesFromBrowser() - returns a list of all cookies from the browser
		 */
		getCookiesFromBrowser: function() {
			var cookies = new Array();
			var ca = new Array();

			// check if there are no cookies - to not create array with single "fake" empty name cookie as result of split on ;
			if (document.cookie !== "") {
				ca = document.cookie.split(';');
			}

			for(var i=0;i < ca.length;i++) {
				var pair = ca[i].split('=');
				pair[0] = pair[0].replace(/ /,"");
				cookies.push(pair[0]);
			}
			return cookies;
		},


		/*
		 * readCookie(name) - returns cookie value, if cookie is not found, return null
		 */
		readCookie: function(name) {
			var nameEQ = name + '=';
			var ca = document.cookie.split(';');
			for(var i=0; i < ca.length; i++) {
				var c = ca[i];
				while ( c.charAt(0) == ' ' ) c = c.substring(1, c.length);
				if ( c.indexOf(nameEQ) == 0 ) return c.substring(nameEQ.length, c.length);
			}
			return null;
		},


		/*
		 * writeCookie(domain, name, value, days) - write cookie, takes as parameter domain name, cookie name, cookie value and cookie lifetime (in days)
		 */
		writeCookie: function(domain, name, value, days) {
			if (days) {
				var date = new Date();
				date.setTime(date.getTime() + (days*24*60*60*1000));
				var expires = '; expires=' + date.toGMTString();
			}
			else var expires = '';
			document.cookie = name + '=' + value + expires + '; path=/; domain=' + domain;
		},


		/*
		 * eraseCookie(domain, name) - set cookie value to empty and lifetime to session
		 */
		eraseCookie: function(domain, name) {
			this.writeCookie(domain, name, '', 0);
			this.log('(' + domain + ') Cookie ' + name + ' has been deleted');
		},


		/*
		 * renderBannerHTML() - renders and returns banner html localized for this.cc country and this.ll language
		 */
		renderBannerHTML: function() {
			var tmpHtml = this.cfg.template;
			var hpeuck_prefs = '';

			/* Check if we're should use "no radio buttons" template */
			if ( this.isNoRadioButtonsTemplate() ) {
				tmpHtml = this.cfg.template_no_radio_buttons;
			}

			/* go through all translation keys defined for language, and replace them in the template */
			for (var key in this.cfg.translation[this.ll]) {
				tmpHtml = tmpHtml.replace('____' + key + '____', this.cfg.translation[this.ll][key]);
			}

			/* render the cc and ll codes appearing in resulting html */
			tmpHtml = tmpHtml.replace('____cc____', this.cc);
			tmpHtml = tmpHtml.replace('____ll____', this.ll);


			/* add debug parameter to display the banner with no answer preselected */
			if ( document.location.href.indexOf('privacyanswerpreselect=0') != -1 ) {
				tmpHtml = tmpHtml.replace('___checked_yes___', '');
				tmpHtml = tmpHtml.replace('___checked_no___', '');
				tmpHtml = tmpHtml.replace('___hpe_privacy_banner_close_style___', 'style="visibility: hidden"');
			}
			else {
				hpeuck_prefs = this.readCookie(this.bannerPrefsCookie);
				/* check if used has already closed the banner, and if answers are 1100 or 1111 (preferences created
				   with new banner with only one yes/no option). If true, use the user's preferences for preselection,
				   otherwise, use locale default. */
				if ( this.isBannerAnswered() && ( (hpeuck_prefs == '1100') || (hpeuck_prefs == '1111') ) ) {
					this.log('preselecting answers based on previous user answer');
					if (hpeuck_prefs == '1100') {
						tmpHtml = tmpHtml.replace('___checked_yes___', '');
						tmpHtml = tmpHtml.replace('___checked_no___', 'checked="checked"');
					}
					if (hpeuck_prefs == '1111') {
						tmpHtml = tmpHtml.replace('___checked_yes___', 'checked="checked"');
						tmpHtml = tmpHtml.replace('___checked_no___', '');
					}
					tmpHtml = tmpHtml.replace('___hpe_privacy_banner_close_style___', '');
				}
				else {
					this.log('preselecting answers based on config');
					if (this.getLocaleOptIn()) {
						tmpHtml = tmpHtml.replace('___checked_yes___', '');
						tmpHtml = tmpHtml.replace('___checked_no___', '');
						tmpHtml = tmpHtml.replace('___hpe_privacy_banner_close_style___', 'style="visibility: hidden"');
					}
					else {
						if (this.getLocaleDefaultAnswer() == 'yes') {
							tmpHtml = tmpHtml.replace('___checked_yes___', 'checked="checked"');
							tmpHtml = tmpHtml.replace('___checked_no___', '');
						}
						if (this.getLocaleDefaultAnswer() == 'no') {
							tmpHtml = tmpHtml.replace('___checked_yes___', '');
							tmpHtml = tmpHtml.replace('___checked_no___', 'checked="checked"');
						}
						tmpHtml = tmpHtml.replace('___hpe_privacy_banner_close_style___', '');
					}
				}
				/* end of answer preselection */
			}
			return tmpHtml;
		},


		/*
		 * insertCSS(style) - inserts style to document's head section
		 */
		insertCSS: function(style) {
			var sheet = document.createElement('style');
			document.getElementsByTagName('head')[0].appendChild(sheet);
			try {
				sheet.innerText = style;
				sheet.innerHTML = style;
			}
			catch(e) {
				sheet.styleSheet.cssText=style;
			}
		},


		/*
		 * insertBannerCSS() - insert privacy banner css code to the page
		 */
		insertBannerCSS: function() {
			if (!this.bannerCssInserted) {
				/* include fonts only if not already available on page - to save bandwith and page load time */
				if ( !(
							(this.isFontAvailable('MetricReg') && this.isFontAvailable('MetricSemibold') )
								||
							(this.isFontAvailable('HPEMetricRegular') && this.isFontAvailable('HPEMetricSemiBold') )
								||
							(this.isFontAvailable('"Metric Regular"') && this.isFontAvailable('"Metric Semibold"') )
						) ) {
					this.log('Metric fonts not found on page - loading font CSS');
					this.insertCSS(this.cfg.css_font);
				}
				else {
					this.log('Metric fonts found on page - not loading font CSS');
				}
				this.insertCSS(this.cfg.css);
				this.bannerCssInserted = true;
			}
		},


		/*
		 * insertBannerHTML() - insert the privacy banner to the page
		 */
		insertBannerHTML: function() {
			if( !this.bannerHtmlInserted && !document.getElementById(this.bannerHTMLContainter) ) {
				var holder = document.createElement('div');
				holder.id = this.bannerHTMLContainter;
				var body = document.body;
				if (body.firstChild) {
					  body.insertBefore(holder, document.body.firstChild);
				}
				else {
					  body.appendChild(holder);
				}
				document.getElementById(this.bannerHTMLContainter).innerHTML = this.renderBannerHTML();
				this.bannerHtmlInserted = true;
			}
		},


		/*
		 * insertCCPAForm - inserts CCPA form in the page
		*/
		insertCCPAForm: function() {
			var container = document.getElementById("hpe_ccpa_optout_form");
			if(container != null) {
				this.insertCSS(this.cfg.ccpa_css);
				container.innerHTML = this.cfg.template_ccpa_form;
				if(this.getCCPAOption() === "0") {
					document.getElementById("ccpa_yes").checked = true;
					document.getElementById("ccpa_no").checked = false;
				}
				else if(this.getCCPAOption() === "1") {
					document.getElementById("ccpa_yes").checked = false;
					document.getElementById("ccpa_no").checked = true;
				}
				return true;
			}
			else {
				//console.log("ccpa container not found!");
				return false;
			}
		},


		/*
		 * hijackFooterCookiesLink() - hijacks footer cookies link to relaunch the banner
		 */
		hijackFooterCookiesLink: function() {
			var self = this;
			if ( this.isFooterCookiesLinkAvailable() ) {
				document.getElementById(this.footerLinkID).onclick = function() {
					if (!self.isBannerVisible()) {
						self.showBanner();
						document.getElementById(self.bannerHTMLContainter).scrollIntoView(true);
						self.trackBannerMetrics(self.cc + "_" + self.ll + "_hpeuck_ban_footerview");
						return false;
					}
					return true;
				};
			}
		},


		/*
		 * trackBannerMetrics(metrics) - checks if metrics are available on page, and sends trackMetrics event for supplied metrics string param
		 */
		trackBannerMetrics: function(metrics) {
			var self = this;
			if(typeof window.digitalData !== 'undefined') {
				digitalData.promises.trackMetricsReady.then(function() {
					self.log("trackBannerMetrics(): " + metrics);
					trackMetrics("new.link", {"link_name": metrics});
				});
			}
			else {
				this.log("trackBannerMetrics(): unable to track, digitalData object not available");
			}
		},


		/*
		 * showBanner() - shows privacy banner on the page, if not shown already
		 */
		showBanner: function() {
			if (!this.isBannerVisible()) {
				var self = this;

				this.bannerVisible = true;

				/* insert banner CSS and HTML */
				this.insertBannerCSS();
				this.insertBannerHTML();

				/* add the close and save answer event for the privacy banner */
				document.getElementById(this.bannerHTMLClose).onclick = function(event) {
					event.preventDefault();
					self.saveAndCloseBanner();
				};

				/* Check if no answer preselected on radio buttons and add events to show the close button on answer selection */
				if (document.location.href.indexOf("privacyanswerpreselect=0") != -1 || this.getLocaleOptIn()) {
					/* add click event on radio buttons to show X back when radios are clicked */
					elements = document.getElementsByClassName('hpe_control-radio');
					for (var i = 0; i < elements.length; i++) {
						elements[i].onclick = function () {
							document.getElementById(self.bannerHTMLClose).style.visibility = 'visible';
						};
					}
				}
				this.dispatchBannerEvent('OPEN');
				this.cookieCleanup();
			}
		},


		/*
		 * hideBanner() - removes privacy banner from page
		 */
		hideBanner: function() {
			/* TODO: perhaps do some small animation, and then remove from page? */
			var bannerContainer = document.getElementById(this.bannerHTMLContainter);
			bannerContainer.parentNode.removeChild(bannerContainer);
			this.bannerHtmlInserted = false;
			this.bannerVisible = false;
			this.dispatchBannerEvent('CLOSE');
			this.cookieCleanup();
			this.hijackFooterCookiesLink();
		},


		/*
		 * userErrorNotification() - notify user that he has to chose an answer
		 */
		/* TODO: disabling the "red color" error notification - remove later
		userErrorNotification: function() {
			elements = document.getElementsByClassName('hpe_control-radio');
			for (var i = 0; i < elements.length; i++) {
				elements[i].style.color = '#ff4500';
			}
			document.getElementById("hpe_privacy_banner_alert_message").style.color = "#ff4500";

			//add click event on radio buttons to remove the userErrorNotification coloring
			elements = document.getElementsByClassName('hpe_control-radio');
			for (var i = 0; i < elements.length; i++) {
				elements[i].onclick = function () {
					elements = document.getElementsByClassName('hpe_control-radio');
					for (var i = 0; i < elements.length; i++) {
						elements[i].style.color = '#fff';
					}
					document.getElementById("hpe_privacy_banner_alert_message").style.color = "#fff";
				};
			}
		},
		*/


		/*
		 * readBannerAnswer() - read the answer from th banner
		 */
		readBannerAnswer: function() {
			if (this.isBannerVisible()) {
				var selector = document.querySelector('input[name="hpe_privacy_answer"]:checked');
				if(selector) {
					if(selector.value == '0') {
						if(ccpa = this.getCCPAOption()) {
							return "1100" + ccpa;
						}
						else {
							return "1100";
						}
					}
					else if(selector.value == '1') {
						if(ccpa = this.getCCPAOption()) {
							return "1111" + ccpa;
						}
						else {
							return "1111";
						}
					}
				}
				else {
					/* TODO: disabling the "red color" error notification - remove later
					   this.userErrorNotification();
					*/
					return null;
				}
			}
		},


		/*
		 * saveAndCloseBanner() - saves selected answers and closes the banner
		 */
		saveAndCloseBanner: function() {
			if (this.isBannerVisible()) {
				if ( this.isNoRadioButtonsTemplate() ) {
					/* in case of "no radio buttons" template - just close the banner */
					this.writeCookie(this.getCookieDomain(), this.bannerAnswerCookie, '1', this.bannerCookieLifeDays);
					/* TODO: should we write banner prefs cookie as well, to have the same TTL as banner answer cookie? It was saved when banner was viewed, which is earlier than banner close. */
					this.hideBanner();

					this.trackBannerMetrics(this.cc + "_" + this.ll + "_hpeuck_ans_1111");
				}
				else {
					/* in case of "radio buttons" template - check if banner is answered, before closing */
					userOption = this.readBannerAnswer();
					if (userOption) {
						this.writeCookie(this.getCookieDomain(), this.bannerAnswerCookie, '1', this.bannerCookieLifeDays);
						this.writeCookie(this.getCookieDomain(), this.bannerPrefsCookie, userOption, this.bannerCookieLifeDays);

						/* Remove the banner from page */
						this.hideBanner();

						this.trackBannerMetrics(this.cc + "_" + this.ll + "_hpeuck_ans_" + userOption);
					}
				}
			}
			return false;
		},


		/*
		 * validateCookiePrefs(hpeuck_prefs) - checks hpeuck_prefs value for a valid value
		 */
		validateCookiePrefs: function(hpeuck_prefs) {
			var result = false;

			if (hpeuck_prefs == null) return false;

			if (hpeuck_prefs.length == 4 || hpeuck_prefs.length == 5) {
				result = true;
				for (i=0; i<hpeuck_prefs.length; i++) {
					switch (hpeuck_prefs.charAt(i)) {
						case "0" :
							break;
						case "1" :
							break;
						default :
							return false;
							break;
					}
				}
			}
			return result;
		},


		/*
		 * cookieCleanup() - removes the cookies from the browser, based on user preferences or country default
		 */
		cookieCleanup: function() {
			var hpeuck_prefs = "";
			var browser_cookies = this.getCookiesFromBrowser();
			var allowed_cookies = new Array();
			var ccpa_cookies = new Array();
			var ccpa;

			// TODO: remove this later, temporary supression for the time of discover event
			if ( window.location.href.indexOf('attend.hpe.com') !== -1 ) {
				return false;
			}

			this.log("Running cookie cleanup...");

			/* read hpeuck_prefs cookie and validate it. If it does not validate (got broken etc) - switch to value based on locales config */
			hpeuck_prefs = this.readCookie(this.bannerPrefsCookie);
			if ( !this.validateCookiePrefs(hpeuck_prefs) ) {
				if (this.getLocaleDefaultAnswer() == 'yes') {
					hpeuck_prefs = "1111";
				}
				else if (this.getLocaleDefaultAnswer() === 'no') {
					hpeuck_prefs = "1100";
				}
			}

			/* GDPR COOKIES CLEANUP HANDLING */
			/* execute GDPR cookie cleanup only if we have found the preference - from hpeuck_prefs or country default */
			if ( (hpeuck_prefs != null) && (hpeuck_prefs != '') ) {
				/* build the list of allowed GDPR cookies based on determined preferences */
				allowed_cookies = this.getGDPRAllowedCookies(hpeuck_prefs);
			}
			else if (this.isCCPA()) {
				/* If locale is US where CCPA applies, and user did not answer GDPR banner for other locale, then GDPR cookies are allowed, so we add them to allowed_cookies in order to cleanup non-registered cookies */
				allowed_cookies = this.getGDPRAllowedCookies("1111");
			}

			/* CCPA COOKIES CLEANUP HANDLING */
			/* If 5th bit exists in hpeuck_prefs, handle it according to user's saved configuration. If not set, but locale is CCPA, allow CCPA cookies (user did not opt out) */
			if(ccpa = this.getCCPAOption()) {
				if(ccpa === "1") {
					allowed_cookies = allowed_cookies.concat(this.getCCPAAllowedCookies(hpeuck_prefs));
				}
				if(ccpa === "0") {
					/* get list of CCPA cookies */
					ccpa_cookies = this.getCCPAAllowedCookies("11111");
					/* if CCPA cookie is on allowed list - delete it, as user opted out from CCPA) */
					for(var j=0; j < ccpa_cookies.length; j++) {
						var deleteElement = ccpa_cookies[j];
						allowed_cookies = allowed_cookies.filter(function(element){
							return element !== deleteElement;
						});
					}
				}
			}
			else if (this.isCCPA()) {
				/* Locale supports CCPA, and user has not opted out from CCPA cookies - allow CCPA cookies */
				allowed_cookies = allowed_cookies.concat(this.getCCPAAllowedCookies("11111"));
			}

			/* cleanup all cookies that are not on the allowed_cookies list */
			for(var i=0; i<browser_cookies.length; i++) {
				//do not delete the hpeuck_prefs cookie
				if (browser_cookies[i] != "hpeuck_prefs") {
					if(this.isCookieToBeDeleted(browser_cookies[i], allowed_cookies)) {
						//this.log("Deleting cookie " + browser_cookies[i]);
						this.eraseCookie(this.getCookieDomain(), browser_cookies[i]);
					}
				}
			}
			this.log("... done.");
		},


		/*
		 * getCCPAOption() - returns CCPA option or false if CCPA digit is not present in the hpeuck_prefs cookie
		 */
		getCCPAOption: function() {
			hpeuck_prefs = this.readCookie(this.bannerPrefsCookie);
			if (this.validateCookiePrefs(hpeuck_prefs) && hpeuck_prefs.length == 5) {
				return hpeuck_prefs.charAt(4);
			}
			else {
				return false;
			}
		},


		/*
		 * dispatchBannerEvent(eventname) - creates and dispatches to document HPEPRIVACYBANNER|HPEALERTBANNER.eventname event.
		 *
		 * Eventnames we expect are:
		 *	READY (banner finished initialization)
		 *	OPEN (banner is opened - either by init() or by user from footer to re-launch banner)
		 *	CLOSE (banner is closed by user)
		 *	CONFIGREADY (banner configuration is ready for first time visitor)
		 */
		dispatchBannerEvent: function(eventname) {
			switch (eventname) {
				case 'READY':
					if ( this.bannerReadyEvent === null) {
						this.bannerReadyEvent = document.createEvent('Event');
						this.bannerReadyEvent.initEvent(this.bannerEventPrefix + eventname, true, true);
					}
					document.dispatchEvent(this.bannerReadyEvent);
					break;
				case 'OPEN':
					if ( this.bannerOpenEvent === null) {
						this.bannerOpenEvent = document.createEvent('Event');
						this.bannerOpenEvent.initEvent(this.bannerEventPrefix + eventname, true, true);
					}
					document.dispatchEvent(this.bannerOpenEvent);
					break;
				case 'CLOSE':
					if ( this.bannerCloseEvent === null) {
						this.bannerCloseEvent = document.createEvent('Event');
						this.bannerCloseEvent.initEvent(this.bannerEventPrefix + eventname, true, true);
					}
					document.dispatchEvent(this.bannerCloseEvent);
					break;
				case 'CONFIGREADY':
					if (this.bannerConfigReadyEvent === null) {
						this.bannerConfigReadyEvent = document.createEvent('Event');
						this.bannerConfigReadyEvent.initEvent(this.bannerEventPrefix + eventname, true, true);
					}
					document.dispatchEvent(this.bannerConfigReadyEvent);
					break;
				default:
					this.log('dispatchBannerEvent() Error - unknown event: ' + this.bannerEventPrefix + eventname);
			}
		},


		/*
		 * addUnloadCookieCleanup() - adds unload event that runs cookie cleanup
		 *
		 * Eventnames we expect are:
		 *	READY (banner finished initialization)
		 *	OPEN (banner is opened - either by init() or by user from footer to re-launch banner)
		 *	CLOSE (banner is closed by user)
		 */
		addCookieCleanupUnloadEvent: function() {
			/* Check if other onbeforeunload events are already defined, and preserve them */
			var preserved_onbeforeunload_fn = null;
			if(typeof window.onbeforeunload == 'function') {
				preserved_onbeforeunload_fn = window.onbeforeunload;
			}
			else {
				preserved_onbeforeunload_fn = function () { ; };
			}

			/* create event to run the cookieCleanup() when user navigates away from the page */
			var self = this;
			window.onbeforeunload = function(event) {
				preserved_onbeforeunload_fn();
				self.cookieCleanup();
			};
		},


		/*
		 * detectLocaleFromURL() - detects if supported locale comes via URL part as /cc/ll/.
		 *
		 * Checks also for partial information - like, only cc and unknown ll, or only ll and unknown cc, to cover for "old" locales like /ro/ro/, or /cz/cs/ etc.
		 *
		 * Returns detected locale information, or null, if unable to find locale from URL.
		 */
		detectLocaleFromURL: function() {
			var tmpLoc = '';
			var url = document.location.href;

			/* check if URL contains /cc/ll/ part for supported locale */
			for (var key in this.cfg.supportedLocales) {
				var ccLLReg = new RegExp('\\/' + this.cfg.supportedLocales[key].cc + '\\/' + this.cfg.supportedLocales[key].ll + '\\/','i');
				if ( url.search(ccLLReg) != -1) {
					return this.cfg.supportedLocales[key];
				}
			}

			return null;
		},


		/*
		 * detectLocaleFromHtmlLang() - detects locale from <html lang="..."> attribute.
		 *
		 * Checks also for partial information - like, only cc and unknown ll, or only ll and unknown cc, to cover for "old" locales like /ro/ro/, or /cz/cs/ etc.
		 *
		 * Returns detected locale information, or null, if unable to find locale from URL.
		 */
		detectLocaleFromHtmlLang: function() {
			var tmpLoc = '';
			var cc = '';
			var ll = '';
			var lang = document.documentElement.lang;

			if ( lang != null ) {
				lang = lang.toLowerCase();
				/* try to split lang ll-cc into cc and ll */
				ccllarr = lang.split("-");
				if (ccllarr.length > 1) { /* lang attribute contains is in the format ll-cc */
					cc = ccllarr[1];
					ll = ccllarr[0];

					/* Check if we find matching locale by cc and ll */
					if ( ( tmpLoc = this.getLocaleConfigByCCLL(cc, ll) ) != null ) {
						return tmpLoc;
					}

					/* Check if we find matching locale by cc */
					if ( ( tmpLoc = this.getLocaleConfigByCC(cc) ) != null ) {
						return tmpLoc;
					}

					/* Check if we find matching locale by ll */
					if ( ( tmpLoc = this.getLocaleConfigByLL(ll) ) != null ) {
						return tmpLoc;
					}
				}
				else {
					/* lang contains only the language - Check if we can find matching locale by ll */
					ll = lang;
					if ( ( tmpLoc = this.getLocaleConfigByLL(ll) ) != null ) {
						return tmpLoc;
					}
				}
			}

			return null;
		},


		/*
		 * detectLocaleFromMeta() - detects locale from target_country meta.
		 * Returns detected locale information, or null.
		 */
		detectLocaleFromMeta: function() {
			var tmpLoc = '';
			var cc = "";
			var ll = "";
			var lang = document.documentElement.lang;

			if(cc = this.getMetaTagContent("target_country")) {
				cc = cc.toLowerCase();
			}

			if(lang != null) {
				var ccllarr = lang.split("-");
				if(ccllarr.length == 1) {
					ll = lang.toLowerCase();
				}
			}

			if(cc != null && ll != "") {
				/* Check if we find matching locale by cc and ll */
				if ( ( tmpLoc = this.getLocaleConfigByCCLL(cc, ll) ) != null ) {
					return tmpLoc;
				}
			}

			if(cc != null) {
				/* Check if we find matching locale by cc */
				if ( ( tmpLoc = this.getLocaleConfigByCC(cc) ) != null ) {
					return tmpLoc;
				}
			}

			return null;
		},


		/*
		 * detectLocaleFromCookie() - detects locale from lang cookie.
		 * Returns detected locale information, or null.
		 */
		detectLocaleFromCookie: function() {
			var tmpLoc = '';
			var cc = '';
			var ll = '';
			var lang = this.readCookie("lang");
			var ccCookie = this.readCookie("cc");

			if(lang != null) {
				lang = lang.toLowerCase();
				var ccllarr = lang.split("-");
				if(ccllarr.length > 1) {//lang contains ll-cc combination
					cc = ccllarr[1];
					ll = ccllarr[0];
					/* Check if we find matching locale by cc and ll */
					if((tmpLoc = this.getLocaleConfigByCCLL(cc, ll)) != null) {
						return tmpLoc;
					}
				}
				if(ccllarr.length == 1) {
					ll = ccllarr[0];
					/* Check if we find matching locale by ll */
					if ( ( tmpLoc = this.getLocaleConfigByLL(ll) ) != null ) {
						return tmpLoc;
					}
				}
			}

			if(ccCookie != null && lang != null) {
				ll = lang.toLowerCase();
				cc = ccCookie.toLowerCase();

				/* Check if we find matching locale by cc and ll */
				if((tmpLoc = this.getLocaleConfigByCCLL(cc, ll)) != null) {
					return tmpLoc;
				}
			}
			return null;
		},


		/*
		 * detectLocaleFromBrowser() - detects locale from browser locale settings.
		 * Returns detected locale information, or null.
		 */
		detectLocaleFromBrowser: function() {
			var browserLang = (navigator.language) ? navigator.language : navigator.userLanguage;
			if(browserLang != null) {
				browserLang = browserLang.toLowerCase();
				var ccllarr = browserLang.split("-");

				if(ccllarr.length > 1) {//browser lang contains ll-cc combination
					cc = ccllarr[1];
					ll = ccllarr[0];
					/* Check if we find matching locale by cc and ll */
					if((tmpLoc = this.getLocaleConfigByCCLL(cc, ll)) != null) {
						return tmpLoc;
					}
				}

				if(ccllarr.length == 1) {
					ll = ccllarr[0];
					/* Check if we find matching locale by ll */
					if ( ( tmpLoc = this.getLocaleConfigByLL(ll) ) != null ) {
						return tmpLoc;
					}
				}

			}
			return null;
		},


		/*
		 * detectLocaleDefault() - tries to detect page or user locale using different methods.
		 *
		 * Returns detected locale information, or null, if unable to find locale.
		 */
		detectLocaleDefault: function() {
			var tmpLoc = null;

			if ( (tmpLoc = this.detectLocaleFromURL() ) != null ) {
				this.log('Locale detected from URL: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			if ( (tmpLoc = this.detectLocaleFromHtmlLang() ) != null ) {
				this.log('Locale detected from HTML lang: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			if ( (tmpLoc = this.detectLocaleFromMeta() ) != null ) {
				this.log('Locale detected from target_country meta: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			if ( (tmpLoc = this.detectLocaleFromCookie() ) != null ) {
				this.log('Locale detected from lang cookie: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			if ( (tmpLoc = this.detectLocaleFromBrowser() ) != null ) {
				this.log('Locale detected from browser settings: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			return null;
		},


		/*
		 * detectLocale() - tries to detect page or user locale; first detectLocale() is used,
		 *                  but in case the target_country set for page is "ww", there is additional
		 *                  check done for locale cookie, and browser's locale preferences if user
		 *                  should see privacy cookie banner. This is to cover situation of user from
		 *                  GDPR enabled locale being sent to hpe page which is worldwide, and to make
		 *                  sure such user will see the Privacy Cookie banner in this scenario.
		 *
		 * Returns detected locale information, or null, if unable to find locale.
		 */
		detectLocale: function() {
			var tmpLoc = this.detectLocaleDefault();
			var target_country = null;

			if(target_country = this.getMetaTagContent("target_country")) {
				target_country = target_country.toLowerCase();
			}

			if(target_country == "ww" && !this.isGDPR(tmpLoc)) {
				if ((tmpLoc = this.detectLocaleFromCookie() ) != null && this.isGDPR(tmpLoc)) {
					this.log('Locale detected from lang cookie: ' + tmpLoc.cc + '/' + tmpLoc.ll);
					return tmpLoc;
				}
				if ((tmpLoc = this.detectLocaleFromBrowser() ) != null && this.isGDPR(tmpLoc)) {
					this.log('Locale detected from browser settings: ' + tmpLoc.cc + '/' + tmpLoc.ll);
					return tmpLoc;
				}
				/* If, for 'ww' target country, detected locale is null at this moment - we should return us/en to apply CCPA rules if locale from cookie or browser is not found. */
				if (tmpLoc == null) {
					this.log('Locale detected from target_country meta: for ww(world-wide) value, if locale is not detected through cookie or browser config, locale is set to us/en.');
					return this.getLocaleConfigByCCLL('us', 'en');
				}
			}

			return tmpLoc;
		},


		/*
		 * isGDPR(locale) - check detected locale and return true if it implements GDPR with Privacy Cookie Banne. locale param is optional - if provided, check will run against this param - otherwise, code will check objects this.cc and this.ll.
		 */
		isGDPR: function(locale) {
			var result = false;
			var cc = null;
			var ll = null;

			if (locale === undefined) {
				cc = this.cc;
				ll = this.ll;
			}
			else if (locale === null) {
				return false;
			}
			else {
				cc = locale.cc;
				ll = locale.ll;
			}

			for (var key in this.cfg.supportedLocales) {
				if ( (cc === this.cfg.supportedLocales[key].cc) && (ll === this.cfg.supportedLocales[key].ll) ) {
					return this.cfg.supportedLocales[key].gdpr;
				}
			}
			return result;
		},


		/*
		 * isCCPA() - check detected locale and return true if it implements CCPA
		 *
		*/
		isCCPA: function() {
			var result = false;
			for (var key in this.cfg.supportedLocales) {
				if ( (this.cc === this.cfg.supportedLocales[key].cc) && (this.ll === this.cfg.supportedLocales[key].ll) ) {
					return this.cfg.supportedLocales[key].ccpa;
				}
			}
			return result;
		},


		/*
		 * init(config) - initializes HPEPRIVACYBANNER object with the provided configuration object
		 */
		init: function (config) {
			var tmpLoc = null;
			var hpeuck_prefs ="";
			/* check if script is executed inside iframe and stop banner logic execution if true */
			if(!this.isScriptInIframe()) {

				this.log('Privacy Banner Init start');
				this.cfg = config;

				/* here we initalize privacy banner */

				/* TODO: we do not yet have methods to detect cc and ll, so below lines with hardcoded cc and ll for testing, should be changed: */
				/*
				this.cc = 'ie';
				this.ll = 'en';
				*/

				/* TODO: this is dummy code to test that renderBannerHTML works */
				/*
				var bannerHtml = this.renderBannerHTML();
				this.log('### Rendered banner html:');
				this.log('*** banner start ***');
				this.log(bannerHtml);
				this.log('*** banner stop ***');
				*/

				/* test iteration for locales TODO: remove this later */
				/*
				this.log('### Supported locales:');
				var tmpLoc = '';
				for (var key in this.cfg.supportedLocales) {
					tmpLoc += this.cfg.supportedLocales[key].cc + '/' + this.cfg.supportedLocales[key].ll + ' ';
				}
				this.log(tmpLoc);
				*/

				/* test getLocaleConfigByCCLL()  TODO: remove this later */
				/*
				this.log('### getLocaleConfigByCCLL(\'es\',\'es\'):');
				if ((tmpLoc = this.getLocaleConfigByCCLL('es','es')) != null) {
					this.log('CC: ' + tmpLoc.cc + ' LL: ' + tmpLoc.ll + ' optIn: ' + tmpLoc.optIn + ' defaultAnswer: ' + tmpLoc.defaultAnswer);
				}
				*/

				/* test getLocaleConfigByCC()  TODO: remove this later */
				/*
				this.log('### getLocaleConfigByCC(\'ro\'):');
				if ((tmpLoc = this.getLocaleConfigByCC('ro')) != null) {
					this.log('CC: ' + tmpLoc.cc + ' LL: ' + tmpLoc.ll + ' optIn: ' + tmpLoc.optIn + ' defaultAnswer: ' + tmpLoc.defaultAnswer);
				}
				*/

				/* test getLocaleConfigByLL()  TODO: remove this later */
				/*
				this.log('### getLocaleConfigByLL(\'pl\'):');
				if ((tmpLoc = this.getLocaleConfigByLL('pl')) != null) {
					this.log('CC: ' + tmpLoc.cc + ' LL: ' + tmpLoc.ll + ' optIn: ' + tmpLoc.optIn + ' defaultAnswer: ' + tmpLoc.defaultAnswer);
				}
				*/

				/* test isExcludedDomain()  TODO: remove this later */
				/*
				this.log('### isExcludedDomain: ' + this.isExcludedDomain());
				*/


				/* Insert CCPA Form */
				if(this.insertCCPAForm()) {

					/*  Execute logic for CCPA cookies optout */
					var ccpaOptoutBtn = document.getElementById("hpe_privacy_ccpa_save");
					ccpaOptoutBtn.onclick = function(e) {
						e.stopPropagation();
						e.preventDefault();

						document.getElementById("ccpa_label_yes").onclick = function() {
							document.getElementById("ccpa_label_yes").style.color = "#000";
							document.getElementById("ccpa_label_yes").style.transition = "250ms ease-in";
							document.getElementById("ccpa_label_no").style.color = "#000";
							document.getElementById("ccpa_label_no").style.transition = "250ms ease-in";
							document.getElementById("hpe_privacy_ccpa_confirm_text").style.display = "none";
						}
						document.getElementById("ccpa_label_no").onclick = function() {
							document.getElementById("ccpa_label_yes").style.color = "#000";
							document.getElementById("ccpa_label_yes").style.transition = "250ms ease-in";
							document.getElementById("ccpa_label_no").style.color = "#000";
							document.getElementById("ccpa_label_no").style.transition = "250ms ease-in";
							document.getElementById("hpe_privacy_ccpa_confirm_text").style.display = "none";
						}

						var ccpa_optout_result = "";
						if(document.getElementById("ccpa_yes").checked) {
							ccpa_optout_result = "0";
						}
						else if(document.getElementById("ccpa_no").checked) {
							ccpa_optout_result = "1";
						}
						else if(!document.getElementById("ccpa_yes").checked && !document.getElementById("ccpa_no").checked) {
							//no answer selected
							document.getElementById("ccpa_label_yes").style.color = "red";
							document.getElementById("ccpa_label_no").style.color = "red";
							return false;
						}

						hpeuck_prefs = HPEPRIVACYBANNER.readCookie(HPEPRIVACYBANNER.bannerPrefsCookie);
						if (HPEPRIVACYBANNER.validateCookiePrefs(hpeuck_prefs)) {
							if(hpeuck_prefs.length == 4) {
								hpeuck_prefs += ccpa_optout_result;
							}
							else {
								hpeuck_prefs = hpeuck_prefs.slice(0, -1) + ccpa_optout_result;
							}
						}
						else {
							hpeuck_prefs = "1111" + ccpa_optout_result;
						}

						document.getElementById("hpe_privacy_ccpa_confirm_text").style.display = "block";

						HPEPRIVACYBANNER.log("CCPA cookie optout. Value set: " + hpeuck_prefs);

						HPEPRIVACYBANNER.writeCookie(HPEPRIVACYBANNER.getCookieDomain(), HPEPRIVACYBANNER.bannerPrefsCookie, hpeuck_prefs, HPEPRIVACYBANNER.bannerCookieLifeDays);
						HPEPRIVACYBANNER.cookieCleanup();

						// send metrics for CCPA answers
						if(ccpa_optout_result == "1") {
							HPEPRIVACYBANNER.trackBannerMetrics("us_en_ccpa_form_ans_no");
						}
						else {
							HPEPRIVACYBANNER.trackBannerMetrics("us_en_ccpa_form_ans_yes");
						}

						return false;
					}
				}


				/* Execute logic to check and show banner if needed */
				if ( !this.isBannerAnswered() || document.location.href.indexOf('privacybannerforce=1') != -1 ) { /* show Privacy Banner if not already answered by user - or if forced to show by debug param*/
					this.log('Banner not answered - detect locale');
					if ( (tmpLoc = this.detectLocale() ) != null ) {
						this.cc = tmpLoc.cc;
						this.ll = tmpLoc.ll;

						if(this.isGDPR()) {
							/* save hpeuck_prefs if banner not answered */
							if ( this.isNoRadioButtonsTemplate() ) {
								/* for no radio buttons template, we always save 1111 to hpeuck_prefs configuration */
								if(ccpa = this.getCCPAOption()) {
									hpeuck_prefs = "1111" + ccpa;
								}
								else {
									hpeuck_prefs = "1111";
								}
								this.log('Saving hpeuck_prefs for no radio template - locale found.');
							}
							else {
								/* for radio buttons template, we're checking locale's default answer yes/no to configure hpeuck_prefs */
								if(this.getLocaleDefaultAnswer() == "yes") {
									if(ccpa = this.getCCPAOption()) {
										hpeuck_prefs = "1111" + ccpa;
									}
									else {
										hpeuck_prefs = "1111";
									}
								}
								else {
									if(ccpa = this.getCCPAOption()) {
										hpeuck_prefs = "1100" + ccpa;
									}
									else {
										hpeuck_prefs = "1100";
									}
								}
								this.log('Saving hpeuck_prefs with country default for radio template - locale found.');
							}
							this.writeCookie(this.getCookieDomain(), this.bannerPrefsCookie, hpeuck_prefs, this.bannerCookieLifeDays);

							/* show banner - cookie cleanup logic is run by showBanner() after it is shown */
							this.log('Showing the banner - locale found.');
							this.showBanner();
							this.addCookieCleanupUnloadEvent();
							this.trackBannerMetrics(this.cc + "_" + this.ll + "_hpeuck_ban_view");
						}
						if (this.isCCPA()) {
							/* Run cookie cleanup for CCPA */
							this.cookieCleanup();
						}
					}
					else {
						/* Check for param that forces banner to show, so we can easily test any web site with banner visible */
						if ( document.location.href.indexOf('privacybannerforce=1') != -1 ) {
							this.log('Privacy Banner forced to show - showing ie/en.');
							this.cc = 'ie';
							this.ll = 'en';
							this.showBanner();
							this.addCookieCleanupUnloadEvent();
							this.trackBannerMetrics(this.cc + "_" + this.ll + "_hpeuck_ban_view");
						}
						else {
							this.log('Not showing the banner - locale not found.');
						}
					}
				}
				else {
					/* if banner is already answered, run cookie cleanup logic and hijack the footer cookies link */
					this.log('Banner answered - run cleanup logic and hijack footer cookies link');
					this.cookieCleanup();
					if ( (tmpLoc = this.detectLocale() ) != null ) {
						this.cc = tmpLoc.cc;
						this.ll = tmpLoc.ll;
						this.log('Locale found for banner re-launch via footer link.');
					}
					else {
						this.cc = 'emea_europe';
						this.ll = 'en';
						this.log('Locale not found for banner re-launch via footer link - falling back to emea_europe/en.');
					}
					this.hijackFooterCookiesLink();
					this.addCookieCleanupUnloadEvent();
				}

			}
			else {
				this.log('Script is being executed inside an iFrame. Disabling privacy banner...');
			}

			/* Dispatch documnet event HPEPRIVACYBANNER.CONFIGREADY to inform any listener that banner configuration is ready for first time visitor */
			this.dispatchBannerEvent('CONFIGREADY');
			/* Dispatch document event HPEPRIVACYBANNER.READY, to inform any web site code listening to it, that privacy cookie banner code has been executed */
			this.dispatchBannerEvent('READY');
			/* let's also create legacy HP.PrivacyBanner.Loaded event that metrics code uses - TODO: remove this when they do not need it anymore: */
			var bannerLoadedEvent = document.createEvent('Event');
			bannerLoadedEvent.initEvent('HP.PrivacyBanner.Loaded', true, true);
			document.dispatchEvent(bannerLoadedEvent);
		}
	}


/*******************************************************************************************************************/

	/*
	 * HPE Alert Banner Configuration object
	 */
	HPEALERTBANNER_CFG = {
		'supportedLocales': [
			{ 'cc': 'asia_pac', 'll': 'en' },
			{ 'cc': 'at', 'll': 'de' },
			{ 'cc': 'au', 'll': 'en' },
			{ 'cc': 'be', 'll': 'en' },
			{ 'cc': 'be', 'll': 'fr' },
			{ 'cc': 'be', 'll': 'nl' },
			{ 'cc': 'br', 'll': 'pt' },
			{ 'cc': 'ca', 'll': 'en' },
			{ 'cc': 'ca', 'll': 'fr' },
			{ 'cc': 'ch', 'll': 'de' },
			{ 'cc': 'ch', 'll': 'fr' },
			{ 'cc': 'cn', 'll': 'zh' },
			{ 'cc': 'cz', 'll': 'en' },
			{ 'cc': 'de', 'll': 'de' },
			{ 'cc': 'dk', 'll': 'en' },
			{ 'cc': 'emea_africa', 'll': 'en' },
			{ 'cc': 'emea_africa', 'll': 'fr' },
			{ 'cc': 'emea_europe', 'll': 'en' },
			{ 'cc': 'emea_middle_east', 'll': 'en' },
			{ 'cc': 'es', 'll': 'es' },
			{ 'cc': 'fi', 'll': 'en' },
			{ 'cc': 'fr', 'll': 'fr' },
			{ 'cc': 'hk', 'll': 'en' },
			{ 'cc': 'ie', 'll': 'en' },
			{ 'cc': 'il', 'll': 'en' },
			{ 'cc': 'in', 'll': 'en' },
			{ 'cc': 'it', 'll': 'it' },
			{ 'cc': 'jp', 'll': 'ja' },
			{ 'cc': 'kr', 'll': 'ko' },
			{ 'cc': 'lamerica', 'll': 'en' },
			{ 'cc': 'lamerica', 'll': 'es' },
			{ 'cc': 'mx', 'll': 'es' },
			{ 'cc': 'my', 'll': 'en' },
			// { 'cc': 'nl', 'll': 'en' },
			{ 'cc': 'no', 'll': 'en' },
			{ 'cc': 'nz', 'll': 'en' },
			{ 'cc': 'pl', 'll': 'en' },
			{ 'cc': 'pt', 'll': 'en' },
			{ 'cc': 'ru', 'll': 'ru' },
			//{ 'cc': 'se', 'll': 'en' },
			{ 'cc': 'sg', 'll': 'en' },
			//{ 'cc': 'tr', 'll': 'en' },
			//{ 'cc': 'tw', 'll': 'en' },
			{ 'cc': 'uk', 'll': 'en' },
			{ 'cc': 'us', 'll': 'en' },
			{ 'cc': 'za', 'll': 'en' },
			{ 'cc': 'nl', 'll': 'nl' },
			{ 'cc': 'se', 'll': 'sv' },
			{ 'cc': 'tr', 'll': 'tr' },
			{ 'cc': 'tw', 'll': 'zh' },
			{ 'cc': 'sa', 'll': 'ar' },
			{ 'cc': 'ae', 'll': 'ar' },
			{ 'cc': 'ww', 'll': 'en' }, // Added on June 14, 2022 for ww/en
		],

		/* countryToLocaleMap can be used to find out what banner supported locale to use, if we could detect only the country, or we detected cc and ll not on supported list */
		'countryToLocaleMap': [
			{ 'cc': 'asia_pac', 'useLocale': { 'cc': 'asia_pac', 'll': 'en' } },
			{ 'cc': 'at', 'useLocale': { 'cc': 'at', 'll': 'de' } },
			{ 'cc': 'au', 'useLocale': { 'cc': 'au', 'll': 'en' } },
			{ 'cc': 'be', 'useLocale': { 'cc': 'be', 'll': 'en' } },
			{ 'cc': 'br', 'useLocale': { 'cc': 'br', 'll': 'pt' } },
			{ 'cc': 'ca', 'useLocale': { 'cc': 'ca', 'll': 'en' } },
			{ 'cc': 'ch', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'cn', 'useLocale': { 'cc': 'cn', 'll': 'zh' } },
			{ 'cc': 'cz', 'useLocale': { 'cc': 'cz', 'll': 'en' } },
			{ 'cc': 'de', 'useLocale': { 'cc': 'de', 'll': 'de' } },
			{ 'cc': 'dk', 'useLocale': { 'cc': 'dk', 'll': 'en' } },
			{ 'cc': 'emea_africa', 'useLocale': { 'cc': 'emea_africa', 'll': 'en' } },
			{ 'cc': 'emea_europe', 'useLocale': { 'cc': 'emea_europe', 'll': 'en' } },
			{ 'cc': 'emea_middle_east', 'useLocale': { 'cc': 'emea_middle_east', 'll': 'en' } },
			{ 'cc': 'es', 'useLocale': { 'cc': 'es', 'll': 'es' } },
			{ 'cc': 'fi', 'useLocale': { 'cc': 'fi', 'll': 'en' } },
			{ 'cc': 'fr', 'useLocale': { 'cc': 'fr', 'll': 'fr' } },
			{ 'cc': 'hk', 'useLocale': { 'cc': 'hk', 'll': 'en' } },
			{ 'cc': 'ie', 'useLocale': { 'cc': 'ie', 'll': 'en' } },
			{ 'cc': 'il', 'useLocale': { 'cc': 'il', 'll': 'en' } },
			{ 'cc': 'in', 'useLocale': { 'cc': 'in', 'll': 'en' } },
			{ 'cc': 'it', 'useLocale': { 'cc': 'it', 'll': 'it' } },
			{ 'cc': 'jp', 'useLocale': { 'cc': 'jp', 'll': 'ja' } },
			{ 'cc': 'kr', 'useLocale': { 'cc': 'kr', 'll': 'ko' } },
			{ 'cc': 'lamerica', 'useLocale': { 'cc': 'lamerica', 'll': 'en' } },
			{ 'cc': 'mx', 'useLocale': { 'cc': 'mx', 'll': 'es' } },
			{ 'cc': 'my', 'useLocale': { 'cc': 'my', 'll': 'en' } },
			//{ 'cc': 'nl', 'useLocale': { 'cc': 'nl', 'll': 'en' } },
			{ 'cc': 'nl', 'useLocale': { 'cc': 'nl', 'll': 'nl' } },
			{ 'cc': 'no', 'useLocale': { 'cc': 'no', 'll': 'en' } },
			{ 'cc': 'nz', 'useLocale': { 'cc': 'nz', 'll': 'en' } },
			{ 'cc': 'pl', 'useLocale': { 'cc': 'pl', 'll': 'en' } },
			{ 'cc': 'pt', 'useLocale': { 'cc': 'pt', 'll': 'en' } },
			{ 'cc': 'ru', 'useLocale': { 'cc': 'ru', 'll': 'ru' } },
			//{ 'cc': 'se', 'useLocale': { 'cc': 'se', 'll': 'en' } },
			{ 'cc': 'se', 'useLocale': { 'cc': 'se', 'll': 'sv' } },
			{ 'cc': 'sg', 'useLocale': { 'cc': 'sg', 'll': 'en' } },
			//{ 'cc': 'tr', 'useLocale': { 'cc': 'tr', 'll': 'en' } },
			{ 'cc': 'tr', 'useLocale': { 'cc': 'tr', 'll': 'tr' } },
			//{ 'cc': 'tw', 'useLocale': { 'cc': 'tw', 'll': 'en' } },
			{ 'cc': 'tw', 'useLocale': { 'cc': 'tw', 'll': 'zh' } },
			{ 'cc': 'uk', 'useLocale': { 'cc': 'uk', 'll': 'en' } },
			{ 'cc': 'gb', 'useLocale': { 'cc': 'uk', 'll': 'en' } },
			{ 'cc': 'us', 'useLocale': { 'cc': 'us', 'll': 'en' } },
			{ 'cc': 'za', 'useLocale': { 'cc': 'za', 'll': 'en' } }
		],

		/* languageToLocaleMap can be used to find out what banner supported locale to use, if we could detect only the language, or we detected cc and ll not on supported list */
		'languageToLocaleMap': [
			{ 'll': 'zh', 'useLocale': { 'cc': 'cn', 'll': 'zh' } },
			{ 'll': 'it', 'useLocale': { 'cc': 'it', 'll': 'it' } },
			{ 'll': 'ja', 'useLocale': { 'cc': 'jp', 'll': 'ja' } },
			{ 'll': 'ko', 'useLocale': { 'cc': 'kr', 'll': 'ko' } },
			{ 'll': 'ru', 'useLocale': { 'cc': 'ru', 'll': 'ru' } }
		],

		/* Below is HTML template for alert banner */
		'template': '<div id="hpealertcomp"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg><div class="hpealertcomp_main_text hpealertcomp_main_text_font"><span>____alert_message____</span></div><a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a></div></div>',

		/* CSS for banner */
		'css_font': '@font-face{font-family:MetricReg;src:url(https://h50007.www5.hpe.com/caas-static/fonts/metric/latin-e-regular-woff.woff) format("woff")} @font-face{font-family:MetricBold;src:url(https://h50007.www5.hpe.com/hfws-static/fonts/metric-hpe/MetricHPE-Web-Bold.woff) format("woff");font-weight:700} @font-face{font-family:MetricSemibold;src:url(https://h50007.www5.hpe.com/caas-static/fonts/metric/latin-e-semibold-woff.woff) format("woff");font-weight:600} @font-face{font-family:MetricLight;src:url(https://h50007.www5.hpe.com/caas-static/fonts/metric/latin-e-light-woff.woff) format("woff");font-weight:100}',
		'css': ' #hpealertcomp_container { background-color: #425563; border-bottom: 2px solid #2bc5bd; } #hpealertcomp { display: flex; position: relative; left: 0px; top: 0px; width: 100%; max-width: 1530px; margin: 0px auto; padding: 15px 0px 15px 0px; } #hpealertcomp .hpealertcomp_main_text { display: block; float: left; width: 100%; color: #fff; font-size: 17px; line-height: 18px; margin: 0px 0px 0px 64px; } #hpealertcomp .hpealertcomp_main_text_font { font-family: MetricReg,"Metric Regular",HPEMetricRegular,Arial,sans-serif !important; } #hpealertcomp .hpealertcomp_main_text_font_ja { font-family: AxisProN-Regular,Arial,sans-serif; font-size: 15px; line-height: 22px; } #hpealertcomp .hpealertcomp_main_text_font_ko { font-family: "YDGothic_120 Pro",Arial,sans-serif; } #hpealertcomp .hpealertcomp_main_text_font_ru { font-family: "Arial Narrow",Arial,sans-serif; } #hpealertcomp .hpealertcomp_main_text a { color: #fff; text-decoration: underline; } #hpealertcomp .hpealertcomp_main_text a:hover { color: #fff; text-decoration: none; } #hpealertcomp .hpealertcomp_main_text a:after { color: #fff; text-decoration: none; } #hpealertcomp .hpealertcomp_close { display: flex; display: -ms-grid; height: auto; float: right; margin: auto 64px auto 60px; } #hpealertcomp .hpealertcomp_close .icon { width: 20px; height: 20px; } @media only screen and (max-width: 991px) { #hpealertcomp .hpealertcomp_main_text { font-size: 16px; line-height: 17px; } #hpealertcomp .hpealertcomp_main_text_font_ja { font-family: AxisProN-Regular,Arial,sans-serif; font-size: 14px; line-height: 20px; } } @media only screen and (max-width: 767px) { #hpealertcomp { display: inline-block; } #hpealertcomp .hpealertcomp_main_text { position: relative; left: inherit; width: auto; width: -webkit-fill-available; width: -moz-fit-content; height: content; margin: 0 50px 0 15px; font-size: 15px; line-height: 16px; } #hpealertcomp .hpealertcomp_close { position: absolute; top: 15px; right: 0px; margin: 0px 15px 0px 0px; color: #fff; } } @media only screen and (max-width: 400px) { #hpealertcomp { display: flow-root; } #hpealertcomp .hpealertcomp_main_text { position: relative; left: inherit; width: auto; width: -webkit-fill-available; width: -moz-fit-content; height: content; margin: 0 50px 0 15px; } #hpealertcomp .hpealertcomp_close { position: absolute; top: 15px; right: 0px; margin: 0px 15px 0px 0px; } } /* Flex Banner Styles Start */ #hpealertcomp.has-flex-banner {display: flex!important; margin: 0!important;height: 55px;justify-content: center; background-color: #01a982; max-width: unset!important;} #hpealertcomp .flex-banner{ max-width: 1800px; display:flex; flex-direction:row; justify-content:space-between; align-items:center; flex-basis:100%; padding:0 100px;}#hpealertcomp .flex-banner .flex-banner-section{font-family:MetricLight,"Metric Light",HPEMetricLight,Arial,sans-serif!important;color:#fff;font-size:18px;display:flex-inline;flex-direction:row;align-items:center;}#hpealertcomp .flex-banner .flex-banner-section span{padding-right:15px;}#hpealertcomp .flex-banner .flex-banner-section b{margin:0 4px;font-family:"Metric Semibold",MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif!important;}#hpealertcomp .flex-banner .flex-banner-section a{display:inline-flex;color:#fff;font-family:"Metric Semibold",MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif; text-decoration: underline !important;}#hpealertcomp .flex-banner .flex-banner-section .banner-pipe{display:inline-flex;width:30px;align-items:center;justify-content:center;}#hpealertcomp .flex-banner .flex-banner-section:last-child{align-items:flex-end;padding-left:20px;}#hpealertcomp .flex-banner .hpealertcomp_close{margin:0!important;position:unset!important;top:unset!important;width:17px;height:17px;}@media only screen and (max-width:1199px){#hpealertcomp .flex-banner{padding:0 80px;}}@media only screen and (max-width:991px){#hpealertcomp .flex-banner{padding:0 50px;}}@media only screen and (max-width:767px){#hpealertcomp .flex-banner{flex-basis:100%;padding:0 20px}#hpealertcomp .flex-banner .flex-banner-section{font-size:16px;line-height:15px!important}#hpealertcomp .flex-banner .flex-banner-section span{padding-right:5px}#hpealertcomp .flex-banner .flex-banner-section b{margin:0 2px}#hpealertcomp .flex-banner .flex-banner-section .banner-pipe{width:14px;}}',

		/* Below we're storing translations for alert banner */
		'translation': {
			'en': {
				'alert_message': 'HPE stands firm against racism and is committed to unconditional inclusion. We have a responsibility to shape a world that is equal for all people. Please <a href="https://www.hpe.com/us/en/newsroom/blog-post/2020/06/hpe-ceo-antonio-neri-building-a-more-equitable-inclusive-world-starts-here.html" target="_blank">read the letter our CEO sent to team members</a>.',
				'close': 'close',
				},
			'de': {
				'alert_message': '<strong>HPE REAGIERT AUF COVID-19</strong><br/>Die Sicherheit und Gesundheit unserer Mitarbeiter und Kunden liegt uns am Herzen. Daher haben wir weltweit bis Ende April 2020 die meisten Veranstaltungen abgesagt oder verschoben, die HPE allein oder gemeinsam mit anderen ausrichtet oder die von HPE gesponsert werden. Nach dem jetztigen Stand wird die HPE Discover 2020 wie geplant vom 23. bis 25. Juni 2020 in Las Vegas stattfinden.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">Vollst&#xE4;ndige Mitteilung zum Umgang von HPE mit COVID-19 lesen</a>.',
				'close': 'Schlie&szlig;en',
				},
			'es': {
				'alert_message': '<strong>HPE RESPONDE AL COVID-19</strong><br/>Nos preocupa enormemente la seguridad y la salud de nuestros empleados y clientes. Por ello, hemos cancelado o pospuesto la mayor&#xED;a de los eventos internacionales organizados, copatrocinados o patrocinados por HPE durante abril de 2020. En este momento, HPE Discover Las Vegas se realizar&#xE1; seg&#xFA;n lo previsto del 23 al 25 de junio de 2020.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">Leer el documento completo &#xAB;Respuesta de HPE al COVID-19</a>.',
				'close': 'Cerrar',
				},
			'fr': {
				'alert_message': '<strong>R&#xC9;PONSE DE HPE AU COVID-19</strong><br/>Nous sommes particuli&#xE8;rement attentifs &#xE0; la s&#xE9;curit&#xE9; et &#xE0; la sant&#xE9; de nos employ&#xE9;s et clients. &#xC0; cet effet, nous avons annul&#xE9;s ou report&#xE9; la plupart des &#xE9;v&#xE9;nements organis&#xE9;s, co-organis&#xE9;s ou sponsoris&#xE9;s par HPE dans le monde entier, jusqu&#x27;en avril 2020. &#xC0; l&#x27;heure actuelle, HPE Discover 2020 est maintenu comme pr&#xE9;vu initialement &#xE0; Las Vegas, du 23 au 25 juin 2020.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">Lire l&#x2019;int&#xE9;gralit&#xE9; de la r&#xE9;ponse de HPE au COVID-19</a>.',
				'close': 'Fermer',
				},
			'it': {
				'alert_message': '<strong>PROVVEDIMENTI ADOTTATI DA HPE IN RISPOSTA AL COVID-19</strong><br/>Abbiamo a cuore la sicurezza e la salute dei nostri dipendenti e dei nostri clienti. Per questo motivo, abbiamo cancellato o posticipato la maggior parte degli eventi HPE organizzati, co-organizzati o sponsorizzati da HPE fino ad aprile 2020 in tutto il mondo. Al momento riteniamo che HPE Discover 2020 si svolger&#xE0; come previsto dal 23 al 25 giugno 2020 a Las Vegas.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">Leggi i provvedimenti adottati da HPE in risposta al COVID-19</a>.',
				'close': 'Chiudi',
				},
			'ja': {
				'alert_message': '<strong>HPE&#x306B;&#x304A;&#x3051;&#x308B;&#x65B0;&#x578B;&#x30B3;&#x30ED;&#x30CA;&#x30A6;&#x30A4;&#x30EB;&#x30B9;&#x611F;&#x67D3;&#x75C7; (COVID-19) &#x3078;&#x306E;&#x5BFE;&#x5FDC;</strong><br/>HPE&#x3067;&#x306F;&#x3001;&#x304A;&#x5BA2;&#x69D8;&#x3068;&#x5F93;&#x696D;&#x54E1;&#x306E;&#x5B89;&#x5168;&#x3068;&#x5065;&#x5EB7;&#x3092;&#x7B2C;&#x4E00;&#x306B;&#x8003;&#x3048;&#x3001;2020&#x5E74;4&#x6708;&#x672B;&#x307E;&#x3067;&#x3001;&#x5F53;&#x793E;&#x304C;&#x5168;&#x4E16;&#x754C;&#x3067;&#x4E3B;&#x50AC;&#x3001;&#x5171;&#x50AC;&#x3001;&#x307E;&#x305F;&#x306F;&#x5F8C;&#x63F4;&#x3059;&#x308B;&#x5927;&#x591A;&#x6570;&#x306E;&#x96C6;&#x5408;&#x578B;&#x30A4;&#x30D9;&#x30F3;&#x30C8;&#x306E;&#x958B;&#x50AC;&#x3092;&#x4E2D;&#x6B62;&#x307E;&#x305F;&#x306F;&#x5EF6;&#x671F;&#x3059;&#x308B;&#x3053;&#x3068;&#x3092;&#x6C7A;&#x5B9A;&#x3057;&#x307E;&#x3057;&#x305F;&#x3002;&#x306A;&#x304A;&#x3001;&#x73FE;&#x6642;&#x70B9;&#x3067;&#x306F;&#x3001;HPE Discover 2020&#x306F;&#x4E88;&#x5B9A;&#x3069;&#x304A;&#x308A;&#x30E9;&#x30B9;&#x30D9;&#x30AC;&#x30B9;&#x306B;&#x3066;2020&#x5E74;6&#x6708;23&#x65E5;&#x3088;&#x308A;25&#x65E5;&#x307E;&#x3067;&#x958B;&#x50AC;&#x3055;&#x308C;&#x307E;&#x3059;&#x3002;<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">HPE&#x306B;&#x304A;&#x3051;&#x308B;COVID-19&#x3078;&#x306E;&#x5BFE;&#x5FDC; (&#x5168;&#x6587;) &#x3092;&#x8AAD;&#x3080;</a>.',
				'close': '&#x9589;&#x3058;&#x308B;',
				},
			'ko': {
				'alert_message': '<strong>HPE&#xC758; COVID-19 &#xB300;&#xC751;</strong><br/>HPE&#xB294; HPE &#xC9C1;&#xC6D0;&#xACFC; &#xACE0;&#xAC1D;&#xC758; &#xC548;&#xC804;&#xACFC; &#xAC74;&#xAC15;&#xC744; &#xAC00;&#xC7A5; &#xC6B0;&#xC120;&#xC2DC;&#xD569;&#xB2C8;&#xB2E4;. &#xADF8;&#xC5D0; &#xB530;&#xB77C; HPE&#xB294; &#xC804; &#xC138;&#xACC4;&#xC801;&#xC73C;&#xB85C; 2020&#xB144; 4&#xC6D4;&#xAE4C;&#xC9C0; HPE&#xAC00; &#xC8FC;&#xCD5C;, &#xACF5;&#xB3D9; &#xC8FC;&#xCD5C; &#xB610;&#xB294; &#xD6C4;&#xC6D0;&#xD558;&#xB294; &#xB300;&#xBD80;&#xBD84;&#xC758; &#xC774;&#xBCA4;&#xD2B8;&#xB97C; &#xCDE8;&#xC18C; &#xB610;&#xB294; &#xC5F0;&#xAE30;&#xD569;&#xB2C8;&#xB2E4;. &#xD604;&#xC7AC;&#xB85C;&#xC11C;&#xB294; HPE Discover 2020&#xC740; &#xACC4;&#xD68D;&#xB300;&#xB85C; 2020&#xB144; 6&#xC6D4; 23&#xC77C;&#xBD80;&#xD130; 25&#xC77C;&#xAE4C;&#xC9C0; &#xB77C;&#xC2A4;&#xBCA0;&#xAC00;&#xC2A4;&#xC5D0;&#xC11C; &#xAC1C;&#xCD5C;&#xB429;&#xB2C8;&#xB2E4;.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">HPE&#xC758; COVID-19 &#xB300;&#xC751; &#xC804;&#xCCB4; &#xC77D;&#xAE30;</a>.',
				'close': '&#xB2EB;&#xAE30;',
				},
			'pt': {
				'alert_message': '<strong>A HPE RESPONDE AO COVID-19</strong><br/>N&#xF3;s nos precupamos profundamente com a seguran&#xE7;a e a sa&#xFA;de dos nossos funcion&#xE1;rios e clientes. Assim, cancelamos ou adiamos a maioria dos eventos promovidos, copromovidos ou patrocinados pela HPE em abril de 2020, no mundo todo No presente momento, a HPE Discover 2020 est&#xE1; mantida para Las Vegas, EUA, de 23 a 25 de junho de 2020.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">Leia a resposta da HPE ao COVID-19 na &#xED;ntegra</a>.',
				'close': 'Fechar',
				},
			'ru': {
				'alert_message': '<strong>&#x420;&#x415;&#x410;&#x41A;&#x426;&#x418;&#x42F; HPE &#x41D;&#x410; &#x423;&#x413;&#x420;&#x41E;&#x417;&#x423; COVID-19</strong><br/>&#x41C;&#x44B; &#x437;&#x430;&#x431;&#x43E;&#x442;&#x438;&#x43C;&#x441;&#x44F; &#x43E; &#x437;&#x434;&#x43E;&#x440;&#x43E;&#x432;&#x44C;&#x435; &#x438; &#x431;&#x435;&#x437;&#x43E;&#x43F;&#x430;&#x441;&#x43D;&#x43E;&#x441;&#x442;&#x438; &#x43D;&#x430;&#x448;&#x438;&#x445; &#x441;&#x43E;&#x442;&#x440;&#x443;&#x434;&#x43D;&#x438;&#x43A;&#x43E;&#x432; &#x438; &#x43A;&#x43B;&#x438;&#x435;&#x43D;&#x442;&#x43E;&#x432;. &#x41F;&#x43E;&#x44D;&#x442;&#x43E;&#x43C;&#x443; &#x43C;&#x44B; &#x440;&#x435;&#x448;&#x438;&#x43B;&#x438; &#x43E;&#x442;&#x43C;&#x435;&#x43D;&#x438;&#x442;&#x44C; &#x438;&#x43B;&#x438; &#x43E;&#x442;&#x43B;&#x43E;&#x436;&#x438;&#x442;&#x44C; &#x431;&#x43E;&#x43B;&#x44C;&#x448;&#x438;&#x43D;&#x441;&#x442;&#x432;&#x43E; &#x43C;&#x435;&#x440;&#x43E;&#x43F;&#x440;&#x438;&#x44F;&#x442;&#x438;&#x439; &#x432;&#x43E; &#x432;&#x441;&#x435;&#x43C; &#x43C;&#x438;&#x440;&#x435;, &#x432; &#x43A;&#x43E;&#x442;&#x43E;&#x440;&#x44B;&#x445; &#x43A;&#x43E;&#x43C;&#x43F;&#x430;&#x43D;&#x438;&#x44F; HPE &#x44F;&#x432;&#x43B;&#x44F;&#x435;&#x442;&#x441;&#x44F; &#x43E;&#x440;&#x433;&#x430;&#x43D;&#x438;&#x437;&#x430;&#x442;&#x43E;&#x440;&#x43E;&#x43C; &#x438;&#x43B;&#x438; &#x441;&#x43F;&#x43E;&#x43D;&#x441;&#x43E;&#x440;&#x43E;&#x43C;, &#x437;&#x430;&#x43F;&#x43B;&#x430;&#x43D;&#x438;&#x440;&#x43E;&#x432;&#x430;&#x43D;&#x43D;&#x44B;&#x435; &#x432;&#x43F;&#x43B;&#x43E;&#x442;&#x44C; &#x434;&#x43E; &#x430;&#x43F;&#x440;&#x435;&#x43B;&#x44F; 2020 &#x433;. &#x412; &#x442;&#x43E; &#x436;&#x435; &#x432;&#x440;&#x435;&#x43C;&#x44F; &#x432;&#x44B;&#x441;&#x442;&#x430;&#x432;&#x43A;&#x430; HPE Discover 2020 &#x441;&#x43E;&#x441;&#x442;&#x43E;&#x438;&#x442;&#x441;&#x44F; &#x432; &#x437;&#x430;&#x43F;&#x43B;&#x430;&#x43D;&#x438;&#x440;&#x43E;&#x432;&#x430;&#x43D;&#x43D;&#x44B;&#x435; &#x441;&#x440;&#x43E;&#x43A;&#x438; &#x432; &#x41B;&#x430;&#x441;-&#x412;&#x435;&#x433;&#x430;&#x441;&#x435; &#x441; 23 &#x43F;&#x43E; 25 &#x438;&#x44E;&#x43D;&#x44F; 2020 &#x433;.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">&#x427;&#x438;&#x442;&#x430;&#x442;&#x44C; &#x43F;&#x43E;&#x43B;&#x43D;&#x44B;&#x439; &#x442;&#x435;&#x43A;&#x441;&#x442; &#x441;&#x43E;&#x43E;&#x431;&#x449;&#x435;&#x43D;&#x438;&#x44F; HPE &#x432; &#x441;&#x432;&#x44F;&#x437;&#x438; &#x441; COVID-19</a>.',
				'close': '&Zcy;&acy;&kcy;&rcy;&ycy;&tcy;&softcy;',
				},
			'zh': {
				'alert_message': '<strong>&#x6167;&#x4E0E;&#x5E94;&#x5BF9;&#x65B0;&#x578B;&#x51A0;&#x72B6;&#x75C5;&#x6BD2;&#x80BA;&#x708E; (COVID-19) &#x75AB;&#x60C5;</strong><br/>&#x6211;&#x4EEC;&#x59CB;&#x7EC8;&#x9AD8;&#x5EA6;&#x91CD;&#x89C6;&#x5458;&#x5DE5;&#x548C;&#x5BA2;&#x6237;&#x7684;&#x5B89;&#x5168;&#x5065;&#x5EB7;&#x3002;&#x4E3A;&#x6B64;&#xFF0C;&#x6211;&#x4EEC;&#x5DF2;&#x53D6;&#x6D88;&#x6216;&#x63A8;&#x8FDF;&#x4E86; 2020 &#x5E74; 4 &#x6708;&#x524D;&#x6167;&#x4E0E;&#x4E3E;&#x529E;&#x3001;&#x5171;&#x540C;&#x4E3B;&#x529E;&#x6216;&#x8D5E;&#x52A9;&#x7684;&#x5927;&#x90E8;&#x5206;&#x6D3B;&#x52A8;&#x3002;&#x76EE;&#x524D;&#xFF0C;2020 &#x5E74; HPE Discover &#x5927;&#x4F1A;&#x5C06;&#x4E8E; 2020 &#x5E74; 6 &#x6708; 23 &#x65E5;&#x81F3; 25 &#x65E5;&#x5982;&#x671F;&#x5728;&#x62C9;&#x65AF;&#x7EF4;&#x52A0;&#x65AF;&#x4E3E;&#x884C;&#x3002;<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">&#x9605;&#x8BFB;&#x6574;&#x4E2A;&#x6167;&#x4E0E;&#x516C;&#x53F8;&#x65B0;&#x51A0;&#x75C5;&#x6BD2;&#x80BA;&#x708E; (COVID-19) &#x75AB;&#x60C5;&#x54CD;&#x5E94;</a>.',
				'close': '&#x95DC;&#x9589;',
				},
			'nl': {
				'alert_message': '<strong>HPE REAGEERT OP COVID-19</strong><br/>Voor ons is de veiligheid en gezondheid van onze medewerkers en klanten ontzettend belangrijk. Daarom hebben we de meeste evenementen die HPE in april 2020 wereldwijd organiseert, mede organiseert of sponsort geannuleerd of uitgesteld. Voorlopig vindt HPE Discover 2020 plaats zoals gepland, van 23 tot 25 juni in Las Vegas.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">Lees de volledige reactie van HPE op COVID-19</a>.',
				'close': 'close',
				},
			'sv': {
				'alert_message': '<strong>HPE SVARAR G&#xC4;LLANDE COVID-19</strong><br/>Vi bryr oss mycket om v&#xE5;ra anst&#xE4;lldas och kunders s&#xE4;kerhet och h&#xE4;lsa. P&#xE5; grund av detta har vi avbrutit eller skjutit upp de flesta evenemang d&#xE4;r HPE &#xE4;r v&#xE4;rd, assisterande v&#xE4;rd eller sponsrar till och med april 2020 &#xF6;ver hela v&#xE4;rlden. F&#xF6;r n&#xE4;rvarande &#xE4;ger HPE Discover 2020 rum precis som planerat i Las Vegas 23&#x2013;25 juni 2020.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">L&#xE4;s hela svaret g&#xE4;llande HPE COVID-19</a>.',
				'close': 'close',
				},
			'tr': {
				'alert_message': '<strong>HPE, COVID-19&#x27;A M&#xDC;DAHALE ED&#x130;YOR</strong><br/>&#xC7;al&#x131;&#x15F;anlar&#x131;m&#x131;z ve m&#xFC;&#x15F;terilerimizin g&#xFC;venli&#x11F;i ve sa&#x11F;l&#x131;&#x11F;&#x131;na &#xE7;ok &#xF6;nem veririz. Bu ama&#xE7;la t&#xFC;m d&#xFC;nyada Nisan 2020 boyunca HPE&#x27;nin tek ba&#x15F;&#x131;na ya da ba&#x15F;ka bir kurulu&#x15F;la ortak &#x15F;ekilde ev sahipli&#x11F;i yapt&#x131;&#x11F;&#x131; veya sponsorluk yapt&#x131;&#x11F;&#x131; &#xE7;o&#x11F;u etkinli&#x11F;i iptal ettik veya erteledik. Di&#x11F;er yandan HPE Discover 2020, planland&#x131;&#x11F;&#x131; gibi 23-25 Haziran 2020&#x27;de Las Vegas&#x27;ta ger&#xE7;ekle&#x15F;tirilecek.<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">T&#xFC;m HPE COVID-19 m&#xFC;dahalesini okuyun</a>.',
				'close': 'close',
				},
			'zh-tw': {
				'alert_message': '<strong>&#x6167;&#x8207;&#x91DD;&#x5C0D;&#x65B0;&#x578B;&#x51A0;&#x72C0;&#x75C5;&#x6BD2; (COVID-19) &#x505A;&#x51FA;&#x56DE;&#x61C9;</strong><br/>&#x6211;&#x5011;&#x975E;&#x5E38;&#x91CD;&#x8996;&#x6167;&#x8207;&#x54E1;&#x5DE5;&#x53CA;&#x5BA2;&#x6236;&#x7684;&#x5065;&#x5EB7;&#x8207;&#x751F;&#x547D;&#x5B89;&#x5168;&#x3002;&#x70BA;&#x6B64;&#xFF0C;&#x6211;&#x5011;&#x53D6;&#x6D88;&#x6216;&#x63A8;&#x9072;&#x4E86; 2020 &#x5E74; 4 &#x6708;&#x4E4B;&#x524D;&#x7531;&#x6167;&#x8207;&#x8209;&#x8FA6;&#x3001;&#x806F;&#x5408;&#x8209;&#x8FA6;&#x6216;&#x8D0A;&#x52A9;&#x7684;&#x5927;&#x591A;&#x6578;&#x5168;&#x7403;&#x6D3B;&#x52D5;&#x3002;HPE Discover 2020 &#x5927;&#x6703;&#x76EE;&#x524D;&#x4ECD;&#x6309;&#x8A08;&#x5283;&#x5728;&#x62C9;&#x65AF;&#x7DAD;&#x52A0;&#x65AF;&#x8209;&#x884C;&#xFF0C;&#x6642;&#x9593;&#x70BA; 2020 &#x5E74; 6 &#x6708; 23 &#x81F3; 25 &#x65E5;&#x3002;<br/> <a href="https://www.hpe.com/____cc____/____ll____/about/alerts.html">&#x95B1;&#x8B80;&#x6167;&#x8207;&#x91DD;&#x5C0D;&#x65B0;&#x578B;&#x51A0;&#x72C0;&#x75C5;&#x6BD2; (COVID-19) &#x7684;&#x5B8C;&#x6574;&#x56DE;&#x61C9;</a>.',
				'close': 'close',
				}
			}
	};


	/*
	 * HPE Alert Banner object
	 */
	HPEALERTBANNER = {
		cfg: null,
		cc: null,
		ll: null,
		bannerCssInserted: false,
		bannerHtmlInserted: false,
		bannerVisible: false,
		cookieDomain: '',
		bannerEventPrefix: 'HPEALERTBANNER.',
		bannerReadyEvent: null,
		bannerOpenEvent: null,
		bannerCloseEvent: null,
		bannerHTMLContainter: 'hpealertcomp_container',
		bannerHTMLClose: 'hpealertcomp_close',
		bannerAnswerCookie: 'hpealert_answ_flexfabric',
		bannerCookieLifeDays: 115, /* Due Russian Alert Banner, extending cookie expiration until end of September, 2022  */
		countdownBannerFinished: false, // Determines if the banners with countdown functionality have finished their count or not

		/*
		 * isNoRadioButtonsTemplate(): - for Alert Banner it returns always true - so we could reuse privacy cookie banner save and close method
		 */
		isNoRadioButtonsTemplate: function() {
			return true;
		},


		/*
		 * renderBannerHTML() - renders and returns banner html localized for this.cc country and this.ll language
		 */
		renderBannerHTML: function() {
			var tmpHtml = this.cfg.template;

			/* go through all translation keys defined for language, and replace them in the template */
			for(var key in this.cfg.translation[this.ll]) {
				tmpHtml = tmpHtml.replace('____' + key + '____', this.cfg.translation[this.ll][key]);
			}

			/* render the cc and ll codes appearing in resulting html */
			tmpHtml = tmpHtml.replace('____cc____', this.cc);
			tmpHtml = tmpHtml.replace('____ll____', this.ll);

			/* change the font class for locales that use different fonts */
			if (this.ll === 'ja') {
				tmpHtml = tmpHtml.replace('hpealertcomp_main_text_font', 'hpealertcomp_main_text_font_ja');
			}
			if (this.ll === 'ko') {
				tmpHtml = tmpHtml.replace('hpealertcomp_main_text_font', 'hpealertcomp_main_text_font_ko');
			}
			if (this.ll === 'ru') {
				tmpHtml = tmpHtml.replace('hpealertcomp_main_text_font', 'hpealertcomp_main_text_font_ru');
			}

			return tmpHtml;
		},


		/*
		 * detectLocale() - tries to detect page or user locale using different methods.
		 *
		 * Returns detected locale information, or null, if unable to find locale.
		 */
		detectLocale: function() {
			var tmpLoc = null;

			if ( (tmpLoc = this.detectLocaleFromURL() ) != null ) {
				this.log('HPE Alert Locale detected from URL: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			if ( (tmpLoc = this.detectLocaleFromHtmlLang() ) != null ) {
				this.log('HPE Alert Locale detected from HTML lang: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			if ( (tmpLoc = this.detectLocaleFromMeta() ) != null ) {
				this.log('HPE Alert Locale detected from target_country meta: ' + tmpLoc.cc + '/' + tmpLoc.ll);
				return tmpLoc;
			}

			/* TODO: implement methods detecting from:
				- locale cookies (cc and lang - AEM is fixed and uses cc and lang cookies now as well)
				- browser locale
			*/

			return null;
		},


		/*
		 * showBanner() - shows alert banner on the page, if not shown already
		 */
		showBanner: function() {
			if (!this.isBannerVisible()) {
				var self = this;

				this.bannerVisible = true;

				/* insert banner CSS and HTML */
				this.insertBannerCSS();
				this.insertBannerHTML();

				/* add the close and save answer event for the alert banner */
				document.getElementById(this.bannerHTMLClose).onclick = function(event) {
					event.preventDefault();
					self.saveAndCloseBanner();
				};

				this.dispatchBannerEvent('OPEN');
			}
		},


		eventPadNumber: function(number) {
			if (number < 10) {
				return '0' + number;
			}
			else {
				return number;
			}
		},


		/*
		 * setEventTimeLeft() - returns time left between now and date object given as param, in the format of DD:HH:MM:SS.
		 */
		setEventTimeLeft: function(dateFuture) {
			var dateNow = new Date();
			var seconds = Math.floor((dateFuture - (dateNow))/1000);
			var minutes = Math.floor(seconds/60);
			var hours = Math.floor(minutes/60);
			var days = Math.floor(hours/24);

			hours = hours-(days*24);
			minutes = minutes-(days*24*60)-(hours*60);
			seconds = seconds-(days*24*60*60)-(hours*60*60)-(minutes*60);

			// Checks if event is here, show countdown if there are seconds left, otherwise, show Join Now:
			if(!this.isEventTime(dateFuture)){
				return this.eventPadNumber(days) + ":" + this.eventPadNumber(hours) + ":" + this.eventPadNumber(minutes) + ":" + this.eventPadNumber(seconds);
			} else {
				clearInterval(document.countdownToEvent); // Clear interval that checks for time to event every second.

				var cookieNameForAttend = this.bannerAnswerCookie+"_attend"; // Here we get current cookie name
				this.bannerAnswerCookie = cookieNameForAttend; // Here we convert current cookiename into thesame + "_attend";
				this.countdownBannerFinished = true;
				this.showTimeOutBannerByCookie();

				return "";
			}
		},


		/* Show Banner message for timeout event by cookie name */
		showTimeOutBannerByCookie: function(){
			var self = this;
			if(!self.isBannerAnswered()){
				// This switch case is intended to provide support for more that one banner (case) at time.
				// This function is triggered after countdown is over.
				switch(self.bannerAnswerCookie){
					case 'hpealert_answ_discover21_attend':
						self.saveAndCloseBanner();
						// What to show when the time is over:
						/*
						self.cfg.translation = {
							"en" : {
								"TXT_JOIN_BEFORE" : "",
								"TXT_JOIN_BOLD"   : "THE EDGE-TO-CLOUD CONFERENCE IS LIVE",
								"TXT_JOIN_AFTER"  : "",
								"BUTTON_TXT"      : "Watch now",
								"BUTTON_LINK"     : "",
								'close'           : 'close'
							},
						};
						self.cfg.template = '<div id="hpealertcomp"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg><div class="hpealertcomp_main_text hpealertcomp_main_text_font"><span>';
							self.cfg.template += '<div id="discover-banner-holder">';
								self.cfg.template += '<div class="db-l-side">____TXT_JOIN_BEFORE____<span class="discover-virtual-exp">____TXT_JOIN_BOLD____</span><span>____TXT_JOIN_AFTER____</span></div>';
								self.cfg.template += '<div class="db-r-side"><a class="discover-reg-button" href="____BUTTON_LINK____">____BUTTON_TXT____</a></div>';
							self.cfg.template += '</div>';
						self.cfg.template += '</span></div><a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a></div></div>';

						if(self.countdownBannerFinished === true){
							document.getElementById(self.bannerHTMLContainter).innerHTML = self.renderBannerHTML();
							self.showBanner();
						} else {
							self.showBanner();
						}
						*/
					break;

					case 'hpealert_answ_greenlakeanouncement_attend':
						self.saveAndCloseBanner();
					break;

					case 'hpealert_answ_securityeventoct21_attend':
						self.saveAndCloseBanner();
					break;

					default:
						// Do nothing
					break;
				}
			}
		},

		/* Check if eVENT is happening now */
		isEventTime: function(dateFuture){
			var dateNow = new Date();
			// Get seconds diff between dates:
			var diff 	= Math.floor((dateFuture.getTime() - dateNow.getTime()) / 1000);
			// Here we compare against 3600, since it's the number of seconds in 1 hour...they wanted to show "Join Now" message 1 hour before:
			// return (diff > 3600) ? false : true;
			return (diff > 0) ? false : true; // Changed to be exact time
		},


		/*
		 * hideBanner() - removes alert banner from page
		 */
		hideBanner: function() {
			/* TODO: perhaps do some small animation, and then remove from page? */
			var bannerContainer = document.getElementById(this.bannerHTMLContainter);
			bannerContainer.parentNode.removeChild(bannerContainer);
			this.bannerHtmlInserted = false;
			this.bannerVisible = false;
			this.dispatchBannerEvent('CLOSE');
		},


		/*
		 * saveAndCloseBanner() - saves info that alert banner was closed, and hides the banner
		 */
		saveAndCloseBanner: function() {
			if (this.isBannerVisible()) {
				this.writeCookie(this.getCookieDomain(), this.bannerAnswerCookie, '1', this.bannerCookieLifeDays);
				this.hideBanner();
			}
			return false;
		},



		/*
			Sep 30, 2020
			This function is an attempt to centralize the way we display different banners.
			The function will detect the value for this.bannerAnswerCookie in order to determine the template,
			the translations and other singularities about each banner.
		*/
		showBannerByCookie: function(){
			var self = this;
			switch(self.bannerAnswerCookie){
				// Feb 16, 2021 => Spaceborne Launch by NASA and HPE
				case 'hpealert_answ_spaceborne':
					var regex =  /(test-pages|\/us\/en\/home\.html|\/us\/en\/compute\/hpc\.html|\/us\/en\/compute\/hpc\/)/gmi;
					if(document.URL.search(regex) !== -1){

						this.insertCSS('#discover-banner-holder{} #discover-banner-holder .db-l-side{float: left; font-size:22px; padding:14px 0px; line-height:26px !important; color: #fff;} #discover-banner-holder .db-l-side #hpe_alert_dsc_time_left{display:inline-block; width: 160px; font-family: \'Metric Semibold\',MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif !important;font-size: 32px;color: #fff;} #discover-banner-holder .db-l-side span{vertical-align:middle; line-height:21px; } #discover-banner-holder .db-l-side .discover-virtual-exp{font-family:\'Metric Semibold\',MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif !important; text-transform:uppercase;color: #fff;font-size: 22px;}  #discover-banner-holder .db-r-side{float: right;} #hpealertcomp_container { background-color: #01A982 !important } #hpealertcomp .hpealertcomp_main_text_font { font-family: MetricLight,"Metric Light",HPEMetricLight,Arial,sans-serif !important } #hpealertcomp { padding: 8px 0px 8px 0px !important;} #hpealertcomp .discover-reg-button{border:2px solid #FFF; color: #fff; text-align:center; padding:10px 0px; margin-top:8px; display:inline-block; width:180px; vertical-align:middle; text-decoration:none !important; font-size:18px; font-family:\'Metric Semibold\',MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif !important;} #hpealertcomp .discover-reg-button:hover{border:4px solid #fff; width:176px; padding:8px 0px;}    @media only screen and (min-width: 401px) and (max-width: 600px){.hpealertcomp_main_text{margin: 0px 15px !important;}#hpe_alert_dsc_time_left{display: block !important;margin: 15px 0px !important;}#discover-banner-holder .db-l-side{padding: 0px !important;font-size: 20px !important;line-height: 18px !important;} #discover-banner-holder .db-l-side .discover-virtual-exp{font-size: 20px !important;line-height: 18px !important;} }@media only screen and (max-width: 400px) {.hpealertcomp_main_text{margin: 0px 15px !important;}#hpe_alert_dsc_time_left{display: block !important;margin: 15px 0px !important;}#discover-banner-holder .db-l-side{padding: 0px !important;font-size: 16px !important;line-height: 14px !important;} #discover-banner-holder .db-l-side .discover-virtual-exp{font-size: 16px !important;line-height: 14px !important;} }');

						// Countries in each region (based on Toolkit):
						var ccInRegion = {
							ams         : ['br','ca','lamerica','mx','us'],
							emea        : ['at','be','ch','cz','de','dk','emea_africa','emea_europe','emea_middle_east','es','fi','fr','ie','il','it','nl','no','pl','pt','ru','za','uk','se','tr','sa','ae'],
							apj         : ['asia_pac','au','cn','hk','in','kr','my','nz','sg','tw','jp']
						};

						// "reg" is set default to "ams"...and next loop determines if it should be overwritten...
						var reg = "ams";
						// Check in wich region "this.cc" is located:
						for(kreg in ccInRegion){
							for(cc in ccInRegion[kreg]){
								if(ccInRegion[kreg][cc] === self.cc){
									reg = kreg;
								}
							}
						}
						reg = "ams"; // Overwrittes to AMS !!!

						var timeZones = {
							"ams" :  new Date("2021-02-20T12:00:00.000-05:00") // Real event start time: 12PM EST, which is UTC
							//"ams" :  new Date("2021-02-19T13:36:00.000-05:00") // Testing
						};
						var eventtime = timeZones[reg];

						// If the translated text doesnt match with this.ll, then we force EN:
						//if(!this.cfg.translation[this.ll]) {
							this.ll = "en"; // Overwrittes to EN !!!
						//}

						// What to show when the datetime is still to happen:
						if(!this.isEventTime(eventtime) && !this.isBannerAnswered()){
							// Defines texts:
							self.cfg.translation = {
								"en" : {
									"TXT_BEFORE" : "",
									"HPEDVE"     : "COUNTDOWN TO SPACEBORNE 2 LAUNCH",
									"TXT_AFTER"  : "",
									"BUTTON_TXT" : "Learn more",
									"BUTTON_LINK": "https://www.hpe.com/ww/sb2launch",
									'close': 'close'
								},
							};

							self.cfg.template = '<div id="hpealertcomp"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg><div class="hpealertcomp_main_text hpealertcomp_main_text_font"><span>';
								self.cfg.template += '<div id="discover-banner-holder">';
									self.cfg.template += '<div class="db-l-side"><span id="hpe_alert_dsc_time_left"></span> <span>____TXT_BEFORE____</span> <span class="discover-virtual-exp">____HPEDVE____</span><span>____TXT_AFTER____</span></div>';
									self.cfg.template += '<div class="db-r-side"><a class="discover-reg-button" href="____BUTTON_LINK____">____BUTTON_TXT____</a></div>';
								self.cfg.template += '</div>';
							self.cfg.template += '</span></div><a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a></div></div>';

							self.showBanner(); // TODO: How to avoid this?
							// There are at least some seconds left until date:
							document.getElementById('hpe_alert_dsc_time_left').innerHTML = self.setEventTimeLeft(eventtime); // Setting initial value immediatelly, so it would not appear after 1 second
							document.countdownToEvent = setInterval(function () {
								if(document.getElementById('hpe_alert_dsc_time_left'))
								document.getElementById('hpe_alert_dsc_time_left').innerHTML=self.setEventTimeLeft(eventtime);
							}, 1000);
						} else {
							if(this.isEventTime(eventtime)){
								self.bannerAnswerCookie = 'hpealert_answ_spaceborne_attend';
								self.showTimeOutBannerByCookie();
							}
						}
					}
				break;

				// Apr 09, 2021 => Request by Darren Strong <darren.w.strong@hpe.com> for "Compute Day"
				case 'hpealert_answ_computeday':
					// Css:
					self.insertCSS('#discover-banner-holder{} #discover-banner-holder .db-l-side{float: left; font-size:20px; padding:14px 0px; line-height:26px !important; color: #fff;} #discover-banner-holder .db-l-side #hpe_alert_dsc_time_left{display:inline-block; width: 160px; font-family: \'Metric Semibold\',MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif !important;font-size: 32px;color: #fff;} #discover-banner-holder .db-l-side span{vertical-align:middle; line-height:21px; } #discover-banner-holder .db-l-side .discover-virtual-exp{font-family:\'Metric Semibold\',MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif !important; text-transform:uppercase;color: #fff;font-size: 22px;}  #discover-banner-holder .db-r-side{float: right;} #hpealertcomp_container { background-color: #01A982 !important } #hpealertcomp .hpealertcomp_main_text_font { font-family: MetricLight,"Metric Light",HPEMetricLight,Arial,sans-serif !important } #hpealertcomp { padding: 8px 0px 8px 0px !important;} #hpealertcomp .discover-reg-button{border:2px solid #FFF; color: #fff; text-align:center; padding:10px 0px; margin-top:8px; display:inline-block; width:180px; vertical-align:middle; text-decoration:none !important; font-size:18px; font-family:\'Metric Semibold\',MetricSemiBold,HPEMetricSemiBold,Arial,sans-serif !important;} #hpealertcomp .discover-reg-button:hover{border:4px solid #fff; width:176px; padding:8px 0px;}    @media only screen and (min-width: 401px) and (max-width: 600px){.hpealertcomp_main_text{margin: 0px 15px !important;}#hpe_alert_dsc_time_left{display: block !important;margin: 15px 0px !important;}#discover-banner-holder .db-l-side{padding: 0px !important;font-size: 20px !important;line-height: 18px !important;} #discover-banner-holder .db-l-side .discover-virtual-exp{font-size: 20px !important;line-height: 18px !important;} }@media only screen and (max-width: 400px) {.hpealertcomp_main_text{margin: 0px 15px !important;}#hpe_alert_dsc_time_left{display: block !important;margin: 15px 0px !important;}#discover-banner-holder .db-l-side{padding: 0px !important;font-size: 16px !important;line-height: 14px !important;} #discover-banner-holder .db-l-side .discover-virtual-exp{font-size: 16px !important;line-height: 14px !important;} }');
					// Defines texts:
					this.cfg.translation = {
						"en" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "Accelerate your transformation from Edge to Exascale. Join Antonio Neri to learn how.",
							"BUTTON_TXT"      : "WATCH NOW",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"de" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "Beschleunigen Sie Ihre Transformation vom Edge zu Exascale.&#xA0; H&#xF6;ren Sie Antonio Neri am 21. April zu diesem Thema zu.",
							"BUTTON_TXT"      : "Jetzt ansehen",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"es" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "Acelere su transformaci&#xF3;n de la periferia a la exaescala.&#xA0; &#xDA;nase a Antonio Neri el 21 de abril y conozca m&#xE1;s.",
							"BUTTON_TXT"      : "Ver ahora",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"it" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "Accelera la trasformazione da edge a exascale.&#xA0; Segui Antonio Neri il 21 aprile per scoprire come.",
							"BUTTON_TXT"      : "Guarda ora",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"ru" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "&#x423;&#x441;&#x43A;&#x43E;&#x440;&#x44C;&#x442;&#x435; &#x43F;&#x440;&#x435;&#x43E;&#x431;&#x440;&#x430;&#x437;&#x43E;&#x432;&#x430;&#x43D;&#x438;&#x44F; &#x43E;&#x442; &#x43F;&#x435;&#x440;&#x438;&#x444;&#x435;&#x440;&#x438;&#x438; &#x434;&#x43E; &#x44D;&#x43A;&#x441;&#x430;&#x444;&#x43B;&#x43E;&#x43F;&#x441;&#x43D;&#x44B;&#x445; &#x43C;&#x430;&#x441;&#x448;&#x442;&#x430;&#x431;&#x43E;&#x432;.&#xA0; &#x41F;&#x440;&#x438;&#x441;&#x43E;&#x435;&#x434;&#x438;&#x43D;&#x44F;&#x439;&#x442;&#x435;&#x441;&#x44C; &#x43A; &#x410;&#x43D;&#x442;&#x43E;&#x43D;&#x438;&#x43E; &#x41D;&#x435;&#x440;&#x438; 21 &#x430;&#x43F;&#x440;&#x435;&#x43B;&#x44F; &#x438; &#x443;&#x437;&#x43D;&#x430;&#x439;&#x442;&#x435;, &#x43A;&#x430;&#x43A;.",
							"BUTTON_TXT"      : "&#x421;&#x43C;&#x43E;&#x442;&#x440;&#x435;&#x442;&#x44C; &#x441;&#x435;&#x439;&#x447;&#x430;&#x441;",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"pt" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "Acelere a sua transforma&#xE7;&#xE3;o da borda para a exaescala.&#xA0; Em 21 de abril, Antonio Neri vai mostrar como.",
							"BUTTON_TXT"      : "Assista agora",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"zh" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "&#x5F9E;&#x908A;&#x7DE3;&#x52A0;&#x901F;&#x9081;&#x5411;&#x767E;&#x842C;&#x5146;&#x7D1A;&#x904B;&#x7B97;&#x7684;&#x8F49;&#x578B;&#x4E4B;&#x8DEF;&#x3002;&#xA0; &#x5728; 4 &#x6708; 21 &#x65E5;&#x8DDF;&#x96A8; Antonio Neri &#x7684;&#x8173;&#x6B65;&#xFF0C;&#x4E00;&#x540C;&#x77AD;&#x89E3;&#x7B87;&#x4E2D;&#x5967;&#x5999;&#x3002;",
							"BUTTON_TXT"      : "&#x7ACB;&#x5373;&#x89C0;&#x770B;",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"ko" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "&#xC5E3;&#xC9C0;&#xC5D0;&#xC11C; &#xC5D1;&#xC0AC;&#xC2A4;&#xCF00;&#xC77C;&#xB85C;&#xC758; &#xC804;&#xD658; &#xAC00;&#xC18D;&#xD654;&#xA0; 4&#xC6D4; 21&#xC77C;&#xC5D0; &#xCC38;&#xC11D;&#xD558;&#xC5EC; Antonio Neri&#xAC00; &#xC804;&#xD558;&#xB294; &#xBC29;&#xBC95;&#xC744; &#xC54C;&#xC544;&#xBCF4;&#xC2ED;&#xC2DC;&#xC624;.",
							"BUTTON_TXT"      : "&#xC9C0;&#xAE08; &#xBCF4;&#xAE30;",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
						"ja" : {
							"TXT_JOIN_BEFORE" : "",
							"TXT_JOIN_BOLD"   : "",
							"TXT_JOIN_AFTER"  : "&#x30A8;&#x30C3;&#x30B8;&#x304B;&#x3089;&#x30A8;&#x30AF;&#x30B5;&#x30B9;&#x30B1;&#x30FC;&#x30EB;&#x307E;&#x3067;&#x30C7;&#x30B8;&#x30BF;&#x30EB;&#x30C8;&#x30E9;&#x30F3;&#x30B9;&#x30D5;&#x30A9;&#x30FC;&#x30E1;&#x30FC;&#x30B7;&#x30E7;&#x30F3;&#x3092;&#x52A0;&#x901F;&#x3059;&#x308B;&#x306B;&#x306F;&#x3002;&#xA0; 4&#x6708;21&#x65E5;&#x3001;Antonio Neri&#x304C;&#x3054;&#x8AAC;&#x660E;&#x3057;&#x307E;&#x3059;&#x3002;&#x305C;&#x3072;&#x3054;&#x53C2;&#x52A0;&#x304F;&#x3060;&#x3055;&#x3044;&#x3002;",
							"BUTTON_TXT"      : "&#x4ECA;&#x3059;&#x3050;&#x8996;&#x8074;",
							"BUTTON_LINK"     : "https://hpe.events.cube365.net/hpe/acceleratingnext",
							'close'           : 'close'
						},
					};
					// HTML Template:
					this.cfg.template = '<div id="hpealertcomp"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg><div class="hpealertcomp_main_text hpealertcomp_main_text_font"><span>';
						this.cfg.template += '<div id="discover-banner-holder">';
							this.cfg.template += '<div class="db-l-side">____TXT_JOIN_BEFORE____<span class="discover-virtual-exp">____TXT_JOIN_BOLD____</span><span>____TXT_JOIN_AFTER____</span></div>';
							this.cfg.template += '<div class="db-r-side"><a class="discover-reg-button" href="____BUTTON_LINK____">____BUTTON_TXT____</a></div>';
						this.cfg.template += '</div>';
					this.cfg.template += '</span></div><a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a></div></div>';

					self.showBanner();
				break;

				// Feb 28 2022, => https://centerpoint.int.hpe.com:8443/browse/XPLAT-173
				case 'hpealert_answ_greenlakemarch2022':
					var bannerMoments = {
						"start" : new Date("2022-03-22T07:30:00.000-07:00"), //new Date("2022-03-21T17:32:00.000-07:00"),  //
						"end" 	: new Date("2022-03-22T09:00:00.000-07:00"), //new Date("2022-03-21T17:32:10.000-07:00"), //
					};
					var regexXPLAT173Includes = /www\.hpe\.com\/.*\/en/gmi; // Include All EN AEM pages
					var regexXPLAT173Psnow = /www\.hpe\.com\/psnow\//gmi; // Include these

					function hideLearnMoreAndPipe(){
						if(document.getElementById('gl-banner-lm')){
							document.getElementById('gl-banner-lm').style.display = 'none';
						}
						if(document.getElementById('gl-banner-pipe')){
							document.getElementById('gl-banner-pipe').style.display = 'none';
						}
					}

					function getBannerConfig(){
						var bannerConfig = {
							'generalText': 'Tune in <b>March 22nd</b> and see why enterprises are embracing a cloud-everywhere strategy with HPE GreenLake.',
							'ctaLink'    : 'https://www.hpe.com/global/assets/Join-us-for-a-special-HPE-GreenLake-announcement-event.ics',
							'ctaText'    : 'Save the date',
							'regexXPLAT173Excludes' : /\/discover-more-network|\/discover|\/greenlake/gmi,
						};

						var addLive = (document.URL.search('greenlake.html') !== -1) ? '#livestream' : '';

						// If the eventStart is still to happen, whe show "before event text":
						if((!self.isEventTime(bannerMoments.start) && !self.isEventTime(bannerMoments.end))){
							console.log('Time until GreenLake event starts', self.setEventTimeLeft(bannerMoments.start));
							// Before ...
						} else if((self.isEventTime(bannerMoments.start) && !self.isEventTime(bannerMoments.end))){
							console.log('Time until GreenLake event ends', self.setEventTimeLeft(bannerMoments.end));
							// During ...
							bannerConfig = {
								'generalText': 'Our next HPE GreenLake Announcement is live. Power your growing business with new cloud services.',
								'ctaLink'    : 'https://www.hpe.com/us/en/discover-more-network/events/hpe-greenlake.html'+addLive,
								'ctaText'    : 'Watch now',
								'regexXPLAT173Excludes' : /\/discover-more-network|\/discover/gmi,
							};
							hideLearnMoreAndPipe();
						} else if((self.isEventTime(bannerMoments.start) && self.isEventTime(bannerMoments.end))){
							console.log('GreenLake has finished');
							// After ...
							bannerConfig = {
								'generalText': 'Watch the recent HPE GreenLake announcement: 12 new cloud services, simplified experience and expanded partner ecosystem.',
								'ctaLink'    : 'https://www.hpe.com/us/en/discover-more-network/events/hpe-greenlake.html'+addLive,
								'ctaText'    : 'Watch now',
								'regexXPLAT173Excludes' : /\/discover-more-network|\/discover/gmi,
							};
							hideLearnMoreAndPipe();
						}

						// Overwrittes with params;
						if(document.URL.search('glbannermoment=before') !== -1){
							bannerConfig = {
								'generalText': 'Tune in <b>March 22nd</b> and see why enterprises are embracing a cloud-everywhere strategy with HPE GreenLake.',
								'ctaLink'    : 'https://www.hpe.com/global/assets/Join-us-for-a-special-HPE-GreenLake-announcement-event.ics',
								'ctaText'    : 'Save the date',
								'regexXPLAT173Excludes' : /\/discover-more-network|\/discover|\/greenlake/gmi,
							};
						}
						if(document.URL.search('glbannermoment=during') !== -1){
							bannerConfig = {
								'generalText': 'Our next HPE GreenLake Announcement is live. Power your growing business with new cloud services.',
								'ctaLink'    : 'https://www.hpe.com/us/en/discover-more-network/events/hpe-greenlake.html'+addLive,
								'ctaText'    : 'Watch now',
								'regexXPLAT173Excludes' : /\/discover-more-network|\/discover/gmi,
							};
							hideLearnMoreAndPipe();
						}
						if(document.URL.search('glbannermoment=after') !== -1){
							bannerConfig = {
								'generalText': 'Watch the recent HPE GreenLake announcement: 12 new cloud services, simplified experience and expanded partner ecosystem.',
								'ctaLink'    : 'https://www.hpe.com/us/en/discover-more-network/events/hpe-greenlake.html'+addLive,
								'ctaText'    : 'Watch now',
								'regexXPLAT173Excludes' : /\/discover-more-network|\/discover/gmi,
							};
							hideLearnMoreAndPipe();
						}

						if(document.getElementById('gl-banner-text') && document.getElementById('gl-banner-cta')){
							document.getElementById('gl-banner-text').innerHTML = bannerConfig.generalText;
							document.getElementById('gl-banner-cta').innerHTML = bannerConfig.ctaText;
							document.getElementById('gl-banner-cta').href = bannerConfig.ctaLink;
						}

						return bannerConfig;
					}

					let bannerConfig = getBannerConfig();

					if(this.ll === 'en' && (document.URL.match(regexXPLAT173Includes) || document.URL.match(regexXPLAT173Psnow)) && !document.URL.match(bannerConfig.regexXPLAT173Excludes)){
						self.cfg.template = '<div id="hpealertcomp" class="has-flex-banner">';
							self.cfg.template += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg>';
							self.cfg.template += '<div class="flex-banner">';
							self.cfg.template += '<div class="flex-banner-section">';
								self.cfg.template += '<span id="gl-banner-text">'+bannerConfig.generalText+'</span>';
								self.cfg.template += '<a id="gl-banner-lm" href="https://www.hpe.com/us/en/discover-more-network/events/hpe-greenlake.html">Learn more</a>';
								self.cfg.template += '<div id="gl-banner-pipe" class="banner-pipe">|</div>';
								self.cfg.template += '<a id="gl-banner-cta" href="'+bannerConfig.ctaLink+'">'+bannerConfig.ctaText+'</a>';
							self.cfg.template += '</div>';
							self.cfg.template += '<div class="flex-banner-section">';
								self.cfg.template += '<a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a>';
							self.cfg.template += '</div>';
							self.cfg.template += '</div>';
						self.cfg.template += '</div>';

						// Interval refresh:
						if(document.countdownToEvent){
							clearInterval(document.countdownToEvent);
						}

						document.countdownToEvent = setInterval(function () {
							let bannerConfig = getBannerConfig();
							if(document.getElementById('gl-banner-text') && document.getElementById('gl-banner-cta')){
								document.getElementById('gl-banner-text').innerHTML = bannerConfig.generalText;
								document.getElementById('gl-banner-cta').innerHTML = bannerConfig.ctaText;
								document.getElementById('gl-banner-cta').href = bannerConfig.ctaLink;
							}
						}, 1000);
					}
				break;

				// March 03 => https://centerpoint.int.hpe.com:8443/browse/XPLAT-152
				case 'hpealert_answ_migrate_sso_2022':
					self.insertCSS('#hpealertcomp.has-flex-banner {background-color: #425563 !important;}');
					// HTML Template:
					this.cfg.template = '<div id="hpealertcomp" class="has-flex-banner">';
						this.cfg.template += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg>';
						this.cfg.template += '<div class="flex-banner">';
						this.cfg.template += '<div class="flex-banner-section">';
							this.cfg.template += '<span>To provide a more seamless experience for our customers, HPE has begun migrating to a Single Sign-On experience for all HPE accounts. HPE MyAccount will use this new sign on experience effective April 21, 2022.</span>';
							this.cfg.template += '<a href="https://www.hpe.com/us/en/sso-learn-more.html">Learn more</a>';
						this.cfg.template += '</div>';
						this.cfg.template += '<div class="flex-banner-section">';
							this.cfg.template += '<a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a>';
						this.cfg.template += '</div>';
						this.cfg.template += '</div>';
					this.cfg.template += '</div>';

					self.showBanner();
				break;

				// April 04, 2022 => https://centerpoint.int.hpe.com:8443/browse/XPLAT-213
				case 'hpealert_answ_flexfabric':
					//self.insertCSS('#hpealertcomp.has-flex-banner {background-color: #425563 !important;}');
					// HTML Template:
					this.cfg.template = '<div id="hpealertcomp" class="has-flex-banner">';
						this.cfg.template += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg>';
						this.cfg.template += '<div class="flex-banner">';
						this.cfg.template += '<div class="flex-banner-section">';
							this.cfg.template += '<span><b>Please note</b>- the HPE FlexFabric 5900AF-48G-4XG-2QSFP+ Switch (JG510A) has been replaced with the HPE FlexFabric 5901AF 48-Port 1GBaseT 4XG 2QSFP+ Switch (JL864A).</span>';
							//this.cfg.template += '<a href="">Learn more</a>';
						this.cfg.template += '</div>';
						this.cfg.template += '<div class="flex-banner-section">';
							this.cfg.template += '<a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a>';
						this.cfg.template += '</div>';
						this.cfg.template += '</div>';
					this.cfg.template += '</div>';

					self.showBanner();
				break;

				// April 29, 2022 => https://centerpoint.int.hpe.com:8443/browse/XPLAT-227
				case 'hpealert_answ_discover_2022':
					self.insertCSS('#hpealertcomp.has-flex-banner {background-color: #425563 !important; padding-top: 0px; padding-bottom:0px;} #hpe_alert_dsc_time_left{ width: 85px; display: inline-block; }');

					var eventtime = new Date("2022-06-28T11:45:00.000-05:00");

					// What to show when the datetime is still to happen:
					if(!this.isEventTime(eventtime) && !this.isBannerAnswered()){
						// HTML Template:
						this.cfg.template = '<div id="hpealertcomp" class="has-flex-banner">';
							this.cfg.template += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg>';
							this.cfg.template += '<div class="flex-banner">';
							this.cfg.template += '<div class="flex-banner-section">';
								this.cfg.template += '<span><b id="hpe_alert_dsc_time_left"></b><b>HPE DISCOVER 2022</b> THE EDGE-TO-CLOUD CONFERENCE LAS VEGAS, JUNE 28–30</span>';
								this.cfg.template += '<a href="https://www.hpe.com/us/en/discover.html">Register now</a>';
							this.cfg.template += '</div>';
							this.cfg.template += '<div class="flex-banner-section">';
								this.cfg.template += '<a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a>';
							this.cfg.template += '</div>';
							this.cfg.template += '</div>';
						this.cfg.template += '</div>';

						self.showBanner();

						// There are at least some seconds left until date:
						document.getElementById('hpe_alert_dsc_time_left').innerHTML = self.setEventTimeLeft(eventtime); // Setting initial value immediatelly, so it would not appear after 1 second
						document.countdownToEvent = setInterval(function () {
							if(document.getElementById('hpe_alert_dsc_time_left')){
								document.getElementById('hpe_alert_dsc_time_left').innerHTML=self.setEventTimeLeft(eventtime);
							}
							if(self.isEventTime(eventtime)){
								self.hideBanner(); // Hiding banner until decision is taken about what to do when time reaches zero
							}
						}, 1000);
					} else {
						if(this.isEventTime(eventtime)){
							//self.bannerAnswerCookie = 'hpealert_answ_spaceborne_attend';
							//self.showTimeOutBannerByCookie();
						}
					}
				break;

				// June 07, 2022 => https://centerpoint.int.hpe.com:8443/browse/XPLAT-265
				case 'hpealert_answ_rucom':
					let bannerVariant = 'has-flex-banner'; //'has-flex-banner'; // is-popup
					if(bannerVariant === 'has-flex-banner'){
						self.insertCSS(`
							#hpealertcomp.has-flex-banner{
								background-color: #425563 !important;
								height: unset !important;
								padding-top: 10px !important;
								padding-bottom: 10px !important;
							}
							#hpealertcomp .flex-banner .flex-banner-section{
								font-size: 16px !important;
							}
							#hpealertcomp .flex-banner .flex-banner-section span:first-child,
							#hpealertcomp .flex-banner .flex-banner-section span:first-child a{
								font-family: "Arial Narrow", Arial, sans-serif !important;
								font-size: 14px !important;
							}
							#hpealertcomp .flex-banner .flex-banner-section span:last-child a{
								font-family: MetricLight,"Metric Light",HPEMetricLight,Arial,sans-serif !important;
							}
							#hpealertcomp .flex-banner .flex-banner-section #collapser-en-version{
								margin-top: 10px;
							}
							#hpealertcomp .flex-banner .flex-banner-section #collapser-en-version .collapser-content{
								display: none;
							}
							#hpealertcomp .flex-banner .flex-banner-section #collapser-en-version.open .collapser-content{
								display: unset;
							}
							#hpealertcomp .flex-banner .flex-banner-section #collapser-en-version #toggle-en-version{
								display: block;
								font-family: MetricLight,"Metric Light",HPEMetricLight,Arial,sans-serif;
								font-size: 12px;
								margin-top:10px;
							}
						`);
					} else {
						//self.insertCSS('#hpealertcomp_container{background-color: rgba(0,0,0,.85) !important;display: flex;flex-direction: row;align-items: center;justify-content: center;position: absolute;top: 0px;left: 0px;right: 0px;bottom: 0px;width: 100%;height: 100%;z-index: 9999;}#hpealertcomp.is-popup{background-color: #425563 !important;width: 40%;position: relative;}#hpealertcomp .flex-banner{flex-direction: column !important;padding: 20px !important;}#hpealertcomp .flex-banner .flex-banner-section span{display: block;margin-bottom: 10px;}#hpealertcomp .flex-banner .flex-banner-section hr{margin: 15px 0px;height: 1px;border: none;border-bottom: 1px solid #fff;}#hpealertcomp #hpealertcomp_close{position: absolute !important;top: 10px !important;right: 10px !important;}');
					}

					// HTML Template:
					this.cfg.template = '<div id="hpealertcomp" class="'+bannerVariant+'">';
						this.cfg.template += '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="display:none;"><symbol id="close" viewBox="0 0 24 24" fill="#fff"><polygon points="21.8,23.4 12,13.7 2.2,23.4 0.6,21.8 10.3,12 0.6,2.2 2.2,0.6 12,10.3 21.8,0.6 23.4,2.2 13.7,12 23.4,21.8 "/></symbol></svg>';
						this.cfg.template += '<div class="flex-banner">';
							this.cfg.template += '<div class="flex-banner-section">';
								this.cfg.template += '<span>После приостановки поставок и продаж в России и Беларуси в конце февраля компания HPE внимательно следила за ситуацией. Для нас больше нецелесообразно продолжать деятельность в России и Беларуси, и мы продолжаем планомерно сворачивать бизнес в этих странах. Мы стремимся к прозрачному общению с членами нашей команды, клиентами и партнёрами, которые терпят неудобства из-за того, что мы сворачиваем деловые операции в двух странах. Следить за обновлениями компании можно на европейском региональном сайте <a href="https://www.hpe.com/emea_europe/en/home.html">перейдя по ссылке</a>.</span>';

								this.cfg.template += '<div id="collapser-en-version">';
									this.cfg.template += '<div class="collapser-content">';
										this.cfg.template += '<hr/>';
										this.cfg.template += '<span>After suspending shipments to and sales in Russia and Belarus in late February, HPE has monitored the situation closely. It is no longer tenable for us to continue operations in Russia and Belarus, and we are proceeding with an orderly exit of our remaining business in these countries. We are committed to transparent communication with our impacted team members, customers and partners as we wind down business operations in the two countries. For future HPE updates, go to the <a href="https://www.hpe.com/emea_europe/en/home.html">European Regional site</a>.</span>';
									this.cfg.template += '</div>';
									this.cfg.template += '<a href="javascript: void(0);" id="toggle-en-version">Show English version</a>';
								this.cfg.template += '</div>';
							this.cfg.template += '</div>';
							this.cfg.template += '<div class="flex-banner-section">';
								this.cfg.template += '<a href="#" id="hpealertcomp_close" class="hpealertcomp_close" title="____close____"><svg class="icon"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#close"></use></svg></a>';
							this.cfg.template += '</div>';
						this.cfg.template += '</div>';
					this.cfg.template += '</div>';

					self.showBanner();

					let toggler = document.getElementById('toggle-en-version');
					toggler.onclick = function(event) {
						event.preventDefault();
						let collapser = document.getElementById('collapser-en-version');
						if(!collapser.classList.contains('open')){
							collapser.classList.add("open");
							toggler.innerHTML= 'Hide English version';
						} else {
							collapser.classList.remove("open");
							toggler.innerHTML= 'Show English version';
						}
					};
				break;

				default:
					// Do nothing...
				break;
			}
		},


		/*
		/*
		 * init(config) - initializes HPEALERTBANNER object with the provided configuration object and HPEPRIVACYBANNER object
		 */
		init: function (config, prvban) {
			var tmpLoc = null;

			/* reuse methods from HPEPRIVACYBANNER object */
			this.log = prvban.log;
			this.isScriptInIframe = prvban.isScriptInIframe;
			this.dispatchBannerEvent = prvban.dispatchBannerEvent;
			this.isBannerVisible = prvban.isBannerVisible;
			this.isBannerAnswered = prvban.isBannerAnswered;
			this.insertCSS = prvban.insertCSS;
			this.insertBannerCSS = prvban.insertBannerCSS;
			this.insertBannerHTML = prvban.insertBannerHTML;
			/*this.saveAndCloseBanner = prvban.saveAndCloseBanner;*/
			this.isFontAvailable = prvban.isFontAvailable;
			this.getContainerWidthForFont = prvban.getContainerWidthForFont;
			this.getCookieDomain = prvban.getCookieDomain;
			this.readCookie = prvban.readCookie;
			this.writeCookie = prvban.writeCookie;
			this.eraseCookie = prvban.eraseCookie;
			this.getLocaleConfigByCCLL = prvban.getLocaleConfigByCCLL;
			this.getLocaleConfigByCC = prvban.getLocaleConfigByCC;
			this.getLocaleConfigByLL = prvban.getLocaleConfigByLL;
			this.detectLocaleFromURL = prvban.detectLocaleFromURL;
			this.detectLocaleFromHtmlLang = prvban.detectLocaleFromHtmlLang;
			this.detectLocaleFromMeta = prvban.detectLocaleFromMeta;
			this.getMetaTagContent = prvban.getMetaTagContent;
			this.getBannerHeight = prvban.getBannerHeight;

			this.log('HPE Alert Banner Init start');
			this.cfg = config;

			/* if not running in iframe, and if privacy banner is not visible */
			if ( !this.isScriptInIframe() && !prvban.isBannerVisible() ) {

				/* set default locale to be us/en, if we cannot detect it */
				//this.cc = 'us';
				//this.ll = 'en';

				if ( (tmpLoc = this.detectLocale()) != null ) {
					this.cc = tmpLoc.cc;
					this.ll = tmpLoc.ll;
					/* handle tw/zh */
					if (this.cc == 'tw' && this.ll == 'zh') this.ll = 'zh-tw';
				}

				// April 04, 2022 => https://centerpoint.int.hpe.com:8443/browse/XPLAT-213
				if(document.URL.search('/us/en/networking/comware.html') !== -1){
					if (!this.isBannerAnswered()){
						this.showBannerByCookie('hpealert_answ_flexfabric');
					}
				} else {
					// June 14, 2022 => https://centerpoint.int.hpe.com:8443/browse/XPLAT-227
					this.bannerAnswerCookie = 'hpealert_answ_discover_2022';
					if (!this.isBannerAnswered()){
						var regexXPLAT227 = /www\.hpe\.com\/us\/en/gmi; // all EN locales => /www\.hpe\.com\/.*\/en/gmi;
						var regexPsnow = /www\.hpe\.com\/psnow\//gmi; // Include psnow pages
						if( (document.URL.search('/h22228/video-gallery') !== -1 || document.URL.match(regexXPLAT227) || document.URL.match(regexPsnow) ) && document.URL.search('/discover') === -1 && this.ll === 'en' && (this.cc === 'us' || this.cc === 'ww')){
							this.showBannerByCookie('hpealert_answ_discover_2022');
						}
					}
				}

				if((this.cc === 'ru' && this.ll === 'ru' && document.location.hostname === 'www.hpe.com') || document.URL.search('www.hpe.com/h20430/emea/by/index.html') !== -1){
					this.bannerAnswerCookie = 'hpealert_answ_rucom';
					this.showBannerByCookie('hpealert_answ_rucom');
				}


				/* Show banner if not already closed by user */
/* Disabling Equality Alert Banner
				if (!this.isBannerAnswered()) {
					// Show equality banner only when locale is us/en
					if(this.cc === "us" && this.ll === "en") {
						this.showBanner();
					}
					// If equality banner is not showing - try showing the Discover Countdown banner
					if (!this.isBannerVisible()) {
						this.showDiscoverCountDownBanner();
					}
				}
				else {
					// If equality banner is not showing - try showing the Discover Countdown banner
*/
/* Discover Banners disabled
					this.showDiscoverCountDownBanner();
*/
/* Disabling Equality Alert Banner
					this.log('HPE Alert Banner already answered - not showing');
				}
*/

				/* Check if we're on R11936/www.hpe.com */
/* disabling old checks (if R11936 and if home page) - showing alert everywhere
				var wsid = this.getMetaTagContent('web_section_id');
				if ( (wsid != null) && (this.getMetaTagContent('web_section_id').toUpperCase() === 'R11936') ) {
					this.log('Alert executed on R11936/www.hpe.com.');
					if ( (tmpLoc = this.detectLocaleFromURL()) != null ) {
						this.log('Locale detected from URL: ' + tmpLoc.cc + '/' + tmpLoc.ll);
						this.cc = tmpLoc.cc;
						this.ll = tmpLoc.ll;
						// check if we're on home page
						if ( document.location.href.indexOf( '/' + this.cc + '/' + this.ll + '/home.html') != -1 ) {
							if (!this.isBannerAnswered()) {
								this.showBanner();
							}
							else {
								this.log('HPE Alert Banner already answered - not showing');
							}

						}
					}
				}
*/

			}

			this.dispatchBannerEvent('READY');
		}
	}



/*******************************************************************************************************************/


	/* TODO: should we have init code executed at dom ready event? or, we let this to be taken care of by init code to place necessary events? */

	/* If page is loaded at the time of execution, intialize banner right away. Otherwise, attach event function to load it when document is complete */
	if (document.readyState == 'complete') {
			/* Initialize Privacy Banner */
			if ( (window.location.href.indexOf('greenlake.hpe.com') === -1) ) { /* do not initialize for greenlake */
			HPEPRIVACYBANNER.init(HPEPRIVACYBANNER_CFG);
			HPEALERTBANNER.init(HPEALERTBANNER_CFG, HPEPRIVACYBANNER);
			}
	}
	else {
		/* Check if other onreadystatechange events are already defined, and preserve them */
		var preserved_onreadystatechange_function = null;
		if(typeof document.onreadystatechange == 'function') {
			preserved_onreadystatechange_function = document.onreadystatechange
		}
		else {
			preserved_onreadystatechange_function = function () { ; }
		}
		document.onreadystatechange = function () {
			preserved_onreadystatechange_function();
			if (document.readyState == 'complete') {
				/* Initialize Privacy Banner */
				if ( (window.location.href.indexOf('greenlake.hpe.com') === -1) ) { /* do not initialize for greenlake */
				HPEPRIVACYBANNER.init(HPEPRIVACYBANNER_CFG);
				HPEALERTBANNER.init(HPEALERTBANNER_CFG, HPEPRIVACYBANNER);
				}
			}
		}
	}
}
