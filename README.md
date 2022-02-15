# Computer-Science-Whitelist

## Table of contents
- <a href="#introduction">Introduction</a>
- <a href="#google-programmable-search-engine">programmablesearchengine.google.com</a>
    - <a href="#sort">Sort</a>
    - <a href="#configuration">Configuration</a>
    - <a href="#ad-filtering">Ad filtering</a>
    - <a href="#focus-on-input-box">Focus on input box</a>
- <a href="#ublacklist">uBlacklist</a>
    - <a href="#introduction-of-ublacklist">introduction of uBlacklist</a>
    - <a href="#whitelist-mode">whitelist mode</a>
    - <a href="#subscription-rules">subscription rules</a>
- <a href="#other-ways-of-using-it">other ways of using it</a>
- <a href="#reference">reference</a>


## introduction

垃圾站点越来越多，而黑名单是无限的，白名单可以是有限的，以有限的精力去维护有限的白名单，于是这个白名单就这么出来了。

这个名单只收集<b>问答论坛</b>，和类似 wiki 的高质量内容网站。

名单整理，用字典比较方便，example:

```py
Whitelist = {
        # 'domain_name': ['prefix', 'suffix', 'score'],
        'baidu':['wenku','com/view','0.4'],    # 百度文库
        'docin':['','com/p-','0.4'],           # 豆丁文库
        'doc88':['','com/p-','0.4'],           # 道客巴巴
        'taodocs':['','com/p-','0.4'],         # 淘豆网
}
```

`main.py` 处理名单(python 字典格式)，并生成对应的 txt、xml，到 whitelists/.

目录结构:

```
│   .gitignore
│   main.py
│   README.md
│   uBlacklist.png
│
├───html
│       cse_google_nginx_conf
│       index.html
│
├───whitelists
│       annotations.xml
│       bbs.txt
│       blogs.txt
│       cse.xml
│       cse_FacetLabels.xml
│       domain_name.txt
│       library.txt
│       repository.txt
│       software.txt
│       video.txt
│       whitelist.txt
│       whitelists_combined.txt
│       wiki.txt
│
├───whitelist_dics
│   │   bbs.py
│   │   blogs.py
│   │   blogs_blacklist.py
│   │   library.py
│   │   video.py
│   │   repository.py
│   │   software.py
│   │   wiki.py
│   │   __init__.py
```

使用与调试：

先用自定义搜索，如果添加了自定义实体，那结果将会被严格限制，如，添加 `Computer Science`，在搜索 "辱骂" 一词时给出的也多为 "辱骂检测技术"，不会显示社会热点。

如果没有想要的结果，再点击页面最下方的 `Search for [关键词] on Google`，使用 uBlacklist 的白名单对 Google 的搜索结果进行过滤，如果还没有想要的结果，点击 Show 显示被过滤的网站，找到比较不错的网站，再添加到白名单中。

## google programmable search engine

配置: <a href="./whitelists/cse.xml">./whitelists/cse.xml</a> 

名单: <a href="./whitelists/annotations.xml">./whitelists/annotations.xml</a>

在高级选项中上传:

<img src="cse_google.jpg" width="70%">

cse.xml 可设项有些多，在网页上修改比较简单。

测试链接：<a href="https://cse.google.com/cse?cx=e9a1e480e37a86080&q=">https://cse.google.com/cse?cx=e9a1e480e37a86080&q=</a>

使用的知识实体为：`Stack Exchange`, `Mathematics`, `Computer Science`, 'network`, `Software development`

### sort

只给 Annotation 添加 score 属性就可以对其排序，value from -1.0 to 1.0

可以在 socre 的基础上给 Label 标签排序，使用 weight 字段，value from -1.0 to 1.0
 
weight > score

<b>一级排序：</b>

为不同的 Label 排序，在 cse.xml 中添加标签(Label)并设置权重(weight, from -1.0 to 1.0)

示例：

```xml
<CustomSearchEngine>
  <Title>My Search</Title>
  <Context>
    <Facet>
      <FacetItem>
        <Label name="wiki" mode="FILTER" weight="1" enable_for_facet_search="true">
          <Rewrite/>
          <entities/>
        </Label>
        <Title>wiki</Title>
      </FacetItem>
      <FacetItem>
        <Label name="bbs" mode="FILTER" weight="0.8" enable_for_facet_search="true">
          <Rewrite/>
          <entities/>
        </Label>
        <Title>bbs</Title>
      </FacetItem>
    </Facet>
    <BackgroundLabels>
      <Label name="_include_" mode="FILTER"/>
      <Label name="_exclude_" mode="ELIMINATE"/>
    </BackgroundLabels>
  </Context>
...
```

上述文件中有两个 Label 分别是 wiki, bbs，其权重分别为 1.0, 0.8

这两个标签下的所有 Annotation 都以这个为排序，每个 Annotation 可以多个 Label。

当 Rewrite 中有内容且没有任何网址拥有这些标签时，对应的 Label 的 mode 只能选 BOOST，不然搜索结果中，该标签下不会有结果

<b>二级排序(标签内部微调):</b>

在 annotations.xml 中为每一个 Annotation 的 Label 添加 score 属性，值同样是 from -1.0 to 1.0

示例：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Annotations start="0" num="84" total="84">
  <Annotation about="*.uptodown.com/*" score="0.8" timestamp="0x0005d6b5044e8329" href="ChAqLnVwdG9kb3duLmNvbS8qEKmGuqLQ1vUC">
    <Label name="_include_"/>
    <Label name="software"/>
    <AdditionalData attribute="original_url" value="*.uptodown.com/*"/>
    <AdditionalData attribute="file" value="annotations.xml"/>
  </Annotation>
  <Annotation about="*.wenku.baidu.com/view*" score="0.7" timestamp="0x0005d6b5044e82a2" href="ChcqLndlbmt1LmJhaWR1LmNvbS92aWV3KhCihbqi0Nb1Ag">
    <Label name="_include_"/>
    <Label name="library"/>
    <AdditionalData attribute="original_url" value="*.wenku.baidu.com/view*"/>
    <AdditionalData attribute="file" value="annotations.xml"/>
  </Annotation>
  <Annotation about="*.edu/*" score="0.3" timestamp="0x0005d6b5044e829f" href="CgcqLmVkdS8qEJ-FuqLQ1vUC">
    <Label name="_include_"/>
    <Label name="blogs"/>
    <AdditionalData attribute="original_url" value="*.edu/*"/>
    <AdditionalData attribute="file" value="annotations.xml"/>
  </Annotation>
  <Annotation about="*.liaoxuefeng.com/wiki*" score="0.5" timestamp="0x0005d6b5044e8292" href="ChcqLmxpYW94dWVmZW5nLmNvbS93aWtpKhCShbqi0Nb1Ag">
    <Label name="_include_"/>
    <Label name="blogs"/>
    <AdditionalData attribute="original_url" value="*.liaoxuefeng.com/wiki*"/>
    <AdditionalData attribute="file" value="annotations.xml"/>
  </Annotation>
</Annotations>
```

当 score <= 0 时，该地址可能不会出现在结果中，所以最小也应该设置为 0.01



### configuration

cse.xml 中的 CustomSearchEngine 的属性，只有 language, encoding, enable_promotions, autocompletions 是需要根据个人需要进行修改。

其他的字段，如 id, creator, cx_id 是固定的，不需要写在文件中，即使上传的 cse.xml 中没有这些，系统会自动生成。还有 last_update_time_millis 字段，也是系统自动生成的，不需要手动添加。

annotations.xml 中的 Annotations 的属性 start, num, total, 也是会自动生成，手动加上方便查看。timestamp, href, 是系统生成的，不需要手动添加。

<b>如果一个 url 不是通过上传 annotations.xml 所添加，那么在高级选项下删除 annotations.xml 也不会将这个 url 移除</b>


### ad filtering

```css
.gsc-adBlock {display:none !important}
```

### focus on input box

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Custom Search Engine</title>
  <script type="text/javascript">
    function focusFieldOne() {
      document.querySelector('input[name="search"]').focus()
    }
  </script>
  <style>
    /*  Google Adsense  */
    .gsc-adBlock {display:none !important}
  </style>
</head>
<body onload="focusFieldOne()">
  <script async src="https://cse.google.com/cse.js?cx=[Your search ID]"></script>
  <div class="gcse-search"></div>
</body>
</html>
```

## ublacklist

### introduction of ublacklist

PC 浏览器(Chrome, Firefox, Edge, Safair(支持移动端))插件。

<a href="https://github.com/iorate/uBlacklist" target="_blank">uBlacklist</a> 目前支持搜索引擎有 Google, Bing, DuckDuckgo, Ecosia, Startpage, Qwant

* 访问速度: Bing 最快。

* 样式: Bing 最好。
  * 在使用油猴本 <a href="https://www.ntaow.com/aboutscript.html" target="_blank">AC-重定向</a> 将搜索结果多列显示时，Bing 的样式要比 Google 整齐。
  * Bing 页面最底端没有搜索关键词对应的相关图片。

* 拦截能力: 对 Google 的拦截效果最好。
  * Bing 下，常出现 3~5 个不在名单中的网站，以及视频卡片，新闻卡片，相关搜索，可通过油猴插件写脚本进行过滤。


### whitelist mode

插件本是针对垃圾网站进行过滤，也就是黑名单模式，修改下使用方式就能实现白名单过滤。

黑名单规则总是优于白名单生效。

所以可以先添加规则 `*://*/*` 以屏蔽所有网址。

添加：`@:*//前缀.域名.后缀`(如 `@:*//*.github.com/*`, 区分大小写) 取消对某个网站的过滤。

规则举例：
```python
# 有前缀
@:*//*.github.com/*

# 没前缀
@:*//github.com/*

# 不完整的后缀
@*://*.docin.com/p-*
@*://*.doc88.com/p-*
@*://*.taodocs.com/p-*

# 完整的后缀
@*://*.appinn.com/*
```

通过前后缀区分一个地址的类型。

<b>使用"最长前缀匹配规则", 过滤奇怪的结果，或者不相关结果。</b>

规则是从左往右匹配的。

如，脚本之家：

```
https://www.jb51.net/                             移动端
https://m.jb51.net/                               电脑端
https://www.jb51.net/list/index_96.htm          脚本专栏
https://www.jb51.net/os/win11/808733.html     某个教程页
https://www.jb51.net/softs/794768.html    某个软件下载页
```

只索引它的软件下载页, 规则：`@*://*.jb51.net/softs*`，就能过滤掉其他页面。

后缀匹配的规则，如 `@*://*.edu/*`。

修改搜索设置，将搜索结果数调得尽可能大，白名单模式会使得每一搜索页中的内容变得特别少, 因为符合白名单的网站，可能不在结果的第一页。

自动翻页插件: <a href="https://chrome.google.com/webstore/detail/uautopagerize/kdplapeciagkkjoignnkfpbfkebcfbpb" target="_blank">uAutoPagerize</a>, 以及油猴脚本 <a href="https://greasyfork.org/en/scripts/438684-pagetual">东方永动机</a> 可以在自动翻页的同时过滤搜索结果。


### subscription rules

为保证白名单生效，先订阅 whitelist.txt

<b>点击添加订阅</b>：<a href="https://iorate.github.io/ublacklist/subscribe?name=whitelist&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/whitelist.txt">whitelist</a>

再分类订阅:

1. <a href="https://iorate.github.io/ublacklist/subscribe?name=wiki&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/wiki.txt">wiki</a>
2. <a href="https://iorate.github.io/ublacklist/subscribe?name=仓库&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/repository.txt">仓库</a>
3. <a href="https://iorate.github.io/ublacklist/subscribe?name=博客&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/blogs.txt">博客</a>
4. <a href="https://iorate.github.io/ublacklist/subscribe?name=论坛&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/bbs.txt">论坛</a>
5. <a href="https://iorate.github.io/ublacklist/subscribe?name=软件下载站&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/software.txt">软件下载站</a>
6. <a href="https://iorate.github.io/ublacklist/subscribe?name=文库&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/library.txt">文库</a>
7. <a href="https://iorate.github.io/ublacklist/subscribe?name=视频&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists/video.txt">视频</a>

或者不分类，直接订阅总列表: <a href="https://iorate.github.io/ublacklist/subscribe?name=whitelists_combined&url=https://raw.githubusercontent.com/bcaso/Google-Chinese-Results-Whitelist/main/whitelists_combined.txt">汇总列表</a>

分类订阅比订阅总列表的可控度高，根据内容需要，可在搜索前只启用一部分：

<img src="uBlacklist.png" width="80%" height="80%">



## other ways of using it

域名列表: <a href="./whitelists/domain_name.txt">./whitelists/domain_name.txt</a> ，在油猴脚本中改下判断规则代码就可以使用。


# reference

[Google I/O 2009 - Advanced Custom Search Configuration https://www.youtube.com/watch?v=fIUHTFvIt9c ](https://www.youtube.com/watch?v=fIUHTFvIt9c)

[google cse documentation https://developers.google.com/custom-search/docs/overview ](https://developers.google.com/custom-search/docs/overview)

[Gaga for Google Custom Search Engines https://www.youtube.com/watch?v=uX5nbIHRTAo ](https://www.youtube.com/watch?v=uX5nbIHRTAo)

[Google Custom Search Engines | Sourcing https://www.youtube.com/watch?v=t1szVhH5dIo ](https://www.youtube.com/watch?v=t1szVhH5dIo)

<a href="https://github.com/cobaltdisco/Google-Chinese-Results-Blocklist" target="_blank">uBlacklist 黑名单规则 github.com/cobaltdisco/Google-Chinese-Results-Blocklist</a>
