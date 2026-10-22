# lordmathis/llamactl

⭐ 158 · Go · MIT · 推送 2026-10-21 · [GitHub](https://github.com/lordmathis/llamactl) · [官网](http://llamactl.org/) · 个人维护

**统一管理与路由 llama.cpp/MLX/vLLM 模型的 Web 仪表盘工具**

用 Go 编写的本地 LLM 管理与路由工具：以 llama.cpp、MLX（Apple Silicon）、vLLM 为原生后端，也支持自定义 OpenAI 兼容后端；提供内置模型下载（HuggingFace GGUF/Safetensors）、单实例动态多模型路由、空闲超时与 LRU 逐出等资源管理、React Web 仪表盘、远程实例分布式部署。API 兼容 OpenAI 与 Anthropic 端点。提供二进制下载、Docker 与源码构建三种安装方式；需先安装所选后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多后端支持：llama.cpp、MLX（Apple Silicon 优化）、vLLM 及自定义 OpenAI 兼容后端
- 从 HuggingFace 直接下载 GGUF/Safetensors 模型
- llama.cpp 路由模式下单实例按需加载多模型，含空闲超时与 LRU 逐出
- React Web 仪表盘管理与监控，支持远程实例集中管理

## 适用场景

- 在一处管理多个本地推理后端和模型实例
- 通过 OpenAI/Anthropic 兼容 API 按实例名路由请求
- 在远程主机部署实例并用单一仪表盘集中管理

## 场景标签

 · 领域:LLM 基础设施

## 证据(README 行号)

> L5: **Unified management and routing for llama.cpp, MLX and vLLM models with web dashboard.**
> L21: - **Multi-Backend Support**: Native support for llama.cpp, MLX (Apple Silicon optimized), and vLLM, plus any OpenAI

## 星数曲线

```mermaid
xychart-beta
    title "lordmathis/llamactl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 157 --> 159
    line [158, 158]
```

2026-10-18 158 → 2026-10-22 158（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `c3389396392e` · [字段定义](../../DATASET.md)*
