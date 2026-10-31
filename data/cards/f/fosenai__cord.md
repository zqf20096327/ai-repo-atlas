# fosenai/cord

⭐ 14 · JavaScript · Apache-2.0 · 推送 2026-06-10 · [GitHub](https://github.com/fosenai/cord) · [官网](https://www.npmjs.com/package/@fosenai/cord) · 组织维护 · 中文 README

**去中心化 agent 互联网络：让 LLM/MCP/后端互相发现与调用**

用 Rust 编写的分布式 agent 网络：将 LLM CLI、MCP 服务器、HTTP 后端、机器人或 IoT 设备封装为网络节点，其他 agent 通过自然语言语义搜索在 mesh 中发现并调用，无中心注册表。传输层支持 TCP/WebSocket/WSS 加密与 NAT 穿透，提供 L0-L3 沙箱、三级可见性（public/unlisted/gated）与 ACL 白名单。安装经 npm 一条命令，首启自动生成 BIP-39 身份并检测本地 LLM CLI。当前版本为 0.1.0-alpha.8，属早期阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 任意 LLM CLI / MCP 服务器 / HTTP 后端一条命令发布为网络能力
- 自然语言语义搜索的分布式 agent 发现，无中心注册表
- L0-L3 多级沙箱与 public/unlisted/gated 三级可见性控制
- SOUL 文件定义 agent 角色、白名单与 ACL，附 12 个模板

## 适用场景

- 把本地 claude/codex/ollama 订阅共享给团队其他机器调用
- 让不同模型或专业 agent 通过 mesh 互相委派协作
- 将 MCP 服务器的全部工具自动注册为可发现能力

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L13: **Cord** turns every AI agent — LLM, MCP server, HTTP backend, robot, or IoT
> L51: - **Wraps anything in one command** — `cord publish-mcp`, `cord soul agent.md`,
> L91: |`/find <natural language>`|semantic search across the mesh|

## 星数曲线

```mermaid
xychart-beta
    title "fosenai/cord 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `1f2dd5c6691c` · [字段定义](../../DATASET.md)*
