# Eversec-ai/AIGov-Insight-Web

⭐ 32 · TypeScript · NOASSERTION · 推送 2026-04-22 · [GitHub](https://github.com/Eversec-ai/AIGov-Insight-Web) · [官网](http://insight.aigovian.com/) · 组织维护 · 中文 README

**大模型与智能体安全治理平台的可视化分析层，面向安全分析师**

恒安嘉新 AIGov-Insight 平台的 Web 可视化与主动防御层，本仓库不含数据采集探针（另见 AIGov-Insight Agent）。提供实时日志监控、多指标 Dashboard、会话级全景分析与全流程拓扑图等可观测功能，并针对 OpenClaw 智能体提供 Block/Confirm/Warn 三级拦截、热加载防护规则与 8 大场景规则模板。技术栈为 Next.js/React/TypeScript，通过 git clone 源码安装，需 Node.js 20+ 与已部署的 Agent 探针，密码以 bcrypt 加密存储。

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

- AI 交互的实时日志监控与会话级全景分析
- OpenClaw 三级防御（Block/Confirm/Warn）与热加载规则
- 8 大场景防护模板（防删库、防密钥泄露等），支持自定义正则
- 不改代码、不拦截流量、不依赖证书的旁路采集模式

## 适用场景

- 安全分析师观测 LLM/Agent 交互的全链路行为
- 对企业 AI 智能体的危险操作做实时拦截与告警
- 跨会话关联分析定位安全事件

## 场景标签

`LLM 可观测性` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L17: **AIGov-Insight Web** 是恒安嘉新大模型与智能体安全治理平台（Eversec AIGov-Insight）的可视化分析层，为安全分析师提供极致丝滑、极具视觉冲击力的观测界面。
> L19: 这是一套专为新一代 AI 系统（LLM / Agent / OpenClaw / MCP / RAG）量身定制的现代化可观测工具。它就像是潜伏在 AI 大脑与双手之间的"行车记录仪"，静静地放在服务器上，不改代码、不拦截流量、不依
> L25: AIGov-Insight Web v0.3.0 迎来重大架构升级，从“被动观测”正式迈向“主动防御”。本次更新重构了底层交互逻辑，引入全新的 OpenClaw 智能防护中心对应针对龙虾全新的安全防护能力，在保持极致视觉体验的同时

## 星数曲线

```mermaid
xychart-beta
    title "Eversec-ai/AIGov-Insight-Web 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5935fa304101` · [字段定义](../../DATASET.md)*
