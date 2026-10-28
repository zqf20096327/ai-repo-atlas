# ecnu-sea/SEA

⭐ 91 · Python · Apache-2.0 · 推送 2026-01-18 · [GitHub](https://github.com/ecnu-sea/SEA) · [官网](https://ecnu-sea.github.io/) · 组织维护

**面向科研作者的自动化论文评审框架（EMNLP 2024）**

ECNU 团队开发的自动化论文评审框架，含 Standardization、Evaluation、Analysis 三个模块，基于自身发布的 SEA 系列模型与数据集（HuggingFace 可下载），为论文生成审稿反馈，供作者改进工作。安装方式为 git clone 源码 + conda 环境 + pip 依赖，下载 SEA-E 模型后通过 run_webui.sh 启动 Web 界面。声明禁止商业使用，定位是供作者参考的评审意见而非录用决策依据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Standardization/Evaluation/Analysis 三模块架构
- 提供 SEA 系列模型与数据集（HuggingFace）
- Web UI 方式运行，可调节超参数

## 适用场景

- 投稿前获取论文的自动化审稿反馈
- 根据 AI 评审意见改进论文质量

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L18: SEA is a novel framework for automated paper reviewing based on three modules: Standardization, Evaluation, and Ana
> L58: It must be underscored that the primary objective of SEA is to provide informative reviews for authors to **furnish

## 星数曲线

```mermaid
xychart-beta
    title "ecnu-sea/SEA 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 90 --> 92
    line [91, 91]
```

2026-10-18 91 → 2026-10-28 91（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `02c84796ad38` · [字段定义](../../DATASET.md)*
