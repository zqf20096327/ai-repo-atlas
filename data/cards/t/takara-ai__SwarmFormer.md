# takara-ai/SwarmFormer

⭐ 16 · Python · 推送 2026-02-28 · [GitHub](https://github.com/takara-ai/SwarmFormer) · [官网](https://takara.ai/thinking/insights/swarmformer/) · 组织维护

**SwarmFormer：结合群体智能与全局注意力的文本分类 PyTorch 实现**

PyTorch 实现的 SwarmFormer 架构，用于英文文本分类（情感分析）：通过 token 分层聚类与局部更新步骤结合全局注意力，配 GELU 动态门控与 0.3-0.4 dropout。提供 Base 与 Small 两个预训练配置（Base 在 IMDb 上准确率 89.03%），含推理脚本、HuggingFace 保存/加载集成，自动选择 CUDA/MPS/CPU 硬件。限制：仅英文文本分类，不适用于文本生成、机器翻译，序列长度上限 256/768。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 局部群体智能 + 全局注意力的层级架构（token 分层聚类、局部更新步骤）
- 两个预训练配置：SwarmFormer-Base（IMDb 准确率 89.03%）与 Small
- 自动硬件选择：CUDA / Apple Silicon MPS / CPU
- HuggingFace 生态集成（save_pretrained / 自动下载预训练模型）

## 适用场景

- 在 IMDb 等英文数据集上运行文本分类推理
- 以代码方式加载预训练 SwarmFormer 模型做情感分析
- 研究局部-全局注意力混合架构的实现

## 场景标签

 · 领域:NLP/深度学习模型

## 证据(README 行号)

> L3: A novel transformer architecture for sentiment analysis that combines local swarm intelligence with global attention
> L36: The package includes a demo script that runs inference on the IMDb dataset:

## 星数曲线

```mermaid
xychart-beta
    title "takara-ai/SwarmFormer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8da0e9ba9aa2` · [字段定义](../../DATASET.md)*
