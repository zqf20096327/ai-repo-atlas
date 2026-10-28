# meta-llama/llama-api-typescript

⭐ 38 · TypeScript · MIT · 推送 2026-06-16 · [GitHub](https://github.com/meta-llama/llama-api-typescript) · 组织维护

**Meta 官方 Llama API 的 TypeScript/JavaScript 客户端 SDK**

由 meta-llama 维护的 Llama API 官方 TypeScript 库（经 Stainless 生成），供服务端 TypeScript/JavaScript 应用调用 Llama API REST 接口。提供 SSE 流式响应、文件上传、自动重试（默认 2 次）与超时配置、TypeScript 类型定义、自定义 fetch 与代理设置、可访问未公开端点与参数。支持浏览器、Node.js 20+、Deno、Bun、Cloudflare Workers 等运行时，不支持 React Native。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SSE 流式响应支持与流取消
- 自动重试与超时可配置
- 支持未公开端点/参数/响应属性的访问
- 兼容多运行时（Node.js/Deno/Bun/浏览器/Workers）

## 适用场景

- 在 TypeScript 服务端集成 Llama API 的聊天补全能力
- 处理 Llama API 调用的错误、重试与超时控制
- 在 Edge/Workers 等多运行时环境接入 Llama API

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L5: This library provides convenient access to the Llama API Client REST API from server-side TypeScript or JavaScript.
> L9: It is generated with Stainless.

## 星数曲线

```mermaid
xychart-beta
    title "meta-llama/llama-api-typescript 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-28 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `91493cf4d269` · [字段定义](../../DATASET.md)*
