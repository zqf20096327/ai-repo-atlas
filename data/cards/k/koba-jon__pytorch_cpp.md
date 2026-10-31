# koba-jon/pytorch_cpp

⭐ 313 · C++ · MIT · 推送 2026-01-22 · [GitHub](https://github.com/koba-jon/pytorch_cpp) · 个人维护

**用 C++/LibTorch 实现深度学习模型的开源示例代码集**

以 LibTorch（PyTorch C++ API）实现深度学习经典模型的可编译示例集合，覆盖分类（AlexNet/VGGNet/ResNet/ViT）、生成建模（VAE/GAN/流模型/扩散模型/DiT/流匹配）、图像翻译、超分、风格迁移、语义分割、目标检测（YOLO v1-v8）、异常检测（AnoGAN/PaDiM/PatchCore）、NeRF/3DGS 等，每项附论文出处。面向希望用 C++ 学习或复现深度学习模型的开发者；依赖 LibTorch、OpenCV、Boost、Gnuplot、libpng 等，需 CMake 自行编译，每个模型目录独立构建训练测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖分类/生成/分割/检测/异常检测/视图合成等十余类模型的 C++ 实现
- 每个模型附原始论文与会议出处
- 内置数据加载（transform/dataset/dataloader）与训练进度、损失图、输出图像监控工具
- 支持 CUDA 与 CPU 的 LibTorch 版本

## 适用场景

- 用 C++/LibTorch 学习经典深度学习模型的实现细节
- 复现论文模型并训练测试自己的数据集
- 作为 C++ 深度学习工程的代码参考（数据输入、进度监控等工具模块）

## 场景标签

`目标检测` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L4: LibTorch
> L501: ## 📦 Requirement (Library)

## 星数曲线

```mermaid
xychart-beta
    title "koba-jon/pytorch_cpp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 312 --> 314
    line [313, 313]
```

2026-10-18 313 → 2026-10-31 313（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `f98c4cf33f8f` · [字段定义](../../DATASET.md)*
