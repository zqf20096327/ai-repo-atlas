# microsoft/MICO

⭐ 34 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/microsoft/MICO) · 组织维护

**微软举办的成员推理攻击竞赛，评估差分隐私训练的抵御效果**

Microsoft Membership Inference Competition（与 IEEE SaTML 2023 共同举办）的官方仓库：参赛者对主办方提供的白盒 ML 模型执行成员推理攻击，判定挑战点是否参与过训练。任务覆盖图像（CIFAR-10/4层CNN）、文本（SST-2/RoBERTa-Base）、表格（Purchase-100/3层全连接）三模态及 DP Distinguisher 任务，各含 ε=∞/高/低差分隐私三种场景。以 TPR@0.1FPR 评分，通过 CodaLab 提交，每任务冠军可获 2000 美元奖励。仓库提供 starting kit Jupyter 笔记本引导参赛。提交已于 2023 年 1 月关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 个任务、3 种模态、按差分隐私预算分 3 档难度场景
- 以 TPR@0.1FPR 为评分指标，dev 集实时排行榜、final 集定最终名次
- 每任务冠军 2000 美元、亚军 1000 美元奖励
- 提供 starting kit Jupyter 笔记本与 pip 安装流程

## 适用场景

- 研究差分隐私训练对白盒成员推理攻击的缓解效果
- 开发和评测成员推理攻击方法并与其他参赛者比较
- 使用 train 集与公开训练数据开发攻击策略

## 场景标签

`模型评测` `网络安全` · 领域:评测与运维

## 证据(README 行号)

> L25: In MICO, your goal is to perform white-box membership inference against a series of trained ML models that we provi
> L28: You can compete on any of four separate membership inference tasks against classification models for image, text, a

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/MICO 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `03f3fa98c935` · [字段定义](../../DATASET.md)*
