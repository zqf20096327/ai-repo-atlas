# oliverguhr/fullstop-deep-punctuation-prediction

⭐ 90 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/oliverguhr/fullstop-deep-punctuation-prediction) · [官网](https://huggingface.co/oliverguhr/fullstop-punctuation-multilang-large) · 个人维护

**多语言文本标点预测模型：为英意法德等语言恢复标点**

面向 SEPP-NLG 共享任务的多语言深度标点预测模型：对自动生成或转录文本预测句尾（EOS）与标点符号，支持英语、德语、法语、意大利语（另有荷兰语、加泰罗尼亚语模型），跨语言迁移训练。以 Python 包 deepmultilingualpunctuation 提供，PunctuationModel 类可处理任意长度文本，支持恢复标点与逐词标签预测两种输出，可切换不同模型。系统需预装 cmake；复现实验需下载数据集。长文本处理耗时较长。

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

- EOS 预测平均 F1 0.94，标点预测平均 F1 0.78（英德法意）
- PunctuationModel 类处理任意长度文本，支持恢复标点与逐词标签输出
- 提供英意法德、含荷兰语、荷兰语、加泰罗尼亚语等多个可选模型
- 提供训练其他语言与复现实验的流程

## 适用场景

- 为 ASR 转录文本恢复标点与句子边界
- 对自动生成的无标点文本做句子切分
- 为荷兰语、加泰罗尼亚语等其他语言恢复标点

## 场景标签

 · 领域:NLP/文本处理

## 证据(README 行号)

> L4: The goal of this task consists in training NLP models that can predict the end of sentence (EOS) and punctuation mar
> L13: If you like to use the model on your own texts, you can use our python package.

## 星数曲线

```mermaid
xychart-beta
    title "oliverguhr/fullstop-deep-punctuation-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 89 --> 91
    line [90, 90]
```

2026-10-18 90 → 2026-10-26 90（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7425a7744e92` · [字段定义](../../DATASET.md)*
