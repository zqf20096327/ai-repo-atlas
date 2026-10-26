# skalenetwork/microsandbox-reef

⭐ 25 · Rust · MIT · 推送 2026-10-20 · [GitHub](https://github.com/skalenetwork/microsandbox-reef) · [官网](https://reef.clawbits.ai) · 组织维护

**在自管服务器 microVM 中运行 AI agent 的角色策略编排工具**

reef 是一个 Rust CLI，在自有服务器上用 microsandbox microVM 运行 OpenClaw、Hermes 等及自建 agent。核心机制是 TOML 角色文件：一次性定义镜像、资源、DNS 强制的出站域名白名单与主机侧密钥绑定（客机只见占位符，不见值）；同一角色版本被所有 agent 继承，落后版本标记 stale。无守护进程，变更命令内联调和，agent 记录比 VM 生命周期更长。提供 fleet 收敛、SSH/exec/端口转发、事件日志与跨主机控制台 UI。限制：仅 Linux x86_64/aarch64（glibc≥2.39）与 Apple Silicon macOS，主机需配套 msb bundle。

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

- TOML 角色文件统一声明镜像、出站域名白名单与密钥绑定
- microVM 隔离运行 agent，密钥值不出现在客机
- 无守护进程，命令内联调和，记录比 VM 更持久
- fleet 收敛、跨主机控制台 UI 与事件日志

## 适用场景

- 在自有服务器上隔离运行 OpenClaw/Hermes 等 agent
- 以可审计的策略文件限定 agent 可访问的域名与密钥
- 跨多台主机统一查看和启停 agent 机队

## 场景标签

 · 领域:AI agent 基础设施/沙箱隔离

## 证据(README 行号)

> L3: **Contained AI agents on your servers.**
> L7: A **role** is a TOML file: the image, the resources, the domains an agent may
> L11: your own servers. There is no daemon: every mutating command reconciles

## 星数曲线

```mermaid
xychart-beta
    title "skalenetwork/microsandbox-reef 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-26 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `19fcf9915877` · [字段定义](../../DATASET.md)*
