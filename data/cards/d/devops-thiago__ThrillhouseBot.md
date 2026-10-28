# devops-thiago/ThrillhouseBot

⭐ 37 · Java · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/devops-thiago/ThrillhouseBot) · 个人维护

**自托管的 AI 代码审查 GitHub App：审 PR diff 并给内联建议**

基于 Quarkus 构建的 GitHub App，以 GraalVM 原生二进制分发，可 Docker Compose 自托管。它把 PR diff 分批发送到任意 OpenAI 兼容聊天 API（默认 DeepSeek，本地可配 Ollama），审查正确性、安全、回归与代码质量，按 critical/high/medium/low 分级，输出可一键应用的行内建议、每 PR 一条汇总评论、二次核验与跟进审查。另提供 20 余条评论命令（/review、/improve、/generate-tests 等）、仓库记忆学习、泄露凭据与 IaC 风险的确定性扫描、WebSocket 实时仪表盘与 OpenTelemetry/Prometheus 指标。运行需创建 GitHub App、PostgreSQL 与 AI 提供商 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- diff 按 token 预算分批并行审查，二次核验发现与修复建议
- 行内建议可一键应用；/improve、/generate-tests、/add-docs 等评论命令
- 无需模型调用的泄露凭据与 Terraform/K8s/CloudFormation 风险确定性扫描
- WebSocket 实时仪表盘、成本/token 统计与 OpenTelemetry/Prometheus 可观测性

## 适用场景

- 在自托管环境中让 AI 自动审查团队 PR 并给出行内修复建议
- 通过 /improve、/generate-tests 等命令按需生成改进与测试
- 追踪审查成本、token 消耗与历史发现的处理状态

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L15: ThrillhouseBot is a GitHub App that reviews pull requests. It is built with
> L17: OpenAI-compatible chat API, including local models served by Ollama. The model

## 星数曲线

```mermaid
xychart-beta
    title "devops-thiago/ThrillhouseBot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-28 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d9e049996e0b` · [字段定义](../../DATASET.md)*
