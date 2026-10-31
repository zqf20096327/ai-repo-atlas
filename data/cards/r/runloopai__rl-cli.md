# runloopai/rl-cli

⭐ 16 · TypeScript · MIT · 推送 2026-09-28 · [GitHub](https://github.com/runloopai/rl-cli) · [官网](https://runloop.ai) · 组织维护

**Runloop.ai 平台的交互式终端 CLI/TUI，含 MCP 服务器**

面向 Runloop.ai 平台使用者的终端工具：提供带菜单与实时更新的交互式 TUI（rli）与传统 CLI 两种模式，输出支持文本/JSON/YAML。命令覆盖 devbox、快照、蓝图、对象、网络策略、密钥、网关与 MCP 配置管理，可在 devbox 中执行命令、SSH、PTY shell 与查看日志。内置 Model Context Protocol 服务器，供 Claude 等 AI 助手操作 devbox，支持 stdio 与 HTTP 模式。通过 npm 全局安装，需 RUNLOOP_API_KEY。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- TUI 与 CLI 双模式，CLI 输出支持 text/JSON/YAML
- 管理 devbox、快照、蓝图、对象、密钥、网络策略等资源
- 内置 MCP 服务器供 AI 助手（如 Claude）操作 devbox，支持 stdio/HTTP
- 支持自定义 RUNLOOP_BASE_URL 指向其他部署

## 适用场景

- 在终端里创建和管理 Runloop devbox 与快照
- 用脚本自动化 Runloop 平台资源操作（JSON/YAML 输出）
- 把 Runloop 接入 Claude Desktop，用对话操作 devbox

## 场景标签

 · 领域:开发者工具/云沙箱管理

## 证据(README 行号)

> L7: A **TUI + CLI** for the Runloop.ai platform. Use it as an **interactive TUI** (Terminal User Interface) with rich UI
> L29: - 🤖 **Model Context Protocol (MCP) server for AI integration**
> L194: Runloop includes a Model Context Protocol (MCP) server that allows AI assistants like Claude to interact with your

## 星数曲线

```mermaid
xychart-beta
    title "runloopai/rl-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `879319da2a27` · [字段定义](../../DATASET.md)*
