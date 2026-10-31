# ismailuddin/gradcam-tensorflow-2

⭐ 48 · Python · 推送 2026-02-21 · [GitHub](https://github.com/ismailuddin/gradcam-tensorflow-2) · [官网](https://ismailuddin.github.io/gradcam-tensorflow-2/) · 个人维护

**TensorFlow 2.X 的 Grad-CAM 实现：生成热力图解释模型**

基于 TensorFlow 2.X 实现 Grad-CAM 论文中的方法，包括基础 Grad-CAM、反事实 Grad-CAM 与带高显著性图的引导 Grad-CAM 三种用法，以三个 Marimo notebook 形式提供，可用 uv run marimo edit 查看。运行依赖 uv。适合需要在图像分类模型上做梯度定位可视化与可解释性分析的开发者和研究者。README 附论文及参考实现链接。

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

- Grad-CAM / 反事实 Grad-CAM / 引导 Grad-CAM 三种 notebook 实现
- 基于 TensorFlow 2.X，遵循原始论文方法
- 通过 uv 与 Marimo notebook 运行

## 适用场景

- 对 CNN 分类结果生成类激活热力图
- 做反事实解释与引导显著性分析
- 可解释性（XAI）研究或教学示例

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: > A TensorFlow 2.X implementation of the various uses of Grad-CAM the original paper, including counterfactual examp
> L10: - GradCam

## 星数曲线

```mermaid
xychart-beta
    title "ismailuddin/gradcam-tensorflow-2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5c739b16b76d` · [字段定义](../../DATASET.md)*
