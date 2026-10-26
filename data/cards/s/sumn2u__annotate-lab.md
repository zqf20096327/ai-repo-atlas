# sumn2u/annotate-lab

⭐ 127 · JavaScript · MIT · 推送 2026-06-10 · [GitHub](https://github.com/sumn2u/annotate-lab) · [官网](https://annotate-docs.dwaste.live/) · 个人维护

**开源图像标注工具：为机器学习数据集创建做图像标注**

由 React 客户端与 Flask 服务端组成的图像标注应用：客户端提供标注界面，服务端负责持久化标注变更、生成掩码与标注图像及配置管理。支持 YOLO 与 COCO JSON 格式导出，可用于 Detectron2、MMDetection、TensorFlow Object Detection API 等框架的数据准备。可选启用 Segment Anything Model（SAM）实现自动边界框标注。通过 npm/pip 手动安装或 docker-compose 运行，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- React + Flask 双组件架构，服务端生成掩码与标注图像
- 支持 YOLO 与 COCO JSON 格式导出，可对接 Detectron2/MMDetection/TensorFlow 等框架
- 可选启用 SAM 实现自动边界框标注
- 提供 docker-compose 运行方式与配置文件（config.py/config.js）

## 适用场景

- 为计算机视觉模型训练准备标注数据集
- 导出 YOLO/COCO 格式标注用于目标检测任务
- 利用 SAM 辅助自动选择边界框加速标注

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L5: Annotate Lab is an open-source application designed for image annotation, comprising two main components: the client
> L216: Selection of bounding box automatically is made possible with the Segment Anything Model (SAM). One can toggle thi

## 星数曲线

```mermaid
xychart-beta
    title "sumn2u/annotate-lab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 126 --> 128
    line [127, 127]
```

2026-10-18 127 → 2026-10-26 127（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `fb22d0740f79` · [字段定义](../../DATASET.md)*
