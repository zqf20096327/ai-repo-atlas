# cswry/SeeSR

⭐ 658 · Python · Apache-2.0 · 推送 2026-04-09 · [GitHub](https://github.com/cswry/SeeSR) · 组织维护

**给研究者/开发者：真实世界图像语义感知超分辨率模型**

CVPR2024 论文 SeeSR 的官方实现：基于 Stable Diffusion 2-base 的真实世界图像超分辨率模型，通过 DAPE（微调的 RAM）从退化图像提取语义标签作为提示，生成语义感知的高分辨率图像。提供推理脚本、sd-turbo 两步加速模式、Gradio 网页演示与 Replicate 在线试用；同时提供 DAPE 与 SeeSR 的完整训练流程（COCO、LSDIR+FFHQ10k 数据集）。附带 RealLR200 真实低分辨率测试集。Apache 2.0 许可发布代码与权重。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 SD2-base 与 DAPE 语义标签提示的真实世界超分辨率
- 支持 sd-turbo 两步推理模式
- 提供 Gradio 本地演示与 Replicate 在线试用
- 提供 DAPE/SeeSR 完整训练流程与 RealLR200 测试集

## 适用场景

- 修复真实场景拍摄的低分辨率照片
- 作为论文基线复现或对比真实世界超分方法
- 在自己的数据集上训练语义感知超分模型

## 场景标签

`图像视频处理` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: ## SeeSR: Towards Semantics-Aware Real-World Image Super-Resolution (CVPR2024)
> L152: This project is based on diffusers and BasicSR. Some codes are brought from PASD and RAM. Thanks for their awesome

## 星数曲线

```mermaid
xychart-beta
    title "cswry/SeeSR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 657 --> 659
    line [658, 658]
```

2026-10-18 658 → 2026-10-30 658（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a451abb06523` · [字段定义](../../DATASET.md)*
