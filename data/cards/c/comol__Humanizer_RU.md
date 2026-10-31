# comol/Humanizer_RU

⭐ 17 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/comol/Humanizer_RU) · [官网](https://skills.sh/comol/Humanizer_RU) · 个人维护 · 中文 README

**俄语文本去 AI 腔工具：规则体检查器加 Agent Skill 供大模型修文**

面向俄语写作场景，把 AI 生成的'机器味'文本改得可读：包含一个无依赖的 Python 体检查器 humanizer_ru（规则检测官话、套话、聊天机器人痕迹，输出 0–100 评分，可作 CI 门禁），以及一个开放格式的 Agent Skill 目录，供 Claude Code、Codex、Cursor 等代理按检查结果改写文本。支持九种体裁（article/spec/legal 等）调整规则，保留作者声音与事实，不追求绕过 AI 检测器。校准语料来自 16 篇 Habr 真实文章。

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

- 规则体检查器零依赖，输出 0–100 评分与分级发现，可作 CI 门禁
- Agent Skill 开放格式，经 Skills CLI 安装到多种代理（Claude Code/Codex/Cursor 等）
- 九种体裁切换规则（spec 中官话为体裁语言而非缺陷）
- 事实锁机制：改写不得引入原文没有的数字、人名或名称

## 适用场景

- 发布 AI 生成文章前清理官话、空话和聊天机器人痕迹
- 在 CI 中用体检查做质量门禁（--fail-below 评分阈值）
- 让代理按我的声音配置（声音配置文件）改写文本

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L11: - **Линтер** `humanizer_ru` — Python, без зависимостей. Находит дефекты, считает ритм, выдаёт оценку 0–100. Годится
> L12: - **Скилл** `skills/humanizer-ru/` — инструкция для LLM-агента (Claude Code, Codex, Cursor, любой чат), который пра

## 星数曲线

```mermaid
xychart-beta
    title "comol/Humanizer_RU 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-31 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `59ec68b80cd6` · [字段定义](../../DATASET.md)*
