# yyu0310/cc-to-antigravity-cli-bridge

⭐ 28 · Shell · MIT · 推送 2026-10-24 · [GitHub](https://github.com/yyu0310/cc-to-antigravity-cli-bridge) · 个人维护 · 中文 README

**从 Claude Code 驱动 Antigravity CLI 的桥接脚本与提示前缀**

由两部分组成的薄桥接：research-prefix.md 提示前缀要求多角度搜索、注明日期来源并给出决策优先回答；scripts/ccagy.sh 在临时目录中应用前缀并调用 agy -p 一次性查询，避免项目 AGENTS.md 泄入。面向已持有 Claude Code 与 Gemini 订阅的用户，用 Gemini（或 Claude Sonnet/Opus、GPT-OSS）补足搜索与轻量辅助，并通过 AGENTS.md→CLAUDE.md 符号链接共享系统提示。限制：截至 2026-07 agy 无原生记忆 API 与 hook schema，无记忆同步。

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

- research-prefix.md 提示前缀：多角度搜索、带日期来源、决策优先回答
- ccagy.sh 在干净 cwd 运行并自动选取最新 Gemini Pro/Flash
- AGENTS.md 符号链接共享 Claude Code 系统提示
- 可在 agy 中调用 Claude Sonnet/Opus 4.6 与 GPT-OSS 120B

## 适用场景

- Claude web_search 失败时用 Gemini 双轨搜索补源
- 用已有 Gemini 订阅额度在终端做一次性研究查询
- 让 Claude Code 与 Antigravity CLI 共用同一系统提示

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: Drive Google's Antigravity CLI (`agy`) from Claude Code: use your Gemini subscription for search and model work that
> L88: - `scripts/ccagy.sh`: prefix + `agy -p` from a clean cwd

## 星数曲线

```mermaid
xychart-beta
    title "yyu0310/cc-to-antigravity-cli-bridge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-28 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e8f12b2df8a9` · [字段定义](../../DATASET.md)*
