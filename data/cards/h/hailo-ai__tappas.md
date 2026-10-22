# hailo-ai/tappas

⭐ 204 · C++ · LGPL-2.1 · 推送 2026-08-20 · [GitHub](https://github.com/hailo-ai/tappas) · [官网](http://hailo.ai/) · 组织维护

**面向 Hailo 边缘设备的视频 AI 流水线框架与预训练应用示例**

Hailo 官方的基础设施项目：基于 GStreamer 构建 AI 视频处理流水线，提供流水线元素、预训练 AI 任务（如单流目标检测示例）与 C++ 后处理元素开发指南。面向使用 Hailo-8/Hailo-10H 硬件加速器的开发者，用于评估、参考代码与演示。需要 Hailo 设备与 HailoRT PCIe 驱动，支持 SW Suite、手动、Yocto 与树莓派 5 等安装方式；v5.0.0 起多数示例应用已迁至独立仓库，hailopython 元素已标记弃用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | LGPL-2.1 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 GStreamer 的 AI 视频流水线元素与框架
- 内置单流目标检测示例应用（HEF 模型经 model_zoo 下载）
- 提供 C++ 自定义后处理元素编写与性能调试/交叉编译文档
- 支持 Hailo-8 与 Hailo-10H 设备，兼容指定版本 HailoRT

## 适用场景

- 在 Hailo 硬件上快速搭建视频目标检测流水线
- 以示例代码为起点开发并微调自己的边缘 AI 应用
- 在树莓派 5 或 Yocto 嵌入式平台上集成 Hailo 推理

## 场景标签

`图像视频处理` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L32: TAPPAS is Hailo's infrastructure for building applications, implementing pipeline elements and
> L33: pre-trained AI tasks.
> L37: Demonstrating Hailo's system integration scenario of specific use cases on predefined systems

## 星数曲线

```mermaid
xychart-beta
    title "hailo-ai/tappas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 203 --> 205
    line [204, 204]
```

2026-10-18 204 → 2026-10-22 204（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3baac981e615` · [字段定义](../../DATASET.md)*
