# AymaneK24/SRE-AI-Agent

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/AymaneK24/SRE-AI-Agent) · [官网](https://rootcauseconsole.online) · 个人维护

**自托管 AI SRE 控制台：接入指标后用 AI 解释故障根因**

名为 Root Cause Console 的自托管运维诊断工具，接入 Prometheus、CloudWatch、Azure Monitor 等指标源及 Loki 日志、Kubernetes 只读状态，用户可向 AI 模型提问故障原因。关键机制：答案核验（引用数字与本地数据比对、执行被引查询）、只读告警、人工执行的修复工作流，软件本身不改动系统。以 Docker 部署于用户自有基础设施，按公司独立部署，自带文档、角色权限与审计日志。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 答案核验：引用数字与本地数据比对并执行被引查询
- 支持 Ollama 本地模型或 Claude/Gemini API 接入
- 只读设计：告警只读、修复工作流仅为人工指引
- 四角色权限、SSO(OIDC) 与可导出审计日志

## 适用场景

- 接入公司指标源后让 AI 分析服务故障原因
- SRE 团队按工作流逐步排查并记录调查结论
- 按项目追踪复发性问题并生成 PDF 报告

## 场景标签

 · 领域:DevOps/运维诊断

## 证据(README 行号)

> L7: Connect your metrics, keep a live picture of your systems, and ask an AI model why something broke.
> L34: |AI models|Ollama on your own server, or Claude or Gemini with an API key|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `f02512a6055f` · [字段定义](../../DATASET.md)*
