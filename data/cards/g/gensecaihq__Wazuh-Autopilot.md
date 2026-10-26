# gensecaihq/Wazuh-Autopilot

⭐ 60 · Python · MIT · 推送 2026-09-24 · [GitHub](https://github.com/gensecaihq/Wazuh-Autopilot) · [官网](https://wazuh-mcp-openclaw.netlify.app/) · 组织维护

**面向 Wazuh 的自治 SOC 平台：13 个 agent 处理告警并规划响应**

自托管的 agentic SOC 平台，基于 Strands Agents 构建 13 个 agent 的群体，通过 Wazuh MCP Server（55 工具）读取告警，完成分诊、关联、调查、富化与响应规划；包含 37 个 SKILL.md 技能（其中 Wazuh 规则 ID 在 CI 中对照官方 4.14 规则集校验）。提供四级自治策略（observe/recommend/supervised/autonomous）、双人规则、审批、RBAC、审计、追踪与评测，以 Docker Compose 单容器加 Postgres 交付，附 Web 控制台；支持 Bedrock、Anthropic、OpenAI 兼容、NVIDIA NIM、vLLM、LiteLLM、Ollama 等模型来源，可离线运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 agent / 37 技能，经 Wazuh MCP Server 分诊、调查与规划响应
- 四级自治策略与双人规则，关键动作始终需人工批准
- agent 不持有可变更状态的 Wazuh 工具，动作执行后经 wazuh_check_* 验证并可回滚
- 覆盖 NIST/MTIRE/CIS/ISO/PCI 等标准，支持空气隔离部署

## 适用场景

- SOC 团队用 agent 群自动分诊与调查 Wazuh 告警
- 在人工审批约束下执行低风险响应动作
- 对接合规框架（NIST/MITRE/PCI 等）跟踪处置流程

## 场景标签

`多智能体` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L3:  An agentic SOC for Wazuh, built on Strands Agents. A 13-agent swarm triages, investigates and responds through the 
> L23: Wazuh Autopilot is a self-hosted platform that works your Wazuh alerts with a swarm of Strands agents. They reach W
> L53: |**Models**|Amazon Bedrock (with Guardrails), Anthropic, OpenAI-compatible, NVIDIA NIM (Nemotron), vLLM, LiteLLM, O

## 星数曲线

```mermaid
xychart-beta
    title "gensecaihq/Wazuh-Autopilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-26 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `5bbd7c9944e8` · [字段定义](../../DATASET.md)*
