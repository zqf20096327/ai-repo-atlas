# akaion-ai/annona

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/akaion-ai/annona) · [官网](https://akaion-ai.github.io/annona/) · 组织维护

**AI agent 主权执行内核：按策略决定每步运行位置并强制记录**

安装于数据所在地的守护进程：对 agent 运行的每个推理与工具调用步骤，依据策略判定其允许执行的底层（本地/自建云/前沿 API），无合规底座时拒绝执行（fail closed），并将每条决策写入可事后审计的账本。默认本地、默认拒绝，宣称 GDPR/欧盟 AI Act 对齐。支持 Ollama、vLLM、任意 OpenAI 兼容 /v1 与 Anthropic 底座，兼容 Anthropic Agent Skills 格式并施加 pins:local 等策略约束；附带 default-deny 工具、本地 vault 与 Tauri 桌面应用。面向需按步骤管控数据出境的企业用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个推理与工具调用的运行位置由策略决定并由运行时强制执行
- fail closed：无合规底座时步骤被 held，不降级不重路由
- 账本记录每次放置决策，可事后审计（annona why）
- 兼容 Anthropic Agent Skills 格式，pins:local 由内核强制

## 适用场景

- 企业需按数据敏感度决定每步推理在本地或云端执行
- 满足 GDPR/欧盟 AI Act 下的数据出境合规审计
- 管控 agent 可调用的工具与技能（default-deny）

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L42: **Annona is the office.** It is a daemon you install where your data already
> L83: > project in which the **placement of every inference and every tool call is a
> L169: |**Substrates**|Ollama, vLLM and any OpenAI-compatible `/v1`, Anthropic, a scripted offline backend|

## 星数曲线

```mermaid
xychart-beta
    title "akaion-ai/annona 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c14098e810a5` · [字段定义](../../DATASET.md)*
