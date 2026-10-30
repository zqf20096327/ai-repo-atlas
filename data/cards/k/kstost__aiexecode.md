# kstost/aiexecode

⭐ 16 · JavaScript · NOASSERTION · 推送 2026-01-25 · [GitHub](https://github.com/kstost/aiexecode) · [官网](https://aiexecode.com/) · 个人维护

**自然语言驱动的 CLI 自主编程 Agent，接入 Z.AI GLM 模型**

面向开发者的命令行 AI 编程代理：用户用自然语言描述任务，AI 自行分析代码、制定计划并执行，覆盖修 bug、加功能、重构、写测试、补文档等场景。模型侧接入 Z.AI 的 GLM 系列（glm-4.5 默认，支持 glm-4.7/4.6/4.5-air，需 Z.AI API key），提供会话暂停恢复、Web 日志查看器、MCP 服务器扩展、自定义提示词/命令/技能与 AGENTS.md 项目上下文。内置 10 个工具（文件编辑、bash、Python 执行、网页抓取、ripgrep 搜索等）。限制：不支持 Windows；需 Node.js 18+ 与 ripgrep。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言描述任务，AI 自主分析与执行
- 接入 Z.AI GLM 系列（glm-4.5 默认，支持 200K 上下文模型）
- 会话管理与 Web 日志查看器（localhost:3000）
- MCP 服务器集成与项目级提示词/命令/技能自定义

## 适用场景

- 用一句话让 AI 修复代码中的 lint 错误或 bug
- 为现有项目添加新功能并生成单元测试
- 暂停后用 session ID 恢复之前的编码任务

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11: **AIEXEcode** is a CLI-based AI coding agent that autonomously handles software development tasks. Simply describe 
> L20: - **Z.AI Integration**: Powered by Z.AI's advanced GLM models

## 星数曲线

```mermaid
xychart-beta
    title "kstost/aiexecode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4dcebeb4fe0f` · [字段定义](../../DATASET.md)*
