# snowdreamtech/template

⭐ 16 · Shell · MIT · 推送 2026-10-30 · [GitHub](https://github.com/snowdreamtech/template) · [官网](https://snowdreamtech.github.io/template/) · 组织维护 · 中文 README

**面向多 AI IDE 协作的企业级项目基础模板（50+ IDE 规则统一）**

解决多 AI 辅助 IDE 配置碎片化问题的基础脚手架：以 `.agent/rules/` 作为 AI agent 行为规则、工作流与项目配置的 Single Source of Truth，通过符号链接/重定向模式将规则同步到 Cursor、GitHub Copilot、Claude Code 等 50+ AI 编辑器；内置 88 个语言/框架规则文件与 SpecKit 标准化工作流命令，配合 POSIX Shell 自动化与 pre-commit、GitHub Actions 三层质量门。运行需 Node.js ≥20、Python ≥3.10 与全局 Git，通过 unirtm 命令初始化安装。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- `.agent/rules/` 单一规则源，经 symlink/redirect 同步至 50+ AI IDE
- 88 个语言/框架行为规则文件（Rust/Go/TypeScript/Kubernetes 等）
- SpecKit 标准化工作流命令跨环境一致运行
- 跨 macOS/Linux/Windows 的 POSIX Shell 自动化与三层质量门

## 适用场景

- 统一团队在 Cursor、Copilot、Claude Code 等多个 AI IDE 中的 agent 行为规则
- 为多语言项目提供预置的编码规范与工作流脚手架
- 通过质量门在 IDE、pre-commit、CI 三层保证代码一致性

## 场景标签

 · 领域:开发工具/AI 工程化

## 证据(README 行号)

> L20: An enterprise-grade, foundational template designed for multi-AI IDE collaboration. This repository serves as a **S
> L25: - **Unified Rule System**: Centralized rule definitions in `.agent/rules/`. Changes propagate automatically to all 
> L39: - Provides a **Unified Rule Engine** that governs AI behavior consistently across 50+ IDEs.

## 星数曲线

```mermaid
xychart-beta
    title "snowdreamtech/template 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `d182ef5f651d` · [字段定义](../../DATASET.md)*
