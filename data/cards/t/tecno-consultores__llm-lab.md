# tecno-consultores/llm-lab

⭐ 19 · Shell · GPL-2.0 · 推送 2026-10-14 · [GitHub](https://github.com/tecno-consultores/llm-lab) · [官网](https://www.tecnoconsultores.net/) · 组织维护

**Docker Compose 编排：一键部署 n8n、Ollama、OpenWebUI 等 LLM 工具栈**

由 Tecno Consultores 维护的 Docker Compose 工程模板，通过 profile 机制按需启动 n8n（含 worker、runner、AI sandbox）、OpenWebUI、Ollama（Nvidia/AMD/CPU 三种配置）、EvolutionAPI、Opencode、Hermes-agent、Qdrant 等服务，以及 Searxng、Browserless、Postgres、KeyDB、NGINX proxy manager 等配套组件。README 提供各服务的架构支持表（AMD64/ARM64/GPU）、健康检查、端口与访问 URL 对照。给需要自托管 LLM 工作流栈的开发者使用，限 Docker 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 docker compose profile 按需组合约 18 个服务
- Ollama 提供 Nvidia/AMD/CPU 三种运行 profile
- 各服务健康检查、端口与容器内外 URL 对照表
- 标注各服务的架构支持（AMD64/ARM64/GPU）

## 适用场景

- 本地或服务器自托管 n8n 工作流加 LLM 工具链
- 按需启停部分服务组成自己的 AI 实验环境
- 快速拉起带向量库（Qdrant）与模型运行时的组合栈

## 场景标签

 · 领域:LLM 基础设施/部署编排

## 证据(README 行号)

> L7: To run N8N (with Postgres and KeyDB) and OpenwebUI:
> L10: docker compose -f docker-compose.yml --env-file env.example --profile n8n --profile n8n-worker --profile n8n-runner
> L15: |Project|AMD64|ARM64|GPU|Ollama|Depends on|Profile|

## 星数曲线

```mermaid
xychart-beta
    title "tecno-consultores/llm-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `bb5c56598cf8` · [字段定义](../../DATASET.md)*
