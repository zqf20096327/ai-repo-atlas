# UniGood/hermes-active

⭐ 14 · Python · 推送 2026-09-28 · [GitHub](https://github.com/UniGood/hermes-active) · 组织维护 · 中文 README

**给 Hermes Agent 加主动消息与持续意识层的伴生服务**

作为独立服务与 Hermes Agent 并行运行的持久意识层：心跳调度器按感知→情绪→决策→行动周期生成主动消息并写回主会话，附带 VA 三维情绪状态、三重发送防护与 Hindsight 长期记忆召回；被动意识通过 Hermes 插件在用户消息前注入思念/热度/天气等上下文（不额外调用 LLM）；另有自由沉思循环、四层记忆模型、cron 定时任务与 Vue3 网页控制台。只读 Hermes 的 state.db，不改写对话历史。LLM 插槽可复用 Hermes 自身调用或接任意 OpenAI 兼容端点。

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

- 心跳循环驱动主动消息，决策由情绪强度×时段×沉默时长×频率上限打分
- Valence/Arousal/社交需求三维情绪状态，确定性演化与 LLM 评估按置信度融合
- 被动意识注入在用户回合不额外调用 LLM，Jinja2 模板可编辑预览
- 四层记忆模型（积淀/近期/中期/远期）支撑无限期沉思链
- 三重发送防护与逐心跳完整日志可观测

## 适用场景

- 让自托管 AI 助手在合适时机主动发消息且保留完整上下文
- 给聊天助手添加随时间演化的情绪与长期记忆状态
- 通过网页控制台管理定时任务、注入模板与消息分析

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Give your AI assistant a heartbeat — let it feel time passing, miss you, think on its own,
> L20: Hermes Active fixes this by running a **persistent consciousness layer** alongside Hermes Agent:
> L73: A scheduler fires every N seconds (default 600) and runs a full perceive → feel → decide → act cycle. Nothing is sc

## 星数曲线

```mermaid
xychart-beta
    title "UniGood/hermes-active 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `f5471006d29c` · [字段定义](../../DATASET.md)*
