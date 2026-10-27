# jahwag/clem

⭐ 32 · Go · MIT · 推送 2026-08-08 · [GitHub](https://github.com/jahwag/clem) · [官网](https://myclementine.ai) · 个人维护

**在自有 Linux 主机上 24/7 运行 Claude Code agent 团队的编排工具**

clem 以 systemd + tmux 为每个 agent 建立独立 Linux 用户并持续运行循环：启动 claude/opencode/codex 运行时、注入提示、等待会话结束、按配置间隔重复。团队通过 Discord、Slack 或 GitHub Issues 协调任务并开 PR，watchdog 自动重启崩溃会话。安全方面在 OS 层做隔离：secret-zero 凭据代理、可选的 nftables 每 UID 出站防火墙（默认关闭）。Go 编写，提供 Linux 二进制发布或源码构建，需 systemd 主机与 tmux/git/python3/age/sops/yq 等依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每个 agent 独立 Linux 用户 + systemd + tmux，watchdog 自愈
- 多运行时支持：claude-code / opencode / codex，可混用 Anthropic、Bedrock、Vertex、Ollama 等 provider
- OS 层安全隔离：secret-zero 凭据代理与 per-UID 内核出站防火墙（均默认关闭、需显式启用）
- Discord / Slack / GitHub Issues 三种可切换协调后端

## 适用场景

- 在自己的服务器上 24/7 运行一个多 agent 编码团队并让其自主开 PR
- 通过 Discord/Slack 给 agent 派活并跟踪进度
- 对自治 agent 做凭据与出站流量的 OS 级隔离

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L21: `clem` runs a team of Claude Code agents 24/7 on any Linux host. Each agent is a separate OS user in a tmux session
> L39: |**Multi-runtime**|`runtime: claude-code \|opencode \|codex`. Mix Anthropic cloud, ChatGPT OAuth, Bedrock, Vertex, 

## 星数曲线

```mermaid
xychart-beta
    title "jahwag/clem 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `41d68beb9842` · [字段定义](../../DATASET.md)*
