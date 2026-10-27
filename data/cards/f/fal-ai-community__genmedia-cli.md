# fal-ai-community/genmedia-cli

⭐ 81 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/fal-ai-community/genmedia-cli) · [官网](https://genmedia.sh) · 组织维护

**面向 fal.ai 模型平台的 agent 优先命令行客户端**

genmedia 是操作 fal.ai 1200+ 生成模型端点的 CLI：搜索模型、查看输入输出 schema、以 CLI flag 传参运行模型、异步提交与状态查询、文件上传至 fal CDN、查询定价与文档搜索。TTY 下输出美化视图，管道或 --json 时输出结构化 JSON，无需 MCP 即可供 AI agent 调用。附带会话级 HTML 产物画廊，通过环境变量与进程树识别 Claude Code、Codex、Cursor 等 agent 会话。安装经 curl/PowerShell 脚本，密钥经 FAL_KEY 或交互式 setup 向导配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- models/schema/run/status 等命令覆盖 fal.ai 模型的搜索、检视与运行
- TTY 美化输出与非 TTY 结构化 JSON 双模式，无 MCP 依赖
- 产物自动记录为会话级静态 HTML 画廊，支持多 agent 会话识别
- 异步队列提交、CDN 上传、定价查询与文档搜索

## 适用场景

- 在终端或 CI 中直接调用 fal.ai 上的生成模型
- 让 Claude Code、Codex 等 coding agent 通过 shell 命令使用生成模型
- 浏览一次会话内多个模型产出的图像/视频/音频资产

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Agent-first CLI for fal.ai — search, run, and manage 1200+ model endpoints.
> L5: Works great for humans in a terminal and equally well for AI agents via shell commands. In a TTY, commands display a
> L100: Any model input parameter can be passed as a `--flag value` pair. Run `genmedia run <endpoint_id> --help` to see a

## 星数曲线

```mermaid
xychart-beta
    title "fal-ai-community/genmedia-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 79 --> 82
    line [80, 81]
```

2026-10-18 80 → 2026-10-27 81（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6c6de0546b1e` · [字段定义](../../DATASET.md)*
