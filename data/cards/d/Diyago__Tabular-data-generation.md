# Diyago/Tabular-data-generation

⭐ 570 · Python · Apache-2.0 · 推送 2026-03-29 · [GitHub](https://github.com/Diyago/Tabular-data-generation) · [官网](https://towardsdatascience.com/review-of-gans-for-tabular-data-a30a2199342) · 个人维护

**给数据科学家的表格数据合成库：GAN/扩散/LLM 生成与过滤**

Python 库 tabgan，提供统一接口用多种生成方法合成表格数据：CTGAN（GANGenerator）、基于树的扩散（ForestDiffusionGenerator）、GReaT LLM 框架（LLMGenerator）、Gaussian Copula 与随机采样基线。共享生成→后处理→LightGBM 对抗过滤管线，支持混合数据类型、条件文本生成（可接 LM Studio/OpenAI/Ollama 等 OpenAI 兼容端点）、约束引擎、质量 HTML 报告、隐私指标（DCR/NNDR/MI）、AutoSynst 自动选优、HuggingFace 数据集合成与 sklearn Pipeline 集成，另有 CLI。基于论文 arXiv:2010.00638，Apache 2.0。

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

- 五种生成器统一 API（CTGAN/扩散/LLM/Copula/基线）
- LightGBM 对抗过滤保持分布一致性
- 约束引擎（范围/唯一/公式/正则）与隐私指标 DCR/NNDR/MI
- AutoSynth 运行全部生成器并按质量与隐私评分选优
- 质量 HTML 报告含 PSI、相关性热图与 TSTR/TRTR

## 适用场景

- 为表格数据集生成扩充训练数据
- 合成带业务规则约束的测试数据
- 发布前评估合成数据的隐私再识别风险
- 不确定选哪种生成器时自动对比选优

## 场景标签

 · 领域:机器学习/数据合成

## 证据(README 行号)

> L18: TabGAN provides a unified Python interface for generating synthetic tabular data using multiple state-of-the-art ge
> L22: |**GANs**|Conditional Tabular GAN (CTGAN)|Mixed data types, complex multivariate distributions|

## 星数曲线

```mermaid
xychart-beta
    title "Diyago/Tabular-data-generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 569 --> 571
    line [570, 570]
```

2026-10-18 570 → 2026-10-29 570（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `82b901ee60e4` · [字段定义](../../DATASET.md)*
