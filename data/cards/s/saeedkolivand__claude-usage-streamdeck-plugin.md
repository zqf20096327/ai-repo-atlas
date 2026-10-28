# saeedkolivand/claude-usage-streamdeck-plugin

⭐ 20 · JavaScript · MIT · 推送 2026-10-04 · [GitHub](https://github.com/saeedkolivand/claude-usage-streamdeck-plugin) · [官网](https://claude-usage.iamsaeed.dev/) · 个人维护

**Stream Deck 插件：在按键上实时显示 Claude 用量限额与本地 token/费用**

面向 Elgato Stream Deck 硬件的用量监控插件，服务 Claude Code 用户：一个可配置动作可放到多个按键，分别显示 5 小时/每周/按模型的实时限额百分比、burn rate，或从本地 Claude Code JSONL 转录解析的 token 与费用统计（今日/7 天/会话），历史数据持久化于 ~/.claude-usage/。实时限额通过社区发现的无文档端点 api.anthropic.com/api/oauth/usage 获取，OAuth token 由插件自行刷新并回写。支持多账号 profile、Stream Deck + 拨盘与 Neo infobar；仅运行于 Windows 10+ 与 macOS 12+（需 Stream Deck app 7.6+），Linux 不支持运行插件。费用为估算下界，Pro/Max 显示的是名义等价 API 支出而非真实账单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单动作多按键：5h/每周/按模型实时限额、burn rate、token/费用统计
- token/费用从本地 Claude Code JSONL 转录解析并持久化 7 天历史
- 每次轮询写出 ~/.claude-usage/stats.json 供 OBS 覆盖层与脚本读取
- 支持多 Claude 账号 profile 与 Stream Deck +/Neo 的拨盘/infobar 动作

## 适用场景

- 在 Stream Deck 按键上实时查看 Claude 5 小时与每周限额余量
- 跟踪本地 Claude Code 的 token 消耗与估算费用（今日/7 天/会话）
- 把用量数据接入 OBS 直播覆盖层或自动化脚本

## 场景标签

 · 领域:开发者工具/LLM 用量监控

## 证据(README 行号)

> L24: |**Session (5h)**|Limit (live)|`oauth/usage` endpoint (same as Claude Code's `/usage`)|big % + ring gauge + reset c
> L29: |**Tokens**|Local logs|Claude Code JSONL transcripts on disk|big value (e.g. `1.2M`) + `today` / `7 days` / `sessio
> L50: Every poll also writes `~/.claude-usage/stats.json` — all profiles' live

## 星数曲线

```mermaid
xychart-beta
    title "saeedkolivand/claude-usage-streamdeck-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `54ffa493437a` · [字段定义](../../DATASET.md)*
