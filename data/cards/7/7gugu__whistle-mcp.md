# 7gugu/whistle-mcp

⭐ 44 · TypeScript · MIT · 推送 2026-04-05 · [GitHub](https://github.com/7gugu/whistle-mcp) · [官网](https://www.npmjs.com/package/whistle-mcp-tool) · 个人维护 · 中文 README

**让 AI 助手通过 MCP 直接管理本地 Whistle 代理服务器**

基于 Model Context Protocol 的 Whistle 代理管理服务器：将规则增删改启停、规则组与 Value 管理、代理与 HTTP/HTTPS 拦截开关、请求查看（URL 过滤/正则）与重放等约 30 个工具暴露给 MCP 客户端（Claude Desktop、Cursor、Raycast），使用户可通过自然语言完成网络调试与代理配置。要求 Node.js ≥18.20.0 与本地运行的 Whistle 服务；传输默认 stdio，可选 http-stream/SSE，支持 Basic Auth 透传。

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

- 覆盖规则/组/Value/代理开关/请求拦截与重放的 MCP 工具集
- 支持 stdio 与 Streamable HTTP/SSE 两种传输模式
- 兼容 Whistle Basic Auth（-n/-w 与 w2 启动参数一致）
- 提供 Smithery 一键安装与 npm 全局安装两种方式

## 适用场景

- 在 Cursor/Claude Desktop 里用自然语言配置和调试 Whistle 代理规则
- 通过 AI 查看和过滤拦截到的网络请求并重放
- 远程场景下用 HTTP/SSE 传输接入 MCP 客户端管理代理

## 场景标签

 · 领域:开发工具/网络代理管理

## 证据(README 行号)

> L7: Whistle MCP Server is a Whistle proxy management tool based on the Model Context Protocol (MCP), allowing AI assista
> L121: Whistle MCP Server provides the following tools, which can be called via the MCP protocol:

## 星数曲线

```mermaid
xychart-beta
    title "7gugu/whistle-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 43 --> 45
    line [44, 44]
```

2026-10-18 44 → 2026-10-25 44（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `d524d3e610f8` · [字段定义](../../DATASET.md)*
