# halalboro/fpga-accelerators

⭐ 16 · C++ · 推送 2025-12-16 · [GitHub](https://github.com/halalboro/fpga-accelerators) · 个人维护

**FPGA 视觉加速器开发教程与资源汇编（Vitis-AI 工具流）**

个人维护的文档型仓库，汇编在 Xilinx/AMD FPGA 上部署计算机视觉硬件加速器所需的工具、资源与教程。记录从主机 CPU 训练神经网络到 FPGA 上实时视频目标检测的完整工具流，梳理 DPU-VitisAI、DPU-PYNQ、Vitis HLS 三种路线，并附作者在 Ultra96v2 上部署 YOLOv3、以及 KV260/ZCU102/ZCU104 上做野火检测 CBAM-YOLOX 的项目实践，涉及 Vitis AI 3.0/2.5、DPU PYNQ 与多种编程 API。README 声明不再积极维护，且未更新至最新版 Vitis-AI 工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 梳理 DPU-VitisAI / DPU-PYNQ / Vitis HLS 三种加速器开发路线
- 覆盖 KV260、ZCU102、ZCU104、Ultra96v2 四类硬件的实现记录
- 包含 YOLOv3 实时目标检测与 CBAM-YOLOX 野火检测两个实践项目
- 汇总 DPU IP 文档与 API_0–API_3、ONNX Runtime 编程 API 资料

## 适用场景

- 嵌入式/ML 入门者了解 FPGA 部署神经网络的全流程
- 查找 Xilinx FPGA 计算机视觉加速的官方文档与工具入口
- 参考 DPU-PYNQ 或 DPU-VitisAI 路线的项目实践细节

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L4: My focus is on documenting the tool flow of developing a hardware accelerator, from training the neural network on a
> L8: When it comes to developing such an accelerator on an FPGA, there are three solutions that one could follow to reach

## 星数曲线

```mermaid
xychart-beta
    title "halalboro/fpga-accelerators 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `60807e83c29f` · [字段定义](../../DATASET.md)*
