# arunsanna/AgentDefense-Bench

⭐ 15 · Python · Apache-2.0 · 推送 2026-04-18 · [GitHub](https://github.com/arunsanna/AgentDefense-Bench) · 个人维护

**评估 MCP AI agent 基础设施层防御的安全基准数据集**

聚合 13 个学术与工业来源共 35,989 条测试用例（35,546 攻击 + 443 良性）的安全基准，覆盖 17 种攻击类别、6 大威胁域，格式为 MCP JSON-RPC 工具调用结构。提供 evaluate.py 脚本通过 mock/http/opa/modsecurity/nemo 五类适配器对接被测防御系统，输出攻击检测率、误报率、基础设施拦截率指标；数据集带 SHA-256 校验和。面向 MCP agent 安全防御的开发与研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 35,546 攻击 + 443 良性测试用例，覆盖 17 种 MCP 攻击向量
- 五种防御接入方式：mock、HTTP 端点、OPA、ModSecurity、NeMo
- ADR/FPR/IBR 三项评估指标
- 全部数据集提供 SHA-256 校验和保证可复现

## 适用场景

- 评估自研 MCP 防御系统的攻击拦截能力与误报率
- 通过 HTTP 端点或 OPA 策略接入对比不同防御方案
- 研究 MCP agent 面临的 17 类攻击向量分布

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L11: AgentDefense-Bench is a curated security benchmark designed to evaluate defenses against attacks on AI agents using
> L68: |`--defense TYPE`|Defense to evaluate: `mock`, `http`, `opa`, `modsecurity`, `nemo`|

## 星数曲线

```mermaid
xychart-beta
    title "arunsanna/AgentDefense-Bench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `fe00a0ba6ff5` · [字段定义](../../DATASET.md)*
