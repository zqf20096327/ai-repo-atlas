# jasonshrepo/qiju

⭐ 25 · Python · Apache-2.0 · 推送 2026-09-08 · [GitHub](https://github.com/jasonshrepo/qiju) · [官网](https://qiju.pages.dev/) · 个人维护 · 中文 README

**本地优先的结构化会话记录，供多款 AI 编码代理延续开发历史**

面向使用 Claude Code、Codex、Kiro、Cursor 等 AI 编码代理的开发者的会话记录工具：以纯本地 Markdown 文件保存开发历史、交接记录与决策，不依赖云、嵌入或特定供应商。通过向各代理宿主安装三个技能（/qiju-log 记录、/qiju-search 检索、/qiju-review 复盘）实现跨代理、跨项目的记录共享；记录可附带 model 与 model_effort 元数据。安装需 Python 3.11+，支持 macOS/Linux，状态为 developer preview。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 本地纯文件记录，无云、无嵌入、无供应商锁定
- 同一记录库安装到 Claude Code / Codex / Kiro / Cursor 四类代理
- 三个技能：/qiju-log 结构化记录、/qiju-search 跨项目检索、/qiju-review 提取经验教训
- 记录可携带 model 与 model_effort 元数据并可按其过滤

## 适用场景

- 会话结束时让代理记录今天做了什么、决定了什么
- 换用另一个编码代理后继续查同一份开发历史
- 周度复盘记录中的失误与经验，改进工作方式

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Local-first, structured session records that let Claude Code, Codex, Kiro,
> L44: **Across platforms:** one record store, every agent. Qiju installs the same
> L45: three skills into Claude Code, Codex, Kiro, and Cursor — record in one, ask in

## 星数曲线

```mermaid
xychart-beta
    title "jasonshrepo/qiju 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `38bd10e44c95` · [字段定义](../../DATASET.md)*
