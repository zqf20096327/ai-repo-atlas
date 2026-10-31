# lumingye/Proof

⭐ 15 · JavaScript · NOASSERTION · 推送 2026-10-16 · [GitHub](https://github.com/lumingye/Proof) · 个人维护 · 中文 README

**给 AI 角色用的饮酒状态引擎：结算、代谢并向模型投递状态**

面向 AI 角色扮演场景的饮品效果状态引擎：记录杯中成分、声称身份、饮用量与经过时间，按六轴（愉悦/唤醒/精度/亲近/守门/欲望）结算内部推动与呕吐、断片、宕机等客观状态，随半衰期衰减。通过 MCP 提供点酒、查状态、reset 等工具，Gateway 兼容 OpenAI/Anthropic 接口每轮注入状态并在断片时过滤历史；状态按可信 Agent 身份在服务端跨 session 持久化。附网页调酒台 UI。限非商用许可（PolyForm Noncommercial），未成年人不得使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六轴状态结算与药理代谢（半衰期 10–180 分钟）
- MCP 工具集 + Gateway（OpenAI/Anthropic 接口）每轮注入与断片历史过滤
- belief/placebo 通道与固定酒、特调、名称声称的身份判定
- 状态按可信 Agent 身份服务端持久化，跨 session 生效

## 适用场景

- 让我的 AI 角色喝酒后产生随时间消退的状态影响
- 给角色扮演客户端接入 MCP/Gateway 获得持续饮酒状态
- 通过网页调酒台递酒并查看饮用历史

## 场景标签

 · 领域:AI 角色扮演/Agent 状态服务

## 证据(README 行号)

> L201: MCP 给 Agent 动作：看吧台、点酒、领取或拒绝 link、查看状态和 reset。Gateway 给 Agent 连续性：每轮自动送入状态，并在断片时真正控制历史可见性。两者平行读取同一份 Proof 状态，不是前后串联
> L211: MCP 工具包括：

## 星数曲线

```mermaid
xychart-beta
    title "lumingye/Proof 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8fe99da800fc` · [字段定义](../../DATASET.md)*
