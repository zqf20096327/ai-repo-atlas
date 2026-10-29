# harper-nottinghill/julia-reader

⭐ 18 · Python · MIT · 推送 2026-05-10 · [GitHub](https://github.com/harper-nottinghill/julia-reader) · 个人维护

**渐进式长文阅读工具：分块 LLM 摘要生成 Markdown 书册**

纯标准库 Python CLI，读取长文本（转录稿、日志、笔记），执行句子切分、有界分块（≤2000 token 估算）、软主题断点，逐块调用 OpenAI 兼容 HTTP 端点生成 JSON 摘要并维护逐步演化的理解，最终规划并生成 Markdown 书册（索引、前言、章节）与含校验报告的 packet，输出到 _reader/ 时间戳目录。支持 --no-llm 离线启发式运行。面向希望实验机器阅读结构的开发者与研究者。附 Next.js 演示。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐块 LLM 摘要与持续更新的 live understanding
- 生成 Markdown Chronicle 书册与 validation_report 校验报告
- 仅标准库 Python，接入任意 OpenAI 兼容端点
- --no-llm 离线启发式回退模式

## 适用场景

- 把长转录稿或日志整理成可浏览引用的 Markdown 书册
- 实验不同的分块策略与机器阅读流程
- 无 LLM 环境下用启发式生成本地摘要

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: This repo is a **standalone progressive Reader harness** for the terminal: sentence splitting, dynamic chunking (≤20
> L9: **What it does.** Julia Reader ingests long, messy source text (transcripts, logs, notes) and walks it the way a car
> L135: 3. **Per-chunk LLM** — JSON chunk summary + live summary update (silent HTTP; no harness streaming).

## 星数曲线

```mermaid
xychart-beta
    title "harper-nottinghill/julia-reader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `05e3a088b699` · [字段定义](../../DATASET.md)*
