# bcmi/DreamCom-Image-Composition

⭐ 23 · Python · 推送 2026-08-20 · [GitHub](https://github.com/bcmi/DreamCom-Image-Composition) · 组织维护 · 中文 README

**论文官方代码：微调文本引导 inpainting 模型做图像合成**

DreamCom 论文的官方仓库，属于 token-to-object 类生成式图像合成方法：给定某主体 3~5 张参考图，微调 Stable Diffusion inpainting 模型，用特殊 token 关联该主体，随后可将主体插入任意背景图，生成光照、几何、语义上与背景兼容的合成图。代码基于 diffusers 库，提供 MureCom 数据集、训练与测试脚本（accelerate launch / test.py / train_and_test.sh），需自行下载 Stable Diffusion Inpainting 模型权重。面向图像合成方向的研究者。

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

- 基于 diffusers 的文本引导 inpainting 微调流程（特殊 token 关联主体）
- 提供 MureCom 数据集的下载与训练/测试脚本
- 提供基于 libcom 工具箱的在线 demo
- 附带图像合成论文/代码/评测指标的资源汇总

## 适用场景

- 复现 DreamCom 论文的图像合成（物体插入）实验
- 用少量参考图定制模型，将特定主体插入新背景
- 在 MureCom 数据集上训练并评测合成方法

## 场景标签

`图像生成` `微调` · 领域:内容生成

## 证据(README 行号)

> L9: > **DreamCom: Finetuning Text-guided Inpainting Model for Image Composition** [[arXiv]](https://arxiv.org/pdf/2309.1
> L23: Given a few (3~5) reference images for a subject, we aim to customize a generative model, which can insert this sub
> L25: Technically, we finetune a text-guided inpainting model based on the reference images of one subject, during which 

## 星数曲线

```mermaid
xychart-beta
    title "bcmi/DreamCom-Image-Composition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fef791171b81` · [字段定义](../../DATASET.md)*
