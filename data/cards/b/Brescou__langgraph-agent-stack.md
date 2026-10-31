# Brescou/langgraph-agent-stack

⭐ 20 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/Brescou/langgraph-agent-stack) · 个人维护

**面向 ML 工程师的多 agent LangGraph 生产级自托管模板**

基于 LangGraph + FastAPI 的多 agent 系统部署模板：默认 Research→Analysis 流水线，以域包（domain pack）组织 13 个内置工作流（研究、生产力、HR、金融、法律），经 FastAPI 以 SSE 流式暴露，含会话历史、幂等重试、单次运行美元预算（超限返回 402）、金丝雀包版本路由。附带 Docker/Helm/Terraform（GKE/EKS/AKS）与 KEDA 自动扩缩容、Prometheus 指标。多租户身份、OAuth2 与计费不在范围内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个内置域包与第三方插件包机制（entry point + 白名单加载）
- 单次运行 USD 预算上限，超限返回 HTTP 402
- Docker/Helm/Terraform（GKE/EKS/AKS）与 KEDA 扩缩容部署路径
- mock provider 模式：无 API key、零成本、确定性输出，800+ 测试默认离线运行

## 适用场景

- 自托管多 agent 服务而不使用托管平台
- 在 Kubernetes 上部署带成本上限与金丝雀路由的 LLM agent API
- 通过 MCP 端点把域包暴露为 Claude 等客户端的工具

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L22: A deployable starting point for ML / data engineers who want a **real** agent stack—not a notebook demo. The defaul
> L88: |Agents|`agents/`|Reusable LangGraph agents (`ResearchAgent`, `AnalystAgent`, …)|

## 星数曲线

```mermaid
xychart-beta
    title "Brescou/langgraph-agent-stack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5c028d854374` · [字段定义](../../DATASET.md)*
