# N1nEmAn/sapper-v2

⭐ 90 · Python · MIT · 推送 2026-10-30 · [GitHub](https://github.com/N1nEmAn/sapper-v2) · 个人维护 · 中文 README

**AI 多智能体军团自主渗透测试框架，含分层事实图谱**

多智能体自动化渗透测试系统：一个 AI 指挥官读取战场板、决策并派发任务，将军与士兵 tmux 窗格中并行攻击，脚本 watchdog 负责保活、密钥轮换与收尾。知识沉淀为三层（标题/摘要/证据文档）事实-意图图谱。模型分级：指挥官/将军用 GLM-5.3，士兵/侦察用 DeepSeek V4.1 Flash。获腾讯智能攻防线上赛冠军（634 队、8 小时无人值守、1B tokens）。仅限授权安全测试，提供 install.sh CLI 与 Docker 两种部署。

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

- 指挥官/将军/侦察/士兵多角色分工的 tmux 运行时架构
- 三层（标题/摘要/证据）事实-意图图谱作为持久知识层
- 模型分级策略：精英模型决策、轻量模型量产
- 零策略 watchdog：崩溃重启、密钥轮换、超时收尾

## 适用场景

- 授权 CTF/攻防比赛中无人值守自动化渗透
- 长周期多目标安全评估任务的并行协作
- 研究多智能体分工与知识传承的涌现行为

## 场景标签

`多智能体` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L14: sapper is not a smarter single agent. It is a legion of AIs that divide labor,
> L86: - **Economy** — model tiering: commander and generals run GLM-5.3, soldiers


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a1c2686ca69e` · [字段定义](../../DATASET.md)*
