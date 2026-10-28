# Daniel09Fernandes/DMCPServer

⭐ 37 · Pascal · MIT · 推送 2026-08-31 · [GitHub](https://github.com/Daniel09Fernandes/DMCPServer) · [官网](https://dmcpserver-doc.lovestoblog.com/) · 个人维护

**将 Delphi 代码封装为 MCP 服务器的 Delphi 库**

用 Delphi 编写的 MCP（Model Context Protocol）服务器库：开发者通过 fluent 接口注册 Action 回调与服务器信息，把现有 Delphi 代码暴露为 MCP 工具供 AI 客户端（如 Claude）调用。传输协议支持 HTTP 与 STDIO，测试覆盖 Delphi 10.x–13.x 版本。安装经由 boss 包管理器或手动添加 Library Path；提供 PT-BR 与 EN-US 的 YouTube 视频及外部文档链接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 Delphi fluent 接口注册 MCP Action 与服务器信息
- 支持 HTTP 与 STDIO 两种传输协议
- 兼容 Delphi 10.x/11.x/12.x/13.x
- 可附加图片等资源到 LLM 记忆供 MCP 使用

## 适用场景

- 把 Delphi 业务代码暴露为 AI 客户端可调用的 MCP 工具
- 在 Claude 的 mcpServers 配置中接入自建 Delphi 服务器
- 为现有 Delphi 项目添加 STDIO 或 HTTP 的 MCP 服务端能力

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L7:  Transform your Delphi code into a MCP-server with DMCPServer.
> L10: DMCPServer is a master control protocol server developed in Delphi.

## 星数曲线

```mermaid
xychart-beta
    title "Daniel09Fernandes/DMCPServer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9bdd789f0b9e` · [字段定义](../../DATASET.md)*
