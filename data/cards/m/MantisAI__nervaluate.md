# MantisAI/nervaluate

⭐ 225 · Python · MIT · 推送 2026-03-12 · [GitHub](https://github.com/MantisAI/nervaluate) · 组织维护

**NER 模型的全实体级评测库：多场景精确率/召回率/F1**

基于 SemEval 2013 Task 9.1 定义的命名实体识别（NER）评测 Python 模块。它不采用逐 token 评测，而是按完整实体在五种错误类型（Correct/Incorrect/Partial/Missing/Spurious）与四种评测模式（strict/exact/partial/type）下计算精确率、召回率与 F1，输出 summary_report。输入支持嵌套标签列表、CoNLL 制表符分隔字符串与 prodi.gy span 列表三种格式，可通过继承 DataLoader 基类扩展新格式。代码扩展自 David Batista 的原始仓库与配套博文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实体级五种错误类型 × 四种评测模式（strict/exact/partial/type）
- 按实体类型与场景输出 summary_report
- 支持嵌套标签列表、CoNLL、prodi.gy 三种输入格式，可自定义 loader 扩展

## 适用场景

- 评测 NER 系统输出时区分边界错误与类型错误
- 按 strict/exact/partial/type 多口径汇报 NER 指标
- 直接读取 CoNLL 或 prodi.gy 标注格式做评测

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L15: `nervaluate` is a module for evaluating Named Entity Recognition (NER) models as defined in the SemEval 2013 - 9.1 
> L176: Then precision, recall and f1-score are calculated for each different evaluation schema. In order to achieve data,

## 星数曲线

```mermaid
xychart-beta
    title "MantisAI/nervaluate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 224 --> 226
    line [225, 225]
```

2026-10-18 225 → 2026-10-27 225（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `28da2453c6ad` · [字段定义](../../DATASET.md)*
