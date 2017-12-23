# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from hospital.items import *
from scrapy.http import Request
# from scrapy.linkextractors.sgml import SgmlLinkExtractor
import re
class HospitalSpider(CrawlSpider):
     name = 'hospitalSpider'
     download_delay = 2
     custom_settings = {'ITEM_PIPELINES':{'hospital.pipelines.HospitalPipeline':200}}
     allowed_domains = ['yyk.99.com.cn']
     mainUrl = 'http://yyk.99.com.cn'
     start_url = 'http://yyk.99.com.cn/miyun'
     addressnameList=['huangpu','luwan','xuhui','changning','jingan','putuo','zhabei','hongkou','yangpu',\
                      'minhang','baoshanqu','jiading','pudong','jinshan','songjiang','fengxian','chongming',\
                      'heping','hedong','hexi','nankai','hebeiqu','hongqiao','tanggu','hangu','dagang','dongli',\
                      'xiqing','jinnan','beichen','wuqing','baodi','jixian','ninghe','jinghai','yuzhong','dadukou',\
                      'jiangbei','shapingba','jiulongpo','nanan','beibei','wansheng','shuangqiao','yubei','banan',\
                      'wanzhou','fuling','chongqing','changshou','hechuan','yongchuan','jiangjin','nanchuan','qijiang',\
                      'tongnan','tongliang','dazu','rongchang','bishan','diejiang','wulong','fengdu','chengkou',\
                      'liangping','kaixian','wuxixian','wushan','fengjie','yunyang','zhongxian','shizhu','pengshui',\
                      'youyang','xiushan','jiangan','jianghan','changkou','hanyang','wuchang','hongshanqu','dongxihu',\
                      'hannan','caidian','jiangxia','huangpi','xinzhou1','qingshanqu','xuanwuqu','baixia','qinhuai',\
                      'jianye','gulou','xiaguan','pukou','liuhe','qixia','yuhuatai','jiangning','lishuixian','gaochun',\
                      'futian','luohu','nanshan','baoan','longgang','yantian','longhuaxinqu','xingning1','jiangnan',\
                      'qingxiu','xixiangtang','yongning','liangqing','wuming','hengxian','binyang','shanglin','longan',\
                      'mashan','chengbeiqu','zhongyuan','erqi','guanchengqu','jinshui','shangjie','mangshan','xinzheng',\
                      'dengfeng','xinmi','gongyi','xingyang','zhongmou','zhengdong','huiji','gongshu','shangcheng',\
                      'xiacheng','jianggan','xihu','binjiang','yuhang','xiaoshan','linan','fuyangshi','jiande',\
                      'tonglu','chunan','xinpu','lianyun','haizhou','ganyu','guanyun','donghai','guannan','qinghequ',\
                      'qingpuqu','chuzhou','huaiyin','jinhu','xuyi','hongze','lianshui','sucheng','suyu','shuyang',\
                      'siyang','sihong','dongtai','dafeng','yandu','sheyang','funingxian','binhai','xiangshui',\
                      'jianhu','tinghu','guanglingqu','weiyang','hanjiangqu''yizheng','jiangdu','gaoyou','baoying',\
                      'hailing','gaogang','jingjiang','taixing','jiangyan','xinghua','chongchuan','gangzha','haimen',\
                      'qidong','tongzhoushi','rugao','rudong','haian','jingkou','runzhou','dantu','yangzhong',\
                      'danyang','jurong','zhonglou','tianning','qishuyan','xinbei','wujin','jintan','liyang','chongan',\
                      'nanchangqu','beitang','binhu','huishan','xishan','jiangyin','yixing','jinchangqu','canglang',\
                      'pingjiang','huqiu','wuzhongqu','xiangcheng','wujiangshi','kunshan','taicang','changshu',\
                      'zhangjiagang','yunlong','quanshan','jiawang','tongshan','xinyishi','pizhou','suining1','peixian',\
                      'fengxian1','jiuli','gulou1','haishu','jiangdong','jiangbeiqu','zhenhai','beilun','yinzhouqu',\
                      'yuyao','cixi','fenghua','ninghai','xiangshanxian','luchengqu','longwan','ouhai','ruian','leqing',\
                      'yongjia','wencheng','pingyang','taishun','dongtou','cangnan','xiucheng','xiuzhou','haining',\
                      'pinghu','tongxiang','jiashan','haiyan','changxing','deqingxian','anji','wuxing','nanxun',\
                      'yuecheng','zhuji','shangyu','shengzhou','shaoxing','xinchang','wuchengqu','jindong','lanxi',\
                      'yongkang','yiwu','dongyang','wuyixian','pujiang','panan','kecheng','qujiangqu','jiangshan',\
                      'changshan','kaihua','longyou','putuoqu','dinghai','daishan','shengsi','jiaojiang','huangyan',\
                      'luqiao','linhai','wenling','sanmen','tiantai','xianju','yuhuan','liandu','longquan','jinyun',\
                      'qingtian','yunhexian','suichang','songyang','qingyuan1','jingning','yaohai','luyang','shushan',\
                      'baohe','changfeng','feidong','feixi','binhu','jinghu','matang','xinwu','jiujiangqu','wuhuxian',\
                      'fanchang','nanling','gejiang','wuweixian','yuhui','zhong','dong','huaiyuan','wuhe','guzhenxian',\
                      'longzihu','bashan','huaishang','tianjiaan','datongqu','xiejiaji','bagongshan','panji',\
                      'fengtaixian','shouxian','qiaocheng','woyang','mengcheng','lixin','guichi','dongzhi','shitai',\
                      'qingyangxian','jiuhuashan','laian','fenglai','shixiaqu','xuanzhou','ningguo','langxi','guangde',\
                      'jingxian1','jingde','jixixian','tianchang','quanjiao','mingguang','laian','fenglai','langya',\
                      'gulouqu','taijiang',\
                      'jinan1','cangshan','mawei','fuqing','changle','minhou','lianjiangxian',\
                      'luoyuan','minqing','yongtai','pingtan','siming','huli','jimei','haicang','tongan','xiangan', \
                      'meilie','sanyuan','yongan','mingxi','qingliu','ninghua','datian','youxi','shaxian','datian', \
                      'datian', 'youxi', 'shaxian', 'jiangle', 'taining', 'jianning', 'chengxiang', 'hanjiang', \
                      'lichengqu', 'xiuyu', 'xianyou','licheng1','fengze','luojiang','quangang','shishi','jinjiang', \
                      'nananshi', 'huian', 'anxi', 'yongchun', 'dehua','licheng2','longwen','longhai','yunxiao', \
                      'zhangpu', 'zhaoan', 'changtai', 'dongshan', 'nanjingxian', 'pinghe', 'huaan','yanping', \
                      'shaowu', 'wuyishan', 'jianou', 'jianyang', 'shunchang', 'pucheng', 'guangze', 'songxi', \
                      'zhenghe', 'xinluo', 'zhangping', 'changting', 'yongding', 'shanghang', 'wuping', 'liancheng', \
                      'jiaochengqu', 'fuan', 'fuding', 'shouning', 'xiapu', 'zherong', 'pingnanxian', 'gutian',\
                      'zhouning','donghu','qingyunpu','wanli','qingshanhu','nanchangxian','xinjian','anyi','jinxian', \
                      'zhushan', 'changjiangqu', 'leping', 'fuliang', 'anyuan', 'xiangdong', 'lianhua', 'shangli',\
                      'luxi', 'xunyangqu','lushan','ruichang','jiujiangxian','wuning','xiushui','yongxiu','dean',\
                      'xingzi','duchang','hukou','pengze','yushui','fenyi','yuehu','guixi','yujiang','zhanggong', \
                      'ruijin', 'nankang', 'ganxian', 'xinfengxian', 'dayu', 'shangyou', 'chongyi', 'anyuanxian',\
                      'longnanxian','dingnan','quannan','ningdu','yudu','xingguo','huichang','xunwu','shicheng',\
                      'zhangjiang','jizhouqu','qingyuanqu','jinggangshan','jianxian','jishui','xiajiang','xinganxian', \
                      'yongfeng', 'taihexian', 'suichuan', 'wanan', 'anfu', 'yongxin', 'yuanzhou', 'fengcheng', \
                      'zhangshu', 'gaoan', 'fengxin', 'wanzai', 'shanggao', 'yifeng', 'jinganxian', 'tonggu', \
                      'linchuan', 'nanchengxian', 'lichuan', 'nanfeng', 'chongren', 'lean', 'yihuang', 'jinxi', \
                      'zixi', 'dongxiang', 'guangchang', 'xinzhouqu', 'dexing', 'shangraoxian', 'guangfeng', \
                      'yushanxian', 'qianshanxian', 'hengfeng', 'yiyang1', 'yugan', 'boyang', 'wuyuanxian', \
                      'wannian', 'shizhongqu', 'lixia', 'huaiyinqu', 'tianqiao', 'licheng3', 'changqing', \
                      'zhangqiu', 'pingyin', 'jiyang', 'shanghe', 'nan', 'bei', 'sifang', 'huangdao', 'laoshan', \
                      'chengyang', 'licang', 'jiaozhou', 'jimo', 'pingdu', 'jiaonan', 'laixi', 'taidong', \
                      'zhangdian', 'zichuan', 'boshan', 'linzi', 'zhoucun', 'huantai', 'gaoqing', 'yiyuan', \
                      'xuecheng', 'yichengqu', 'taierzhuang', 'shanting', 'tengzhou', 'shizhong', 'dongyingqu', \
                      'hekou', 'kenli', 'lijin', 'guangrao', 'weicheng', 'hanting', 'fangzi', 'kuiwen', 'anqiu', \
                      'changyi', 'gaomi', 'qingzhou', 'zhucheng', 'shouguang', 'linqu', 'changlexian', 'zhifu', \
                      'fushanqu', 'laishan', 'mouping', 'qixiashi', 'haiyang', 'longkou', 'laiyang', 'laizhou', \
                      'penglai', 'zhaoyuan', 'changdao', 'huancui', 'rongchengshi', 'rushan', 'wendeng', 'szq', \
                      'rencheng', 'qufu', 'yanzhou', 'zoucheng', 'weishan', 'yutai', 'jinxiang', 'jiaxiang', \
                      'wenshang', 'sishui', 'liangshanxian', 'taishanqu', 'daiyue', 'xintai', 'feicheng', \
                      'ningyang', 'dongping', 'lanshanqu', 'donggang', 'wulian', 'juxian', 'laicheng', \
                      'gangcheng', 'lanshan', 'hdq', 'luozhuang', 'tancheng', 'cangshanxian', 'junan', 'yishui', \
                      'mengyin', 'pingyi', 'feixian', 'yinan', 'linshu', 'decheng', 'leling', 'yucheng', \
                      'lingxian', 'pingyuanxian', 'xiajin', 'wucheng', 'qihe', 'linyixian', 'ningjinxian', \
                      'qingyun', 'dongchangfu', 'linqing', 'yanggu', 'shenxian', 'chiping', 'donga', 'guanxian', \
                      'gaotang', 'shixiaqu', 'bincheng', 'huiminxian', 'yangxin', 'wudi', 'zhanhua', 'boxing', \
                      'zouping', 'mudan', 'caoxian', 'dingtao', 'chengwu', 'danxian', 'juye', 'yunchengxian', \
                      'juancheng', 'dongming', 'changan1', 'qiaodong', 'qiaoxi', 'xinhua', 'yuhua', \
                      'jingxingkuangqu', 'xinji', 'gaocheng', 'jinzhouxian', 'xinle', 'luquan', 'jingxing', \
                      'zhengding', 'luancheng', 'xingtang', 'lingshou', 'gaoyi', 'shenze', 'zanhuang', 'wuji', \
                      'pingshan', 'yuanshi', 'zhaoxian', 'lubei', 'lunan', 'guye', 'kaipingxian', 'fengnan', \
                      'fengrun', 'zunhua', 'qianan', 'luanxian', 'luannan', 'leting', 'qianxixian', 'yutian', \
                      'tanghai', 'haigang', 'shanhaiguan', 'beidaihe', 'changli', 'funing', 'lulong', 'qinglong', \
                      'congtai', 'hanshan', 'fuxing', 'fengfengkuang', 'wuan', 'linzhang', 'chengan', 'daming', \
                      'shexian', 'cixian', 'feixiang'
                      ]

















     def start_requests(self):
         for a in self.addressnameList:
             self.start_url= self.mainUrl+'/%s'%(a)
             url = self.start_url
             yield  Request(url=url, callback=self.parse)
     def parse(self, response):
         res = Selector(response)
         item = hospitalItem()
         
         # nameList=res.xpath('//div[@class="hpi_content clearbox"]/ur/li/b/span/text()').extract()
         urlList = res.xpath('//div[@class="tablist"]/ul/li/a/@href').extract()
         nameList = res.xpath('//div[@class="tablist"]/ul/li/a/@title').extract()
         for l in urlList:
            yield Request(url=l, callback=self.parse_detail)
         item['name'] = nameList
         item['url'] = [l for l in urlList]
         
         yield item
     def parse_detail(self, response):
         res = Selector(response)
         detailItem = hospitalDetailItem()
         conList = res.xpath('//div[@class="hpi_content clearbox"]/ul/li/span[not(@class)]/text()').extract()  # 提取字符串以列表的形式返回
         
         print conList
         print len(conList)
         nicknameList = [re.sub('\s+', '', conList[0])]
         propertyList = [re.sub('\s+', '', res.xpath('//div[@class="hpi_content clearbox"]/ul/li/text()').extract()[0])]
         rankList = [re.sub('\s+', '', conList[1])]
         telList = [re.sub('\s+', '', conList[2])]
         addressList = [re.sub('\s+', '', conList[3])]
          
         detailItem['nickname'] = nicknameList
         detailItem['property'] = propertyList
         detailItem['rank'] = rankList
         detailItem['tel'] = telList
         detailItem['address'] = addressList
         detailItem['url'] = [response.url]
         yield detailItem
