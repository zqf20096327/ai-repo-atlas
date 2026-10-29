# webpro255/agentlock

⭐ 19 · Python · AGPL-3.0 · 推送 2026-09-18 · [GitHub](https://github.com/webpro255/agentlock) · [官网](https://agentlock.dev) · 个人维护

**LLM 智能体工具调用的来源授权门控库**

面向 LLM agent 工具调用的前置授权参考实现：为进入上下文的每项内容标记来源权威级（authoritative/derived/untrusted），并据此实施三种门控机制——会话写门（不读载荷、deny-by-default）、按工具选启的参数溯源（v1.3+）、延迟提交（回合结束重新裁决），v1.4 增加按动作类的选择性门控。支持 Ed25519 签名回执与审计日志，提供 MCP、AutoGen、FastAPI、Flask 等可选集成。在 AgentDojo 上做了对抗性评测并公开代价数据（slack 场景效用显著受限），附两篇论文与逐版本测试数。以 pip 包发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于来源（provenance）而非内容的 deny-by-default 写门
- 参数溯源追踪到不可信内容且未追溯到用户请求的值
- 延迟提交：回合结束时按完整来源记录重新裁决
- v1.4 选择性动作类门控与 audit_action_classes() 审计工具

## 适用场景

- 为工具型 agent 部署防间接提示注入的授权层
- 审计 agent 动作类声明是否符合自身流量
- 研究来源门控防御在 AgentDojo 类基准上的攻防效果

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L16: Pre-action authorization for LLM agent tool calls. The gate decides from
> L27: in the paper (DOI below). AgentLock gates actions on where the session's
> L32: Every item entering the context window is recorded with a provenance

## 星数曲线

```mermaid
xychart-beta
    title "webpro255/agentlock 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b74a67cb3866` · [字段定义](../../DATASET.md)*
