# infrahouse/terraform-aws-openclaw

⭐ 20 · HCL · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/infrahouse/terraform-aws-openclaw) · [官网](https://infrahouse.github.io/terraform-aws-openclaw) · 组织维护

**在 AWS 上一键部署 OpenClaw AI agent 网关的 Terraform 模块**

Terraform 模块，在 AWS 上部署 OpenClaw AI agent 网关：EC2 后端挂 ALB，前置 Cognito 认证（可选 MFA），EFS 持久化配置与 agent 数据，API 密钥存 Secrets Manager 并 KMS 加密。LLM 多提供方支持 AWS Bedrock（默认，走 IAM 免密钥）、Anthropic API、OpenAI API 与本地 Ollama。附带 systemd 加固、CloudWatch 365 天日志、按模型规模给出 EC2 实例选型表。面向用 Terraform 管理 AWS 基础设施的开发者/运维。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 LLM 提供方：Bedrock 默认（IAM 免 API key）、Anthropic/OpenAI API、本地 Ollama
- Cognito + ALB 认证替代共享网关令牌，可选 MFA
- API 密钥 KMS 加密存于 Secrets Manager，systemd 加固
- Ollama 模型对应的 EC2 实例选型与月成本表

## 适用场景

- 用 Terraform 在自有 AWS 账号生产化部署 OpenClaw 网关
- 切换/组合云端与本地（Ollama）LLM 后端
- 满足密钥管理、日志留存等安全合规要求

## 场景标签

 · 领域:云基础设施/IaC

## 证据(README 行号)

> L14: Deploys OpenClaw AI agent gateway on AWS
> L15: using EC2 behind an ALB with Cognito authentication and multi-provider
> L23: - Multiple LLM provider support: AWS Bedrock, Anthropic API, OpenAI API, Ollama (local)

## 星数曲线

```mermaid
xychart-beta
    title "infrahouse/terraform-aws-openclaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `94156833d940` · [字段定义](../../DATASET.md)*
