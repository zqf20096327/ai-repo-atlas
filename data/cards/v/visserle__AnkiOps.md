# visserle/AnkiOps

⭐ 24 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/visserle/AnkiOps) · 个人维护

**Anki 与 Markdown 双向同步工具，支持 Git 与 LLM 编辑**

AnkiOps 将 Anki 牌组映射为 Markdown 文件，提供笔记、笔记类型、牌组与媒体的双向同步命令（anki-to-files / files-to-anki），通过 note_key 与 .ankiops.db 追踪条目，同步前自动创建 Git 快照。支持自定义笔记类型（note_type.yaml 定义字段与模板）、图像宽度归一化、JSON 序列化，以及基于 GitHub 仓库与拉取请求的协作牌组。LLM 集成以可编程任务形式对序列化为 JSON 的笔记批量应用编辑（内容审阅、语法修正、翻译等），仅支持 OpenAI response API。以 uv 从 PyPI 安装，另有 Anki 插件可选。早期开发阶段，可能出现破坏性变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 牌组↔Markdown 双向同步，含笔记类型与媒体，同步前自动 Git 快照
- note_type.yaml 自定义笔记类型（字段标签、卡片模板、样式）
- 可编程 LLM 任务批量编辑序列化（JSON）笔记，限定模型只读所需内容
- collab 命令将牌组发布到 GitHub 并通过拉取请求协作

## 适用场景

- 用文本编辑器编辑 Anki 牌组并用 Git 做版本管理
- 通过 GitHub 仓库与他人协作维护共享牌组
- 用 LLM 任务对整库或单副牌做语法修正、翻译等内容改进
- 把现有 Anki 集合迁移为 Markdown 文件管理

## 场景标签

 · 领域:学习工具/知识卡片管理

## 证据(README 行号)

> L5: AnkiOps is a bidirectional bridge between Anki and the filesystem, where each deck becomes a Markdown file. This let
> L93: LLM tasks apply programmable edits to existing notes, from content review and grammar fixes to translation. In cont
> L176: If you want it simple, just prompt an LLM (Codex, Claude Code, etc.) to edit your Markdown files. If you want it i

## 星数曲线

```mermaid
xychart-beta
    title "visserle/AnkiOps 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 22 --> 25
    line [23, 24, 24]
```

2026-10-18 23 → 2026-10-27 24（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2d5d39c59607` · [字段定义](../../DATASET.md)*
