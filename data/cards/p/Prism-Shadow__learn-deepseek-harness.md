# Prism-Shadow/learn-deepseek-harness

⭐ 15 · TypeScript · 推送 2026-08-23 · [GitHub](https://github.com/Prism-Shadow/learn-deepseek-harness) · 个人维护 · 中文 README

**逐课构建 DeepSeek agent harness 的 TypeScript 实战教程**

教学仓库：从最简单的 agent 循环出发，一课一个可独立运行的 TypeScript 小包，逐步搭建 agent harness，覆盖插件架构、append-only Session Log、KV Cache 前缀缓存敏感设计、工具管线与权限、上下文压缩、跨 session 记忆与子 agent 等主题，进阶篇包含运行时自我修改（RSI 雏形）。每课通过 npm 运行并连接真实 DeepSeek 模型（OpenAI 兼容 SDK），需自备 DEEPSEEK_API_KEY。提供网页版在线阅读，类型策略从简并配中文注释，面向想理解 harness 运作机制的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每课为独立可运行的 TypeScript 小包，npm install 即可连真实 DeepSeek 模型
- 围绕三支柱展开：一切皆插件、append-only Session Log、KV Cache 前缀缓存敏感
- 基础篇 8 课 + 进阶篇（子 agent、运行时自我修改）
- 提供网页版在线阅读，含目录、代码与逐课 Diff

## 适用场景

- 跟着课程从零理解 agent harness 的核心机制
- 学习插件化架构与前缀缓存友好的上下文设计
- 对照阅读 DeepSeek Harness 与 Claude Code 的设计差异

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: 从最裸的一个循环开始，一课一课地把它长成一个**真正的 agent harness**。每一课是一个能独立运行的 TypeScript 小包，`npm install && npm run dev` 就能跟真实 DeepSeek 模
> L44: ### 基础篇 Basics（`basics/`）

## 星数曲线

```mermaid
xychart-beta
    title "Prism-Shadow/learn-deepseek-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7bea4a95e73f` · [字段定义](../../DATASET.md)*
