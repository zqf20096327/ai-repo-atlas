# richardartoul/swarmd

⭐ 32 · Go · BSD-3-Clause · 推送 2026-09-23 · [GitHub](https://github.com/richardartoul/swarmd) · 个人维护

**多租户后台 Agent 运行时：以 YAML 定义、沙箱化安全运行**

Go 编写的多租户 agent 运行时（agent harness）：Agent 以 YAML 定义，作为 goroutine 在多租户服务器中运行，配备虚拟 shell、内置工具与允许列表式自定义工具。沙箱不依赖操作系统原语，文件系统与网络访问均经接口限制；支持 OpenAI 与 Anthropic 作为 worker driver。提供 SQLite 状态存储与本地 TUI，pkg/agent 可嵌入自有 Go 应用。README 声明为 alpha 软件，未经过大规模测试与生产加固。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- YAML 定义 Agent，goroutine 多租户运行
- 不依赖操作系统沙箱原语，文件/网络访问经受控接口
- 内置 9 种工具，另附 Datadog/GitHub/Slack 允许列表式自定义工具
- pkg/agent 可直接嵌入 Go 应用，无需完整服务器

## 适用场景

- 在共享服务器上安全运行多个后台 Agent
- 把沙箱化 Agent 嵌入自己的 Go 应用
- 为团队提供带 Slack/GitHub/Datadog 工具的后台自动化 Agent

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L11: `swarmd` is a multi-tenant runtime for running background Agents in a safe and secure manner. Agents are defined in
> L22: `swarmd` does not rely on any operating system sandboxing primitives. It will run anywhere you can run a Go applica

## 星数曲线

```mermaid
xychart-beta
    title "richardartoul/swarmd 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a950f8ed1027` · [字段定义](../../DATASET.md)*
