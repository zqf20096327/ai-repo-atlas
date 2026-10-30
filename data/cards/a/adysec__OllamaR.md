# adysec/OllamaR

⭐ 96 · GPL-3.0 · 推送 2025-11-06 · [GitHub](https://github.com/adysec/OllamaR) · [官网](https://ollama.adysec.com) · 个人维护 · 中文 README

**Ollama 负载均衡代理服务器：均衡分发请求并隐藏源端口**

面向自建或公网 Ollama 服务器的负载均衡代理：从 /api/tags 自动发现并存储源服务器列表（ollama.db），将请求分发到后端节点，支持动态增删节点无需重启。代理 /、/api/tags、/v1/models、/api/version、/api/chat、/api/embed 等接口，其中 /v1/models 兼容 OpenAI 接口格式；出于安全考虑不转发 /api/pull、/api/delete 等模型管理类接口，避免源服务器模型和数据被删改，也不暴露原生 Ollama 端口。给需要提升多后端可用性与响应速度的开发者使用。README 未给出安装命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 /api/tags 自动发现后端 Ollama 服务器并存储于 ollama.db
- 支持动态添加/移除后端节点，无需重启
- 代理 /api/chat 与 /api/embed/embeddings，/v1/models 兼容 OpenAI 接口
- 不转发 /api/pull、/api/delete 等模型管理接口，避免源服务器数据被改动

## 适用场景

- 多个 Ollama 后端之间分发 LLM 与 embedding 请求
- 以代理方式对外提供服务，不暴露原生 Ollama 端口
- 后端故障时的快速故障转移

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L1: # Ollama 负载均衡服务器
> L21: `ollama.db`: 存储源服务器列表，通过`/api/tags`接口获取，可使用自建Ollama或公网开放的Ollama服务器
> L33: `/api/chat`：LLM模型调用

## 星数曲线

```mermaid
xychart-beta
    title "adysec/OllamaR 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 94 --> 97
    line [95, 96, 96]
```

2026-10-18 95 → 2026-10-30 96（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `be7579a6d833` · [字段定义](../../DATASET.md)*
