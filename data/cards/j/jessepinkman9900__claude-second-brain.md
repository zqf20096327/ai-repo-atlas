# jessepinkman9900/claude-second-brain

⭐ 46 · JavaScript · MIT · 推送 2026-04-20 · [GitHub](https://github.com/jessepinkman9900/claude-second-brain) · [官网](https://jessepinkman9900.github.io/claude-second-brain/) · 个人维护

**一条命令搭建 LLM 驱动的个人知识库（Claude Code+Obsidian+qmd）**

npm 脚手架 CLI：npx claude-second-brain 生成一个可直接在 Obsidian 打开的 vault，由 Claude Code 读取投喂的资料源，生成五种带 YAML frontmatter 的互链 wiki 页面，qmd 提供本地向量+BM25 混合检索，GitHub 作为版本与同步中心。内置 /brain-ingest、/brain-search、/brain-refresh 等 slash 技能覆盖摄取、问答与索引维护；CLI 自动安装 mise、node、pnpm，首次构建嵌入需下载约 2GB GGUF 模型；支持创建多个相互隔离的 brain。面向希望积累、可引用地检索个人笔记的用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令脚手架生成 Obsidian vault 并预配置 obsidian-git 同步
- Claude Code 摄取资料并生成五种结构化互链 wiki 页面，标记知识矛盾
- qmd 本地混合检索（向量+BM25），/brain-search 返回带 wiki 链接引用的答案
- CLI 自动安装 mise/node/pnpm，支持多个相互隔离的 brain

## 适用场景

- 把读过的论文、文章、书籍沉淀为可交叉引用的个人 wiki
- 数月后向知识库提问并获得带引用出处的回答
- 通过 Obsidian 移动端与 GitHub 在任意设备读写知识库

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L14: - Claude ingests your sources and maintains a cross-linked wiki
> L35: |**Claude Code**|Reads sources, writes wiki pages, cross-links, flags contradictions|

## 星数曲线

```mermaid
xychart-beta
    title "jessepinkman9900/claude-second-brain 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-31 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ae27b327641` · [字段定义](../../DATASET.md)*
