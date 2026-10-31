# jondot/mcptap

⭐ 16 · Rust · 推送 2026-01-03 · [GitHub](https://github.com/jondot/mcptap) · 个人维护

**给开发者的 MCP 通信诊断代理：实时拦截与监控 MCP 流量**

Rust 编写的 Model Context Protocol 诊断工具，作为透明代理插入 MCP 客户端与服务器之间：改写 MCP 配置文件使流量经过自身，实时展示 JSON-RPC 消息、工具调用与双向流量，支持 stdio 与 HTTP 传输。提供基于 CEL 表达式的策略过滤，observe 模式仅高亮记录、enforce 模式可阻断请求，可按 MCP 服务器配置不同规则。支持导出 stdout 供脚本处理；untap 命令恢复原配置。从 GitHub Releases 下载二进制安装，也可用 cargo 从源码构建。面向调试 MCP 集成的开发者与审计工具使用的安全人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 透明代理拦截 MCP 客户端与服务器间的全部流量，终端 UI 实时展示
- CEL 表达式策略过滤，observe 高亮与 enforce 阻断两种模式
- 支持 stdio 与 HTTP 传输，自动检测
- tap/untap 自动备份与恢复 MCP 配置文件

## 适用场景

- 调试 MCP 集成时查看工具为何不工作
- 审计 MCP 工具调用与流量模式
- 用 enforce 策略阻断特定请求实现安全控制

## 场景标签

`LLM 可观测性` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L8: **mcp-tap** is a diagnostics tool for Model Context Protocol (MCP) communications—think Wireshark for MCP. It acts a
> L119: mcp-tap works by rewriting your MCP configuration file to insert itself as a proxy between your client and MCP ser

## 星数曲线

```mermaid
xychart-beta
    title "jondot/mcptap 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1d62a9d6d35b` · [字段定义](../../DATASET.md)*
