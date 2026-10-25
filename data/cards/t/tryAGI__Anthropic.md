# tryAGI/Anthropic

⭐ 43 · C# · MIT · 推送 2026-10-24 · [GitHub](https://github.com/tryAGI/Anthropic) · [官网](https://tryagi.github.io/Anthropic/) · 组织维护

**C#/.NET 开发者调用 Anthropic API 的官方规格生成 SDK**

基于 Anthropic 官方 OpenAPI 规范用 AutoSDK 全自动生成的 C# SDK，供 .NET 开发者接入 Claude 的消息、聊天补全、工具调用、视觉、批量请求、token 计数与提示缓存等全部端点。提供源生成器以 C# 接口原生定义工具，支持 Microsoft.Extensions.AI 的 IChatClient 集成，兼容 .NET Framework/.NET Standard 2.0 及 nullability、trimming、NativeAOT。OpenAPI 规范更新时自动发布新预览版。非 Anthropic 官方维护，声明无隶属关系。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于官方 OpenAPI 规范由 AutoSDK 全量生成，规范更新自动发新预览版
- 源生成器支持用 C# 接口原生定义工具
- 实现 Microsoft.Extensions.AI 的 IChatClient
- 支持 API 全部端点，含批量请求、计数 token、提示缓存

## 适用场景

- 在 .NET 项目中调用 Claude 完成聊天补全与工具调用
- 通过 Microsoft.Extensions.AI 抽象统一接入 Anthropic 模型
- 利用 NativeAOT/trimming 构建高性能 .NET AI 应用

## 场景标签

 · 领域:LLM 基础设施/SDK

## 证据(README 行号)

> L11: - Fully generated C# SDK based on official OpenAPI specification using AutoSDK
> L17: - Supports all endpoints of the API, including batch requests, count tokens, and prompt caching.

## 星数曲线

```mermaid
xychart-beta
    title "tryAGI/Anthropic 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `51bbe07a4334` · [字段定义](../../DATASET.md)*
