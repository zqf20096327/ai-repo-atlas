# david-thrower/cerebros-core-algorithm-alpha

⭐ 28 · Jupyter Notebook · NOASSERTION · 推送 2026-07-20 · [GitHub](https://github.com/david-thrower/cerebros-core-algorithm-alpha) · 个人维护

**生物启发的神经网络架构搜索（NAS/AutoML）框架**

Cerebros 是一个开源的神经架构搜索/AutoML 包，以多维 Dense 层格点与纵向/侧向随机连接模拟生物神经元连接方式，由搜索算法决定层数、单元数、每层神经元数与连接拓扑。提供 Keras/TensorFlow 实现，含 Ames 房价回归示例与从零训练生成式 LLM（NotGPT）的两阶段脚本（先小数据搜索架构，再全量训练），采用 iRoPE 与前馈块使训练时间随序列长度线性增长。社区版免费使用（含伦理条款），另有托管于 GCP 的商业版 Cerebros Enterprise。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多维 Dense 层格点 + 纵向/侧向随机连接的架构搜索
- 两阶段 LLM 训练脚本：小数据 NAS 后全量训练，从零训练生成式模型
- iRoPE 与 NAS 前馈块使训练时间随序列长度呈 O(n) 增长
- 提供 Kubeflow/Katib 清单与 Kale Jupyter notebook 复现流程

## 适用场景

- 自动搜索适配我任务的神经网络架构
- 从零训练一个小型生成式 LLM 并观察文本生成样例
- 在 Kubeflow/Katib 上复现穷举式架构搜索

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L5: The Cerebros package is an ultra-precise Neural Architecture Search (NAS) / AutoML that is intended to much more clo
> L107: Stage I-a (Neural Architecture Search): Cerebros rapidly searches for an optimal, biologically-inspired neural net

## 星数曲线

```mermaid
xychart-beta
    title "david-thrower/cerebros-core-algorithm-alpha 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-29 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `932dcfa56c78` · [字段定义](../../DATASET.md)*
