# zou-group/sirius

⭐ 113 · Python · MIT · 推送 2025-12-01 · [GitHub](https://github.com/zou-group/sirius) · [官网](https://arxiv.org/pdf/2502.04780) · 组织维护

**自提升多智能体框架：从轨迹经验库引导推理增强**

NeurIPS 2025 论文 SiriuS 的官方代码库。核心机制是维护成功轨迹构成的经验库，并对失败轨迹生成反馈后再生成为改进轨迹，再在此基础上微调智能体以持续增强多智能体系统的推理能力。支持三种多智能体设定：协作问答（大学物理/化学、PubMedQA 式）、Actor–Judgment–Critic 迭代精炼、以及双人对弈竞争博弈。示例微调路径使用 OpenAI SFT API，也可接入其他微调框架。安装方式为 git clone 源码 + conda 环境。

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

- 维护成功轨迹经验库并从失败轨迹引导再生（bootstrapping）
- 三种多智能体设定：协作问答 / Actor-Critic / 竞争博弈
- 轨迹驱动的智能体微调数据构建管线（示例用 OpenAI SFT API，可替换其他框架）
- 附带物理问题训练数据样例 dataset/phy_train.jsonl

## 适用场景

- 用多智能体自产轨迹数据微调提升 LLM 推理能力
- 在大学物理/化学、生物医学问答任务上构建自提升系统
- 复现论文中的多智能体实验设定

## 场景标签

`多智能体` `微调` · 领域:Agent 开发

## 证据(README 行号)

> L8: SIRIUS is a self-improving multi-agent framework that continuously enhances reasoning ability by maintaining an expe
> L124: We use the OpenAI Supervised Fine-Tuning (SFT) API in our example, but you can plug in any fine-tuning framework o

## 星数曲线

```mermaid
xychart-beta
    title "zou-group/sirius 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 112 --> 114
    line [113, 113]
```

2026-10-18 113 → 2026-10-25 113（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `053278c8cb23` · [字段定义](../../DATASET.md)*
