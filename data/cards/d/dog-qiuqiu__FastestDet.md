# dog-qiuqiu/FastestDet

⭐ 863 · Python · BSD-3-Clause · 推送 2026-05-12 · [GitHub](https://github.com/dog-qiuqiu/FastestDet) · 个人维护 · 中文 README

**超轻量 anchor-free 目标检测算法（仅 0.24M 参数）**

基于 PyTorch 实现的超轻量 anchor-free 目标检测算法，参数量 0.24M，采用单尺度检测头、跨网格多候选目标、动态正负样本分配。在 RK3568 ARM CPU（NCNN）上单核 70.62ms、多核 23.51ms；支持 NCNN/RKNN/ONNX Runtime/Android 等多平台部署，训练数据格式与 Darknet YOLO 相同。提供训练、评估、ONNX/TorchScript 导出脚本与 NCNN C++ 示例。面向需要在边缘 CPU 设备上做实时目标检测的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- anchor-free 设计，参数量仅 0.24M
- 单尺度检测头与动态正负样本分配
- 多平台基准：RK3568/骁龙 835/x86 CPU，支持 NCNN/RKNN NPU 部署
- 提供 ONNX/TorchScript 导出与 Darknet YOLO 同格式训练流程

## 适用场景

- 在 ARM 嵌入式设备上跑实时目标检测
- 用自有数据集训练轻量检测模型并导出部署
- 对比轻量级检测模型的精度与速度

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L2: # :zap:FastestDet:zap:
> L21: FastestDet|25.3%|13.0%|352X352|23.51ms|70.62ms|0.24M

## 星数曲线

```mermaid
xychart-beta
    title "dog-qiuqiu/FastestDet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 862 --> 864
    line [863, 863]
```

2026-10-18 863 → 2026-10-25 863（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `fe4e301b8362` · [字段定义](../../DATASET.md)*
