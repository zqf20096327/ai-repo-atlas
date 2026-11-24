# mftnakrsu/airgap-anything

⭐ 3 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/mftnakrsu/airgap-anything) · [官网](https://airgap-anything.mefby.com) · 个人维护

**为离线隔离环境设计 LLM 系统的 agent 技能**

面向无互联网网络的 agent skill 集合，含 airgap-architect 与 airgap-transfer 两个技能：前者通过访谈收集组织与硬件信息，按 tier 与 size.py 脚本计算 GPU/服务器/电力规模，从决策表为每层选出组件并输出蓝图与传输清单；后者将清单转为可自校验的离线搬运包（fetch 脚本、SHA-256、分盘、runbook）。设计在联网机器上完成，网内执行不需要互联网或 LLM。以 Claude Code 插件或 Agent Skills 通用格式分发，需 Python 3.11+，无其他依赖且不发起网络调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- airgap-architect：访谈→分层决策→GPU sizing→蓝图与 transfer manifest 的 8 步流程
- airgap-transfer：自校验离线搬运包（fetch.sh、SHA-256、分盘、verify.sh/load.sh）
- 决策条目带 field/docs/estimate 证据标签，estimate 决策列入待验证清单
- 支持 Claude Code 插件安装及 Codex/Cursor/OpenCode 等 75+ agent

## 适用场景

- 为内网环境规划 LLM 平台的分层架构与 GPU 数量
- 生成需人工携入隔离网络的模型、镜像、软件包清单
- 在内网无互联网条件下校验并加载搬运的文件包

## 场景标签

 · 领域:LLM 基础设施/离线部署规划

## 证据(README 行号)

> L14: `airgap-anything` is a home for agent skills that design systems for networks without internet access. Its first sk
> L89: > Design an air-gapped LLM platform for my organization.
> L30: |`airgap-architect`|Interviews you and writes the blueprint, GPU sizing, the agent block and the transfer manifest 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `5ccce033e1c0` · [字段定义](../../DATASET.md)*
