# exelite-dev/Free-Gemini-pro-API

⭐ 21 · HTML · MIT · 推送 2026-09-12 · [GitHub](https://github.com/exelite-dev/Free-Gemini-pro-API) · 个人维护

**自托管代理：把 Gemini/DeepSeek/ChatGPT 网页会话转成 OpenAI/Anthropic 兼容 API**

基于 FastAPI 的自托管 AI 代理服务器：读取 Gemini、DeepSeek（V3/R1，内置纯 Python 23 轮 Keccak-f[1600] PoW 求解器）与 ChatGPT 的网页会话 Cookie，转换为 OpenAI 兼容（/v1/chat/completions）与 Anthropic 兼容（/anthropic/v1/messages）端点，支持 SSE 流式与 reasoning_content 思考流。机制包括账号池轮询与冷却切换、后台 Cookie 自动刷新、TLS 指纹模拟（curl-cffi Chrome-120）、sk-omni API key 管理与波斯语管理面板。需 Python 3.11+ 或 Docker 部署，凭据通过浏览器 DevTools 提取 Cookie 获得。

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

- Gemini/DeepSeek/ChatGPT 三源代理为 OpenAI/Anthropic 兼容端点
- 账号池轮询负载均衡与自动冷却故障切换，后台自动刷新 Cookie
- DeepSeekHashV1 PoW 纯 Python 求解器（23 轮 Keccak-f[1600]）
- 含流量图表、Playground 与 Cookie 提取指南的管理面板

## 适用场景

- 把 Gemini 网页版会话封装成 OpenAI 格式 API 供现有客户端调用
- 在 Cursor IDE、NextChat 等工具中接入自托管代理端点
- 多账号池化分摊请求负载并自动切换可用账号

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L23: **A high-performance, self-hosted AI proxy server that translates Google Gemini, DeepSeek (V3 & R1 with automatic P
> L38: |🤝 **OpenAI Compatible**|Drop-in replacement for `POST /v1/chat/completions` and `GET /v1/models`|
> L39: |🔶 **Anthropic Compatible**|Full `POST /anthropic/v1/messages` support|

## 星数曲线

```mermaid
xychart-beta
    title "exelite-dev/Free-Gemini-pro-API 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26", "2026-10-31"]
    y-axis "stars" 18 --> 22
    line [19, 20, 21, 21]
```

2026-10-18 19 → 2026-10-31 21（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `2f067acd92f2` · [字段定义](../../DATASET.md)*
