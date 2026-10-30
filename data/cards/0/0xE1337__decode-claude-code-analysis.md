# 0xE1337/decode-claude-code-analysis

⭐ 22 · MIT · 推送 2026-04-01 · [GitHub](https://github.com/0xE1337/decode-claude-code-analysis) · [官网](https://0xE1337.github.io/decode-claude-code-analysis/) · 个人维护 · 中文 README

**Claude Code v2.1.88 架构深度解析文档（12 章）**

基于 Claude Code v2.1.88 npm 包内 59.8MB source map 提取的完整 TypeScript 源码（1,906 文件、515,029 行）所做的结构化架构分析文档：12 章覆盖启动优化、Agent 循环、System Prompt 设计、40+ 工具系统、权限与安全模型、多 Agent 协作、MCP 服务层与 88 个 Feature Flags 等。面向想理解 Claude Code 工作原理与设计的开发者与研究者，提供双语 HTML 阅读（GitHub Pages），构建方式为 node build.mjs 生成 index.html。仓库不含原始源码，仅含分析与解读，声明仅用于教育研究目的。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 12 章逐层分析 Claude Code 完整技术栈
- 覆盖 40+ 工具、80+ 斜杠命令、88 个 Feature Flags 的量化梳理
- 安全模型专章：17,885 行安全代码、23 个 Bash 验证器、双引擎 AST
- 中英双语版本，支持语法高亮与全文搜索

## 适用场景

- 研究 Claude Code 的 Agent 循环与工具系统实现方式
- 学习大型 AI CLI 应用的架构与安全设计
- 了解 200K/1M 上下文管理与三层压缩机制

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L18: This project is a structured, chapter-by-chapter architecture analysis of **how Claude Code works and why it was de
> L80: 本项目是一份结构化的、逐章节的架构分析，回答的核心问题是：**Claude Code 怎么工作、为什么这样设计**。覆盖完整技术栈：从启动优化到 Agent 循环、System Prompt 设计、工具系统、安全模型、多 Agen

## 星数曲线

```mermaid
xychart-beta
    title "0xE1337/decode-claude-code-analysis 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 20 --> 23
    line [21, 22, 22]
```

2026-10-18 21 → 2026-10-30 22（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `97dcf4aaf0d3` · [字段定义](../../DATASET.md)*
