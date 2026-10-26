# Chimera-Protocol/csl-core

⭐ 27 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/Chimera-Protocol/csl-core) · [官网](https://runtime.chimera-protocol.com/) · 组织维护

**发现并治理主机上 AI agent 的策略执行框架：Z3+TLA+ 证明、模型外强制**

面向运维与安全工程师的 AI agent 治理工具链：cslcore venom 扫描主机上的助手、MCP 服务器、定时任务等 agent，构建可达图并找出多 agent 级联链；cslcore setup 以十步可恢复流程为每个 agent 生成策略，用 Z3 证明一致性、TLA+（TLC）模型检查，测试映射代码对绕过手法（路径穿越、命令替换等）的抵抗；策略在模型外编译执行，通过 Claude Code PreToolUse hook 或 Python 工具装饰器接入调用路径，支持 log/block 模式、审批流与 kill switch，变更记录于 audit.jsonl。限制：工作区须在本地磁盘（NFS 不可靠），纯 schema 工具无法自动接线，TLA+ 检查需 Java。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- venom 扫描发现 agent 并构建可达图，识别多 agent 级联链
- 策略经 Z3 一致性证明与 TLA+（TLC）模型检查
- 映射代码以绕过技巧用例（路径穿越、命令替换等）做回归测试
- 通过 Claude Code hook 与 Python 装饰器在模型外确定性执行，含审批与 kill switch

## 适用场景

- 盘点我机器上到底跑着哪些 AI agent、各自能触达什么
- 在启用拦截前预览策略会拦住哪些真实调用
- 以 csl-limits.ini 把 agent 权限纳入代码评审与 CI 门禁
- 对 Claude Code / LangChain 等工具调用做审批与实时管控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L12: CSL-Core finds every AI agent on a host and what it can reach, writes a policy for each one,
> L13: proves the policies with Z3 and TLA+, tests the code that connects agents to policies against
> L14: bypass tricks, and enforces them deterministically, outside the model. The model never sees the

## 星数曲线

```mermaid
xychart-beta
    title "Chimera-Protocol/csl-core 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dc245af329fc` · [字段定义](../../DATASET.md)*
