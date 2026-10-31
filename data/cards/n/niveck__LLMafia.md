# niveck/LLMafia

⭐ 25 · Python · MIT · 推送 2025-11-12 · [GitHub](https://github.com/niveck/LLMafia) · [官网](https://niveck.github.io/Time-to-Talk/) · 组织维护

**异步 LLM Agent：与真人进行线上狼人杀对局的研究代码与数据集**

EMNLP 2025 Findings 论文 "Time to Talk" 的开源代码与数据：构建一个由 scheduler（决定何时发言）与 generator（决定说什么）两个模块组成的自适应异步 LLM Agent，嵌入多人异步群聊中与真人玩家进行在线 Mafia（狼人杀）对局，并以对局胜负与融入人类玩家的程度作为评估指标。仓库 games 目录收录采集的对局数据（消息、元数据、结果、配置，已匿名化），完整数据托管在 HuggingFace，README 未给出安装运行命令。

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

- scheduler+generator 双模块的异步群聊 Agent 设计
- 与真人玩家进行在线 Mafia 对局并采集评估数据
- games 目录收录匿名化的对局消息、元数据与结果
- 附 EMNLP 2025 Findings 论文

## 适用场景

- 研究 LLM 在异步群聊中的发言时机与内容生成
- 复现论文中对局实验与分析
- 获取真人+LLM 混合的社交推理游戏对话数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: Our Mafia games code for an **Asynchronous LLM Agent** playing games of *Mafia* with multiple human players.
> L15: In our paper we propose an agent designed for asynchronous conversations. Our agent consists of two modules: the *s
> L33: The collected data of games is available under the `games` directory.

## 星数曲线

```mermaid
xychart-beta
    title "niveck/LLMafia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-31 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `7d47772e973f` · [字段定义](../../DATASET.md)*
