# halfrost/threes-ai

⭐ 165 · Python · GPL-3.0 · 推送 2026-08-24 · [GitHub](https://github.com/halfrost/threes-ai) · [官网](https://threes.halfrost.com) · 个人维护 · 中文 README

**用 Go 实现的 Threes! 游戏自动对弈 AI（Expectimax 搜索）**

Go 编写的 Threes! 棋盘游戏 AI，采用 Expectimax 最大期望搜索树：枚举四方向移动与新砖块出现的概率分布递归计算期望值，以权重矩阵与棋盘矩阵相乘评估局面，通过概率阈值与样本方差限制递归深度。附带按官方规则复刻的 Meteor web 版游戏，Go 服务端监听 9000 端口，经 websocket 通信；也可编译为 c-shared 动态库供 Python 调用，配合 Chrome remote debug 在官方网页版上代下棋。README 记录了三处 200 盘跑分、游戏分析与 MCTS/Minimax 算法讨论，机器学习第二版列为 To-Do 未实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Expectimax 搜索树按新砖块概率分布递归计算期望值
- Go 打包 c-shared 动态库（threes.so）供 Python 调用
- 附带 Meteor 复刻 web 版与 Docker 镜像（go/web 各一）
- 支持经 Chrome remote debug 接入官方网页版代下棋

## 适用场景

- 观察 AI 在 Threes! 中自动对弈刷分
- 研究 Expectimax/棋盘游戏 AI 的实现方式
- 本地或 Docker 部署复刻版 web 游戏进行测试

## 场景标签

 · 领域:游戏 AI/算法实现

## 证据(README 行号)

> L1: 🤖 AI for the Threes! game. 🎮
> L142: 接下来需要利用 chrome 的 remote debug 模式，建立一个 ws 连接。`threes_ai_web.py` 干的事情就是把 web 上的棋盘数字信息传递给 go，go 函数处理完成以后返回下一步要移动的方向。最

## 星数曲线

```mermaid
xychart-beta
    title "halfrost/threes-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 164 --> 166
    line [165, 165]
```

2026-10-18 165 → 2026-10-27 165（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8d2c77f50893` · [字段定义](../../DATASET.md)*
