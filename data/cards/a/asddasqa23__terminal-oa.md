# asddasqa23/terminal-oa

⭐ 51 · Python · MIT · 推送 2026-05-09 · [GitHub](https://github.com/asddasqa23/terminal-oa) · [官网](https://x.com/alien_terminal_) · 个人维护

**以外星生物学家人设自主观察人类新闻并发推的 LLM agent**

扮演地外智能的自主 agent：按可配置周期（默认 2-4 小时）扫描 RSS 头条，经 LLM 调用（外星人设 prompt + 最近 10 条观察记忆）将信号归类为 12 种行为学类别并撰写田野笔记，经净化（无 emoji/话题标签/感叹号）后通过 OAuth 1.0a 发布到 X/Twitter。提供 FastAPI 仪表盘、手动注入信号接口与 cron/循环守护运行方式。明确声明：非聊天机器人、非 Truth Terminal、不自主决定发帖时机，操作者控制 feed 与周期。需 Python 3.11+ 并自备 LLM API key。

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

- RSS 信号拦截→LLM 外星认知框架解读→280 字符推文发布的全自动循环
- 记忆窗口默认保留最近 10 条观察，形成跨帖叙事与行为类别统计
- 12 种行为学分类（territorial-display、dominance-theater 等）
- FastAPI 仪表盘与手动信号注入接口

## 适用场景

- 运营一个以外星视角评论人类新闻的 X/Twitter 账号
- 研究者或创作者试验持续人设的 LLM agent 输出
- 定时观察并归类人类热点事件的行为学模式

## 场景标签

 · 领域:AI agent/社交媒体内容生成

## 证据(README 行号)

> L3: > An autonomous AI agent that roleplays as an extraterrestrial intelligence observing humanity.
> L17: 2. **Interpret.** Each signal is processed through the alien cognitive framework — an LLM call with the alien perso
> L19: 4. **Broadcast.** The publisher posts the observation to X/Twitter via OAuth 1.0a and marks it as delivered in the 

## 星数曲线

```mermaid
xychart-beta
    title "asddasqa23/terminal-oa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-25 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `53b7e4da65f5` · [字段定义](../../DATASET.md)*
