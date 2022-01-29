Whitelist = {
        'gitee':['','io'],
        'github': ['','io'],          # 没法 用 @://github.*/* 来表示 .com 和 .io，因为这条规则是有问题的
        'cnblogs':['www','com'],      # 博客园，加上 www 是为了过滤 https://recomm.cnblogs.com/ 这个地址
        'zhihu':['zhuanlan','com'],   # 知乎专栏
        'liaoxuefeng':['','com/wiki'],# 廖雪峰的官方网站
        'ruanyifeng':['','com'],      # 阮一峰的网络日志
        'coolshell':['','cn/articles'],        # 酷壳
        'leetcode-cn':['','com/problems'], # 乐扣试题区，不好分类的网址

}
