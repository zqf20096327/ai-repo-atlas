# optimalone/build-your-own-coding-agent

⭐ 105 · Python · MIT · 推送 2026-03-30 · [GitHub](https://github.com/optimalone/build-your-own-coding-agent) · [官网](https://buildyourowncodingagent.com) · 个人维护

**《Build Your Own Coding Agent》一书配套源码：用纯 Python 从零构建编码 agent**

教学书的配套代码仓库：分 12 章逐步构建终端 AI 编码 agent 'Nanocode'，每章目录是可运行的代码快照，覆盖事件循环、多 provider 接入（Claude/DeepSeek/Ollama 本地模型）、文件读写工具、跨会话持久记忆、命令执行反馈循环、DuckDuckGo 网络搜索与流式输出，最终约 700 行脚本。不依赖 LangChain 等框架，仅用 requests 与 subprocess。需 Python 3.10+ 与 Anthropic API key，DeepSeek/Ollama 为可选项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 章递进式可运行代码快照，从事件循环到最终 agent
- 支持 Claude、DeepSeek 与 Ollama 本地模型多 provider 接入
- 不依赖编排框架，仅用 requests/subprocess 实现
- 含计划模式安全机制与跨会话持久记忆

## 适用场景

- 跟随书籍分章学习编码 agent 的构建原理
- 获得一个可运行的最小终端编码 agent 作为改造起点
- 了解如何接入本地 Ollama 模型运行 agent

## 场景标签

`教程课程` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: This is the companion code repository for **Build Your Own Coding Agent** — a book that teaches you how to build an 
> L22: Each `chXX/` folder contains a complete, runnable snapshot of the code at the end of that chapter:

## 星数曲线

```mermaid
xychart-beta
    title "optimalone/build-your-own-coding-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 104 --> 106
    line [105, 105]
```

2026-10-18 105 → 2026-10-24 105（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `6d168b73c0ea` · [字段定义](../../DATASET.md)*
