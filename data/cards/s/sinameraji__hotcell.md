# sinameraji/hotcell

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/sinameraji/hotcell) · [官网](https://directionallylocal.com/hotcell/) · 组织维护

**自托管的 AI agent 沙箱运行时：Docker/microVM 隔离，密钥不入沙箱**

在自有硬件上批量创建隔离 agent 沙箱的 CLI 工具：支持 Docker、Firecracker（Linux/KVM）与 Apple VZ（macOS）三种隔离后端，统一接口管理。核心机制是网关密钥替换——真实 API key 留在宿主机，沙箱内仅持有可计量、可限额、可撤销的短期令牌；内置 OpenAI/Anthropic/OpenRouter/GitHub/Stripe 五条路由，非 HTTP 协议与请求签名类凭证不在保护范围。提供五实例并行克隆同仓库、一次性 run 命令、默认拒绝出站流量（Linux/microVM 内核强制）。通过 npm 全局安装，另有 Python SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 真实 API key 留在宿主机，沙箱内仅持有网关令牌，按用量计量并可撤销
- 三种隔离后端：Docker、Firecracker（Linux/KVM）、Apple VZ（macOS）
- 单命令创建 5 个沙箱各挂一个分支并行跑 agent，实时显示每沙箱 CPU/内存/成本
- 准入控制拒绝超售而非 OOM；可选默认拒绝出站流量

## 适用场景

- 在同一仓库上并行跑多个 agent 各做不同特性
- 让不可信 agent 代码在隔离沙箱里执行而不泄露 API key
- 在自有 Mac Mini/云主机/裸金属上自托管 agent 运行环境
- 按沙箱计量和限额各 agent 的 LLM 调用开销

## 场景标签

`Agent 框架` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L8: **Sandboxes for AI agents, on your own hardware.** A Mac Mini on your desk, a cloud VM, a bare-metal box — as many i
> L56: - **Keys stay out.** Sandboxes reach LLMs and GitHub through a gateway that swaps a per-sandbox token for the real 
> L58: - **Containers or microVMs** — Docker everywhere, Firecracker (Linux/KVM) and Apple VZ (macOS) for VM-grade isolati

## 星数曲线

```mermaid
xychart-beta
    title "sinameraji/hotcell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `3c7c208ef5eb` · [字段定义](../../DATASET.md)*
