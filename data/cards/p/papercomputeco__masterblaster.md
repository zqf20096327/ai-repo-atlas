# papercomputeco/masterblaster

⭐ 76 · Go · AGPL-3.0 · 推送 2026-09-24 · [GitHub](https://github.com/papercomputeco/masterblaster) · 组织维护

**为 AI agent 创建与管理 stereOS 沙箱虚拟机的命令行工具**

Masterblaster（mb）是一个 CLI 工具，用于启动基于 NixOS 的 stereOS Linux 虚拟机，作为 AI agent 的隔离沙箱，并管理其完整生命周期：拉取预置 agent harness 的 mixtape 镜像、通过 jcard.toml 定义 CPU/内存/磁盘/网络/共享目录/秘密注入等配置、启动与销毁沙箱。沙箱为临时性、可复现，支持 QEMU（macOS Apple Silicon、Linux aarch64）与 Apple Virt 后端。默认 agent harness 为 claude-code，可选 opencode、gemini-cli 或自定义。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 NixOS 的 stereOS 沙箱，管理镜像拉取、创建、秘密注入、共享目录挂载与编排
- 单一 jcard.toml 配置文件定义资源、网络（nat/bridged/none、端口转发、出站白名单）与 agent 参数
- 支持 claude-code / opencode / gemini-cli / custom 多种 agent harness
- QEMU 与 Apple Virt 两种虚拟化后端

## 适用场景

- 在隔离沙箱中安全运行 AI coding agent 处理项目
- 为 agent 配置只读共享目录与出站网络白名单限制
- 用可复现镜像批量创建临时 agent 运行环境

## 场景标签

 · 领域:AI 基础设施/虚拟化

## 证据(README 行号)

> L3: Create, manage, and orchestrate AI agents sandboxes.
> L7: Masterblaster boots stereOS machines - a
> L9: full lifecycle: image pulling, machine creation, secret injection, shared directory
> L74: |`[agent]`|`harness`|`"claude-code"`|`"claude-code"`, `"opencode"`, `"gemini-cli"`, `"custom"`|

## 星数曲线

```mermaid
xychart-beta
    title "papercomputeco/masterblaster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 75 --> 77
    line [76, 76]
```

2026-10-18 76 → 2026-10-27 76（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b8b231115176` · [字段定义](../../DATASET.md)*
