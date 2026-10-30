# zrr1999/emotion-recognition

⭐ 32 · Python · MIT · 推送 2026-03-24 · [GitHub](https://github.com/zrr1999/emotion-recognition) · 个人维护 · 中文 README

**科研用多模态情绪识别训练套件：文本/音频/视频情绪分类**

面向研究者的多模态情绪识别实验套件：支持文本(T)、音频(A)、视频(V)三模态单独与组合训练，覆盖 MELD、IEMOCAP、SIMS 数据集，提供从预处理到训练、评估的工具链。技术机制包括 SafeTensors 特征缓存、混合精度训练、多模态知识蒸馏合并、TOML 配置化模块设计（Pydantic 校验）与软连接检查点存储。文本编码器用 BERT/RoBERTa/ModernBERT，音频用 Whisper/Distil-Whisper，融合支持拼接/Deep/MoE/注意力。需 Python 3.12+ 与 PyTorch 2.4.1，通过 git clone 与 uv 安装，多模态实验结果待补充。

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

- T/A/V 三模态单独与组合的情绪分类训练
- SafeTensors 特征缓存与软连接检查点存储优化
- 支持全参数微调、LoRA、冻结骨干三种训练方式
- TOML 模块化配置 + nanoflow 实验运行

## 适用场景

- 在 MELD/IEMOCAP/SIMS 上做多模态情绪识别实验
- 复现或扩展 APCL/SPCL 等对比学习方法
- 研究不同模态组合与融合策略对情绪分类的影响

## 场景标签

`科研工具` `多模态` · 领域:学习与行业

## 证据(README 行号)

> L4: > 基于深度学习的多模态情绪识别方法研究套件，支持文本、音频、视频三种模态的情绪分类与情感分析任务。
> L14: - 🎯 **多模态融合**：支持文本(T)、音频(A)、视频(V)三种模态的单独和组合使用

## 星数曲线

```mermaid
xychart-beta
    title "zrr1999/emotion-recognition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7b1f0863c702` · [字段定义](../../DATASET.md)*
