# Dqz00116/opencode-solo

⭐ 32 · MIT · 推送 2026-09-24 · [GitHub](https://github.com/Dqz00116/opencode-solo) · 个人维护 · 中文 README

**opencode 的多子代理编排配置：专家模型规划、快速模型执行**

面向 opencode 编码 agent 的配置文件集合：一个闭环编排代理 solo 通过 bash 运行测试并以失败数为信号迭代（编辑→测试→决策，直到测试通过），将代码修改委派给 explore/editor/verify/reviewer 等 6 个专职子代理。子代理会话隔离上下文，主代理仅保留摘要与决策（约 5-10K token），按角色映射到不同模型（专家模型规划、快速模型执行）。安装方式为克隆仓库并复制 .md 配置文件到 opencode 配置目录，需已安装 opencode 与至少一个 LLM provider。README 附 SWE-bench Verified 50 实例评测数据，并说明结果仅供参考。

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

- 闭环工作流：bash 直接感知测试结果，迭代至目标测试通过
- 6 个专职子代理（explore/editor/verify/reviewer/observer/general）+ solo 编排者
- 上下文隔离：主代理仅持有摘要与决策（约 5-10K token）
- agent 文件与模型无关，通过 opencode.jsonc 按代理映射 provider

## 适用场景

- 在 opencode 中用多代理架构处理长周期、多文件工程任务
- 通过模型分层降低 token 成本同时保留专家级规划
- 为编码代理加入对抗性验证与按需代码评审

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L7:  A closed-loop orchestrator + specialized subagent system for opencode.
> L105: Agent files are **model-agnostic**. Map each agent to a provider in your `opencode.jsonc`:
> L145: All `.md` files contain only behavior (prompt, permissions, mode). Models are configured separately in `opencode.j
> L149: - opencode

## 星数曲线

```mermaid
xychart-beta
    title "Dqz00116/opencode-solo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c499186aaff9` · [字段定义](../../DATASET.md)*
