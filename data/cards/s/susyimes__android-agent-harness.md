# susyimes/android-agent-harness

⭐ 33 · Kotlin · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/susyimes/android-agent-harness) · 个人维护 · 中文 README

**Android/JVM 上构建受约束 agent 的 Kotlin SDK**

Provider 中立的 Kotlin SDK，在 JVM 与 Android 上提供单一受治理的运行内核及可选组件：CCP V2 上下文编译（来源信任/风险、token 预算）、State Vault 记忆/技能候选的验证-审批-晋升-回滚、效果审批协议、调度（Cron/LongTask）、Phone Use 严格观察-单动作循环、Web4Agent WebView 工具、语音与多模态适配。附一个可安装的示例 App，支持 OpenAI 兼容流式传输及 Kimi/Ark/Codex 等提供方。宿主持有凭据与审批策略，确定性 JVM demo 无需网络与凭据即可运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 AgentSdk 运行内核：可取消、事务性、带截止期与确定性回放检查
- CCP V2 上下文编译：来源信任/隐私/风险、预算、冲突解决与确定性审计压缩
- State Vault：记忆/技能/人格候选的验证、评估、精确审批、晋升与回滚
- Phone Use 严格协议：观察-单动作-再观察，受步数/时长/审批/Stop 约束

## 适用场景

- 在 Android 应用中集成受预算与审批约束的设备操作 agent
- 构建带记忆晋升与回滚治理的对话式 agent
- 通过 Web4Agent 工具让模型在受控 WebView 中读取与操作网页

## 场景标签

`Agent 框架` `浏览器自动化` `GUI 自动化` · 领域:Agent 开发

## 证据(README 行号)

> L7: Android Agent Harness is a provider-neutral Kotlin SDK for building bounded agents on the JVM and Android. It provid
> L54:     SDK["AgentSdk — the only run kernel"]

## 星数曲线

```mermaid
xychart-beta
    title "susyimes/android-agent-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cf67b6f32438` · [字段定义](../../DATASET.md)*
