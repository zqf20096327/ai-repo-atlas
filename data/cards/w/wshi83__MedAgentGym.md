# wshi83/MedAgentGym

⭐ 134 · Python · 推送 2026-04-12 · [GitHub](https://github.com/wshi83/MedAgentGym) · [官网](https://wshi83.github.io/MedAgentGym-Page/) · 组织维护

**训练 LLM Agent 代码式医学推理的公开环境与数据集**

ICLR 论文官方仓库，提供首个公开的 LLM agent 训练环境 MedAgentGYM：包含基于 12 个数据集（如 EHR 相关）构建的训练/测试任务，通过 Docker 隔离的代码执行环境运行 agent 实验，支持 SFT、DPO 等后训练方法的实验。预处理的 EHR 数据需签署 PhysioNet DUA 并获批准后凭脚本下载，当前版本不含 MIMIC-III、eICU、TREQS 与 EHRSHOT 数据。面向从事 LLM agent 训练研究的人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- train_tasks.jsonl / test_tasks.jsonl 提供任务定义与 ground truth 答案
- 基于 12 个数据集，预处理数据需签署 PhysioNet DUA 后凭脚本下载
- Docker 容器提供隔离的编码与执行环境
- 实验覆盖 SFT、SFT+DPO、推理/训练时间扩展等训练方法

## 适用场景

- 对 LLM agent 做代码式医学推理的训练与评测
- 复现论文中的 SFT/DPO 后训练实验
- 研究推理时间与训练时间的扩展规律

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L9: This is the official repository for the paper: "MedAgentGym: Training LLM Agents for Code-Based Medical Reasoning at
> L31: Since our dataset relies on a Docker environment for isolated coding and execution, you may first build the Docker 

## 星数曲线

```mermaid
xychart-beta
    title "wshi83/MedAgentGym 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 133 --> 135
    line [134, 134]
```

2026-10-18 134 → 2026-10-24 134（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `8bad29e43e94` · [字段定义](../../DATASET.md)*
