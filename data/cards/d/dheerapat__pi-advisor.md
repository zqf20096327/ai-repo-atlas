# dheerapat/pi-advisor

⭐ 18 · TypeScript · 推送 2026-06-14 · [GitHub](https://github.com/dheerapat/pi-advisor) · 个人维护

**pi coding agent 扩展：卡住时把问题委托给更强的顾问模型**

面向 pi coding agent 的顾问扩展：日常使用便宜快速的模型工作，遇到难题时通过 /advisor:ask 提问、/advisor:describe 让顾问模型审阅整个对话，或由 LLM 自行调用 ask_advisor 工具。顾问模型只读、无工具、不改文件，其回答注入对话供工作模型继续使用。支持 anthropic/openai 等 provider 配置，含 thinking level、上下文消息数限制、失败重试与配置校验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种求助方式：直接提问 / 对话审阅 / LLM 自行调用 ask_advisor 工具
- 顾问模型只读无工具，回答注入对话上下文
- 全局与项目级配置文件，项目级独占生效
- 瞬态失败自动重试与 Typebox 配置校验

## 适用场景

- 用便宜模型编码、难题时请更强模型给建议
- 不确定该问什么时让顾问模型整体审阅对话
- 按项目隔离不同的顾问模型配置

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Delegate hard problems to a more capable advisor model while working with a cheaper, faster model day-to-day.
> L21: pi install git:github.com/dheerapat/pi-advisor
> L34: - Provider (e.g., `anthropic`, `openai`)

## 星数曲线

```mermaid
xychart-beta
    title "dheerapat/pi-advisor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `83f81939fb6d` · [字段定义](../../DATASET.md)*
