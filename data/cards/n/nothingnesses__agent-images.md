# nothingnesses/agent-images

⭐ 47 · Shell · BlueOak-1.0.0 · 推送 2026-10-25 · [GitHub](https://github.com/nothingnesses/agent-images) · 个人维护

**用 Nix 可复现构建 AI 编程 agent 沙箱容器镜像**

面向 AI 编程 agent 的 OCI 容器镜像构建项目：消费 llm-agents.nix 提供的 agent 包，产出可用 agent-box 编排或独立运行于 Podman/Docker 的沙箱镜像，目的在于限制 agent 对宿主文件系统与密钥的访问。预置 20 余个 agent 镜像（Claude Code、Codex CLI、Gemini CLI 等）及 AI 助手类镜像；镜像内置基础 CLI 工具集，默认以非 root 的 agent 用户与 /workspace 工作目录运行。通过 mkAgentImage 可自定义包集、用户、XDG 目录、容器内 Nix 与 nix-ld。限制：需 Nix（flakes）与 Podman/Docker，镜像仅支持 Linux（macOS 需远程 Linux 构建器），NixOS 需额外 rootless Podman 配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | BlueOak-1.0.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Nix flakes 可复现构建 20+ 个 AI 编程 agent 的 OCI 镜像
- 默认非 root agent 用户、/workspace 工作目录与预置基础 CLI 工具集
- mkAgentImage 支持自定义 basePackages、用户/组、XDG 目录与额外可写路径
- 可选启用容器内 Nix 与 nix-ld 以运行外来动态链接二进制

## 适用场景

- 把 AI 编程 agent 跑进容器，隔离其对 SSH 密钥与云凭据的访问
- 配合 agent-box 以 local 或 git worktree 沙箱模式运行 agent
- 自定义构建最小化或含 Nix 工具链的 agent 镜像

## 场景标签

 · 领域:AI agent 基础设施/容器化

## 证据(README 行号)

> L5: Consumes agent packages from llm-agents.nix and produces images usable with agent-box or standalone Podman/Docker.
> L8: llm-agents.nix (packages)  ->  agent-images (images)  ->  agent-box (orchestration)
> L15: Running agents inside containers limits what they can see. Nix makes the images

## 星数曲线

```mermaid
xychart-beta
    title "nothingnesses/agent-images 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-25 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1bc717ed5878` · [字段定义](../../DATASET.md)*
