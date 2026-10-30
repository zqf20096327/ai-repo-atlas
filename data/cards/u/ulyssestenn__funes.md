# ulyssestenn/funes

⭐ 18 · Python · AGPL-3.0 · 推送 2026-09-01 · [GitHub](https://github.com/ulyssestenn/funes) · 个人维护

**Git 仓库式的 LLM 知识管理框架：AI 图书馆员维护引用可溯的 Markdown 知识库**

以 Git 仓库结构、Librarian 协议（AGENTS.md/protocol.md）和可选维护工具组成的框架：用户向任意能读写文件的编码 agent（如 Claude Code、Codex）下达指令，agent 将 PDF、网页剪藏、笔记等原始资料不可变地存入 raw/ 层，编译成 sources/concepts/topics 三层互链 wiki，并基于该 wiki 产出带引用的回答、报告、阅读计划等。声明无需服务器、向量库或嵌入管道；自带健康检查（链接审计、重复概念、矛盾检测）与 CI lint。面向研究者、学生和爱好者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- raw/wiki 三层结构：原始资料不可变保存，抽象发生在 wiki 层
- 每条声明链接回所依据的源笔记或原始文档
- 无服务器/向量库/嵌入管道，纯 Markdown + Git 仓库
- 内置健康检查：矛盾、缺口、重复概念、失效链接审计

## 适用场景

- 把散落的 PDF、剪藏、笔记整理成可检索的引用式知识库
- 让 AI 基于自己的资料库生成带出处的报告和阅读计划
- 在单一 Git 仓库中并行维护多个主题知识库

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L50: 2. **Point your agentic coding tool of choice at your repo.** Use Claude Code, Codex, or any LLM agent that can rea
> L39: - **No application stack required.** Funes needs no server, vector database, embedding pipeline, or proprietary run
> L5: Drop in PDFs, transcripts, web clips, screenshots, notes, articles, or pasted text. The Librarian preserves the raw 

## 星数曲线

```mermaid
xychart-beta
    title "ulyssestenn/funes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `66f84c8bbc81` · [字段定义](../../DATASET.md)*
