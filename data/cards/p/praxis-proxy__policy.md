# praxis-proxy/policy

⭐ 21 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/praxis-proxy/policy) · 组织维护

**面向代理流量的 Rust 策略引擎：鉴权、数据管控与审计**

Praxis Policy Engine 是一个类型化、分阶段的插件运行时与策略评估器，用于代理（agent）流量治理：解析并独立校验用户、代理与工作负载身份，评估 APL 谓词与可插拔决策点（含关系型授权），通过 RFC 8693 做凭证委派，支持在途字段脱敏、Session Taint 跨调用传播、带外审批，并为每个决策发出审计事件。以 Rust crate 形式提供，内置九个扩展（jwt、cedar、opa、cel 等），需 Rust 1.92 或更新版本；API 尚在稳定过程中，次版本间可能变动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 身份解析/授权/委派/数据脱敏/审计的分阶段策略评估
- 九个内置扩展按 feature 可选编译（jwt、cedar、opa、cel、oauth 等）
- PluginFactory 机制允许宿主替换任意内置插件，未注册 kind 启动即失败
- 参考示例含 PII 扫描器与签名、哈希链 OCSF 审计 sink

## 适用场景

- 为 agent 工具调用做准入与数据流出管控
- 在代理链路中做凭证委派与最小权限 token 签发
- 对每个策略决策留痕审计（含 OCSF 事件输出）

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: A typed, phased plugin runtime and policy evaluator for agent traffic. It decides
> L23: - **Authorization**: Evaluates APL predicates and pluggable decision points,

## 星数曲线

```mermaid
xychart-beta
    title "praxis-proxy/policy 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-23 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `223a5787d5bd` · [字段定义](../../DATASET.md)*
