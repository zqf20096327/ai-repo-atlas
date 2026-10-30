# elementor/angie-sdk

⭐ 28 · TypeScript · 推送 2026-10-26 · [GitHub](https://github.com/elementor/angie-sdk) · [官网](https://elementor.github.io/angie-sdk/demo/) · 组织维护

**WordPress Angie AI 助手的 MCP 扩展 SDK，供插件开发者接入**

Elementor 维护的 TypeScript SDK，用于为 WordPress AI 助手 Angie 创建自定义 MCP 服务器：基于官方 TypeScript MCP SDK（MCP 1.20.1），支持在浏览器中以 JavaScript 模块运行 MCP server、无需外部网关即可向 Angie 注册，并可让 Angie 在当前页面上下文中调用插件能力。提供工具注册、指令说明、Angie 扩展的 tool annotations、prompt/context 触发（含 URL hash 深链）、嵌入式聊天 UI（loadSidebarV2）等 API。限制：不支持 Prompts、OAuth 2.0 外部认证、Elicitation、Roots 与 STDIO 传输；后端安全（权限/nonce）由开发者负责。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在浏览器中运行 MCP server，无需 PHP 或外部 SSE/HTTP 服务
- 无外部 MCP 网关即可向 Angie 注册 server
- 以 prompt/contextAttachment/suggestions 触发 Angie，支持 URL hash 深链
- 扩展 MCP tool annotations（资源依赖、模型偏好等 Angie 专有元数据）

## 适用场景

- WordPress 插件开发者把插件功能暴露为 Angie 可调用的 MCP 工具
- 在当前页面让 Angie 感知并操作用户屏幕上的内容
- 将 Angie 聊天 UI 嵌入任意网页（侧栏或悬浮窗）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **An SDK for extending Angie AI Assistant capabilities.**
> L7: This SDK enables you to create custom MCP servers that Angie can discover and use to run your plugin features.
> L13: Angie is a WordPress AI Assistant that can perform almost any task on a WordPress website.

## 星数曲线

```mermaid
xychart-beta
    title "elementor/angie-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `27fc03d17665` · [字段定义](../../DATASET.md)*
