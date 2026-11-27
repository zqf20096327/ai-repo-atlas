# enthouan/komodo-mcp

⭐ 8 · Rust · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/enthouan/komodo-mcp) · [官网](https://komodo-mcp.com) · 个人维护

**给 LLM 客户端提供 Komodo 基础设施读写工具的 Rust MCP 服务器**

用 Rust 与官方 rmcp SDK 编写的可自托管 Model Context Protocol 服务器，通过官方 komodo_client 连接 Komodo Core，提供 64 个只读工具检查服务器、Stack、部署、构建、Swarm 集群、Docker 资源，并输出作用域化的 TOML 巡检报告。支持 stdio 与带 Bearer 令牌的 Streamable HTTP 两种传输；写操作类工具（操作、配置编辑、清理、终端）默认关闭，需逐项显式开启，并依赖 Core 端权限。需 Rust 1.99.1 编译运行，配置三个必需环境变量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 64 个只读工具：清单巡检、日志读取、stack 一键诊断、TOML 导出
- stdio 与带令牌的 Streamable HTTP 两种传输方式
- 破坏性能力（清理/操作/终端）默认关闭、逐项 opt-in
- 支持按名称启用/禁用单个工具

## 适用场景

- 在 MCP 客户端中巡检 Komodo 管理的服务器、Stack 与部署状态
- 让 LLM 客户端读取容器网络/镜像/卷等 Docker 资源
- 通过审批后的受控工具执行单次工作负载操作或扩缩容

## 场景标签

 · 领域:DevOps/基础设施管理

## 证据(README 行号)

> L11: A Rust Model Context Protocol server for
> L14: exactly with optional features disabled. Sixty-four read-only tools list and inspect
> L117: Configure an MCP client to launch the compiled executable using its absolute

## 星数曲线

```mermaid
xychart-beta
    title "enthouan/komodo-mcp 星数(近 3 点)"
    x-axis ["2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 4 --> 9
    line [5, 8, 8]
```

2026-11-25 5 → 2026-11-27 8（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f3d0212787b7` · [字段定义](../../DATASET.md)*
