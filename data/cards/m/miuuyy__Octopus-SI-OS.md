# miuuyy/Octopus-SI-OS

⭐ 872 · Rust · MIT · 推送 2026-11-24 · [GitHub](https://github.com/miuuyy/Octopus-SI-OS) · 个人维护

**给长期自主运行 agent 的自演化操作系统（研究预览）**

一个基于操作系统原理构建的 agent 持久化工作平台：目标、权限、运行、工具、上下文以持久记录形式存在，Rust 内核负责授权生成、工件移动与追加式账本记录。用户通过 macOS 客户端或终端客户端以文本/语音对话，创建 Projects、Agents、Tasks 并授予文件、浏览器、桌面应用等工具权限。默认模型为 Gemini 4 Neon（经 Antigravity），初始登录依赖 ChatGPT 账号。项目自述为研究预览，面向长时程开放自主任务，非标准基准或日常编码用途。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Rust 内核 + append-only movement ledger 记录边界跨越（含拒绝）
- 自演化机制：agent 可创建/修订目标、新增接口与工具并跨任务持久化
- macOS 客户端支持语音通话、Projects/Agents/Tasks 管理与终端客户端共享状态
- 运行时 provider-agnostic，接口以 JSON 文件夹方式声明式接入

## 适用场景

- 让 agent 在数小时到数天的长时程任务中自主组织目标与触发器
- 以显式授权和沙箱方式管理 agent 对文件/浏览器/桌面应用的访问
- 为 agent 自行编写驱动和接口并注册进系统做实验

## 场景标签

`Agent 框架` `GUI 自动化` · 领域:Agent 开发

## 证据(README 行号)

> L16: Octopus is an operating system for persistent agent work. Goals, permissions,
> L41: > Octopus gives you nothing that a plain agent loop like Codex CLI does not
> L47: > Active experiments focus there while the runtime stays provider-agnostic, with

## 星数曲线

```mermaid
xychart-beta
    title "miuuyy/Octopus-SI-OS 星数(近 26 点)"
    x-axis ["2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 0 --> 957
    line [13, 15, 16, 316, 537, 581, 603, 613, 623, 626, 629, 16, 734, 755, 757, 760, 761, 765, 771, 773, 775, 776, 779, 777, 827, 872]
```

2026-10-23 13 → 2026-11-25 872（+859）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `215f5530d377` · [字段定义](../../DATASET.md)*
