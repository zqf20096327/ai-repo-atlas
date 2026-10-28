# oniani/covid-19-chatbot

⭐ 21 · Python · 推送 2025-11-23 · [GitHub](https://github.com/oniani/covid-19-chatbot) · 个人维护

**用 COVID-19 论文语料微调 GPT-2 的问答聊天机器人（论文代码）**

论文配套代码：从 CORD-19 数据集的商业用子集（9000 篇学术论文）抽取摘要与正文合并为语料，重新训练 GPT-2 774M 模型（Adam 优化器、学习率 0.0001、2500 次迭代、batch size 8），模型托管于 Google Drive。提供命令行交互脚本与 Flask Web 应用（默认端口 5000），并给出 Google Colaboratory 上的迁移学习再训练示例。README 声明生成的健康信息仅供一般研究，非诊断工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 CORD-19 子集（9000 篇论文）重新训练 GPT-2 774M
- 提供命令行交互脚本与 Flask Web 应用
- 支持用自有数据在 Google Colaboratory 上做迁移学习

## 适用场景

- 复现论文中 COVID-19 问答实验
- 用自有语料对 GPT-2 做迁移学习
- 作为研究用途的领域问答聊天机器人运行

## 场景标签

`聊天机器人` `微调` · 领域:对话与助手

## 证据(README 行号)

> L29: We have retrained GPT-2 774M model with the COVID-19 corpus.
> L14: The dataset is the initial _commercial use subset_ taken from

## 星数曲线

```mermaid
xychart-beta
    title "oniani/covid-19-chatbot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `1d7dba35b627` · [字段定义](../../DATASET.md)*
