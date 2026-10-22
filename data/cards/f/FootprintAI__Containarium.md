# FootprintAI/Containarium

⭐ 310 · Go · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/FootprintAI/Containarium) · [官网](https://containarium.dev) · 组织维护

**给 AI agent 的自托管隔离运行时：每个 agent 一个 SSH 可达容器**

开源 agent 运行时：在 LXC 或 Kubernetes 上为每个 AI agent 提供一个持久化、SSH 可达的非特权容器（box），通过 MCP 暴露平台管理与盒内文件/命令工具（shell_exec、read_file 等）。安全机制包括可选的每租户 eBPF 出网策略、审计日志拒绝记录、模型网关使 provider API key 不进入容器、agent 仅持有 SSH key 而非集群 token。支持自带 agent（Claude Code、Cursor、OpenCode 等），提供 curl 一键安装脚本与 quickstart 流程，另有托管云选项。默认配置与各项安全声明的依据记录在 docs/security/CLAIMS.md。

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

- 每个 agent 一个持久化 SSH 容器，运行于 LXC 或 Kubernetes 后端
- 盒内 agent-box MCP 服务器：shell_exec/read_file/write_file 等有界工具（30s 默认超时、256KiB 输出上限）
- 可选每租户 eBPF 出网策略与审计日志；模型网关使 API key 不进入容器
- quickstart 一条命令完成建 box、SSH 配置与 agent MCP 接线（默认 Claude Code，可选 gemini/codex）

## 适用场景

- 让 AI agent 在隔离沙箱里构建、安装、部署和验证，而非在本机
- agent 长时间任务（如跑测试）在 box 内运行，断线后 byte-exact 重连查看输出
- 把 agent 构建的应用通过 expose-port 暴露到公网域名
- CI 失败后保留环境供 agent 调试（ci-context/ci-prompt MCP 资源）

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L58: That's the runtime Containarium gives you. It runs as a self-hosted
> L60: ships a second MCP server that lives *inside* the box so the agent can
> L165: Your agent reaches the box through `agent-box`, an MCP server that runs

## 星数曲线

```mermaid
xychart-beta
    title "FootprintAI/Containarium 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 303 --> 310
    line [304, 309, 309]
```

2026-10-18 304 → 2026-10-21 309（+5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fb29c674ddeb` · [字段定义](../../DATASET.md)*
