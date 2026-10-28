# anishreddy3/Crack-Semantic-Segmentation

⭐ 64 · Python · MIT · 推送 2026-10-26 · [GitHub](https://github.com/anishreddy3/Crack-Semantic-Segmentation) · [官网](https://docs.google.com/document/d/1gJtviJ3ks5ddoKysCEBuZs0xUSVYecq-EYUO7ba8fp4/edit?usp=sharing) · 个人维护

**用 U-Net 做实时裂缝分割：训练、导出 ONNX、图像/视频推理**

基于 PyTorch、OpenCV 与 ONNX Runtime 的裂缝语义分割流水线：用 unet_train.py 训练 U-Net 并保存 .pt 权重，经 pytorch_to_onnx.py 导出 ONNX，随后对图像文件夹或视频执行分割推理。提供示例数据集与 Google Drive 预训练权重。README 声明这是 2019 年流水线的作品集快照，非积极维护产品；原 2019 环境为 Python 3.6 + CUDA 10，pin 仅作存档复现用途。

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

- U-Net 训练与 ONNX 导出流水线
- 支持文件夹批量图像与视频两种推理模式
- 提供示例数据集与预训练模型下载

## 适用场景

- 对路面或结构图像批量检测裂缝并生成分割结果
- 对视频流做实时裂缝分割
- 复现或改造 2019 年的裂缝分割训练流水线

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: Real-time crack segmentation with **PyTorch**, **OpenCV**, and **ONNX Runtime**.
> L5: Train a U-Net, export to ONNX, then run folder or video inference.

## 星数曲线

```mermaid
xychart-beta
    title "anishreddy3/Crack-Semantic-Segmentation 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-28"]
    y-axis "stars" 63 --> 65
    line [64, 64]
```

2026-10-26 64 → 2026-10-28 64（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `ebf34407145c` · [字段定义](../../DATASET.md)*
