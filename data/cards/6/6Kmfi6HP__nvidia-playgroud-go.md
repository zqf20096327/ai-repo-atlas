# 6Kmfi6HP/nvidia-playgroud-go

⭐ 20 · Go · MIT · 推送 2026-09-14 · [GitHub](https://github.com/6Kmfi6HP/nvidia-playgroud-go) · 个人维护 · 中文 README

**逆向 NVIDIA Playground 的 Go 客户端与 OpenAI 兼容代理**

对 NVIDIA Build Playground（build.nvidia.com）逆向工程的 Go 客户端与多格式反向代理：内置 11 个可匿名调用模型的注册表（DeepSeek、Kimi、MiniMax、Nemotron 等），运行时定期抓取目录页热刷新并按 model 路由到 predict 端点。验证码用纯 Go 的 hCaptcha PoW 求解器（v8go 内嵌 V8，无浏览器）维护预热 token 池；网关嵌入 CLIProxyAPI，对外提供 OpenAI Chat Completions/Responses 与 Claude Messages 接口，不启用入站 api-keys 校验。提供 Docker 镜像，但 Windows/Intel-mac 不发布二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置 11 个匿名 playground 模型注册表，运行时自动抓取目录热刷新
- 纯 Go hCaptcha PoW 求解器（v8go 内嵌 V8），无需浏览器，token 池默认 90s TTL
- 网关对外提供 OpenAI Chat Completions/Responses 与 Claude Messages 三种格式
- 目录抓取含 AWS WAF 挑战自动求解与 Chrome 131 TLS 指纹模拟

## 适用场景

- 在本地通过 OpenAI 兼容接口调用 NVIDIA Playground 匿名模型
- 把 NVIDIA Playground 模型接入已有 OpenAI/Claude 客户端工具链
- 做流式延迟与并发基准实验

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L12: > **English:** A reverse-engineered Go client and multi-format reverse proxy for **NVIDIA Build Playground** (build
> L198: ### 方式 3：多格式本地代理（CLIProxyAPI）
> L200: `serve` 嵌入 CLIProxyAPI 网关：内置翻译器把 Claude `/v1/messages` 与 OpenAI `/v1/responses` 转成 openai chat，再由 nvidia ProviderE

## 星数曲线

```mermaid
xychart-beta
    title "6Kmfi6HP/nvidia-playgroud-go 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-29"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-29 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `ed3682fd8351` · [字段定义](../../DATASET.md)*
