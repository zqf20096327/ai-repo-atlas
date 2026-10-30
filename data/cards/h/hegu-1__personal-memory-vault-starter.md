# hegu-1/personal-memory-vault-starter

⭐ 20 · Python · CC0-1.0 · 推送 2026-07-10 · [GitHub](https://github.com/hegu-1/personal-memory-vault-starter) · 个人维护 · 中文 README

**个人记忆网络模板库：Markdown+Git，供人与 LLM 共同读写**

以纯 Markdown 文件与 git 组成的个人记忆仓库模板：节点带 YAML frontmatter 与 [[wiki-link]] 交叉引用形成图结构，每节点含 visibility 字段（默认 private）。仓库同时为人类与 LLM 提供入口：LLM_GUIDE.md 规定 AI 协作规范，HUMAN_GUIDE.md（中文）面向新手。设计原则为本地主权、不绑定厂商与编辑器，任何具备 git clone 访问能力的 LLM 可读取整个仓库。使用方式为克隆模板后按节点类型（person/concept/playbook 等 9 类）添加文件。非 Obsidian/Notion 替代品，也不存储凭据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | CC0-1.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Markdown 节点 + [[wiki-link]] 组成图状记忆网络，9 种节点类型
- LLM_GUIDE.md 规定 AI 协作时的节点结构、边界与行为规范
- visibility 字段控制 private/semi-public/public 可见性，默认 private
- 不依赖特定工具：VS Code/Obsidian/Logseq 等均可直接作用于该仓库

## 适用场景

- 搭建个人知识库并让任意 LLM 读取、检索和共同维护
- 用 git 版本管理个人笔记并本地掌握数据主权
- 以中文入门指南为零基础用户上手个人记忆管理

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L14: ## 🤖 If you're an LLM reading this repo
> L53: |**Cross-AI readable**|Any LLM with `git clone` access reads your full vault. Not tied to one vendor's "memory" fea
> L32: You don't need to be technical. **Level 0** users just need a text editor — Markdown + git are optional progression

## 星数曲线

```mermaid
xychart-beta
    title "hegu-1/personal-memory-vault-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b744aa5bdf0e` · [字段定义](../../DATASET.md)*
