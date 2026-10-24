# rubycatco/claude-agent-sdk-ruby

⭐ 50 · Ruby · MIT · 推送 2026-10-23 · [GitHub](https://github.com/rubycatco/claude-agent-sdk-ruby) · [官网](https://rubydoc.info/gems/claude-agent-sdk) · 组织维护

**面向 Ruby/Rails 的 Claude Code agent 运行时非官方 SDK**

社区维护的 Ruby SDK，封装 Claude Code CLI 运行时：以子进程方式启动 claude CLI 并通过 stream-JSON 协议通信，提供 query()/ask() 一次性调用与 Client 双向会话，覆盖会话恢复、子代理、沙箱、结构化输出与检查点回退。面向生产 Ruby/Rails 应用，附带 Rails 生成器、CLI 固定版本 vendor 安装、ActiveRecord 安全回调线程、内置 OpenTelemetry 观测与会话转录镜像（Postgres/Redis/S3 参考适配）。非官方项目，逐版本跟踪官方 TS/Python SDK。需 Ruby 3.2+ 与 Claude Code CLI 2.0.0+，凭 ANTHROPIC_API_KEY 或 OAuth token 认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 与官方 SDK 相同协议：子进程运行 claude CLI，stream-JSON 通信
- 33 个 hook 生命周期事件与权限回调，可拦截审计每次工具调用
- Ruby block 定义进程内自定义工具（SDK MCP server），JSON Schema 参数校验
- CLIInstaller 固定版本 vendor CLI 二进制，生产部署不依赖全局 npm install

## 适用场景

- 在 Rails 应用中集成 Claude agent 处理后台任务与 ActionCable 流式输出
- 用 Ruby 定义进程内工具并让 agent 直接访问应用状态
- 通过 hook 与权限回调对 agent 的工具调用做程序化门控和审计
- 将会话转录镜像到自有存储并跨主机恢复会话

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: A Ruby SDK for the Claude Code agent runtime, built for running agents in production Ruby and Rails apps. It has th
> L22: - **Same wire protocol as the official SDKs.** Spawns the `claude` CLI as a subprocess and speaks stream-JSON over 
> L199: ## Comparison with the official SDKs

## 星数曲线

```mermaid
xychart-beta
    title "rubycatco/claude-agent-sdk-ruby 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-24 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `68776ce754a3` · [字段定义](../../DATASET.md)*
