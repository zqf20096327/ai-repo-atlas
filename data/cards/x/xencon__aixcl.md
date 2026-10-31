# xencon/aixcl

⭐ 19 · Shell · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/xencon/aixcl) · [官网](https://www.xenithconsulting.com/) · 个人维护

**自托管本地 LLM 的 Agentic SDLC 平台**

面向开发者与团队的本地优先开发平台：以 rootless Podman（或 Docker）为容器引擎，通过 ./aixcl CLI 初始化并启动完整服务栈，包含 Ollama 本地推理、Open WebUI、HashiCorp Vault 密钥管理、pgAdmin、Grafana/Prometheus/Loki 监控。强制要求 GPG 签名提交，Vault 用 GPG 密钥加密 unseal key 与 root token，每次重启需手动 unseal。支持从 Git URL 安装自有应用或脚手架创建，提供模型添加、凭据轮换、日志查看等命令。最低要求 Linux、4 核 CPU、8 GB 内存。

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

- ./aixcl CLI 一键 init/start 本地 LLM 服务栈
- Ollama 本地推理 API（localhost:11434）与 Open WebUI
- HashiCorp Vault 动态密钥管理与自动轮换，GPG 签名提交强制
- rootless Podman 无特权容器运行

## 适用场景

- 团队自托管一套带密钥管理与监控的本地 LLM 开发环境
- 在离线/本地优先环境下运行 Agentic SDLC 工作流
- 通过 BYO 应用框架把已有项目接入本地 AI 基础设施

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **Agentic SDLC. Bring your own app or create it from scratch.**
> L5: Run Large Language Models locally with HashiCorp Vault, GPG-signed commits, and rootless Podman.

## 星数曲线

```mermaid
xychart-beta
    title "xencon/aixcl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `46a25dfbc50b` · [字段定义](../../DATASET.md)*
