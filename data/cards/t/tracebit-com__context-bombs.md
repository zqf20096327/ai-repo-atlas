# tracebit-com/context-bombs

⭐ 147 · 推送 2026-09-14 · [GitHub](https://github.com/tracebit-com/context-bombs) · [官网](https://agentic.tracebit.com/context-bombs) · 组织维护

**可触发攻击方 AI 安全护栏的诱饵字符串集合，用于检测与阻断恶意 agent**

Tracebit 发布的 context bomb 字符串资源库：将此类字符串部署为环境中的 canary 资源（如 AWS secret），当攻击性 AI agent 读取到这些内容时，既触发告警（检测），又借助模型自身安全护栏中止其行为（阻断）。README 说明字符串效果随模型提供方而异，并列出对七个前沿模型及一个去护栏（abliterated）模型在真实 AWS 环境红队测试中的结果。属于 AI 安防研究资源，未提供安装运行流程，完整研究见其官网链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 字符串兼具 canary 检测（告警）与护栏触发（阻断）两种作用
- 已在五个前沿模型 + AWS 真实环境红队测试中验证
- 覆盖测试去护栏（abliterated）模型的效果差异
- 效果随模型提供方不同而变化（西方模型 vs 中国提供方模型）

## 适用场景

- 在环境中部署 canary 资源检测侦察我方基础设施的攻击性 AI agent
- 利用攻击方模型自身的安全护栏作为阻断开关
- 评估不同模型与去护栏模型对诱饵字符串的敏感性

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: context_bomb
> L5: ### Strings that can stop AI attackers by tripping their safety guardrails.
> L6: When used as the content of canary resources in your environment, context bombs can both detect (raising an alert) a

## 星数曲线

```mermaid
xychart-beta
    title "tracebit-com/context-bombs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-24"]
    y-axis "stars" 141 --> 146
    line [142, 144, 145]
```

2026-10-18 142 → 2026-10-24 145（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6d4f0052ff9a` · [字段定义](../../DATASET.md)*
