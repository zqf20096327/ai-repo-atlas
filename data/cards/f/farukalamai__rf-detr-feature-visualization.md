# farukalamai/rf-detr-feature-visualization

⭐ 14 · Python · 推送 2026-07-10 · [GitHub](https://github.com/farukalamai/rf-detr-feature-visualization) · 个人维护

**可视化 RF-DETR 主干网络推理时特征图的脚本工具**

一个 Python 脚本工具：对 RF-DETR 目标检测模型运行单次前向传播，通过 hook 捕获主干网络（DINOv2 中间输出与 C2f 融合层）的特征图，经 PCA 降为 3 通道映射为 RGB 并保存，同时叠加检测框输出。支持 small/medium/base/large 四种模型规格与阈值、仅网格输出等参数。依赖 pip 安装 rfdetr 与 supervision。面向计算机视觉开发与研究者，用于检查主干网络各阶段特征。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- hook 捕获 DINOv2 中间输出与 C2f 融合层特征图
- PCA→RGB 自动降维渲染，无需手动选通道
- 检测框叠加在每个特征面板上
- 支持 small/medium/base/large 四种模型规格

## 适用场景

- 调试或分析 RF-DETR 主干网络各阶段的特征表示
- 为目标检测模型生成可解释性可视化图
- 对比不同模型规格下的特征图差异

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Visualize what RF-DETR's backbone sees during inference. Runs a single forward pass and saves the projector feature 
> L39: The script hooks into `backbone.0.projector.stages_sampling` (4 per-scale resampling layers) and `backbone.0.projec

## 星数曲线

```mermaid
xychart-beta
    title "farukalamai/rf-detr-feature-visualization 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b4b5fa955429` · [字段定义](../../DATASET.md)*
