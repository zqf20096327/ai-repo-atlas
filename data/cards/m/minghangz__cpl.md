# minghangz/cpl

⭐ 65 · Python · 推送 2026-03-22 · [GitHub](https://github.com/minghangz/cpl) · 个人维护

**视频时序句子定位研究代码：弱监督高斯对比提议学习（CPL）**

CVPR 2022 / TPAMI 2025 论文的官方 PyTorch 实现，面向弱监督时序句子定位任务：给定句子在长视频中定位对应片段。方法用多个可学习高斯函数在同一视频内生成正负提议，配合由易到难的负提议挖掘策略；在 Charades-STA 与 ActivityNet Captions 上给出指标并提供可下载的已训练模型。训练与推理通过 python train.py 加配置文件运行，需自行准备 C3D/I3D 特征数据（HDF5 格式），依赖 pytorch/h5py/nltk/fairseq。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 弱监督设定：仅视频级标注即可定位句子对应片段
- 可学习高斯函数生成正负提议，由易到难负样本挖掘
- 提供 Charades-STA 与 ActivityNet Captions 的已训练模型与评测命令
- 同一代码库覆盖 CVPR 2022 与 TPAMI 2025 两篇论文

## 适用场景

- 复现论文结果或下载模型做时序句子定位评测
- 在自建数据集上训练弱监督视频定位模型
- 作为视频-语言定位研究的基线方法参考

## 场景标签

 · 领域:计算机视觉/视频-语言定位

## 证据(README 行号)

> L9: In this paper, we propose Contrastive ProposalLearning (CPL) for the weakly supervised temporal sentence grounding t
> L10: video that can characterize the multiple events in a long video. Then, we propose a controllable easy to hard negat

## 星数曲线

```mermaid
xychart-beta
    title "minghangz/cpl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 64 --> 66
    line [65, 65]
```

2026-10-18 65 → 2026-10-29 65（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ed5519ff9708` · [字段定义](../../DATASET.md)*
