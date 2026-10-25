# KubeRocketCI/kuberocketai

⭐ 34 · Go · Apache-2.0 · 推送 2026-01-15 · [GitHub](https://github.com/KubeRocketCI/kuberocketai) · [官网](https://krci-ai.kuberocketci.io) · 组织维护

**AI-as-Code 框架：以版本化 Markdown 定义、校验并分发 AI agent**

面向团队规模化复用 AI agent 的声明式框架：将 agent 定义为带 YAML frontmatter 的 Markdown 文件，纳入版本控制，通过 krci-ai CLI 注入 IDE（如 Cursor）、CI 流水线或打包为带完整项目上下文的 Markdown 供 Web 聊天工具使用；提供安装前的配置与依赖校验机制，支持跨多仓库维护 agent 库。以 Go 编写，提供 Homebrew、二进制下载与源码构建三种安装方式，Apache-2.0 许可，由 KubeRocketCI 团队维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 以 Markdown + YAML frontmatter 定义并纳入版本控制
- 同一 agent 定义可注入 IDE、CI 流水线或打包供 Web 聊天使用
- 部署前内置配置与依赖校验
- 提供 macOS/Linux/Windows 安装与 CLI 工具 krci-ai

## 适用场景

- 团队把已验证的 agent 配置像 Pipeline-as-Code 一样分发与回滚
- 同一 agent 定义在 IDE 编码、CI 代码审查与头脑风暴间复用
- 跨多个仓库维护一致的 agent 配置库

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L12: AI-as-Code framework for structuring AI-assisted software development. Define AI agents as version-controlled Markd
> L39: KubeRocketAI brings the proven **"Pipeline-as-Code" model to AI agent management**. Teams define agents in version-
> L53: 1. **Agent-as-Code Distribution**: Version-control and share your proven agent configurations just like you do with

## 星数曲线

```mermaid
xychart-beta
    title "KubeRocketCI/kuberocketai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-25 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `2e88c9342d73` · [字段定义](../../DATASET.md)*
