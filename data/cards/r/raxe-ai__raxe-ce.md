# raxe-ai/raxe-ce

⭐ 121 · Python · NOASSERTION · 推送 2026-10-26 · [GitHub](https://github.com/raxe-ai/raxe-ce) · [官网](https://www.raxe.ai) · 组织维护

**本地运行时安全层：检测 AI agent 的提示注入与工具攻击**

面向 AI agent 的运行时安全工具，提供 L1 规则匹配（515+ 条规则、14 个威胁家族）与 L2 端侧 ML 检测（5 头神经网络集成），覆盖提示注入、越狱、目标劫持、记忆投毒、工具链滥用等场景。以 pip 包与 SDK 形式集成到 LangChain、CrewAI、LiteLLM 等框架，支持后台扫描模式与 SIEM（Splunk/Sentinel 等）对接。全部扫描在本地执行，提示内容不出设备；免费版默认发送匿名元数据遥测，Pro/Enterprise 可关闭。README 自报内部基准数据，Community Edition 为专有软件免费使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- L1 规则（515+ 条，P95 <5ms）+ L2 ML 集成双层检测
- agent 专项检测：目标劫持、记忆投毒、工具链校验、多 agent 交接扫描
- 与 LangChain/CrewAI/AutoGen/LiteLLM 等框架及 SIEM 平台集成
- 100% 本地扫描，支持后台异步扫描模式

## 适用场景

- 在 agent 工作流中拦截提示注入与越狱攻击
- 对 agent 记忆写入与工具调用序列做安全校验
- 将威胁检测结果接入 Splunk/Sentinel 等 SOC 平台

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L25: RAXE is **runtime security for AI agents** — like Snort for networks or Falco for containers.
> L32: - **On-device ML ensemble** (5 neural network heads) for novel attacks
> L97: ## Integrations

## 星数曲线

```mermaid
xychart-beta
    title "raxe-ai/raxe-ce 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-28 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `06a80681079e` · [字段定义](../../DATASET.md)*
