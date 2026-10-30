# Windsland52/create-maa-project

⭐ 15 · TypeScript · AGPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/Windsland52/create-maa-project) · 个人维护 · 中文 README

**MaaFW 项目脚手架 CLI 与 MCP Server，生成并维护 Pipeline/Agent 项目**

面向 MaaFramework（MaaFW）应用开发者的脚手架工具：交互式问答后生成可直接构建的 Pipeline 或 Python Agent 项目，选择记录在 maa-project.json 中，通过 --add/--sync/--update/--doctor 命令做增量维护与只读诊断；写入前登记备份、失败自动回滚，并提供稳定 JSON report（CMP_* 错误码）。AI coding agent 可经 Agent Skill 包或内置 MCP stdio server 接入，两条路径共用同一写入路径。CLI 自身不含 OCR，但负责获取 OCR 模型、MaaFW runtime 等资产。经 npm/PyPI 分发，需 Node.js >= 22.13。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成 Pipeline / Python Agent 两类 MaaFW 项目，--doctor 只读诊断
- Agent Skill 与内置 MCP stdio server 两种 AI 接入方式，共用写入与回滚机制
- 写入前备份、失败自动回滚、项目运行锁与 stale lock 清理
- --report 输出机器可读 JSON（schemaVersion、CMP_* 错误码）

## 适用场景

- 快速创建可提交、可构建的 MaaFramework Pipeline 或 Agent 项目
- 让 Claude Code 等 AI 工具经 Agent Skill 或 MCP 调用 CLI 生成和维护项目
- 为已有 MaaFW 项目补齐 OCR 模型、runtime 与 add-ons

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L11: `create-maa-project` 是 MaaFramework（MaaFW）应用项目的脚手架 CLI：回答几个问题，它会生成一个可以直接提交、构建的 Pipeline 或 Python Agent 项目。创建时的所有选择都
> L13: AI coding agent 推荐通过 Agent Skill 接入：agent 读取工作流指引后，直接调用与人类用户相同的 CLI 命令。CLI 也内置 MCP stdio server 作为替代接入方式，适合 agent 没

## 星数曲线

```mermaid
xychart-beta
    title "Windsland52/create-maa-project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e4283deecb67` · [字段定义](../../DATASET.md)*
