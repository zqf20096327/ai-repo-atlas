# A1batr055/Drivesoid

⭐ 75 · JavaScript · NOASSERTION · 推送 2026-07-20 · [GitHub](https://github.com/A1batr055/Drivesoid) · [官网](https://github.com/A1batr055/Drivesoid) · 个人维护 · 中文 README

**AI 人格的情感驱动状态侧车：随对话演化的多维情绪模型**

以 HTTP sidecar 形式与 AI 桥接并行的 Node.js 服务：桥接端上报对话事件，服务维护 16 个心理维度（依恋、焦虑、满足等）的情感状态，AI 可读取该状态并注入 system prompt。状态模型含快慢双时间尺度（base 情绪向 mood 收敛）、习惯化衰减、负性偏差等机制，并跟踪睡眠周期与亲密意图/挫败。依赖 OpenAI 兼容 API 做消息分类（推荐 DeepSeek），内置 loopback 限定的内部 API、live dashboard 与离线仿真脚本。需 Node.js ≥18、Python 3（Claude Code hooks）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 16 维情感状态实时演化，双时间尺度（情绪→心境→气质锚点）
- 17 类消息分类标签驱动维度变化，习惯化与负性偏差机制
- 输出可直接注入 system prompt 的 [drives] 文本块
- 离线仿真脚本回放 10 个验收场景（虚拟时钟+固定随机种子）

## 适用场景

- 为我的 AI 伴侣/人格注入持续演化的情感状态
- 在对话系统中加入睡眠周期与情绪恢复建模
- 通过 dashboard 实时查看并调参 AI 的情绪状态

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L9: Drivesoid runs as a lightweight HTTP sidecar alongside your AI bridge. Your bridge reports conversation events; Driv
> L66: |`/api/drives/context`|GET|Pre-formatted `[drives]` block for system prompt injection (plain text; empty when stale

## 星数曲线

```mermaid
xychart-beta
    title "A1batr055/Drivesoid 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 74 --> 76
    line [75, 75]
```

2026-10-18 75 → 2026-10-24 75（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bb046ed836fd` · [字段定义](../../DATASET.md)*
