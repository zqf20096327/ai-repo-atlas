# pranrichh/gemini-canvas-proxy

⭐ 35 · Python · MIT · 推送 2026-08-06 · [GitHub](https://github.com/pranrichh/gemini-canvas-proxy) · [官网](https://github.com/pranrichh/gemini-canvas-proxy) · 个人维护

**把 Gemini Canvas 会话转为本地 OpenAI 兼容 API 端点**

由 Chrome 扩展、Canvas 内嵌 HTML 与本地代理组成的工具链：将免费的 Gemini Canvas 会话封装为 http://127.0.0.1:8765/v1 的 OpenAI 兼容接口，任何 OpenAI 客户端可指向该端点、以生成的 token 作为 API key 调用。支持聊天补全、工具调用、多模态输入与图像生成，默认仅监听回环地址并以 Bearer 认证，通过 Private MessageChannel 桥接而非 WebSocket。提供 setup 脚本安装与 Docker/noVNC 部署方式，README 注明将 Canvas 凭据用于 Canvas 之外可能违反 Google 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 Gemini Canvas 会话转为 OpenAI 兼容本地端点
- 支持工具调用、多模态输入与图像生成
- 兼容 Hermes Agent、OpenClaw、LiteLLM、LangChain、OpenAI SDK 等
- Bearer 认证、默认仅回环地址，Private MessageChannel 桥接

## 适用场景

- 让现有 OpenAI 客户端通过本地端点调用 Gemini
- 在不支持 Gemini 的应用中以 OpenAI API 形式接入
- 通过 Docker/noVNC 在无浏览器桌面环境部署

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Turns a free Gemini Canvas session into a local OpenAI-compatible endpoint at `http://127.0.0.1:8765/v1`. Point any 
> L32: - Compatible with Hermes Agent, OpenClaw, LiteLLM, LangChain, the OpenAI SDK, curl

## 星数曲线

```mermaid
xychart-beta
    title "pranrichh/gemini-canvas-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-31 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `46a28aac1e5b` · [字段定义](../../DATASET.md)*
