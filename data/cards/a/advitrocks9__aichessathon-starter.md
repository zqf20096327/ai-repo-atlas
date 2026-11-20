# advitrocks9/aichessathon-starter

⭐ 10 · Python · MIT · 推送 2026-09-12 · [GitHub](https://github.com/advitrocks9/aichessathon-starter) · [官网](https://aichessathon.com) · 个人维护

**AI Chessathon 黑客马拉松的 agent 开发起点模板**

面向 AI Chessathon 参赛者的 fork 起始仓库：提供可提交的 agent.py（单函数 get_move(fen, time_left_ms)）、四个基线 agent（random/greedy/minimax/numba），以及与平台协议和时钟一致的本地对局 harness。支持 make play 单局、make arena 多局计分、PGN 记录、基于局号的确定性回放，make zip 打包并自动跑两局冒烟测试以降低上传失败成本。规则以 aichessathon.com/docs 为准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单函数 get_move(fen, time_left_ms) 的提交接口，内置合法随机走子起步
- 本地 harness 与平台协议、时钟一致，支持对局与多局 arena 计分（含置信区间）
- 四个基线：随机、单层贪心、两层 minimax、numba 加速版
- make zip 打包并自动运行平台冒烟对局验证

## 适用场景

- fork 后直接开发可提交的 AI Chessathon 棋类 agent
- 本地与基线对弈检验改动是否有效再上传
- 用 arena 脚本批量对局并查看胜率与区间

## 场景标签

`Agent 框架` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L3: Fork this to build an agent for AI Chessathon. It gives you a working
> L22: def get_move(fen: str, time_left_ms: int) -> str:

## 星数曲线

```mermaid
xychart-beta
    title "advitrocks9/aichessathon-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-11-20"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-18 10 → 2026-11-20 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `63d0dee5ed2f` · [字段定义](../../DATASET.md)*
