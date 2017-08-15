#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by yaochao on 2017/8/1


common_map = {
    # ********** brand ***********

    'http://socialbeta.com/tag/%E6%A1%88%E4%BE%8B': {
        'url': 'http://socialbeta.com/tag/%E6%A1%88%E4%BE%8B',
        'name': 'socialbeta',
        'cn_name': 'socialbeta',
        'posts_xpath': '//*[@class="postimg"]/li',
        'post_url_xpath': 'div/div/h3/a/@href',
        'post_title_xpath': 'div/div/h3/a/text()',
    },
    'http://www.qdaily.com/categories/18.html/': {
        'url': 'http://www.qdaily.com/categories/18.html/',
        'name': 'qdaily1',
        'cn_name': '好奇心日报',
        'posts_xpath': '//*[@class="packery-container articles"]/div',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/div/div/img/@alt',
    },
    'http://www.jiemian.com/lists/49.html': {
        'url': 'http://www.jiemian.com/lists/49.html',
        'name': 'jiemian1',
        'cn_name': '界面',
        'posts_xpath': '//div[@id="load-list"]/div',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    'http://www.toodaylab.com/field/308': {
        'url': 'http://www.toodaylab.com/field/308',
        'name': 'toodaylab',
        'cn_name': '理想生活实验室',
        'posts_xpath': '//*[@class="content"]/div',
        'post_url_xpath': 'div[@class="post-info"]/p/a/@href',
        'post_title_xpath': 'div[@class="post-info"]/p/a/text()',
    },
    'http://www.madisonboom.com/category/works/': {
        'url': 'http://www.madisonboom.com/category/works/',
        'name': 'madisonboom',
        'cn_name': '麦迪逊邦',
        'posts_xpath': '//*[@id="gallery_list_elements"]/li',
        'post_url_xpath': 'h3/a/@href',
        'post_title_xpath': 'h3/a/@title',
    },
    'http://iwebad.com/': {
        'url': 'http://iwebad.com/',
        'name': 'iwebad',
        'cn_name': '网络广告人社区',
        'posts_xpath': '//*[@class="new_search_works"]/div',
        'post_url_xpath': 'div[@class="works_info"]/h4/span/a/@href',
        'post_title_xpath': 'div[@class="works_info"]/h4/span/a/text()',
    },
    'http://www.adquan.com/': {
        'url': 'http://www.adquan.com/',
        'name': 'adquan',
        'cn_name': '广告门',
        'posts_xpath': '//div[@class="w_l_inner"]',
        'post_url_xpath': 'h2/a/@href',
        'post_title_xpath': 'h2/a/text()',
    },
    'http://www.digitaling.com/projects': {
        'url': 'http://www.digitaling.com/projects',
        'name': 'digitaling',
        'cn_name': '数英网',
        'posts_xpath': '//div[@id="pro_list"]/div',
        'post_url_xpath': 'div[@class="works_bd"]/div/h3/a/@href',
        'post_title_xpath': 'div[@class="works_bd"]/div/h3/a/text()',
    },
    'http://a.iresearch.cn/': {
        'url': 'http://a.iresearch.cn/',
        'name': 'iresearch',
        'cn_name': '艾瑞咨询',
        'posts_xpath': '//div[@id="tab-list"]/div/ul/li',
        'post_url_xpath': 'h3/a/@href',
        'post_title_xpath': 'h3/a/text()',
    },
    'http://www.ebrun.com/brands/': {
        'url': 'http://www.ebrun.com/brands/',
        'name': 'ebrun',
        'cn_name': '亿邦动力网',
        'posts_xpath': '//div[@id="create10"]/div[1]/div[@class="chanlDiv"]',
        'post_url_xpath': 'p/span/a/@href',
        'post_title_xpath': 'p/span/a/text()',
    },

    # ********** product **********
    'https://www.huxiu.com/': {
        'url': 'https://www.huxiu.com/',
        'name': 'huxiu',
        'cn_name': '虎嗅',
        'posts_xpath': '//*[@class="mod-info-flow"]/div[@class="mod-b mod-art "]',
        'post_url_xpath': 'div[@class="mod-thumb "]/a/@href',
        'post_title_xpath': 'div[@class="mod-thumb "]/a/@title',
    },
    'http://api.cyzone.cn/index.php?m=content&c=index&a=init&tpl=index_page&page=1': {
        'url': 'http://api.cyzone.cn/index.php?m=content&c=index&a=init&tpl=index_page&page=1',
        'name': 'cyzone',
        'cn_name': '创业邦',
        'posts_xpath': '//div[@class="article-item clearfix"]',
        'post_url_xpath': 'div[@class="item-intro"]/a/@href',
        'post_title_xpath': 'div[@class="item-intro"]/a/text()',
    },
    'https://www.leiphone.com/': {
        'url': 'https://www.leiphone.com/',
        'name': 'leiphone',
        'cn_name': '雷锋网',
        'posts_xpath': '//*[@class="lph-pageList index-pageList"]/div[2]/ul/li',
        'post_url_xpath': 'div/div[2]/h3/a/@href',
        'post_title_xpath': 'div/div[2]/h3/a/@title',
    },
    'http://www.iheima.com/': {
        'url': 'http://www.iheima.com/',
        'name': 'iheima',
        'cn_name': 'i黑马',
        'posts_xpath': '//article[@class="item-wrap cf"]',
        'post_url_xpath': 'div/div/a/@href',
        'post_title_xpath': 'div/div/a/text()',
    },
    'http://www.tmtpost.com/': {
        'url': 'http://www.tmtpost.com/',
        'name': 'tmtpost',
        'cn_name': '钛媒体',
        'posts_xpath': '//li[@class="post_part clear"]',
        'post_url_xpath': 'div/h3/a/@href',
        'post_title_xpath': 'div/h3/a/text()',
    },
    'http://www.iyiou.com/newpost': {
        'url': 'http://www.iyiou.com/newpost',
        'name': 'iyiou',
        'cn_name': '亿欧网',
        'posts_xpath': '//ul[@class="specificpost-list"]/li[@class="clearFix"]',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    'http://www.im2maker.com/fresh/': {
        'url': 'http://www.im2maker.com/fresh/',
        'name': 'im2maker',
        'cn_name': '镁客网',
        'posts_xpath': '//div[@id="article-list"]/div',
        'post_url_xpath': 'div/a[2]/@href',
        'post_title_xpath': 'div/a[2]/@title',
    },
    'http://www.geekpark.net/': {
        'url': 'http://www.geekpark.net/',
        'name': 'geekpark',
        'cn_name': '极客公园',
        'posts_xpath': '//*[@id="collection-all"]/div/article[@class="article-item"]',
        'post_url_xpath': 'div/div/a[2]/@href',
        'post_title_xpath': 'div/div/a[2]/text()',
    },
    'http://www.ikanchai.com/': {
        'url': 'http://www.ikanchai.com/',
        'name': 'ikanchai',
        'cn_name': '砍柴网',
        'posts_xpath': '//*[@id="mainList"]/ul/li[@class="rtmj-box"]',
        'post_url_xpath': 'dl/dt/a/@href',
        'post_title_xpath': 'dl/dt/a/@title',
    },
    'http://www.lieyunwang.com/': {
        'url': 'http://www.lieyunwang.com/',
        'name': 'lieyunwang',
        'cn_name': '猎云网',
        'posts_xpath': '//*[@class="article-bar clearfix"]',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/text()',
    },
    'https://www.jiqizhixin.com/': {
        'url': 'https://www.jiqizhixin.com/',
        'name': 'jiqizhixin',
        'cn_name': '机器之心',
        'posts_xpath': '//*[@class="article-inline"]',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    'http://www.donews.com/': {
        'url': 'http://www.donews.com/',
        'name': 'donews',
        'cn_name': 'donews',
        'posts_xpath': '//dl[@class="block pb30 mb30 line_b clearfix"]',
        'post_url_xpath': 'dd/h3/a/@href',
        'post_title_xpath': 'dd/h3/a/text()',
    },
    'http://news.chinabyte.com/': {
        'url': 'http://news.chinabyte.com/',
        'name': 'chinabyte',
        'cn_name': '比特网',
        'posts_xpath': '//div[@class="sec_left"]/div[2]/div[not(contains(@class, "Browse_more"))]',
        'post_url_xpath': 'div[@class="hot_"]/h4/a/@href',
        'post_title_xpath': 'div[@class="hot_"]/h4/a/text()',
    },
    'http://www.sootoo.com/tag/1/?&day=--&page=1': {
        'url': 'http://www.sootoo.com/tag/1/?&day=--&page=1',
        'name': 'sootoo',
        'cn_name': '速途网',
        'posts_xpath': '//li[@class="ZXGX_list clearfix"]',
        'post_url_xpath': 'h3/a/@href',
        'post_title_xpath': 'h3/a/text()',
    },
    'http://www.qdaily.com/categories/18.html': {
        'url': 'http://www.qdaily.com/categories/18.html',
        'name': 'qdaily2',
        'cn_name': '好奇心日报',
        'posts_xpath': '//div[@class="packery-container articles"]/div',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/div/div/img/@alt',
    },
    'http://www.qdaily.com/categories/4.html': {
        'url': 'http://www.qdaily.com/categories/4.html',
        'name': 'qdaily3',
        'cn_name': '好奇心日报',
        'posts_xpath': '//div[@class="packery-container articles"]/div',
        'post_url_xpath': 'a/@href',
        'post_title_xpath': 'a/div/div/img/@alt',
    },
    'http://www.jiemian.com/lists/6.html': {
        'url': 'http://www.jiemian.com/lists/6.html',
        'name': 'jiemian2',
        'cn_name': '界面',
        'posts_xpath': '//div[@id="load-list"]/div',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    'http://www.jiemian.com/lists/66.html': {
        'url': 'http://www.jiemian.com/lists/66.html',
        'name': 'jiemian3',
        'cn_name': '界面',
        'posts_xpath': '//div[@id="load-list"]/div',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    'http://www.jiemian.com/lists/73.html': {
        'url': 'http://www.jiemian.com/lists/73.html',
        'name': 'jiemian4',
        'cn_name': '界面',
        'posts_xpath': '//div[@id="load-list"]/div',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    # 'http://www.ifanr.com/category/product?page=1&pajax=1&post_id__lt=&show_type=card': {
    #     'url': 'http://www.ifanr.com/category/product?page=1&pajax=1&post_id__lt=&show_type=card',
    #     'name': 'ifanr1',
    #     'cn_name': '爱范儿',
    #     'posts_xpath': '//div[@class="article-item article-item--list "]',
    #     'post_url_xpath': 'div[@class="article-info"]/h3/a/@href',
    #     'post_title_xpath': 'div[@class="article-info"]/h3/a/text()',
    #     'headers': {
    #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    #     }
    # },
    # 'http://www.ifanr.com/category/business?page=1&pajax=1&post_id__lt=&show_type=card': {
    #     'url': 'http://www.ifanr.com/category/business?page=1&pajax=1&post_id__lt=&show_type=card',
    #     'name': 'ifanr2',
    #     'cn_name': '爱范儿',
    #     'posts_xpath': '//div[@class="article-item article-item--list "]',
    #     'post_url_xpath': 'div[@class="article-info"]/h3/a/@href',
    #     'post_title_xpath': 'div[@class="article-info"]/h3/a/text()',
    # },
    'http://cn.technode.com/post/category/technode-talks/': {
        'url': 'http://cn.technode.com/post/category/technode-talks/',
        'name': 'technode',
        'cn_name': '动点科技',
        'posts_xpath': '//div[@class="td_mod_wrap td_mod9 "]',
        'post_url_xpath': 'div/a/@href',
        'post_title_xpath': 'div/a/@title',
    },
    # '': {
    #     'url': '',
    #     'name': '',
    #     'cn_name': '',
    #     'posts_xpath': '',
    #     'post_url_xpath': '',
    #     'post_title_xpath': '',
    # },
}
