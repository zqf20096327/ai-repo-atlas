# saisrivathsa/StyleTransfer-PyTorch

⭐ 18 · Jupyter Notebook · MIT · 推送 2026-10-30 · [GitHub](https://github.com/saisrivathsa/StyleTransfer-PyTorch) · 个人维护

**PyTorch 实现的图像风格迁移笔记本，供使用者生成风格化图片**

以 Jupyter Notebook 形式提供的图像风格迁移实现：基于 PyTorch 与卷积神经网络，读取 content 与 style 两张图片，通过优化生成风格迁移后的输出图片到 output 文件夹。支持 CPU 与 GPU 运行（GPU 不可用时可手动将 device 设为 cpu），可调整 style_weights 与 content/style 权重比控制迁移效果。通过 pip install -r requirements.txt 安装依赖，附论文链接与示例输出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 PyTorch 的图像风格迁移 notebook 实现
- 支持 CPU 与 GPU 运行
- 可自定义 content/style 图片并调整各层权重

## 适用场景

- 把自己照片与艺术风格图合成风格化图片
- 学习风格迁移论文方法的代码实现
- 调整内容/风格权重观察迁移效果差异

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L2: Implementation of image style transfer in PyTorch.
> L10: This notebook works on both CPU and GPU.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d3ed9bfe0f3a` · [字段定义](../../DATASET.md)*
