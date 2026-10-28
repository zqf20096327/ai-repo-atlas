# yvsgrndjn/RXNMapper_v2

⭐ 21 · Python · MIT · 推送 2026-08-20 · [GitHub](https://github.com/yvsgrndjn/RXNMapper_v2) · 个人维护

**化学反应原子映射工具：从反应 SMILES 生成原子映射并可自训模型**

RXNMapper v2 基于 ALBERT 模型，通过掩码语言建模从无监督的反应 SMILES 中学习原子对应关系，输出带置信度分数的映射反应。提供两个打包模型（默认 alberta-uspto-2800k 与 original）离线使用，支持批量映射（BatchedMapper 对无效输入不抛错）与数据集批处理脚本。另含从零训练完整管线：构建词表、按 token 长度预处理、MLM 预训练、在自有验证集上选择最优 head/layer/checkpoint，并用图同构方法（atommap-eval）评估映射质量。面向化学信息学与反应数据处理的科研用户，Python ≥3.8，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ALBERT 无监督学习反应 SMILES 的原子映射，输出映射反应与置信度
- 完整训练管线：建词表→预处理→MLM 预训练→head/layer/checkpoint 选择
- 基于反应图同构的映射质量评估（atommap-eval）
- 两个模型随包发布可离线运行，另在 Hugging Face Hub 开放 150 个 checkpoint

## 适用场景

- 为化学反应数据集批量生成原子映射标注
- 当默认词表或化学空间不匹配时，用自有数据训练映射模型
- 在验证集上对比并挑选最优模型/head/layer/checkpoint

## 场景标签

`科研工具` `模型训练` · 领域:学习与行业

## 证据(README 行号)

> L5: RXNMapper v2 builds on the original RXNMapper (Schwaller *et al.*, *Science Advances* 2021), which showed that atom 
> L39: `RXNMapper` loads a packaged default model and maps a list of reaction SMILES:

## 星数曲线

```mermaid
xychart-beta
    title "yvsgrndjn/RXNMapper_v2 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-28 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `cbeed7a946f5` · [字段定义](../../DATASET.md)*
