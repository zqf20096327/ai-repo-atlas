# hereisSwapnil/memwiki

⭐ 20 · JavaScript · 推送 2026-06-06 · [GitHub](https://github.com/hereisSwapnil/memwiki) · 个人维护

**给 AI 编程代理的持久化项目记忆协议（markdown 记忆库）**

面向 Cursor、Claude Code、GitHub Copilot 等 AI 编程代理的记忆协议工具：通过 npx memwiki init 在项目根生成 .memory 目录与钩子文件（.cursorrules、CLAUDE.md、copilot-instructions.md），指引代理读取 hot.md 短期上下文与 wiki 知识库；AGENTS.md 协议指示代理在会话中自动记录决策、模式与进展，结束前更新 hot.md 与 log.md。支持 /memwiki-ingest 等斜杠命令全库扫描填充记忆，原始资料放 .raw/ 仅供读取。零依赖、纯 markdown、供应商无关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令初始化项目级持久记忆（.memory/wiki + hot.md 热缓存）
- 自动生成 Cursor/Claude Code/Copilot 的根钩子文件
- 代理按 AGENTS.md 协议在会话中自动维护 wiki 与 log
- 内置 /memwiki-ingest、/memwiki-lint、/memwiki-fold 斜杠命令

## 适用场景

- 新会话中让 AI 代理恢复项目决策、技术栈与未完成工作的上下文
- 团队成员使用不同 AI 工具时共享同一项目记忆
- 让代理扫描存量代码库快速生成 stack/patterns/decisions 文档

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L11: `memwiki` gives your project a persistent brain. It leverages the fact that modern AI agents naturally read markdow
> L33: When you run `npx memwiki init`, it creates a `.memory` directory and places specific hook files (`.cursorrules`, `

## 星数曲线

```mermaid
xychart-beta
    title "hereisSwapnil/memwiki 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3981dc00b275` · [字段定义](../../DATASET.md)*
