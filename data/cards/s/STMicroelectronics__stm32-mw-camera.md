# STMicroelectronics/stm32-mw-camera

⭐ 14 · C · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/STMicroelectronics/stm32-mw-camera) · 组织维护

**STM32 摄像头传感器硬件抽象中间件，统一 9 款传感器接口**

STMicroelectronics 维护的 C 语言摄像头中间件，位于传感器驱动与应用之间：统一传感器初始化配置、DCMIPP 管线管理（缩放/裁剪/格式）、流式采集启动、曝光与白平衡等特性控制，并抽象硬件与板级差异。支持 IMX335、OV5640、IMX477 等 9 款传感器，部分经 STM32 ISP 库链式调用自动运行 AE/AWB。使用方式为复制配置头文件模板并链接源码集成到应用，非独立安装包。README 未展示 AI 功能，仅仓库主题标签含 ai。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 9 款摄像头传感器（IMX335/OV5640/IMX477/VD66GY 等）
- 可选自动链式调用 STM32 ISP，在 CMW_CAMERA_Run() 中运行 AE/AWB
- DCMIPP 管线配置辅助（缩放、裁剪、格式）与传感器能力运行时查询
- 提供添加新传感器的文档与配置头文件模板

## 适用场景

- 在 STM32 应用中接入不同摄像头传感器而无需处理板级细节
- 通过统一 API 配置曝光、白平衡与采集管线
- 为视觉采集应用快速搭建摄像头初始化与流式读取

## 场景标签

 · 领域:嵌入式/摄像头中间件

## 证据(README 行号)

> L30: The Camera Middleware is a hardware abstraction layer between camera sensor
> L36: - Abstracting hardware and board-specific details

## 星数曲线

```mermaid
xychart-beta
    title "STMicroelectronics/stm32-mw-camera 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 low · 依据 README sha `780cc9536a32` · [字段定义](../../DATASET.md)*
