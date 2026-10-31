# drivendataorg/zamba

⭐ 162 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/drivendataorg/zamba) · [官网](https://zamba.drivendata.org/docs/stable/) · 组织维护

**用机器学习自动识别相机陷阱影像中动物物种的 Python 工具**

面向生态保护与野生动物研究的 Python 包和命令行工具，用计算机视觉从相机陷阱的图像与视频中检测、分类动物：官方视频模型可识别空白视频及非洲 32 种、欧洲 11 种常见物种；图像模型覆盖全球 178 类（lila.science）或 2,000+ 类（speciesnet）。支持用自己的标注数据微调训练新模型、过滤空白影像，以及仅限视频的深度估计来推算动物与相机距离。另有网站应用 ZambaCloud，用户可在 Model Zoo Wiki 分享自训模型。安装需 Python>=3.11，视频工作流需 FFmpeg。

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

- 官方模型覆盖空白+32 非洲种+11 欧洲种（视频）、178 或 2000+ 类（图像）
- 用自己的标注图像/视频微调训练并预测新物种或新生态
- 仅限视频的深度估计，推算动物与相机的距离
- 以 CLI（zamba predict/train/depth）和 Python 包两种形式提供

## 适用场景

- 批量识别相机陷阱影像中出现的物种并过滤空白画面
- 用本地标注数据训练适应自己生境的物种分类模型
- 估计视频中动物与相机的距离

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L11: **`zamba` is a tool built in Python that uses machine learning and computer vision to automatically detect and clas
> L19: The official video models in `zamba` can identify blank videos (where no animal is present) along with 32 species c

## 星数曲线

```mermaid
xychart-beta
    title "drivendataorg/zamba 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 161 --> 163
    line [162, 162]
```

2026-10-18 162 → 2026-10-31 162（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `dfae6939711b` · [字段定义](../../DATASET.md)*
