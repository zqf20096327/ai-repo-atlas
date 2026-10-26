# rcarmo/agentbox

⭐ 153 · Dockerfile · MIT · 推送 2026-10-10 · [GitHub](https://github.com/rcarmo/agentbox) · [官网](https://rcarmo.github.io/projects/agentbox/) · 个人维护

**Docker 化的编程 agent 沙箱容器，隔离运行多个编码代理**

基于 Docker 的编程 agent 沙箱环境：默认镜像为 Debian Stable 开发环境，预装 Copilot CLI、Codex、Pi 等编码代理与 gh、lazygit 等工具，另可通过容器内 Makefile 安装 Toad、OpenCode、Gemini CLI、mistral-vibe。提供服务开关（Docker-in-Docker、SSH、RDP）、工作区骨架、XFCE+XRDP 的 GUI 镜像与 Docker Compose 工作流，配合 webterm 运行多个 agent 会话。安全上默认关闭所有服务，需显式启用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预装 Copilot CLI、Codex、Pi，可再装 Toad/OpenCode/Gemini CLI/mistral-vibe
- ENABLE_DOCKER/SSH/RDP 环境变量控制服务，默认全部禁用
- 含 XFCE/XRDP/VS Code 的 GUI 镜像标签
- 内置工作区骨架与 agent 技能（workspace-skel）

## 适用场景

- 为编码 agent 提供隔离的容器化运行环境
- 并行运行多个 agent 会话（配合 webterm）
- 通过 SSH/RDP 远程访问容器内的开发环境

## 场景标签

 · 领域:开发工具/容器化环境

## 证据(README 行号)

> L7: Agentbox is a Docker-based coding agent sandbox, originally inspired by Batrachian Toad, and now generalized to more
> L15: - **Preinstalled coding agents**: Copilot CLI, Codex, Pi
> L18: - **Optional agent tooling**: install `toad`, `opencode`, `gemini`, and `vibe` via `make -C ~ ...`

## 星数曲线

```mermaid
xychart-beta
    title "rcarmo/agentbox 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 151 --> 154
    line [152, 153, 153]
```

2026-10-18 152 → 2026-10-26 153（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `cd5715e93eac` · [字段定义](../../DATASET.md)*
