# NVIDIA/Deep-Learning-Accelerator-SW

⭐ 239 · Python · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/NVIDIA/Deep-Learning-Accelerator-SW) · 组织维护

**面向嵌入式开发者的 NVIDIA DLA 推理软件工具与基准参考库**

NVIDIA 官方仓库，提供在 Orin/Xavier SoC 的 DLA 硬件加速核心上运行深度学习推理工作负载的软件组成说明、模型准备脚本与基准数据：涵盖 DLA 编译器与运行时栈（经 TensorRT、NvMedia-DLA、cuDLA 调用）、常见网络（ResNet、RetinaNet、SSD）的 INT8 精度与吞吐/能效基准、2:4 结构化稀疏加速方法及支持的 ONNX 算子清单。给嵌入式 AI 开发者做 DLA 部署选型与复现参考，Python 依赖仅支持 x86 主机安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DLA 编译器将网络图编译为 DLA 可加载二进制，可经 TensorRT/NvMedia-DLA/cuDLA 调用
- 提供 ResNet/RetinaNet/SSD 等网络的 INT8 精度与各功耗档吞吐基准数据
- 2:4 结构化稀疏实测可带来 1.24x-1.47x 的 dense→sparse 加速
- 列出 DLA 已支持与计划支持的 ONNX 算子

## 适用场景

- 在 Jetson Orin/DRIVE 平台上评估 DLA 与 GPU 的推理分工
- 复现 MLPerf 类网络的 DLA INT8 精度与吞吐基准
- 为低功耗部署选择 DLA 稀疏化加速方案

## 场景标签

`推理引擎` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L1: # Deep Learning Accelerator
> L5: DLA software consists of the DLA compiler and the DLA runtime stack. The offline compiler translates the neural netw
> L127: Install the Python dependencies with (only supported on x86 hosts):

## 星数曲线

```mermaid
xychart-beta
    title "NVIDIA/Deep-Learning-Accelerator-SW 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 238 --> 240
    line [239, 239]
```

2026-10-18 239 → 2026-10-24 239（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `2250c5a51b22` · [字段定义](../../DATASET.md)*
