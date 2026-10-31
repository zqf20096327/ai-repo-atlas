# CoderChen01/InterCLIP-MEP

⭐ 16 · Python · MIT · 推送 2025-11-13 · [GitHub](https://github.com/CoderChen01/InterCLIP-MEP) · [官网](https://dl.acm.org/doi/10.1145/3776561) · 组织维护

**多模态反讽检测论文官方实现：CLIP 交互编码+记忆增强预测**

ACM TOMM 论文 InterCLIP-MEP 的官方代码库：提出 Interactive CLIP 训练策略，将跨模态信息嵌入各编码器以获得融合表征， trainable 参数量约为现有方法的 1/20.6；另含 Memory-Enhanced Predictor，在推理阶段以双通道动态记忆缓存测试样本知识并作非参数分类器。在 MMSD/MMSD2.0/DocMSU 上复现实验，提供数据转换、OpenCLIP 权重转换与多组实验脚本。面向多模态情感与反讽检测方向的研究者，需 Python 3.9 + poetry 环境，自行准备并上传数据集后按 config 指定路径运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- InterCLIP 将跨模态信息嵌入各编码器，可训练参数约为已有方法的 1/20.6
- MEP 双通道动态记忆在推理期缓存测试样本知识，作非参数分类器
- 覆盖 MMSD/MMSD2.0/DocMSU 的主结果、消融、LoRA 与超参实验脚本
- 提供 MMSD2.0 转 Hugging Face datasets 格式的转换脚本

## 适用场景

- 复现论文中多模态反讽检测实验结果
- 在自建数据集上训练/评测反讽检测模型
- 研究 CLIP 高效微调与非参数记忆分类机制

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L16: Sarcasm in social media, frequently conveyed through the interplay of text and images, presents significant challen
> L1: # [ACM TOMM] InterCLIP-MEP: Interactive CLIP and Memory-Enhanced Predictor for Multi-modal Sarcasm Detection

## 星数曲线

```mermaid
xychart-beta
    title "CoderChen01/InterCLIP-MEP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1836ef9e3b6f` · [字段定义](../../DATASET.md)*
