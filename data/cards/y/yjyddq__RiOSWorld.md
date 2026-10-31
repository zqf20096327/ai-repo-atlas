# yjyddq/RiOSWorld

⭐ 125 · HTML · 推送 2025-12-02 · [GitHub](https://github.com/yjyddq/RiOSWorld) · [官网](https://yjyddq.github.io/RiOSWorld.github.io/) · 组织维护

**评测多模态计算机使用 agent 风险的基准（NeurIPS'25）**

NeurIPS 2025 论文的官方代码仓库：提供评测多模态 computer-use agent 风险的基准环境。基于虚拟机 Provider（VMware 默认，支持 Docker、AWS、VirtualBox 等）运行 Ubuntu 桌面任务，内置 reCAPTCHA、钓鱼网站、账号/密码欺诈、钓鱼邮件等环境风险场景的搭建流程；提供 multi_llm_run.sh 运行实验、multi_evaluation.sh 用 LLM-as-a-judge 评估 agent 意图，并在 HuggingFace 发布评测轨迹数据。部分代码来自 OSWorld 与 PopupAttack。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于虚拟机（VMware/Docker/AWS 等 Provider）的桌面环境风险评测
- 内置 reCAPTCHA、钓鱼网站、账号欺诈、钓鱼邮件等风险场景搭建
- 提供 LLM-as-a-judge 自动化评估流水线
- HuggingFace 发布评测轨迹数据供后续研究

## 适用场景

- 评测我的 computer-use agent 在风险场景下的行为
- 研究 CUA 安全性并复用轨迹数据
- 搭建可控的钓鱼/欺诈风险测试环境

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L3:  [NeurIPS'25] RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents
> L169: For evaluation, especially for assessing the intentions of Agents using LLM-judges, an automated pipeline is also 

## 星数曲线

```mermaid
xychart-beta
    title "yjyddq/RiOSWorld 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 124 --> 126
    line [125, 125]
```

2026-10-18 125 → 2026-10-31 125（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `0a46389e13d6` · [字段定义](../../DATASET.md)*
