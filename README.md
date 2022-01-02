# AI版的五子棋小游戏 
## 内容简介 
 本项目实现的五子棋博弈游戏是基于AI的五子棋游戏。游戏模式可以分为人机对弈和双人对弈两种模式。本程序采用基于启发式max/min算法的alpha-beta剪枝技术来选择出最佳的机器落子位置。除此之外，本项目还设置了残局闯关模式，在增加了游戏趣味性的同时给用户们带来了更好的游戏体验。
## 算法描述 
本程序主要是用 α-β 剪枝法实现的。其基本思想或算法是，边生成博弈树边计算评估各节点的倒推值，并且根据评估出的倒推值范围，及时停止扩展那些已无必要再扩展的子节点，即相当于剪去了博弈树上的一些分枝，从而节约了机器开销，提高了搜索效率。具体的剪枝方法如下:

- 对于一个与节点 MIN，若能估计出其倒推值的上确界 β，并且这个 β值不大于 MIN 的父节点(一定是或节点)的估计倒推值的下确界 a，即a≥β，则就不必再扩展该 MIN 节点的其余子节点了(因为这些节点的估值对MIN 父节点的倒推值已无任何影响了)。 这一过程称为 a 剪枝。

- 对于一个或节点 MAX,若能估计出其倒推值的下确界 a，并且这个 a 值不小于 MAX 的父节点(- -定是与节点)的估计倒推值的上确界 β，即 a≥β，则就不必再扩展该 MAX 节点的其余子节点了(因为这些节点的估值对 MAX 父
节点的倒推值已无任何影响了)。 这一过程称为 β 剪枝。
![α-β 剪枝](https://img-blog.csdnimg.cn/603957ec6ed44cc0bcab9787d1fe2858.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaHltZWkw,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
## 基本设计 

 - [ ] 界面设计：
基于 tkinter 设计的界面，包括游戏模式菜单、残局菜单，
关于菜单三个部分组成，游戏模式菜单部分包括了人机对弈（AI 先手）、人机对弈（玩家先手）、双人对弈（白子先手）、双人对弈黑子先手）等多种模式，各种模式的随意切换，突出程序灵活的特性。残局菜单栏我们设计了五种残局，难易程度程度依次递增，增强了游戏的趣味性。

 - [ ] 棋盘设计：
我们的程序棋盘的显示部分是利用 tkinter 库的画布实现的，画布的背景设
置为水鸭色，界面大气美观。在画布上画上 14*14 的小格子表示棋盘，交点处放棋子，所以棋盘的大小为 15*15。程序中的棋盘对应 15*15 的二维数组 chess_b，初始化为 0，黑子用 1 填充数组，白子用 2 填充数组。
至于画棋子，我们是根据棋盘数组将对应的位置用贴图的方法将黑棋白棋贴
上去。
 - [ ] 胜负判断：
只需考虑横、竖、左斜和右斜四个方向，当棋盘数组 chess_b 中某个方向存在连续的五个‘1’或者‘2’时即黑子或者白子胜利，程序调用重置函数，清空棋盘，进入初始换界面，然后选择模式可继续开新局。
## 效果展示
![人机对弈](https://img-blog.csdnimg.cn/4dbff7ebf5984114abeeaba61f458a11.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaHltZWkw,size_20,color_FFFFFF,t_70,g_se,x_16)
![残局挑战](https://img-blog.csdnimg.cn/2629cbe5e0cc41a08901360415cb2f30.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAaHltZWkw,size_20,color_FFFFFF,t_70,g_se,x_16)

项目地址：[https://github.com/hymei0/5chess](https://github.com/hymei0/5chess)
