# Imalwayshere/Open-Detector

⭐ 249 · Python · MIT · 推送 2026-03-31 · [GitHub](https://github.com/Imalwayshere/Open-Detector) · [官网](https://www.xyzscience.com) · 个人维护 · 中文 README

**面向学术文本的 BERT AI 生成检测模型，供个人与本地部署**

基于 BERT-base-uncased 的二分类模型，判断学术论文文本更接近人类写作还是 AI 写作风格。作者声明在约 140 万样本上训练，报告准确率 99.57%、召回 99.94%、误报率 0.82%（数据来自 README 自述，未附评测细节）。模型文件托管于 Hugging Face，通过 pip 安装 transformers/torch 后用 Python 加载推理，标签 0=人类、1=AI，最大长度 512 tokens。README 声明当前仅为风格检测，未来目标是内容真实性与 AI 幻觉识别，另提供在线 Demo 与一个人改写模型。

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

- BERT 二分类：判定学术文本属人类/AI 写作风格
- 作者报告准确率 99.57%、召回 99.94%、误报率 0.82%（自述数据）
- 模型权重托管 Hugging Face，pip 安装依赖后本地推理
- 声明为 Turnitin 等商业检测服务的开源替代

## 适用场景

- 学生在提交前自查论文的 AI 风格分值
- 研究者本地部署做学术文本风格检测
- 作为商业查重/AI 检测服务的低成本替代方案

## 场景标签

 · 领域:NLP/AI 检测

## 证据(README 行号)

> L10: **Open Detector** is a BERT binary classification model for identifying whether academic papers are closer to **hum
> L71: from transformers import BertTokenizer, BertForSequenceClassification

## 星数曲线

```mermaid
xychart-beta
    title "Imalwayshere/Open-Detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 248 --> 250
    line [249, 249]
```

2026-10-18 249 → 2026-10-27 249（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a7aac457cf64` · [字段定义](../../DATASET.md)*
