# IvanMurzak/Unity-AI-Tools-Template

⭐ 22 · C# · MIT · 推送 2026-10-16 · [GitHub](https://github.com/IvanMurzak/Unity-AI-Tools-Template) · 个人维护

**Unity MCP 工具/RQL 扩展的项目模板，供 AI 游戏开发者定制**

面向 Unity 引擎 MCP 工具开发的项目模板：通过 init.ps1 初始化脚本重命名包并替换占位符，指导开发者将模板转为可发布的 Unity 包（更新 package.json、生成 .meta 文件、配置 CI/CD、发布到 OpenUPM/npm/GitHub）。扩展机制以 RQL 模块为主——注册类型适配器、源与指南供 agent 通过 rql-query/rql-mutate/rql-schema 三个通用工具读写 Unity 场景与资产；仅对 RQL 无法表达的场景（二进制输出、长耗时任务、外部进程）才添加经典 MCP 工具，按 Editor/Runtime 目录划分运行环境。模板附测试基类与示例代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 初始化脚本一键重命名包并替换全部占位符
- 以 RQL 模块（类型适配器/源/指南）扩展 agent 对 Unity 场景与资产的读写
- 仅为二进制输出、长耗时或异步任务提供经典 MCP 工具（Editor/Runtime 两类运行环境）
- 包含版本管理脚本、GitHub Actions CI/CD 示例与 OpenUPM/npm/GitHub 发布指引

## 适用场景

- 快速创建自己的 Unity MCP 工具或 RQL 扩展包
- 让 AI agent 通过 RQL 查询与修改 Unity 场景和资产
- 按模板流程把自定义工具发布到 OpenUPM 供他人安装

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: Template for AI MCP Tools for AI Game Developer (Unity-MCP). Use this template to create your custom MCP tools for U
> L65: AI Game Developer gives agents three generic tools: `rql-query`, `rql-mutate` and `rql-schema`
> L99: Add a classic MCP tool only for binary output (images, files), long-running or asynchronous work (builds, bakes, im

## 星数曲线

```mermaid
xychart-beta
    title "IvanMurzak/Unity-AI-Tools-Template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-31 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d941deb9e161` · [字段定义](../../DATASET.md)*
