# THU-BPM/Omni-SafetyBench

⭐ 116 · Python · Apache-2.0 · 推送 2026-08-26 · [GitHub](https://github.com/THU-BPM/Omni-SafetyBench) · [官网](https://arxiv.org/abs/2508.07173) · 组织维护 · 中文 README

**全模态大模型安全评测基准：23,000+ 平行样本**

面向全模态大语言模型（OLLM，文本/图像/视频/音频输入）的安全评测基准：基于 972 条种子数据扩展为覆盖单模态、双模态、全模态三类范式的平行数据集，含 24 个子类别、总计超 23,000 个样本，图像/视频含扩散生成与排版式变体，音频为 TTS 变体。指标包含 C-ASR、C-RR、Safety-score 与跨模态安全一致性 CMSC-score。数据托管于 Hugging Face，提供 Qwen2.5-omni-7b 的使用示例与 evaluation.py 评测脚本。含危害性内容示例，供研究人员使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 972 条种子扩展为 24 个平行子类别、超 23,000 样本
- C-ASR/C-RR/Safety-score 与跨模态一致性 CMSC-score 指标
- 提供 Qwen2.5-omni-7b 的单/双/全模态评测示例

## 适用场景

- 评测全模态大模型跨模态的输出安全性
- 检测模型对模态转换攻击的脆弱性
- 比较不同 OLLM 的安全对齐一致性

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L9: > Omni-SafetyBench is the first comprehensive **parallel benchmark** specifically designed for evaluating the safety
> L11: Omni-SafetyBench is built upon 972 seed entries from MM-SafetyBench, Video-SafetyBench, SALAD-Bench ,FigStep and Au
> L57: - **Conditional Attack Success Rate (C-ASR)**: Percentage of understood harmful samples where the model produces un

## 星数曲线

```mermaid
xychart-beta
    title "THU-BPM/Omni-SafetyBench 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 115 --> 117
    line [116, 116]
```

2026-10-18 116 → 2026-10-23 116（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `751a72ba39ef` · [字段定义](../../DATASET.md)*
