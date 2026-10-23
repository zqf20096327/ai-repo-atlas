# zkmkarlsruhe/ofxTensorFlow2

⭐ 119 · C++ · NOASSERTION · 推送 2026-02-04 · [GitHub](https://github.com/zkmkarlsruhe/ofxTensorFlow2) · 组织维护

**在 openFrameworks 中加载运行 TensorFlow 2 模型的 C++ 插件**

由 ZKM | Hertz-Lab 开发的 openFrameworks 插件（addon），通过 cppflow 封装 TensorFlow 2 C API，提供加载与运行模型的封装类，并附带图像、像素、音频样本等 openFrameworks 常用类型与张量之间的转换工具函数。面向用 C++ 做创意编码的开发者，示例涵盖风格迁移、目标识别、姿态估计、Pix2Pix、关键词 spotting 与视频抠像。以源码形式克隆到 openFrameworks addons 目录安装，需运行脚本下载预编译 libtensorflow，GPU 支持为可选项，Windows 未测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 cppflow 封装 TensorFlow 2 C API，无需 Bazel 或完整 TensorFlow 安装
- 提供 openFrameworks 类型（图像/像素/音频样本）与张量的转换工具
- 脚本自动下载预编译 libtensorflow，可选 GPU 构建与指定版本
- 示例覆盖风格迁移、目标识别、姿态估计、视频抠像等

## 适用场景

- 在 openFrameworks 创意编码项目中加载并运行 TensorFlow 2 模型
- 构建实时视觉/音频推理的互动装置或应用
- 复用官方示例快速上手模型集成

## 场景标签

 · 领域:创意编程/机器学习集成

## 证据(README 行号)

> L30: ofxTensorFlow2 is an openFrameworks addon for loading and running ML models trained with the TensorFlow 2 ML (Machi
> L36: The addon utilizes the TensorFlow 2 C library wrapped by the open source cppflow C++ interface:
> L42: Additional classes wrap the process of loading & running a model and utility functions are provided for conversion 

## 星数曲线

```mermaid
xychart-beta
    title "zkmkarlsruhe/ofxTensorFlow2 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 118 --> 120
    line [119, 119]
```

2026-10-18 119 → 2026-10-23 119（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `15a65942ee9c` · [字段定义](../../DATASET.md)*
