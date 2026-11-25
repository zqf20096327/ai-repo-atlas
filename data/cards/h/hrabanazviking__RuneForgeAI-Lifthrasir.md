# hrabanazviking/RuneForgeAI-Lifthrasir

⭐ 3 · Python · GPL-2.0 · 推送 2026-11-20 · [GitHub](https://github.com/hrabanazviking/RuneForgeAI-Lifthrasir) · 个人维护

**面向 Linux 运维的研究项目：诊断故障、授权修复、可回滚**

Lífþrasir 是一个探索自进化 Linux 系统的研究项目，围绕 Heimdall（观测）、Mímir（本地证据记忆）、Replicater（多 agent 调查）、Eir（授权修复回滚）、Thor（威胁防御）、Upstream Forge（内核补丁档案）六个角色组织。仓库当前包含 44 个 Python 模块、69 个测试模块、SQLite 证据存储与只读主机观察器；自主修复等能力仍处于提案/分阶段实施状态，安全边界规定 LLM 不持有 root 权限，所有主机变更经确定性策略引擎与窄权限 broker 执行。GPLv2 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六角色架构：观测、证据记忆、多 agent 调查、授权修复、防御、补丁档案
- 确定性策略引擎与窄权限 broker，LLM 不持有 root 权限
- SQLite 证据存储、来源哈希、隐私脱敏与因果假设记录
- 一次性 VM 中完成离线故障检测、修复提案与回滚验证的里程碑设计

## 适用场景

- 在一次性 VM 中检测并修复损坏的非关键用户服务
- 为内核维护者生成可人工评审的补丁档案
- 只读观测主机服务、日志与内核健康状态

## 场景标签

`多智能体` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L12: Lífþrasir is a **Mythic Engineering / RuneForgeAI research project** exploring Linux that can diagnose failures, sa
> L48: **Security boundary:** An LLM never holds unrestricted root privileges. All host changes use a deterministic policy
> L121: |Source|**44 Python modules** under src/lifthrasir, plus laboratory drivers and an observer, a read-only CLI, and 

## 星数曲线

```mermaid
xychart-beta
    title "hrabanazviking/RuneForgeAI-Lifthrasir 星数(近 2 点)"
    x-axis ["2026-11-15", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-15 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `7bbe8a71c6c8` · [字段定义](../../DATASET.md)*
