# Treasure-hub-agent/interactive-fiction-skill

⭐ 38 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/Treasure-hub-agent/interactive-fiction-skill) · [官网](https://github.com/Treasure-hub-agent/interactive-fiction-skill) · 组织维护 · 中文 README

**装进 AI 助手的中文互动小说创作技能：你选，它写**

以 SKILL.md 形式分发的 AI agent 技能，为 AI 助手注入互动小说创作规则：每轮正文后强制输出 A/B/C/D/E 五选项，由用户选择推进剧情。规则覆盖视角一致性、字数区间（500-1200 字主区间）、三档存档系统、角色卡系统与酒馆（SillyTavern 等）角色卡导入；规则按 P0/P1/P2 分层按需加载。通过 npx skills 安装，或手动复制到 Hermes、Claude Code、Cursor、Operit 等客户端的技能目录；硬性要求仅为文件读写权限，模型与运行环境需自备。

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

- 每轮正文强制跟随 A/B/C/D/E 五选项的选项驱动叙事
- 三档存档系统与角色卡系统（含 SillyTavern 等 PNG/JSON/CHARX 卡导入）
- 规则 P0/P1/P2 分层加载，可选记忆外置与子 Agent 模式
- 支持 Hermes、Claude Code、Cursor、Operit 等多种客户端技能目录

## 适用场景

- 在 AI 助手里玩选项驱动的文字冒险互动小说
- 把酒馆下载的角色卡导入后继续长篇互动剧情
- 在手机端 Operit 上离线玩并保存小说进度

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: An AI-agent skill for interactive fiction — Chinese-first: choice-driven storytelling with 5 options per turn, long
> L25: **interactive-fiction** 是给 AI 用的「互动小说创作指南」——装上它，AI 就能写出一部有选项、有张力、有沉浸感的互动小说，像玩一场文字冒险游戏，却体验着商业软件般的打磨。
> L41: |🔴 铁律 #0 选项机制|每轮正文输出后强制跟 A/B/C/D/E 五选项（参考指引+兜底），自由输入等权/优先推进；正文结束不结束对话|

## 星数曲线

```mermaid
xychart-beta
    title "Treasure-hub-agent/interactive-fiction-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-30 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `af1d3968b511` · [字段定义](../../DATASET.md)*
