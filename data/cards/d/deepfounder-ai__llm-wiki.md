# deepfounder-ai/llm-wiki

⭐ 14 · Shell · MIT · 推送 2026-04-19 · [GitHub](https://github.com/deepfounder-ai/llm-wiki) · 组织维护

**Claude Code 插件：让 Claude 持续维护个人 markdown 知识库**

面向 Claude Code 用户的插件，将 Claude 变为主动的知识管理员：通过 /wiki-ingest 将 URL、文件或当前会话写入持久化 markdown wiki，由 wiki-curator 子代理作为唯一写入者维护页面、交叉链接与索引；/wiki-query 从 wiki 页面回答问题。三层结构为不可变原始来源、带 YAML frontmatter 的页面、以及规定维护规则的 schema.md。三个 hook 实现主动保存提醒、周期性未保存提示与跨会话待入库标记。全局 wiki 位于 ~/.claude/wiki/，可按项目划分。v0.1-v0.2 已实现，v0.3 的 lint/stats 计划中。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- wiki-ingest 命令将 URL/文件/会话写入持久化 wiki，自动决定更新或新建页面
- wiki-curator 子代理为唯一写入者，依据 schema.md 维护命名与链接规则
- 三个 hook 实现主动保存、每 N 轮软提醒与待入库跨会话标记
- 全局 wiki 跨项目共享，可选按项目 wiki 并按内容自动路由

## 适用场景

- 让 Claude Code 会话中的有价值内容自动沉淀为个人知识库
- 通过 /wiki-query 基于自己积累的 wiki 页面提问
- 把常用文章与文件整理成带交叉链接的可维护笔记

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: A Claude Code plugin that turns Claude into an active librarian for your own knowledge.
> L24: /plugin marketplace add deepfounder-ai/llm-wiki

## 星数曲线

```mermaid
xychart-beta
    title "deepfounder-ai/llm-wiki 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e865677ebb1f` · [字段定义](../../DATASET.md)*
