# MD-Mushfiqur123/lychee

⭐ 42 · Go · MIT · 推送 2026-06-17 · [GitHub](https://github.com/MD-Mushfiqur123/lychee) · [官网](https://github.com/MD-Mushfiqur123/lychee) · 个人维护

**本地 LLM 运行时：兼容 Ollama 端口，支持 HuggingFace 模型直拉**

用 Go 编写的本地 LLM 运行时与编排层，以 llama.cpp 与 MLX 为推理引擎，监听 11434 端口（与 Ollama 相同），提供 OpenAI 与 Anthropic 兼容 API。支持从 HuggingFace 拉取任意 GGUF 模型、DAG 多模型流水线、SQLite 持久会话、加权负载均衡路由、JSON Schema 结构化输出与自动重试，含浏览器 Dashboard 与 24 个 CLI 命令；另有 Windows 原生桌面应用与多语言官方 SDK。安装提供一键脚本、预编译二进制、Docker 镜像与 go install。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 HuggingFace 直接拉取任意 GGUF 模型（50+ 模型，SHA256 校验、多分片并发）
- OpenAI Chat Completions 与 Anthropic Messages 双兼容 API
- DAG 多模型流水线、SQLite 持久会话、加权负载均衡路由
- JSON Schema 结构化输出与自动纠错重试

## 适用场景

- 本地运行与对话 HuggingFace 上的 GGUF 模型
- 把现有指向 Ollama/OpenAI 的 SDK 切到本地推理服务
- 编排多模型流水线并做结构化输出校验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5:  The Universal Local LLM Runtime & Orchestration Layer
> L204: |**Core inference engine**|✅ llama.cpp|✅ llama.cpp + MLX|

## 星数曲线

```mermaid
xychart-beta
    title "MD-Mushfiqur123/lychee 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 40 --> 43
    line [41, 42, 42]
```

2026-10-18 41 → 2026-10-26 42（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3490f17d092c` · [字段定义](../../DATASET.md)*
