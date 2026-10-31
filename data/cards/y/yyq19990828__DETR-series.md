# yyq19990828/DETR-series

⭐ 13 · Python · Apache-2.0 · 推送 2026-08-16 · [GitHub](https://github.com/yyq19990828/DETR-series) · [官网](https://yyq19990828.github.io/DETR-series/) · 个人维护 · 中文 README

**六大 DETR 系列实时目标检测模型的统一 PyTorch 实现与 CLI**

将 RT-DETRv3、D-FINE、DEIM、RT-DETRv4、DEIMv2 等 6 个模型家族共 30 个 COCO 变体收进单一 PyTorch 运行时，用户写一份配置即可通过统一入口 detrs 的 train/eval/infer/export/convert/models 子命令完成训练、评测、推理与 ONNX/TorchScript 导出，推理无需额外 NMS。每个官方 checkpoint 记录上游版本、SHA-256 与数值对齐证据，val2017 结果按预登记容差核对。默认锁定文件面向 PyTorch CUDA 12.1（Linux x86_64 / Windows amd64），用 uv 管理环境；官方 Paddle 实现仅作为只读参考子模块，核心运行时不导入 Paddle。深入文档以中文撰写。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 6 个模型家族、30 个 COCO 变体共享统一数据管线与单一 detrs CLI
- 推理无额外 NMS，ONNX(opset 17)/TorchScript 导出逐值验证
- checkpoint 记录上游修订、SHA-256 与数值对齐证据，按预登记容差核对 AP
- DEIMv2 覆盖 50.3M 至 0.5M 参数规模，面向 GPU/边缘/移动部署

## 适用场景

- 在统一 CLI 下训练或评测多种 DETR 系列检测模型
- 导出 ONNX/TorchScript 用于部署环境
- 用已验收的官方权重做 COCO 目标检测推理

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L10: DETR-series is a unified PyTorch collection of real-time DETR object detectors. Six model families with **30 COCO v
> L16: - **Unified runtime**: all six families share the data pipeline, two-stage training protocol, EMA, checkpoint resum
> L18: - **Deployment friendly**: inference runs no additional NMS; ONNX (opset 17, fixed height/width, dynamic batch) and

## 星数曲线

```mermaid
xychart-beta
    title "yyq19990828/DETR-series 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `e8fe4ae9dfa3` · [字段定义](../../DATASET.md)*
