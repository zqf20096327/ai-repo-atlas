# pedrofariasx/qwenproxy

⭐ 182 · TypeScript · ISC · 推送 2026-10-21 · [GitHub](https://github.com/pedrofariasx/qwenproxy) · [官网](https://buymeacoffee.com/pedrofariasx) · 个人维护

**将 Qwen 网页版封装为 OpenAI 兼容 API 的本地代理**

基于 Hono 与 Playwright 浏览器自动化的本地代理：把发往 chat.qwen.ai 的请求转成 OpenAI 兼容的 /v1/chat/completions、/v1/models、/v1/upload 接口。支持多 Qwen 账号负载路由、多用户 API key 与 RPM/并发配额、SQLite 持久化混合会话、reasoning_effort 控制、多模态上传、工具执行与 React 管理面板。需 Node.js v20 与 Playwright 浏览器，提供 npm 全局安装与 Docker 部署，不支持 serverless。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容接口（/v1/chat/completions、/v1/models、/v1/upload）
- 多 Qwen 账号负载感知路由、cooldown 与浏览器会话持久化
- 多用户 API key，含 RPM 限流与并发上限，SQLite 存储
- React + shadcn/ui 管理面板，SSE 实时图表与 Prometheus 指标

## 适用场景

- 让已有 OpenAI SDK 客户端直接调用 Qwen 网页版模型
- 用多个 Qwen 账号分摊请求负载
- 在团队内按用户分发 API key 并限制速率与并发

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Proxy API local compatível com OpenAI que roteia requisições para os modelos do **Qwen (chat.qwen.ai)** via automaçã
> L14: - **OpenAI API Compatible** — Interface compatível com `/v1/chat/completions`, `/v1/models` e `/v1/upload`.
> L35:     Client[Cliente OpenAI/SDK] -->|HTTP| Proxy[QwenProxy - Hono]

## 星数曲线

```mermaid
xychart-beta
    title "pedrofariasx/qwenproxy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 179 --> 183
    line [180, 181, 182]
```

2026-10-18 180 → 2026-10-23 182（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `4a79559e46f0` · [字段定义](../../DATASET.md)*
