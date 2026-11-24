# maxesisnclaw/ThinTNPU

⭐ 3 · C++ · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/maxesisnclaw/ThinTNPU) · 个人维护

**昇腾310P上运行YOLO推理的轻量PyTorch后端**

在 Ascend 310P 上直接以 PyTorch PrivateUse1 后端实现 YOLO 系列（v5/v8/11/26）的 Detect/Segment/Classify 推理，不依赖 torch_npu，通过 ACL 调用与预编译 Ascend C 内核进行 FP16 图捕获与回放。以 Docker 容器内源码编译方式构建，需自行准备 CANN SDK、模型定义与权重。README 声明其为仅推理、窄范围的实现，不支持训练、batch>1、YOLO11n 等，规划系数针对特定 310P3 环境标定，更换硬件需重新校准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 直接在 ACL runtime 与预编译 Ascend C 内核上实现 PrivateUse1 后端，不导入 torch_npu
- 覆盖 YOLOv5/v8/11/26 三类任务（Detect/Segment/Classify），无捆绑权重或加载器
- 容量驱动的算子规划，无固定形状查找表；设备端 BGR/JPEG 前端融合预处理
- Segment/Classify 返回 CPU 端 Ultralytics Results 对象

## 适用场景

- 在昇腾 310P NPU 上部署 YOLO 目标检测推理
- 在 310P 上运行 YOLOv8 分割与分类任务
- 对比 torch_npu 原生图捕获路径的延迟测量实验

## 场景标签

`目标检测` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L7: ThinTNPU implements PyTorch `PrivateUse1` directly on ACL runtime calls and precompiled Ascend C kernels. Its infere
> L9: `WholeBlocked` provides architecture adapters for classic **YOLOv5**, **YOLOv8**, **YOLO11**, and **YOLO26** across 
> L102: Tested toolchain: aarch64 Linux, CANN 9.0.0 / AscendC, PyTorch 2.8.0+cpu, Python 3.11.15, and Ascend 310P (`dav-20


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `0af1f8adb9a7` · [字段定义](../../DATASET.md)*
