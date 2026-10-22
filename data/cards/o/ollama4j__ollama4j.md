# ollama4j/ollama4j

⭐ 506 · Java · MIT · 推送 2026-10-22 · [GitHub](https://github.com/ollama4j/ollama4j) · [官网](https://ollama4j.github.io/ollama4j) · 组织维护

**Java 库：封装 Ollama REST API，供 Java 应用调用本地模型**

Ollama server 的 Java 包装库，把文本生成、多轮对话、流式输出、工具/函数调用、MCP 外部工具、多模态图像输入、向量嵌入、异步生成与模型管理（拉取/创建/删除）等 Ollama REST 能力封装为 Java API，并提供认证、超时配置、日志钩子与 Prometheus 指标导出（Beta）。面向 Java/JVM 开发者，通过 Maven Central 或 GitHub Packages 以依赖形式引入；运行需要 Java 环境与已运行的 Ollama server，另可对接兼容 Ollama API 的本地模型运行时 llmman。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 封装 Ollama 的生成/对话/嵌入/模型管理等 REST 能力
- 基于注解的工具/函数调用与 MCP 外部工具调用
- Prometheus 指标导出（Beta）与请求/响应日志钩子
- 兼容 Ollama API 的其他本地运行时（如 llmman）可直接接入

## 适用场景

- 在 Java/Spring 项目中接入本地 Ollama 模型做对话或生成
- 构建带工具调用的 Java AI agent
- 为 Ollama 应用采集请求与模型使用指标

## 场景标签

 · 领域:LLM 基础设施/开发库

## 证据(README 行号)

> L5: A Java library (wrapper/binding) for Ollama server.
> L24: - **Text generation**: Single-turn `generate` with optional streaming and advanced options
> L132: llmman is a local model runner that serves the Ollama API (alongside OpenAI- and

## 星数曲线

```mermaid
xychart-beta
    title "ollama4j/ollama4j 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 505 --> 507
    line [506, 506]
```

2026-10-18 506 → 2026-10-22 506（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `8409624e3786` · [字段定义](../../DATASET.md)*
