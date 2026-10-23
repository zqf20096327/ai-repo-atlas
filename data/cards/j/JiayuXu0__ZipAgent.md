# JiayuXu0/ZipAgent

⭐ 113 · Python · MIT · 推送 2026-08-03 · [GitHub](https://github.com/JiayuXu0/ZipAgent) · [官网](https://github.com/JiayuXu0/ZipAgent) · 个人维护 · 中文 README

**轻量级 Python AI Agent 框架，700 行核心代码构建智能助手**

Python 编写的 AI Agent 框架，以约 700 行核心代码实现 Agent 引擎、工具系统与对话管理，面向需要快速搭建智能助手的开发者。核心机制包括 @function_tool 装饰器定义工具、原生 MCP 协议集成外部工具、流式输出与多轮上下文管理，模型层通过 OpenAIModel 类接入 OpenAI API 或其他兼容 LLM API。要求 Python 3.10+ 与 API Key，pip 安装后几行代码即可运行 Agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- @function_tool 装饰器扩展工具，本地工具与 MCP 工具可混合使用
- 原生 MCP 集成连接外部工具
- 流式输出（StreamEventType）与多轮对话上下文管理
- 约 700 行核心代码，120+ 测试用例

## 适用场景

- 搭建客服、问答、闲聊机器人
- 构建代码助手、写作助手、数据分析助手
- 通过 MCP 集成 API、数据库、第三方服务做多步任务自动化

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L14: ZipAgent 是一个现代化的 Python AI Agent 框架，专注于简洁、高效和易扩展。**仅用 700 行核心代码实现 Agent 引擎、工具系统、对话管理的完整智能体框架，让你快速构建专属的 AI 助手。**
> L48: - **🔗 MCP 集成**: 原生支持 Model Context Protocol，集成外部工具

## 星数曲线

```mermaid
xychart-beta
    title "JiayuXu0/ZipAgent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23"]
    y-axis "stars" 111 --> 114
    line [112, 113, 113]
```

2026-10-18 112 → 2026-10-23 113（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `bf06eb25e44a` · [字段定义](../../DATASET.md)*
