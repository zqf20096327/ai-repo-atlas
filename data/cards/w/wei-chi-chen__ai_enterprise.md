# wei-chi-chen/ai_enterprise

⭐ 5 · Python · 推送 2026-10-31 · [GitHub](https://github.com/wei-chi-chen/ai_enterprise) · 个人维护 · 中文 README

**全离线多 agent 自主软件开发框架，本地 Ollama 驱动**

基于 Ollama 的 100% 离线多 agent 框架，默认提供 12 位虚拟研发员工（架构师、主管、审查员等）的示例编制，角色数量与每员工挂载的本地模型均可通过配置文件增删调整。核心机制包括 ExecutionSandbox 沙盒中的 TDD 单元测试闭环、测试失败时由 14B→32B 模型逐级接管的三级重构机制、以及基于 PID 的进程锁、断点续跑与显存动态平衡。主要支持 Windows 10/11，Linux/macOS 仅有基本兼容代码，通过 git clone 与 Python 3.10/3.11 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 沙盒 TDD 闭环：代码须在 ExecutionSandbox 中通过独立单元测试才交付
- 三级主管阶梯重构：14B 审查员自修→32B 主管重构→32B 仲裁长终裁
- 员工数量、模型选择、内存配额与并行槽位均可配置
- 断点续跑、PID 进程锁与 Ollama /api/ps 显存动态平衡

## 适用场景

- 在完全离线环境中让本地模型自主完成软件研发任务
- 企业内部代码生成不接触云端 API
- 按自家硬件内存预算定制多 agent 团队规模与模型阶梯

## 场景标签

`Agent 框架` `多智能体` `代码生成` · 领域:Agent 开发

## 证据(README 行号)

> L18: **Local Autonomous AI Enterprise** 是一個 100% 離線運行的多代理人（Multi-Agent）自主研發與軟體生產框架。
> L105: > ⚠️ **Core Concept: This project provides a flexible, self-healing, multi-agent architectural framework.**

## 星数曲线

```mermaid
xychart-beta
    title "wei-chi-chen/ai_enterprise 星数(近 3 点)"
    x-axis ["2026-10-31", "2026-11-01", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-31 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `cca3c4f27f16` · [字段定义](../../DATASET.md)*
