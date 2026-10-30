# parham1998/Facial-Privacy-Protection

⭐ 16 · Python · 推送 2025-12-03 · [GitHub](https://github.com/parham1998/Facial-Privacy-Protection) · 个人维护

**CVPR 2025 论文官方实现：扩散模型生成对抗人脸图像防人脸识别**

论文《Enhancing Facial Privacy Protection via Weakening Diffusion Purification》的官方代码。基于扩散模型生成对抗性人脸图像，抵御未授权人脸识别系统：先学习无条件嵌入以增强对抗修改的学习容量，再引导对抗潜码修改以削弱扩散净化效应，并加入保身份结构保持原图与生成图的结构一致性。支持 impersonation 与 obfuscation 两种模式，在 CelebA-HQ 和 LADN 数据集上实验。使用需自行下载 AMT-GAN 的预训练人脸识别模型与数据集，conda 环境安装依赖后运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 学习无条件嵌入引导对抗潜码修改，削弱扩散净化效应
- 保身份结构保持原图与生成图像的结构一致性
- 支持 impersonation 与 obfuscation 两种保护模式
- 在 CelebA-HQ 与 LADN 数据集上实验

## 适用场景

- 生成对抗人脸图像防止被自动人脸识别系统识别
- 人脸隐私保护研究的方法复现与对比实验
- 研究扩散净化效应对对抗样本保护成功率的影响

## 场景标签

`图像生成` `网络安全` · 领域:内容生成

## 证据(README 行号)

> L1: # Enhancing Facial Privacy Protection via Weakening Diffusion Purification (CVPR 2025) [ArXiv]
> L9:  The rapid growth of social media has led to the widespread sharing of individual portrait images, which pose seriou

## 星数曲线

```mermaid
xychart-beta
    title "parham1998/Facial-Privacy-Protection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c9f7a681db3a` · [字段定义](../../DATASET.md)*
