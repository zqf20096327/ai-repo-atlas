# unrealandychan/Hermes-Agent-Cloud

⭐ 29 · Shell · MIT · 推送 2026-07-06 · [GitHub](https://github.com/unrealandychan/Hermes-Agent-Cloud) · [官网](https://hermes-easy-deploy.vercel.app) · 个人维护

**一条命令将 Hermes Agent 部署到 AWS/Azure/GCP 的 CLI 工具**

Bash + Terraform 编写的部署 CLI：通过向导式或 flags 模式将 Hermes Agent 配置到 AWS EC2、Azure VM、GCP Compute Engine，含安全组/IAM/防火墙等基础设施编排；支持多配置文件隔离多实例、双云冗余与故障切换、EBS 持久卷、GitHub Actions CI 集成、Helm 部署到 K8s 及 Terraform Registry 模块复用。每次部署自动安装 WebUI（仅绑 127.0.0.1，SSH 隧道访问），支持 OpenRouter/OpenAI/Anthropic/Gemini/NovitaAI/xAI 六家 LLM 提供商。VPS 直配为规划路线，未成一级支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 向导式 CLI 一键部署到 AWS/Azure/GCP，零明文密钥
- 多 Profile 隔离多实例，各配独立 API key/端口/systemd 服务
- 双云冗余部署与一键 failover，备份到 S3/GCS/Azure Blob
- 提供 Helm Chart 与 Terraform Registry 模块复用现有 IaC

## 适用场景

- 把我的 Hermes Agent 部署到 AWS/GCP/Azure 云端 VM
- 在同一台机器上隔离运行工作与个人两套 Agent 实例
- 用现有 Terraform 代码库以模块方式接入 Hermes Agent

## 场景标签

 · 领域:云基础设施/AI 部署工具

## 证据(README 行号)

> L14: > Deploy the Hermes Agent to AWS, GCP, or Azure with a beautiful wizard-first CLI — zero plaintext secrets, zero ma
> L32: |`cli/`|Bash + Terraform|CLI that provisions Hermes Agent on cloud VMs|

## 星数曲线

```mermaid
xychart-beta
    title "unrealandychan/Hermes-Agent-Cloud 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-27 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `968cc343ba6c` · [字段定义](../../DATASET.md)*
