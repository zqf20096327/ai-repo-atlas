# Croups/is-it-ai

⭐ 18 · Python · MIT · 推送 2026-03-24 · [GitHub](https://github.com/Croups/is-it-ai) · 个人维护

**可自托管的 AI 文本检测器，自带模型校准，本地或 Modal GPU 运行**

基于 Fast-DetectGPT 算法的自托管 AI 文本检测工具：文本按句子边界分块，用 HuggingFace 因果语言模型的 log 概率差异打分，经贝叶斯高斯分类聚合为整体 AI 概率。用户需在自有领域数据上校准（默认校准值为占位符，未校准结果不可靠），校准与模型、领域绑定，换模型或换领域需重新校准。支持本地 uv/PyTorch 运行，或部署到 Modal GPU（T4/L4/A10G/A100/H100）并以 HTTP 端点调用。提供 Python 库、CLI 与示例数据集。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 句子对齐分块 + log 概率差异打分 + 高斯贝叶斯分类输出 AI 概率
- 接入任意 HuggingFace 因果 LM，数据不离开用户基础设施
- 领域数据校准流程（prepare→calibrate→detect），输出 AUROC 评估
- 支持本地运行或 Modal GPU 部署为 HTTP 端点

## 适用场景

- 在自有数据上校准后检测目标领域的 AI 生成文本
- 将 AI 文本检测作为自托管服务部署，数据不出基础设施
- 检测部分 AI 撰写的文本（小分块对局部编辑更敏感）

## 场景标签

 · 领域:NLP/AI 检测

## 证据(README 行号)

> L3: A self-hostable, **bring-your-own-calibration** AI text detector based on the Fast-DetectGPT algorithm. Unlike hoste
> L5: It splits text into sentence-aligned chunks, scores each chunk using a language model's log-probability discrepancy,

## 星数曲线

```mermaid
xychart-beta
    title "Croups/is-it-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `f75219478a17` · [字段定义](../../DATASET.md)*
