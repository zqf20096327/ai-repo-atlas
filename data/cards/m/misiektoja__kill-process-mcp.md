# misiektoja/kill-process-mcp

⭐ 14 · Python · GPL-3.0 · 推送 2026-02-06 · [GitHub](https://github.com/misiektoja/kill-process-mcp) · 个人维护

**跨平台 MCP 服务器：让 LLM 客户端列出并终止系统进程**

基于 Python 3.13+ 与 uv 的 MCP 服务器，向 Claude Desktop、Cursor 等 MCP 客户端暴露两个工具：process_list（按 CPU/内存排序，支持按名称、用户、状态、阈值过滤）与 process_kill（终止指定进程），用户以自然语言让 AI 助手查询并结束进程。提供 uvx 一键运行与克隆仓库手动安装两种方式，可选本地 shim 加快启动。跨 macOS/Windows/Linux，依赖 mcp 与 psutil 库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- process_list 支持按名称/用户/状态/CPU/内存阈值过滤与排序
- process_kill 终止指定进程
- uvx 方式免克隆直接运行，自动拉取最新版本
- 可选 uv tool install 本地 shim 加快启动与离线使用

## 适用场景

- 让 Claude Desktop 或 Cursor 按自然语言指令查找占用资源的进程
- 按用户、名称或阈值筛选进程列表
- 通过对话直接终止指定进程

## 场景标签

 · 领域:系统工具/MCP 服务器

## 证据(README 行号)

> L8: Cross-platform **MCP** (Model Context Protocol) server exposing LLM-accessible tools to **list and kill OS processes
> L18: The following tools are exposed to MCP clients:

## 星数曲线

```mermaid
xychart-beta
    title "misiektoja/kill-process-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `4dd1423c076a` · [字段定义](../../DATASET.md)*
