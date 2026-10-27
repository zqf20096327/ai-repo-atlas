# Coding-Meet/Library-Insight

⭐ 23 · Kotlin · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/Coding-Meet/Library-Insight) · [官网](https://coding-meet.github.io/Library-Insight/) · 个人维护

**面向 Java/Kotlin/KMP 的 API 索引与 MCP Server，供 AI IDE 查询**

分析 JAR、AAR、KLib、Maven 依赖与本地源码，从字节码（含 Kotlin @Metadata）或源码构建版本正确的可搜索 API 索引。提供 CLI 与 stdio MCP Server 两种使用方式，可接入 Cursor、Claude Desktop 等 MCP 兼容 IDE，用于 API 探索、版本对比迁移、依赖与 ABI 分析、调用图生成及 AI 上下文导出。支持 Kotlin Multiplatform 平台变体合并与 Maven BOM 自动解析。安装需 JDK 17+，通过 install.sh 脚本全局安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从字节码（含 Kotlin @Metadata）或源码构建版本正确的 API 索引
- MCP Server 接入 Cursor / Claude Desktop 等 MCP 兼容 IDE
- KMP 支持与 Maven BOM 自动解析合并
- 版本对比迁移建议、依赖与 ABI 冲突检测、AI 上下文导出

## 适用场景

- 让 AI 编码助手基于项目实际使用的库版本查询 API，避免过时文档导致的幻觉
- 对比两个库版本找出新增、移除、弃用的 API 以辅助迁移
- 分析依赖冲突与 LinkageError/NoSuchMethodError 等链接问题

## 场景标签

 · 领域:开发者工具/JVM 生态

## 证据(README 行号)

> L36: - **MCP Server**: Connect Cursor, Claude Desktop, or any MCP-compatible IDE to query APIs directly.
> L9: **Library Insight** solves this by analyzing the exact JAR, AAR, Maven dependency, Gradle output, or local Java/Kotl
> L48: - **Exporter Tools**: Export API indexes as JSON, Markdown reference documentation, or token-optimized AI context p

## 星数曲线

```mermaid
xychart-beta
    title "Coding-Meet/Library-Insight 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `16c95ae8d42e` · [字段定义](../../DATASET.md)*
