# captain-marketing/anti-slop-fr

⭐ 15 · MIT · 推送 2026-05-25 · [GitHub](https://github.com/captain-marketing/anti-slop-fr) · [官网](https://captainmarketing.io) · 个人维护

**法语写作用 Claude skill：让 AI 文本读起来更像人写的**

面向法语内容创作者的 Claude 技能包：以 SKILL.md 指令文件加参考清单与示例的形式，检测并修正 LLM 文本的空泛套语与结构化模式（二元对比、被动语态、单调节奏等），并提供五维度 50 分制评分，低于 35/50 触发重写。核心机制是 VOICE.md 个人声线配置与黑名单、转换示例的自定义扩充。可安装到 Claude Projects、Claude Code/Cowork 或直接粘贴到自定义指令中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双层检测：空泛套语（blacklist.md）与结构化模式（structures.md）
- identity/VOICE.md 填写语域、标志性表达、个人禁忌与范文来定义个人声线
- 五维度评分表（直接性/节奏/自信/真实感/密度），低于 35/50 重写
- 支持 Claude Projects、Claude Code/Cowork 与自定义指令三种接入方式

## 适用场景

- 用法语写作时去除 AI 文本的套路化痕迹
- 把我自己的写作风格配置进 Claude 生成的内容里
- 为特定行业或个人风格维护禁用表达黑名单

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: Un skill pour écrire du contenu qui sonne humain, pas généré.
> L28: ### Claude Projects (claude.ai)

## 星数曲线

```mermaid
xychart-beta
    title "captain-marketing/anti-slop-fr 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `4f111e8e7ed8` · [字段定义](../../DATASET.md)*
