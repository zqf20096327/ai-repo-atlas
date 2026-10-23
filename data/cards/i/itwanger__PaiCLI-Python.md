# itwanger/PaiCLI-Python

⭐ 106 · Python · MIT · 推送 2026-07-28 · [GitHub](https://github.com/itwanger/PaiCLI-Python) · 个人维护 · 中文 README

**终端 AI Agent CLI：面向真实项目开发的读写/执行/检索/记忆工具链**

Python 实现的终端 AI Agent CLI，面向真实项目开发场景：内置文件读写、Shell、grep、glob、网页搜索抓取等工具，支持 ReAct、Plan-and-Execute 与 Multi-Agent 三种模式。OpenAI-compatible 流式客户端默认面向 DeepSeek 配置，支持 MCP client/server、Skill 分层加载、SQLite 长期记忆、上下文压缩、快照恢复，并通过 Runtime API 对外提供线程、事件和后台任务。危险操作经 HITL 确认与审计日志。需 Python 3.11+ 与 uv，通过 git clone 源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ReAct / Plan-and-Execute / Multi-Agent 三种运行模式
- MCP client 与自身可作为 MCP server 暴露内置工具
- 静态+SQLite 动态记忆、上下文预算压缩与快照恢复
- Runtime API 提供线程、事件日志与持久化后台任务

## 适用场景

- 在终端里让 Agent 读写文件、执行命令、搜索代码完成开发任务
- 通过 Runtime API 把 Agent 线程和后台任务接入外部系统
- 学习 Agent 工程（ReAct、MCP、记忆、RAG）并准备简历面试

## 场景标签

`编码 Agent` `Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: PaiCLI Python 是一个运行在终端里的 AI Agent CLI，面向真实项目开发场景：读写文件、搜索代码、执行命令、联网检索、调用 MCP 工具、保存记忆、生成快照、恢复现场，并通过 Runtime API 对外提供线程
> L26: - OpenAI-compatible 流式 LLM 客户端，默认面向 DeepSeek 配置

## 星数曲线

```mermaid
xychart-beta
    title "itwanger/PaiCLI-Python 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 105 --> 108
    line [107, 106, 106]
```

2026-10-18 107 → 2026-10-23 106（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `6e564ce4bfdf` · [字段定义](../../DATASET.md)*
