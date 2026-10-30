# ondrsh/mcp4k

⭐ 70 · Kotlin · Apache-2.0 · 推送 2026-06-04 · [GitHub](https://github.com/ondrsh/mcp4k) · 个人维护

**Kotlin Multiplatform 上构建 MCP 客户端/服务端的编译器驱动框架**

面向 Kotlin 开发者的 Model Context Protocol（MCP）框架，基于 Kotlin 编译器插件在编译期生成 JSON-RPC 处理器、JSON schema 与注册代码，实现 resources、prompts、tools、sampling 等协议能力。支持以 @McpTool、@McpPrompt 注解定义工具与提示模板，参数类型错误与 KDoc 引用错误会在编译期报错。客户端可连接任意 MCP 服务器调用工具、读取资源；传输层目前支持 stdio，HTTP-Streaming 在路线图中。以 Gradle 插件形式经 Maven Central 分发，各版本与特定 Kotlin 版本硬绑定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编译期生成 JSON-RPC 处理器与 schema，参数类型错误编译期报错
- 实现 MCP 规范主要内容：resources、prompts、tools、sampling、生命周期管理
- 支持运行时增删工具并自动发送 ToolListChanged 通知，基于协程的协作式请求取消
- 提供可插拔的 ResourceProvider 与 SamplingProvider 抽象，含可选文件资源模块

## 适用场景

- 在 Kotlin 项目中把函数暴露为 MCP 工具或提示模板
- 构建连接 MCP 服务器、调用工具与读取资源的客户端
- 为数据库、API 或文件等数据源实现 MCP resource 暴露

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10:  mcp4k is a compiler-driven framework for building both clients and servers using the
> L14: mcp4k automatically generates JSON-RPC handlers, schema metadata, and manages the complete lifecycle for you.
> L19: - **Server**: Exposes resources, prompts, and tools to MCP-compatible clients, handling standard JSON-RPC messages 

## 星数曲线

```mermaid
xychart-beta
    title "ondrsh/mcp4k 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-30 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `c7a51d9a5626` · [字段定义](../../DATASET.md)*
