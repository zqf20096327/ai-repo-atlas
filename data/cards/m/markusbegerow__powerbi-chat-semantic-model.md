# markusbegerow/powerbi-chat-semantic-model

⭐ 22 · JavaScript · GPL-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/markusbegerow/powerbi-chat-semantic-model) · [官网](https://markus-begerow.de/linktree) · 个人维护

**Power BI 外部工具：用聊天界面借助 AI 分析语义模型**

基于 Electron 的 Windows 桌面应用，注册为 Power BI Desktop 外部工具，通过 XMLA 端点与 ADOMD.NET 桥接读取语义模型的表、列、度量值、关系与示例数据。用户在聊天界面中提问、生成并执行 DAX 查询，AI 部分由 OpenAI、Azure OpenAI 或本地 LLM 端点（如 Ollama）提供。需自行编译 .NET 桥（dotnet build），AI 功能依赖外部 API key，本体不含模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经 XMLA 端点实时连接 Power BI Desktop 语义模型，展示元数据与示例数据
- 聊天界面内生成并执行 DAX 查询
- 支持 OpenAI / Azure OpenAI / 本地 LLM 端点配置
- 以 install-tool.bat 注册为 Power BI 外部工具，也可独立运行

## 适用场景

- 在 Power BI 中对话式浏览语义模型结构与关系
- 让 AI 帮我编写并执行 DAX 查询
- 用本地 LLM 端点分析数据模型而不依赖云端 API

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: An AI-powered Power BI External Tool that provides an intelligent chat interface to analyze and interact with your P
> L14: - **AI-Powered Assistant** - Uses OpenAI or compatible APIs to provide intelligent insights about your data model
> L16: - **DAX Query Execution** - Execute DAX queries directly from the chat interface

## 星数曲线

```mermaid
xychart-beta
    title "markusbegerow/powerbi-chat-semantic-model 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `b1d4cb027c43` · [字段定义](../../DATASET.md)*
