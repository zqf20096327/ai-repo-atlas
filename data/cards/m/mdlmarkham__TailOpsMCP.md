# mdlmarkham/TailOpsMCP

⭐ 19 · Python · 推送 2025-12-28 · [GitHub](https://github.com/mdlmarkham/TailOpsMCP) · 个人维护

**经 Tailscale 安全连接的 MCP 控制平面网关，用 AI 助手管理分布式基础设施**

TailOpsMCP 是一个 MCP（Model Context Protocol）服务器，作为单一控制平面网关，通过 SSH、Docker socket 与 HTTP 连接管理多个目标节点，供 Claude、ChatGPT 等 MCP 兼容客户端以自然语言执行运维操作。安全机制包括基于能力的授权与参数校验（防 LLM 臆造指令）、OAuth 2.1（Tailscale TSIDP）、审计日志与非 root systemd 沙箱；无内置 TLS，强制要求 Tailscale 加密传输，审批门需外部 webhook。面向基础设施团队、SRE 与 DevOps 工程师，典型部署于 Proxmox LXC 容器，提供一键安装脚本与 git clone 开发流程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一网关经 SSH/Docker/HTTP 管理多目标，无需在各节点部署 agent
- 能力白名单授权与参数校验防 'LLM imagination' 风险
- Tailscale TSIDP OAuth 2.1 认证、审计日志、systemd 沙箱加固
- Proxmox LXC 一键部署脚本与多网关分段冗余设计

## 适用场景

- 通过 AI 助手对多台服务器批量执行部署、更新与日志分析
- homelab/分布式环境下集中管理 SSH、Docker 与 HTTP 目标
- 按网段部署多个网关实现故障隔离与高可用

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L6: > Model Context Protocol (MCP) server that operates as a control plane gateway, managing SSH, Docker, and HTTP targe
> L21: TailOpsMCP is a control plane gateway that centralizes management of distributed infrastructure through AI assistan

## 星数曲线

```mermaid
xychart-beta
    title "mdlmarkham/TailOpsMCP 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `629d06f54d62` · [字段定义](../../DATASET.md)*
