# romanklis/openclaw-contained

⭐ 32 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/romanklis/openclaw-contained) · 个人维护

**在 Docker/gVisor 沙箱中运行 AI agent 的可审计编排平台**

包裹 OpenClaw agent 运行时的独立编排层：以能力制安全模型在 Docker 容器中运行 agent，初始仅最小权限，新增包、网络等能力需经人工审批并触发镜像重建。由 Temporal 提供持久化工作流，gVisor（runsc）提供用户态内核隔离，每次 LLM 调用均记录审计日志，并通过 Trivy 自动生成 SPDX/CycloneDX 双格式 SBOM。支持 Ollama、Gemini、Anthropic、OpenAI 多提供方路由，内置 Open WebUI 聊天界面与 OpenAI 兼容 API 网关。以 15 个 Docker Compose 服务部署，需 Docker 24+ 与 16GB 以上内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 能力制安全：agent 请求新能力需人工审批并重建容器镜像
- gVisor（runsc）用户态内核隔离，无需特权模式
- Temporal 持久化工作流，审批时可暂停/恢复
- Trivy 自动生成 SPDX/CycloneDX SBOM 与漏洞扫描

## 适用场景

- 以沙箱隔离方式安全运行会生成代码的 AI agent
- 对 agent 的每次 LLM 调用与能力变更留痕审计
- 通过 Open WebUI 聊天界面下达任务并让 agent 构建部署应用
- 治理 agent 镜像的软件供应链（包白名单、SBOM）

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: **Auditable Agent Orchestration for OpenClaw**
> L18: TaskForge runs AI agents in sandboxed Docker containers with **capability-based security**.
> L30: - **Multi-provider LLM routing** — Ollama, Gemini, Anthropic, and OpenAI via a unified OpenAI-compatible proxy

## 星数曲线

```mermaid
xychart-beta
    title "romanklis/openclaw-contained 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `6f2b30a75f4b` · [字段定义](../../DATASET.md)*
