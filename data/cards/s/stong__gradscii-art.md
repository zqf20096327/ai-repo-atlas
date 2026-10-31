# stong/gradscii-art

⭐ 269 · Python · AGPL-3.0 · 推送 2026-01-24 · [GitHub](https://github.com/stong/gradscii-art) · [官网](https://bad.apple.zellic.io) · 个人维护

**用梯度下降生成 ASCII 艺术图的工具，面向图像转字符画用户**

将图像转 ASCII 艺术的问题建模为可微分优化：以 softmax 在每个网格位置对全部字符做加权混合渲染，用 PyTorch/AdamW 最小化与目标图像的 MSE，配合温度退火、Gumbel-Softmax、多样性熵正则与多尺度损失，逐步收敛到离散字符选型。支持 Apple Silicon(MPS)/CUDA/CPU 运行，提供 Epson 小票打印(CP437)与 Discord 预设，支持动画的时间正则、可学习仿射对齐(warping)、动态对比度与 RGB→灰度 MLP 映射。以 Python 脚本(train.py)形式提供，需自备字体文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可微分渲染 + 梯度下降优化字符摆放，替代亮度查表方式
- 温度退火与 Gumbel-Softmax 实现从软混合到离散字符选择
- 支持动画（时间正则）、可学习 warp 对齐、动态对比度、RGB→灰度 MLP
- MPS/CUDA/CPU 运行，内置小票打印机(CP437)与 Discord 输出预设

## 适用场景

- 把图片转成适合小票打印机输出的 ASCII 艺术图
- 生成适配 Discord 文本块的字符画
- 制作带时间正则的 ASCII 动画（如 Bad Apple）

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: An approach to ASCII art generation that uses gradient descent optimization instead of lookup tables. This project p
> L113: ## Overview
> L124: 4. **Use gradient descent** (AdamW optimizer) to adjust which characters to place

## 星数曲线

```mermaid
xychart-beta
    title "stong/gradscii-art 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-18 269 → 2026-10-31 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `fbc42e1e9de8` · [字段定义](../../DATASET.md)*
