# timoncool/prompt-warrior

⭐ 24 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/timoncool/prompt-warrior) · [官网](https://t.me/nerual_dreming) · 个人维护

**把 AI 编码会话日志变成游戏化角色卡片的 agent 技能**

一个运行在 Claude Code 中的 agent skill（也支持插件方式安装）：读取本地会话日志（Claude Code 原生支持，Codex CLI/OpenCode/Gemini CLI/Copilot 经文档化的日志格式），用纯标准库 Python 离线计算固定量表指标，生成含头衔、等级、74 个成就、六项量表、经济与武器库统计的角色卡片；LLM 仅撰写编年史与优缺点挑选。输出为聊天内嵌组件和自包含 HTML 卡片，全程本地运行、无网络调用、无 API key，提供 RU/EN 双语。

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

- 读取 Claude Code/Codex CLI/OpenCode/Gemini CLI/Copilot 会话日志生成游戏化档案
- 74 个成就与冻结公式的固定量表指标（SCALE）
- 纯标准库 Python、100% 本地、零依赖、无网络调用
- 输出内嵌聊天组件与自包含 HTML 卡片，RU/EN 双语

## 适用场景

- 查看自己与 AI 结对编程的行为画像与成就
- 对比不同时期的指标变化与等级成长
- 获取基于自身指标并附研究出处的改进建议

## 场景标签

 · 领域:开发者工具/会话分析

## 证据(README 行号)

> L16: Prompt Warrior is an agent skill that reads your local session logs — Claude Code out
> L135: Under the hood: `scripts/analyze.py` reads `~/.claude/projects` JSONL logs (read-only),
> L136: deduplicates your messages, computes metrics and writes `profile.json`; Claude authors

## 星数曲线

```mermaid
xychart-beta
    title "timoncool/prompt-warrior 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-28 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `8b24ae7ec960` · [字段定义](../../DATASET.md)*
