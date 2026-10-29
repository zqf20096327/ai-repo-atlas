# Ranrar/rustic-prompt

⭐ 57 · MIT · 推送 2026-02-03 · [GitHub](https://github.com/Ranrar/rustic-prompt) · 个人维护

**面向 Rust 开发者的 AI 指令文件集合：为编码助手提供提示词**

面向 Rust 开发者的 AI 指令文件（instruction files）合集，用于驱动 GitHub Copilot、VS Code 等 AI 开发助手。内容含 Rust 专项指令包（代码规范、跨平台编译、lint 分析、Pest 解析器、RON）、路径感知的多 agent 指令包（含路由 index 与各领域专家文件），以及通用指令（语法错误诊断、调试、文本卫生、GitHub 安全）。README 给出三种接入方式：Custom Instructions 持久模式、Chat Mode 会话模式、Agents 多步工作流。另附带推荐 VS Code 扩展清单与外部 prompt 仓库索引。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 专项指令包覆盖跨平台编译、lint 分析、Pest、RON
- 多 agent 指令包：路径感知的 index 路由 + 各专家文件
- 三种 VS Code 接入方式（Instructions/Chat Mode/Agents）
- 通用语言指令（语法诊断、调试、GitHub 安全）

## 适用场景

- 给 Copilot 等编码助手配置 Rust 编码规范与工作流
- 用多 agent 指令包做 lint 排查、Pest 语法、RON 等专项任务
- 在 VS Code 中以 chat mode 临时应用某个调试或迁移指南

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L2: A collection of AI instruction files designed specifically for **Rust developers**.
> L5: - **Instruction sets** - predefined prompts and role definitions for Rust-related tasks.

## 星数曲线

```mermaid
xychart-beta
    title "Ranrar/rustic-prompt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 56 --> 58
    line [57, 57]
```

2026-10-18 57 → 2026-10-29 57（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `50a961d5e0b4` · [字段定义](../../DATASET.md)*
