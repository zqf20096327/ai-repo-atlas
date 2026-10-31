# mirkolenz/llmhop

⭐ 13 · Nix · MIT · 推送 2026-10-26 · [GitHub](https://github.com/mirkolenz/llmhop) · [官网](https://mirkolenz.github.io/llmhop/) · 个人维护

**按 model 字段分发请求的 OpenAI 兼容 LLM 网关路由器**

纯 Go 编写的无状态单二进制 HTTP 路由器：读取 OpenAI 兼容请求中的 model 字段，将请求反向代理到配置匹配的后端，主要面向 vLLM、sglang 等单模型推理服务器，也支持 Ollama、LocalAI、OpenRouter 等任何 OpenAI 兼容上游。零第三方依赖、无 CGO，自身实现 /v1/models 目录、/health 探测、Bearer 认证、路径路由（/route/{model}/）、请求体大小（默认 100 MiB）与并发（默认 8）限制。以静态二进制、Docker 镜像和 NixOS 模块交付，后者可为 llama.cpp、vLLM、sglang 启动隔离 worker 并在构建期校验配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 model 字段或 /route/{model}/ 路径分发到 OpenAI 兼容后端
- 零外部依赖的纯 Go 单二进制，无数据库/缓存/后台进程
- 原生 /v1/models 目录、/health 探测、Bearer 认证与 per-model 头注入
- NixOS 模块可在路由器旁启动 llama.cpp、vLLM、sglang worker 并含构建期配置校验

## 适用场景

- 把多个单模型推理服务器聚合到一个端口供客户端调用
- 为无法携带 model 字段的客户端用路径路由访问后端
- 在 NixOS 上以沙箱化 systemd 服务统一托管路由器与推理后端

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: LLMhop peeks at the `model` field of an incoming OpenAI-compatible request and reverse-proxies it to the matching ba
> L10: - OpenAI-compatible reverse proxy, model router and request dispatcher for self-hosted LLM inference.

## 星数曲线

```mermaid
xychart-beta
    title "mirkolenz/llmhop 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `89aaebe67bcc` · [字段定义](../../DATASET.md)*
