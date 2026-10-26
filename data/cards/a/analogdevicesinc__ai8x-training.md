# analogdevicesinc/ai8x-training

⭐ 115 · Jupyter Notebook · Apache-2.0 · 推送 2026-08-24 · [GitHub](https://github.com/analogdevicesinc/ai8x-training) · 组织维护

**为 MAX78000/MAX78002 边缘 AI 芯片训练模型的 PyTorch 工具链**

Analog Devices 维护的深度学习模型训练仓库，面向 MAX78000/MAX78002 超低功耗 AI 加速器的开发者：基于 PyTorch 2.3 / Python 3.11 开发和训练模型，配合 ai8x-synthesis 仓库用 izer 工具把训练好的模型转换为 C 代码以部署到芯片。官方完整支持平台为 Ubuntu 20.04/22.04 amd64（可选 NVIDIA CUDA 加速），macOS 用 MPS 加速，Windows 经 WSL2；TensorFlow/Keras 支持已弃用。安装需系统级包（libsndfile、sox、portaudio 等）与 pyenv 管理 Python 3.11。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 MAX78000/MAX78002 边缘 AI 芯片的模型开发与训练流程
- 与 ai8x-synthesis 配合，将训练模型经 izer 转为 C 代码
- 支持 CUDA / ROCm / Apple Silicon MPS 硬件加速与多 GPU 自动分配
- 官方支持 Ubuntu 20.04/22.04 + PyTorch 2.3 + Python 3.11 平台

## 适用场景

- 为 MAX78000/MAX78002 评估板训练并部署神经网络模型
- 在 CUDA 服务器上训练模型后转 C 代码用于边缘设备
- 在 WSL2 或 macOS 环境下搭建训练环境

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L13: 3. The training repository, which is used for deep learning *model development and training*:
> L15: 4. The synthesis repository, which is used to *convert a trained model into C code* using the “izer” tool:

## 星数曲线

```mermaid
xychart-beta
    title "analogdevicesinc/ai8x-training 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-26 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `ec8eafe894ec` · [字段定义](../../DATASET.md)*
