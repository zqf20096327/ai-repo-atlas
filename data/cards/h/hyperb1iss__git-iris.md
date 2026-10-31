# hyperb1iss/git-iris

⭐ 43 · Rust · Apache-2.0 · 推送 2026-09-07 · [GitHub](https://github.com/hyperb1iss/git-iris) · [官网](https://hyperb1iss.github.io/git-iris) · 个人维护

**AI agent 驱动的 Git 工具：生成提交信息、代码审查与变更日志**

Rust 编写的 Git CLI 工具，内含名为 Iris 的智能 agent，通过工具调用主动探索代码库（分析 diff、文件关系）后生成上下文感知的提交信息、多维代码审查、PR 描述、Keep a Changelog 格式变更日志与发布说明，并提供语义化 blame 与终端 Studio 聊天界面。面向使用 Git 的开发者，需配置 OpenAI/Anthropic/Google 之一的 API key。支持 Homebrew、Cargo、Docker、GitHub Releases 二进制及 GitHub Action 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- agent 用工具调用迭代探索代码库后生成提交信息/审查/变更日志
- Iris Studio 终端界面：按 / 聊天并可通过工具调用直接更新内容
- 支持 OpenAI、Anthropic、Google 三家 provider
- 提供 GitHub Action 用于 CI/CD 自动生成发布说明与变更日志

## 适用场景

- 让 AI 根据代码变更生成提交信息并自动提交
- 在合并前对分支或单次提交做多维代码审查
- 从 git tag 区间生成变更日志与面向用户的发布说明
- 在 CI/CD 中自动生成 changelog 和 release notes

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L25: Git-Iris is powered by **Iris**, an intelligent agent that actively explores your codebase to understand what you'r
> L83: Supports **OpenAI**, **Anthropic**, and **Google**. See the Configuration Guide for details.

## 星数曲线

```mermaid
xychart-beta
    title "hyperb1iss/git-iris 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `99e71b0d827e` · [字段定义](../../DATASET.md)*
