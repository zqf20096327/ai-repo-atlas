# DavidVeksler/CodeContext

⭐ 23 · C# · MIT · 推送 2026-10-14 · [GitHub](https://github.com/DavidVeksler/CodeContext) · 个人维护

**将代码库转为文本供 LLM 读取的 CLI 工具与 MCP 服务器**

跨平台 C#/.NET 9 命令行工具，同时可作为 MCP（Model Context Protocol）服务器：扫描项目目录，生成层级结构与源码内容文本，自动过滤二进制、依赖与生成代码，遵循 .gitignore 规则，供 ChatGPT、Claude 等 AI 编程助手使用。agentic 模式下支持 token 预算优化与基于任务描述的相关性评分，提供 GreedyByScore、ValueOptimized、Balanced 三种文件选择策略，输出纯文本或 JSON。需 .NET 9 SDK，通过 git clone 源码构建运行；README 提示另有 code2prompt 等替代工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成项目层级结构与源码内容文本，自动过滤二进制/依赖/生成代码
- MCP 服务器模式，提供 GetCodeContext、GetProjectStructure 等 4 个工具
- token 预算优化与按任务描述的文件相关性评分（3 种选择策略）
- 遵循 .gitignore，支持纯文本与 JSON 两种输出格式

## 适用场景

- 把整个项目喂给 ChatGPT/Claude 而无需手动复制粘贴文件
- 在 Claude Code、Cline 等 agent 中按任务按预算获取代码上下文
- 大代码库中按相关性筛选文件控制 token 消耗

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: CodeContext is a cross-platform C# CLI tool and MCP (Model Context Protocol) server for Mac, Windows, and Linux that
> L30: - **MCP Server Mode**: Native integration with Claude Code, Cline, and other MCP-compatible agents
> L120: CodeContext now supports **Model Context Protocol (MCP)**, enabling native integration with agentic coding tools l

## 星数曲线

```mermaid
xychart-beta
    title "DavidVeksler/CodeContext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `847bcb2c31e6` · [字段定义](../../DATASET.md)*
