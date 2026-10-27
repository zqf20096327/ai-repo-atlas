# ibaiGorordo/Sapiens-Pytorch-Inference

⭐ 153 · Jupyter Notebook · MIT · 推送 2026-02-17 · [GitHub](https://github.com/ibaiGorordo/Sapiens-Pytorch-Inference) · [官网](https://pypi.org/project/sapiens-inferece/) · 个人维护

**Sapiens 人体基础模型 PyTorch 推理封装与示例代码**

对 Meta 的 Sapiens 人体基础模型（法线估计、深度估计、人体部位分割、姿态估计）提供 PyTorch 推理封装：SapiensPredictor 类支持多任务同时运行，模型从 HuggingFace 自动下载，提供图像、视频与摄像头实时示例脚本，以及 ONNX 导出脚本（README 注明 ONNX 推理速度慢）。限制：建议使用 1B 模型，输入尺寸固定 768x1024 效果最好；模型本体为 CC BY-NC 4.0 非商用许可。以 pip 包或源码方式安装。

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

- SapiensPredictor 类支持法线/深度/分割/姿态多任务同时推理
- 模型从 HuggingFace 自动下载
- 提供图像、视频、摄像头实时运行示例脚本
- 提供 ONNX 导出脚本（README 注明 ONNX 推理速度慢）

## 适用场景

- 对图像或视频运行人体深度/法线/分割推理
- 用摄像头实时运行 Sapiens 人体感知任务
- 将 Sapiens 模型导出为 ONNX 格式

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L2:  Minimal code and examples for inferencing Sapiens foundation human models in Pytorch
> L40: The `SapiensPredictor` class allows to run multiple tasks simultaneously. It has the following methods:

## 星数曲线

```mermaid
xychart-beta
    title "ibaiGorordo/Sapiens-Pytorch-Inference 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 152 --> 154
    line [153, 153]
```

2026-10-18 153 → 2026-10-27 153（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `680be56912f5` · [字段定义](../../DATASET.md)*
