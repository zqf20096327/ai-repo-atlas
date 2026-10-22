# schmitech/orbit

⭐ 355 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/schmitech/orbit) · [官网](https://schmitech.ca/orbit) · 组织维护

**自托管 AI 网关：私有数据接入本地/托管模型并统一 API**

ORBIT（Open Retrieval-Based Inference Toolkit）是自托管的 AI 网关与控制平面：通过 YAML 配置的适配器连接文件、SQL、NoSQL、向量库、API 与 MCP 工具，在本地或托管模型（Ollama、OpenAI、Gemini、OpenRouter、Cohere）之间切换，对外暴露一个 OpenAI 兼容 API。内置认证、配额、审计日志、提供者回退、监控与管理界面，支持离线（air-gapped）部署。面向需要在自己的基础设施上运行私有 RAG、自然语言数据访问与工具调用 agent 的开发者与企业，提供 Docker 预构建镜像、tarball 安装脚本与 Node.js/Python 客户端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- YAML 适配器连接文件/SQL/NoSQL/向量库/API/MCP 工具
- 本地与托管提供者统一到一个 OpenAI 兼容 API
- 内置认证、配额、审计日志、提供者回退与管理界面
- 五种 Docker 预构建 flavor（含内置 Ollama 的本地推理镜像）

## 适用场景

- 在自己服务器上搭建私有 RAG 与文档问答
- 统一管理多个本地/托管模型并提供 API key 与配额控制
- 为 agent 配置 MCP 工具并做实时决策类应用

## 场景标签

 · 领域:LLM 基础设施/AI 网关

## 证据(README 行号)

> L9:  Connect your data and tools to local or hosted models through one API.
> L49: |**Your choice of models**|Switch between local and hosted providers behind one OpenAI-compatible API.|
> L50: |**Your infrastructure**|Self-host on-premises or in a private cloud, use local models for air-gapped deployments.|

## 星数曲线

```mermaid
xychart-beta
    title "schmitech/orbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 354 --> 356
    line [355, 355]
```

2026-10-18 355 → 2026-10-22 355（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `dcc1d428218c` · [字段定义](../../DATASET.md)*
