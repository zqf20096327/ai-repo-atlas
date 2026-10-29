# jolokia/jolokia-mcp-server

⭐ 18 · Java · Apache-2.0 · 推送 2026-10-02 · [GitHub](https://github.com/jolokia/jolokia-mcp-server) · 组织维护

**让 LLM 通过 JMX/Jolokia 管理 Java 应用的 MCP 服务器**

面向 Jolokia（JMX-HTTP 桥）的 MCP server，使 LLM 能对连接的 JVM 执行 JMX 操作。提供两种发行版：Standalone MCP Server（stdio 或 HTTP 注册到 MCP host，经 Jolokia agent 以 JMX over HTTP 通信）与 JVM Agent MCP Server（以 javaagent 方式附加，直接开放 HTTP 端口，将 Java 应用本身变为 MCP server）。提供 6 个工具：列出 MBean、列出/读写 MBean 属性、列出并执行 MBean 操作。单次仅连接一个 JVM。

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

- 6 个 MBean 工具：listMBeans / listMBeanOperations / listMBeanAttributes / readMBeanAttribute / writeMBeanAttribute / executeMBeanOperation
- 两种发行版：Standalone 与 JVM Agent（将 Java 应用变为 MCP server）
- 支持 stdio 与 HTTP 传输，可通过 jar 下载或 JBang 运行
- README 给出各版本与 Jolokia 版本的兼容对照表

## 适用场景

- 让 AI 助手通过 MCP 检查和调优运行中的 Java 应用
- 以自然语言查询 JVM 的 MBean 属性与指标
- 在不改业务代码的情况下用 javaagent 为 Java 应用接入 MCP

## 场景标签

 · 领域:Java 应用运维/AI 工具接入

## 证据(README 行号)

> L7: MCP server for Jolokia, a JMX-HTTP bridge for Java applications. This MCP server enables an LLM to manage a Java app
> L29: With this distribution, you simply attach the MCP Server's JVM Agent to your application instead of the standard Jo

## 星数曲线

```mermaid
xychart-beta
    title "jolokia/jolokia-mcp-server 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-29 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `de527539877f` · [字段定义](../../DATASET.md)*
