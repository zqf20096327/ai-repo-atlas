# RuoJi6/memory-shell-mcp

⭐ 27 · Python · MIT · 推送 2026-01-14 · [GitHub](https://github.com/RuoJi6/memory-shell-mcp) · 个人维护 · 中文 README

**检测与清除 Java 内存马的 MCP 服务器，支持本地/SSH 执行**

基于 FastMCP 构建的 MCP 服务器，封装 memory-shell-detector 工具，向支持 MCP 的 AI 客户端提供 9 个工具：下载检测 JAR、列出 Java 进程、扫描指定进程、反编译查看可疑类源码、移除内存马、导出报告等。移除操作需 AI 先查看源码并显式确认（ai_confirmed=True）。支持本地执行与 SSH 远程执行，SSH 参数可经环境变量或对话传入。目标机器需 JDK 1.8+，本机需 Python 3.10+ 与 uv；Agent 型内存马无法移除，需重启应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供扫描/反编译查看/移除内存马/导出报告等 9 个 MCP 工具
- 移除前强制 AI 确认（ai_confirmed=True）的安全机制
- 支持 SSH 远程执行，参数可经环境变量或对话动态传入
- 覆盖 Filter/Servlet/Listener/Spring/Agent 型等 7 类内存马说明

## 适用场景

- 让 Claude Desktop 等 AI 客户端帮我排查 Java 服务里的内存马
- 通过 SSH 远程检测并清除服务器上的可疑类
- 检测后导出报告存档

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: 基于 FastMCP 构建的 Java 内存马检测和清理工具 MCP 服务器，支持本地执行和 SSH 远程执行。
> L43: > **支持 MCP 的客户端**：本工具可配置到任何支持 Model Context Protocol 的 AI 客户端，包括但不限于：

## 星数曲线

```mermaid
xychart-beta
    title "RuoJi6/memory-shell-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 26 --> 29
    line [28, 27, 27]
```

2026-10-18 28 → 2026-10-30 27（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1f677ade3a06` · [字段定义](../../DATASET.md)*
