# dfci/matchminer-ai-inference

⭐ 29 · Python · NOASSERTION · 推送 2026-10-27 · [GitHub](https://github.com/dfci/matchminer-ai-inference) · [官网](https://doi.org/10.48550/arXiv.2412.17228 ) · 组织维护

**癌症临床试验匹配的推断工作流 Python 包**

实现 Altreuter 等人 MatchMiner-AI 论文所述临床试验匹配推断流程的 Python 包：模块化提供试验与患者病史摘要生成、双方向嵌入、候选匹配检索、匹配质量评分及排除标准评估等核心步骤函数。面向需要批量执行试验匹配推断的研究与临床信息学开发者；推荐 GPU 环境，要求 Python 3.12+，在 Linux 环境测试，提供示例 notebook。包当前为 pre-v1 活跃开发状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖摘要、嵌入、候选检索、评分、排除标准评估的模块化函数
- 实现 MatchMiner-AI 开源癌症临床试验匹配方案
- 提供基于示例数据的 Quickstart notebook

## 适用场景

- 对癌症患者队列批量执行临床试验匹配推断
- 复现或扩展 MatchMiner-AI 论文的匹配工作流
- 研究场景下评估患者-试验匹配质量与排除标准

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: `matchminer-ai` is a Python package for running the clinical trial matching inference workflow described in Altreute
> L41: >Altreuter J, Trukhanov P, Paul MA, Hassett MJ, Riaz IB, Afzal MU, Mohammed AA, Sammons S, Lindsay J, Mallaber E, K

## 星数曲线

```mermaid
xychart-beta
    title "dfci/matchminer-ai-inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-28 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `8327cdec490e` · [字段定义](../../DATASET.md)*
