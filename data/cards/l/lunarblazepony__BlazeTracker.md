# lunarblazepony/BlazeTracker

⭐ 14 · TypeScript · MIT · 推送 2026-03-23 · [GitHub](https://github.com/lunarblazepony/BlazeTracker) · 个人维护

**SillyTavern 扩展：LLM 追踪角色扮演中的叙事状态并注入上下文**

面向 SillyTavern 角色扮演用户的状态追踪扩展：通过多次 LLM 调用从对话中抽取时间、天气、位置、角色服装与位置、双向关系、叙事张力与章节事件，投影成状态后注入上下文以维持一致性。提供紧凑消息块、关系/事件编辑器、章节张力图、基于真实气候数据的程序化天气预报（无需 LLM），以及 STScript 批量命令。要求 SillyTavern 1.12.0+ 与较强模型（Gemma 3 27B 约为下限），每条消息产生多次顺序 LLM 调用，建议开启前缀缓存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从对话抽取时间/位置/服装/关系/张力等状态并注入上下文
- 关系、事件、时间事件的编辑器与实时状态预览
- 7 天天气预报由真实气候数据程序化生成，无需 LLM 调用
- STScript 命令支持批量/全量重新抽取

## 适用场景

- 长篇慢节奏角色扮演中保持角色位置、服装、时间线一致
- 查看与手动修正角色间关系的演变事件
- 纵览章节张力曲线把握剧情节奏

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3: A SillyTavern extension that tracks narrative state across roleplay conversations — time, weather, locations, charac
> L13: **Yes if:** You want deep state tracking, run capable models (Gemma 3 27B+), and don't mind multiple LLM calls per 

## 星数曲线

```mermaid
xychart-beta
    title "lunarblazepony/BlazeTracker 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `82248ce80707` · [字段定义](../../DATASET.md)*
