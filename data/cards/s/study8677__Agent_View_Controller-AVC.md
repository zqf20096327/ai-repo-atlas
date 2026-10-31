# study8677/Agent_View_Controller-AVC

⭐ 69 · JavaScript · Apache-2.0 · 推送 2026-05-22 · [GitHub](https://github.com/study8677/Agent_View_Controller-AVC) · [官网](https://github.com/study8677/Agent_View_Controller-AVC/releases/latest) · 个人维护 · 中文 README

**给 CLI 编码 agent 的可视化人机决策管道：JSON 进、改后 JSON 出**

Go 编写的 3MB 单二进制 Unix 管道工具：从 stdin 读取 JSON，弹出系统原生 WebView 窗口，人通过拖拽、编辑、排序、跳过步骤做可视化决策，修改后的 JSON 写回 stdout，agent 继续执行。内置 token 阈值过滤（默认 3000），短内容直接透传不弹窗。支持 plan 与 graph 两种视图，diff/table 等在路线图中。面向配合 Codex CLI、Claude Code、Gemini CLI、Cursor 等 agent 使用，通过技能目录或项目配置文件接入。UI 支持 7 种语言。macOS 经 CI 验证，Linux/Windows 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- stdin JSON → 原生 WebView 交互 → stdout 修改后 JSON 的管道模式
- token 阈值过滤：短内容透传，超 3000 token 才弹窗
- plan/graph 视图就绪，支持拖拽排序、编辑、跳过、增删步骤
- agent 无关：提供 Claude Code / Codex / Gemini / Cursor 的技能与配置接入方式

## 适用场景

- 让 agent 生成的多步执行计划经人工可视化确认后再执行
- 在终端管道中人工审阅并修改 agent 输出的架构图或迁移方案
- 为多种 CLI 编码 agent 统一挂一个人工决策 UI

## 场景标签

 · 领域:开发者工具/AI agent 交互

## 证据(README 行号)

> L223: ## Using AVC with AI Agents
> L227: ### ⭐ Method 1: Install as a Skill (Recommended)

## 星数曲线

```mermaid
xychart-beta
    title "study8677/Agent_View_Controller-AVC 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-31 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `79484aa281a7` · [字段定义](../../DATASET.md)*
