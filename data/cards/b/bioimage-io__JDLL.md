# bioimage-io/JDLL

⭐ 37 · Java · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/bioimage-io/JDLL) · [官网](https://github.com/bioimage-io/JDLL/wiki) · 组织维护

**Java 库：在 Java 软件中运行 PyTorch/TensorFlow/ONNX 深度学习模型**

由 Icy 团队（bioimage.io）维护的 Java 深度学习模型运行库：提供统一接口加载模型、创建张量并执行推理，底层支持 PyTorch、TensorFlow 1/2、ONNX 等多种引擎，可在同一会话中使用多个框架。默认不安装引擎，用户按需下载对应框架版本；张量基于 ImgLib2 实现，框架间转换由库内部处理。与 Bioimage.io 模型库深度集成，可按模型名下载模型并自动安装所需引擎。面向想把深度学习集成进应用的软件开发者，也可供有 Python 基础的生物图像分析人员通过 Jython 脚本使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一接口运行 PyTorch/TensorFlow 1/2/ONNX 模型，同一会话可用多框架
- 按需安装 DL 引擎，避免默认占用磁盘空间
- Bioimage.io 模型下载与按模型名自动安装所需引擎
- 基于 ImgLib2 的框架无关张量，内部完成框架特定张量转换

## 适用场景

- 在 Java 应用中集成深度学习模型推理而不直接处理各框架 API
- 通过 Jython 脚本运行 Bioimage.io 模型改进图像处理流程
- 同一软件内同时使用多个深度学习框架的模型

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: This project provides a Java library for running Deep Learning (DL) models agnostically, enabling communication betw
> L10: JDLL is able to load models and make inference, create tensors, download Bioimage.io models and manage the supporte

## 星数曲线

```mermaid
xychart-beta
    title "bioimage-io/JDLL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-30 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `4f38217472b1` · [字段定义](../../DATASET.md)*
