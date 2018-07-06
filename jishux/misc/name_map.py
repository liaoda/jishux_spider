#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/1


from .name_map_params import *

common_map = {
    # ********** news list ***********
    # 'http://mobile.51cto.com/': {
    #     'url': {
    #         'http://mobile.51cto.com': 'mobile',
    #         # 'http://blog.51cto.com/dingbo/p1': 'mobile',
    #     },
    #     'cn_name': '51CTO',
    #     'posts_xpath': '//div[@class="home-left-list"]//li',
    #     'post_url_xpath': 'div[@class="rinfo"]/a/@href',
    #     'post_title_xpath': 'div[@class="rinfo"]/a/text()',
    # },

    # 'http://blog.51cto.com/': {
    #     'url': blog_51cto_urls,
    #     'cn_name': '51CTO博客',
    #     'posts_xpath': '//div[@china="博文"]/h4/a',
    #     'post_url_xpath': '@href',
    #     'post_title_xpath': 'text()',
    #     'next_page': {
    #         'type': 'CLICK_NEXT_BUTTON',
    #         'xpath': '//a[text()="next >"]/@href',
    #     },
    # },

    'https://www.2cto.com/': {
        'url': cto2_urls,
        'cn_name': '红黑联盟',
        'posts_xpath': '//*[@id="fontzoom"]/ul/li',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//*[text()="下一页"]/@href',
        },
    },

    'http://www.xitongcheng.com/': {
        'url': {
            'http://www.xitongcheng.com/jiaocheng/xtazjc/': 'os',
            'http://www.xitongcheng.com/jiaocheng/xp/': 'os',
            'http://www.xitongcheng.com/jiaocheng/win7/': 'os',
            'http://www.xitongcheng.com/jiaocheng/win8/': 'os',
            'http://www.xitongcheng.com/jiaocheng/win10/': 'os',
            'http://www.xitongcheng.com/jiaocheng/dnrj/': 'os',
        },
        'cn_name': '系统城',
        'posts_xpath': '//div[@class="left"]/ul/li',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//*[text()="下一页"]/@href',
        },
    },

    'http://www.linuxidc.com/': {
        'url': {
            'http://www.linuxidc.com/it/': 'news',
            'http://www.linuxidc.com/Linuxit/': 'os',
            'http://www.linuxidc.com/linuxsoft/': 'os',
            'http://www.linuxidc.com/MySql/': 'db',
            'http://www.linuxidc.com/RedLinux/': 'other',
            'http://www.linuxidc.com/download/': 'other',
            'http://www.linuxidc.com/Apache/': 'network',
            'http://www.linuxidc.com/Unix/': 'network',
        },
        'cn_name': 'linux公社',
        'posts_xpath': '//div[@class="summary"]',
        'post_url_xpath': 'div[@class="cont"]/div[@class="title"]/a/@href',
        'post_title_xpath': 'div[@class="cont"]/div[@class="title"]/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//*[text()="»"]/@href',
        },
    },

    'https://linux.cn/': {
        'url': {
            'https://linux.cn/news/': 'news',
            'https://linux.cn/tech/': 'os',
            'https://linux.cn/talk/': 'os',
            'https://linux.cn/share/': 'os',
        },
        'cn_name': 'Linux中国',
        'posts_xpath': '//ul[@class="article-list leftpic"]',
        'post_url_xpath': 'li/h2/span[@class="title"]/a/@href',
        'post_title_xpath': 'li/h2/span[@class="title"]/a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
    },

    'http://www.thebigdata.cn/': {
        'url': {
            'http://www.thebigdata.cn/YeJieDongTai/': 'news',
            'http://www.thebigdata.cn/KaiYuanJiShu/': 'bigdata',
            'http://www.thebigdata.cn/YingYongAnLi/': 'bigdata',
            'http://www.thebigdata.cn/JieJueFangAn/': 'bigdata',
            'http://www.thebigdata.cn/ShangYePingTai/': 'bigdata',
            'http://www.thebigdata.cn/ShuJuFenXi/': 'bigdata',
        },
        'cn_name': '中国大数据',
        'posts_xpath': '//div[@class="summary"]',
        'post_url_xpath': 'div[@class="cont"]/div[@class="title"]/a/@href',
        'post_title_xpath': 'div[@class="cont"]/div[@class="title"]/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//*[text()="»"]/@href',
        },
    },

    'http://it.dataguru.cn/': {
        'url': {
            'http://it.dataguru.cn/': 'bigdata',
        },
        'cn_name': '炼数成金',
        'posts_xpath': '//dl[@class="bbda cl"]',
        'post_url_xpath': 'dt/a/@href',
        'post_title_xpath': 'dt/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
    },

    'https://www.jianshu.com/': {
        'url': jianshu_urls,
        'cn_name': '简书',
        'posts_xpath': '//*[contains(@id,"note")]',
        'post_url_xpath': 'div/a[@class="title"]/@href',
        'post_title_xpath': 'div/a[@class="title"]/text()',
        'post_content_xpath': '//*[@class="show-content"]',
        'headers': {
            "Accept-Encoding": "gzip, identity",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": "remember_user_token=W1syMjEwMDk4XSwiJDJhJDEwJDZQU3ZteVdlMjkvdjdVVURDNjB0OWUiLCIxNTAzNDgyNjMwLjkyNDIxMTciXQ==--32ae8134ca911d1d332f8f8c42998581b18eb5ea; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1502267438,1502849321,1503026189,1503482168; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1503483324; _ga=GA1.2.938018437.1493976814; _gid=GA1.2.392185505.1503482168; _session_id=dGVjRndIQkNNYUx3UVN5YnFIMnlHd0pRSG9aR05XVS9pYnNTbU5kVExWSzVJelBxT2RSeUFqOEJjeFMzSDNTVU40aHpMbjQzWmpNQkFLRFdIWHZBcmxPZEc5aFdGaWYwdXVpSkVFL0tpbmlJdU1udzVUbU1uZnhMR0crYnR6RktEMmdIQkpyOXM1N3RyS1MwcEt4YnJybUg1bktYTHo1SStlN0U3Yk1vektTUzdhOXVtOVRJakxTa2xLTHRtcmVkdFBNQUZiay9QRWVzQlRKblk1Q0ZjL2VrckZQNHJ2QmxFOXMvaEw3T1BZUUcwYURsQjF2anBaN1JlSldBeXhtbCtjc2grYVpqOCtFOEpjRlAySlpxNHBQc0NhZjhicjVGcFBKOWRLdEdYZndabUtOTXNvdktsT3l1V1g1aC9GNms2VzhkZVJ3QXdNRS82cjhiSU52ZWdkSkFKNUd0dnpRUFJvYzAzVXl1alBNalArVGM3bWVkd0lQYXhYS1A5N1ZiYXF5eWZkLzhoR2prekxoOHRUUmE1dlNDK2lwMkFnb0dtMHBEc242Wm1pQT0tLWsxc2UvUDlhWnR5Qk1aQkJ3TWxsTmc9PQ==--0bfa89637e8adbc729937a3a07b21cf7c76723aa",
            "If-None-Match": "W/\"baebc4bb3d3c66947d8cbdedf66a8726\"",
        }
    },
    # 'http://lib.csdn.net/': {
    #     'url': {
    #         'http://lib.csdn.net/android/node/188': 'mobile',
    #         'http://lib.csdn.net/react/node/408': 'frontend',
    #         'http://lib.csdn.net/ai/node/762': 'ai',
    #         'http://lib.csdn.net/aiplanning/node/845': 'ai',
    #         'http://lib.csdn.net/javaee/node/174': 'backend',
    #         'http://lib.csdn.net/java/node/102': 'backend',
    #         'http://lib.csdn.net/javase/node/92': 'mobile',
    #         'http://lib.csdn.net/objective-c/node/744': 'mobile',
    #         'http://lib.csdn.net/knowledgeengineering/node/842': 'other',
    #     },
    #     'cn_name': 'CSDN',
    #     'posts_xpath': '//li[contains(@class,"clearfix")]',
    #     'post_url_xpath': 'div[@class="scontentright"]/p/a/@href',
    #     'post_title_xpath': 'div[@class="scontentright"]/p/a/text()',
    #     'next_page': {
    #         'type': 'CLICK_NEXT_BUTTON',
    #         'xpath': '//a[@class="btn btn-xs btn-default btn-next"]/@href',
    #     },
    #     'use_proxy': True
    # },

    'http://www.ailab.cn/': {
        'url': {
            'http://www.ailab.cn/': 'ai',
        },
        'cn_name': '人工智能网',
        'posts_xpath': '//ul[@class="list_jc"]/li',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
    },

    # 'http://blog.csdn.net/': {
    #     'url': csdn_urls,
    #     'cn_name': 'csdn',
    #     'posts_xpath': '//div[@class="list_item article_item"]',
    #     'post_url_xpath': 'div[@class="article_title"]/h1/span/a/@href',
    #     'post_title_xpath': 'div[@class="article_title"]/h1/span/a/text()',
    #     'next_page': {
    #         'type': 'CLICK_NEXT_BUTTON',
    #         'xpath': '//a[text()="下一页"]/@href',
    #     },
    # },

    'https://segmentfault.com/': {
        'url': segmentfault_urls,
        'cn_name': 'segmentfault',
        'post_content_xpath': "//*[contains(@class,'main')]/div[contains(@class,'article__content')]",
        'posts_xpath': '//div[@id="blog"]/section',
        'post_url_xpath': 'div[@class="summary"]/h2/a/@href',
        'post_title_xpath': 'div[@class="summary"]/h2/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
        'use_proxy': True
    },

    'http://www.56cto.com/': {
        'url': cto56_urls,
        'cn_name': '56cto',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/h2/a/@href',
        'post_title_xpath': 'header/h2/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
    },

    'http://www.cnblogs.com/': {
        'url': cnblogs_urls,
        'cn_name': '博客园',
        'posts_xpath': '//div[@class="day"]',
        'post_url_xpath': 'div[@class="postTitle"]/a/@href',
        'post_title_xpath': 'div[@class="postTitle"]/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
    },

    'https://tech.meituan.com/': {
        'url': {
            'https://tech.meituan.com/?l=4000': 'bigdata'
        },
        'cn_name': '美团技术团队博客',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/a/@href',
        'post_title_xpath': 'header/a/text()',
    },

    'http://www.php100.com/': {
        'url': {
            'http://www.php100.com/html/php/': 'backend',
            'http://www.php100.com/html/dujia/': 'backend',
            'http://www.php100.com/html/program/': 'frontend',
            'http://www.php100.com/html/it/': 'news',
        },
        'cn_name': 'php100',
        'posts_xpath': '//div[@class="col-md-9 category-list"]/div[@class="media"]',
        'post_url_xpath': 'h3/a/@href',
        'post_title_xpath': 'h3/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页"]/@href',
        },
    },

    'http://www.jb51.net/': {
        'url': jb51_urls,
        'cn_name': '脚本之家',
        'posts_xpath': '//dl/dt',
        'post_url_xpath': 'a/@href | span/a/@href',
        'post_title_xpath': 'a/text() | span/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下页"]/@href | //a[text()="下一页"]/@href',
        },
    },
    'http://www.open-open.com/': {
        'url': openopen_urls,
        'cn_name': '深度开源',
        'posts_xpath': '//div[@class="col-md-8"]/ul[@class="list"]/li',
        'post_url_xpath': 'div[@class="cont"]/h3/a/@href',
        'post_title_xpath': 'div[@class="cont"]/h3/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[@class="next"]/@href',
        },
    },

    'http://www.css88.com/': {
        'url': {
            'http://www.css88.com/': 'frontend',
        },
        'cn_name': 'WEB前端开发',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/h1/a/@href',
        'post_title_xpath': 'header/h1/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页 »"]/@href',
        },
    },

    'https://www.oschina.net/': {
        'url': {
            'https://www.oschina.net/news': 'news',
        },
        'cn_name': '开源中国',
        'post_content_xpath': '//*[starts-with(@class,"editor-viewer")]|//*[@id="articleContent"]',
        'posts_xpath': '//*[@id="all-news"]/div',
        'post_url_xpath': 'div[1]/a/@href',
        'post_title_xpath': 'div[1]/a/span/text()',
    },

    'http://www.uedbox.com/': {
        'url': {
            'http://www.uedbox.com/web-security/sourcing/': 'os',
            'http://www.uedbox.com/entertainment/macos/': 'os',
            'http://www.uedbox.com/web-security/vdbexp/': 'os',
            'http://www.uedbox.com/web-security/vdbexp/page/2/': 'db',
            'http://www.uedbox.com/design/htmlcss/': 'frontend',
            'http://www.uedbox.com/entertainment/news/': 'news',
        },
        'cn_name': '体验盒子',
        'posts_xpath': '//*[starts-with(@id,"post")]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/div[@class="media-body"]/h4/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[@title="Next »"]/@href',
        },
    },
    'http://www.luoxiao123.cn/': {
        'url': {
            'http://www.luoxiao123.cn/windows10': 'os',
            'http://www.uedbox.com/entertainment/macos/': 'os',
            'http://www.uedbox.com/web-security/vdbexp/': 'os',
            'http://www.uedbox.com/web-security/vdbexp/page/2/': 'db',
            'http://www.uedbox.com/design/htmlcss/': 'frontend',
            'http://www.uedbox.com/entertainment/news/': 'news',
        },
        'cn_name': '体验盒子',
        'posts_xpath': '//*[starts-with(@id,"post")]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/div[@class="media-body"]/h4/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[@title="Next »"]/@href',
        },
    },
    #
    'http://zhouww.com/': {
        'url': {
            'http://zhouww.com/archives/': 'backend',
        },
        'cn_name': '技术栈',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/h3/a/@href',
        'post_title_xpath': 'header/h3/a/span/text()',
        'post_content_xpath': '//*[@class="post-body"]',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[@rel="next"]/@href',
        },
    },

    'http://mrlongx.com/': {
        'url': {
            'http://mrlongx.com/': 'backend',
        },
        'cn_name': '技术栈',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/h2/a/@href',
        'post_title_xpath': 'header/h2/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[@class="next page-numbers"]/@href',
        },
    },

    'http://web.jobbole.com/': {
        'url': {
            'http://web.jobbole.com/all-posts/': 'frontend',
        },
        'cn_name': 'jobbole_web',
        'posts_xpath': '//div[@class="post floated-thumb"]/div[@class="post-thumb"]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页 »"]/@href',
        },
    },
    'http://python.jobbole.com/': {
        'url': {
            'http://python.jobbole.com/all-posts/': 'backend',
        },
        'cn_name': 'jobbole_python',
        'posts_xpath': '//div[@class="post floated-thumb"]/div[@class="post-thumb"]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页 »"]/@href',
        },
    },
    'http://www.importnew.com/': {
        'url': {
            'http://www.importnew.com/all-posts': 'backend',
        },
        'cn_name': 'importnew',
        'posts_xpath': '//div[@class="post floated-thumb"]/div[@class="post-thumb"]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页 »"]/@href',
        },
    },
    'http://android.jobbole.com/': {
        'url': {
            'http://android.jobbole.com/all-posts/': 'mobile',
        },
        'cn_name': 'jobbole_android',
        'posts_xpath': '//div[@class="post floated-thumb"]/div[@class="post-thumb"]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页 »"]/@href',
        },
    },
    'http://ios.jobbole.com/': {
        'url': {
            'http://ios.jobbole.com/all-posts/': 'mobile',
        },
        'cn_name': 'jobbole_ios',
        'posts_xpath': '//div[@class="post floated-thumb"]/div[@class="post-thumb"]',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/@title',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[text()="下一页 »"]/@href',
        },
    },
    'http://www.hankcs.com/': {
        'url': {
            'http://www.hankcs.com/': 'ai',
        },
        'cn_name': '码农场',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/h2/a/@href',
        'post_title_xpath': 'header/h2/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//li[@class="next-page"]/a/@href',
        },
    },
    'https://learnblockchain.cn/': {
        'url': {
            'https://learnblockchain.cn/': 'ai',
        },
        'cn_name': '区块链',
        'posts_xpath': '//a[@class="post-title-link"]',
        'post_url_xpath': '@href',
        'post_title_xpath': 'text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//a[@class="extend next"]/@href',
        },
    },
    'https://cuiqingcai.com/': {
        'url': {
            'https://cuiqingcai.com/': 'ai',
        },
        'cn_name': '静觅',
        'posts_xpath': '//article',
        'post_url_xpath': 'header/h2/a/@href',
        'post_title_xpath': 'header/h2/a/text()',
        'next_page': {
            'type': 'CLICK_NEXT_BUTTON',
            'xpath': '//*[@class="next-page"]/a/@href',
        },
    },

    # 'https://www.ibm.com/': {
    #     'url': {
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=AIX+and+Unix&search_by=&topic_by=%E6%89%80%E6%9C%89+AIX+and+Unix+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+AIX+and+Unix+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'os',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Big+data+and+analytics&search_by=&topic_by=%E6%89%80%E6%9C%89+Big+data+and+analytics+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+Big+data+and+analytics+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'bigdata',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Cloud+computing&search_by=&product_by=%E6%89%80%E6%9C%89+Cloud+computing+%E4%B8%AA%E4%BA%A7%E5%93%81&topic_by=%E6%89%80%E6%9C%89+Cloud+computing+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+Cloud+computing+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'bigdata',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Cognitive+computing&search_by=&product_by=-1&topic_by=-1&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'bigdata',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=DevOps&search_by=&topic_by=%E6%89%80%E6%9C%89+DevOps+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+DevOps+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'backend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=IBM+i&search_by=&topic_by=%E6%89%80%E6%9C%89+IBM+i+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+IBM+i+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'db',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Information+management&search_by=&product_by=%E6%89%80%E6%9C%89+Information+management+%E4%B8%AA%E4%BA%A7%E5%93%81&topic_by=%E6%89%80%E6%9C%89+Information+management+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+Information+management+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'db',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Internet+of+Things&search_by=&type_by=%E6%89%80%E6%9C%89+Internet+of+Things+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'other',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Java+technology&search_by=&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'backend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Linux&search_by=&topic_by=%E6%89%80%E6%9C%89+Linux+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+Linux+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'os',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Lotus&search_by=&topic_by=%E6%89%80%E6%9C%89+Lotus+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+Lotus+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'backend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Middleware&search_by=&topic_by=-1&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'network',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Mobile+development&search_by=&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'mobile',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Open+source&search_by=&topic_by=%E6%89%80%E6%9C%89+Open+source+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+Open+source+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'backend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Rational&search_by=&topic_by=-1&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'backend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=SOA+and+web+services&search_by=&topic_by=%E6%89%80%E6%9C%89+SOA+and+web+services+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+SOA+and+web+services+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'frontend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=Web+development&search_by=&topic_by=-1&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'frontend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=WebSphere&search_by=&topic_by=-1&type_by=%E6%89%80%E6%9C%89%E7%B1%BB%E5%88%AB&ibm-search=%E6%90%9C%E7%B4%A2': 'backend',
    #         'https://www.ibm.com/developerworks/cn/views/web/libraryview.jsp?sort_by=&show_abstract=false&show_all=&search_flag=&contentarea_by=XML&search_by=&topic_by=%E6%89%80%E6%9C%89+XML+%E4%B8%BB%E9%A2%98&type_by=%E6%89%80%E6%9C%89+XML+%E7%A7%8D%E7%B1%BB%E5%9E%8B&ibm-search=%E6%90%9C%E7%B4%A2': 'frontend',
    #     },
    #     'cn_name': 'IBM',
    #     'posts_xpath': '//tbody/tr/td[1]',
    #     'post_url_xpath': 'a/@href',
    #     'post_title_xpath': 'a/strong/text()',
    #     'next_page': {
    #         'type': 'CLICK_NEXT_BUTTON',
    #         'xpath': '//a[text()="下一页"][1]/@href',
    #     },
    # },

    #  '': {
    #     'url': {
    #         '': '',
    #     },
    #     'cn_name': '',
    #     'posts_xpath': '',
    #     'post_url_xpath': '',
    #     'post_title_xpath': '',
    #     'next_page': {
    #         'type': '',
    #         'xpath': '',
    #     },
    #     'headers': {
    #         'key1': 'value',
    #         'key2': 'value',
    #         'key3': 'value',
    #         'key4': 'value',
    #     },
    # },

    # '': {
    #     # [必选] url: 起始抓取地址
    #     'url': '',
    #     # [必选] cn_name: 中文名称，用于显示转载网站
    #     'cn_name': '',
    #     # [必选] posts_xpath: 文章列表xpath
    #     'posts_xpath': '',
    #     # [必选] post_url_xpath: 列表单个item的超链接xpath
    #     'post_url_xpath': '',
    #     # [必选] post_title_xpath: 列表单个item的标题xpath
    #     'post_title_xpath': '',
    #     # [必选] post_type: 文章类型，比如news,bigdata,mobile
    #     'post_type': '',
    #     # [可选] next_page: 下一页具体配置
    #     'next_page': {
    #         'type': '',
    #         'xpath': '',
    #     },
    #     # [可选] headers: 请求所需特殊headers，例如Referer
    #     'headers': {
    #         'key1': 'value',
    #         'key2': 'value',
    #         'key3': 'value',
    #         'key4': 'value',
    #     },
    # },

    # # url_spider conf
    # 'http://blog.csdn.net/': {
    #     'url': {
    #         'http://blog.csdn.net/peoplelist.html?channelid=1&page=1': 'mobile',
    #         'http://blog.csdn.net/peoplelist.html?channelid=15&page=1': 'network',
    #         'http://blog.csdn.net/peoplelist.html?channelid=2&page=1': 'bigdata',
    #         'http://blog.csdn.net/peoplelist.html?channelid=17&page=1': 'network',
    #         'http://blog.csdn.net/peoplelist.html?channelid=12&page=1': 'network',
    #         'http://blog.csdn.net/peoplelist.html?channelid=6&page=1': 'db',
    #         'http://blog.csdn.net/peoplelist.html?channelid=14&page=1': 'frontend',
    #         'http://blog.csdn.net/peoplelist.html?channelid=3&page=1': 'other',
    #     },
    #     'posts_xpath': '//dl',
    #     'post_url_xpath': 'dt/a/@href',
    #     'next_page': {
    #         'type': 'CLICK_NEXT_BUTTON',
    #         'xpath': '//a[text()="下一页"]/@href',
    #     },
    # },

}
