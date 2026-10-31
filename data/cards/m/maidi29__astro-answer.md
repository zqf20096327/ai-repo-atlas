# maidi29/astro-answer

⭐ 17 · JavaScript · 推送 2026-10-05 · [GitHub](https://github.com/maidi29/astro-answer) · [官网](https://astro-answer.com) · 个人维护

**按定位渲染星图并生成 AI 每日星座运势的 Web 应用**

Web 应用，使用 D3 Celestial 按用户所在位置渲染实际星图与星座；用户设定星座后，由 OpenAI 模型生成当日简短星座运势，模型可通过 OPENAI_MODEL 环境变量更换，默认 gpt-5-mini。同时以 Chrome 扩展与 Chrome 新标签页扩展形式提供，线上站点为 astro-answer.com。README 未给出安装命令或运行说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- D3 Celestial 按用户位置渲染星图与星座
- 设定星座后生成 AI 每日运势
- OPENAI_MODEL 环境变量可更换模型（默认 gpt-5-mini）
- 提供 Chrome 扩展与 Chrome 新标签页扩展形态

## 适用场景

- 查看自己所在位置的实际星图和星座
- 获取每日 AI 生成的星座运势
- 通过 Chrome 扩展或新标签页快速访问

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L9: If you set your zodiac sign it gives an AI-generated small horoscope for the day.
> L10: The OpenAI model can be changed with the `OPENAI_MODEL` env var (default `gpt-5-mini`).

## 星数曲线

```mermaid
xychart-beta
    title "maidi29/astro-answer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-31 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7fe3ad0229ed` · [字段定义](../../DATASET.md)*
