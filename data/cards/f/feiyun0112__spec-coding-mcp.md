# feiyun0112/spec-coding-mcp

⭐ 50 · C# · MIT · 推送 2026-01-08 · [GitHub](https://github.com/feiyun0112/spec-coding-mcp) · 个人维护 · 中文 README

**为 AI IDE 提供规格驱动开发流程的 MCP Server**

基于 Model Context Protocol 的 MCP 服务器，将规格驱动开发（Spec-Driven Development）流程接入 AI IDE（如 GitHub Copilot）。通过"Spec 文件夹"机制，为每个功能模块生成三个文件：EARS 语法的需求文档 requirements.md、技术方案 design.md、可执行任务清单 tasks.md，由 AI IDE 依次完成功能定义、需求收集、设计、任务规划与逐项执行。以 NuGet 包 SpecCodingMcpServer 分发，需要 .NET 10 运行时，在 VS Code 中通过 .vscode/mcp.json 配置接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 为每个功能模块生成 requirements.md / design.md / tasks.md 三文件结构
- 需求文档采用 EARS 语法编写用户故事与验收标准
- 兼容任何支持 MCP 的 AI IDE，以 GitHub Copilot 为示例演示
- 通过 NuGet 包分发，接入 VS Code 工作区配置即可使用

## 适用场景

- 在 AI IDE 中按规格驱动流程从想法生成可执行的开发计划
- 把模糊需求转化为可追溯、可验证的规格文档再编码
- 用结构化 Spec 文件夹管理功能模块的开发过程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L23: > The MCP in `spec-coding-mcp` stands for Model Context Protocol, which is an important bridge connecting external 
> L39: `SpecCodingMcpServer` requires `.NET 10` to run. Please ensure you have .NET 10 installed locally (https://dotnet.m

## 星数曲线

```mermaid
xychart-beta
    title "feiyun0112/spec-coding-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-25 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c1ee8089a661` · [字段定义](../../DATASET.md)*
