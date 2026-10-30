# iLearn-Lab/MM23-RTQ

⭐ 15 · Python · BSD-3-Clause · 推送 2026-04-07 · [GitHub](https://github.com/iLearn-Lab/MM23-RTQ) · 组织维护

**视频-语言理解研究代码：基于图文模型的检索/描述/问答框架**

ACM Multimedia 2023 论文 RTQ 的官方代码：提出 Refine、Temporal model、Query 三阶段框架，基于图文模型（BLIP 权重）联合建模信息冗余、时序依赖与场景复杂性，在文本-视频检索、视频描述、视频问答任务上训练与评估，无需视频-语言预训练。要求 Python>=3.8、PyTorch>=1.10、CUDA>=10.2，数据集与预训练模型需按 tools/data 指引自行下载。面向复现实验的多模态研究人员。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Refine-Temporal-Query 三阶段视频-语言建模框架
- 无需视频-语言预训练即可执行检索/描述/问答任务
- 提供数据集与 BLIP 预训练权重下载脚本

## 适用场景

- 复现 ACM MM 2023 论文的视频问答/检索实验
- 在自建视频-语言数据集上训练与评估模型
- 研究图文模型迁移到视频任务的方法

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L14: With a simple yet insightful framework **RTQ** (Refine, Temporal model, and Query), our model demonstrates outstand
> L21: 3. We demonstrate that, even without pre-training on video-languag data, our method can achieve superior (or compar
> L29: #### Video question answering

## 星数曲线

```mermaid
xychart-beta
    title "iLearn-Lab/MM23-RTQ 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8c6d1876d515` · [字段定义](../../DATASET.md)*
