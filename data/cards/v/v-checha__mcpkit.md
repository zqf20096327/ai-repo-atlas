# v-checha/mcpkit

⭐ 27 · TypeScript · MIT · 推送 2026-02-02 · [GitHub](https://github.com/v-checha/mcpkit) · 个人维护

**TypeScript 装饰器框架：用注解方式构建 MCP 服务器**

面向 TypeScript 开发者的 Model Context Protocol (MCP) 服务器构建库：通过 @Tool、@Param 等装饰器声明方法与参数，由框架自动生成 schema 与处理器接线，免去手动注册。内置认证、限流、指标、追踪与健康检查，支持插件系统，提供 stdio、HTTP/SSE 与 Streamable HTTP 三种传输。配套 CLI 脚手架与测试工具包，可接入 Claude Desktop。要求 Node.js 18+ 与 TypeScript 5.0+。

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

- 装饰器 API 自动生成 schema 与处理器接线（受 NestJS 启发）
- 内置认证、限流、指标、追踪与健康检查
- 支持 stdio、HTTP/SSE、Streamable HTTP 三种传输
- 提供 core 框架、CLI 脚手架、测试工具三个包

## 适用场景

- 用 TypeScript 快速搭建 MCP 工具服务器
- 为 Claude Desktop 等客户端提供自定义 MCP 工具
- 构建带认证与观测能力、可上线的 MCP 服务

## 场景标签

 · 领域:MCP/LLM 基础设施

## 证据(README 行号)

> L6: A modern, decorator-based framework for building Model Context Protocol (MCP) servers in TypeScript.
> L53: |@mcpkit-dev/core|Core framework with decorators and server|

## 星数曲线

```mermaid
xychart-beta
    title "v-checha/mcpkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ec22bf55b978` · [字段定义](../../DATASET.md)*
