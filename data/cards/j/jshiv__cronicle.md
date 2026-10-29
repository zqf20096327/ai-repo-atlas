# jshiv/cronicle

⭐ 23 · Go · MIT · 推送 2026-10-24 · [GitHub](https://github.com/jshiv/cronicle) · 个人维护

**以 cron 调度 AI agent 与 shell 任务的 HCL 工作流引擎**

Go 编写的调度器，将 AI agent 任务与 shell 任务纳入同一声明式运行时：用 cronicle.hcl 定义 cron 触发、DAG 依赖（depends/for_each）、失败时自动跳过下游任务。agent 任务支持指定模型、工具、max_turns 与 budget_usd 成本上限，声称原生支持 Anthropic Agent Skills 与 MCP 服务器。运行透明化：绘制 DAG 树、逐任务输出带命令的框式日志、失败时给出可粘贴重现行，可输出 pretty/text/json 三种格式并写 JSONL 转录。配置文件可由远程 git 仓库追踪与刷新，支持三种 git 认证与加密 secret store。通过 install.sh 一键安装或下载二进制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HCL 声明式配置，shell 与 agent 任务共用同一调度器
- agent 任务支持 budget_usd 成本上限、工具与轮次限制
- DAG 树可视化输出、per-run JSONL 转录与失败重现行
- 配置可由远程 git 仓库追踪，支持 SSH/env/secret 三种认证

## 适用场景

- 定时触发 AI agent 执行代码审查、日报生成等任务
- 用 DAG 依赖把多个 shell/agent 步骤串成流水线
- 对每次 agent 运行的成本与输出做审计留痕

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L2: Production-grade scheduling for AI agents. Cron triggers, git versioning, HCL config, slog audit trails, per-run cos
> L4: Shell tasks still work the way they always did. Agent tasks share the same scheduler, the same git/HCL config, the s
> L260:  model = "claude-sonnet-4-6"

## 星数曲线

```mermaid
xychart-beta
    title "jshiv/cronicle 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5b6532632d45` · [字段定义](../../DATASET.md)*
