# samueltuoyo15/AR-Object-Scanner

⭐ 26 · TypeScript · 推送 2026-03-13 · [GitHub](https://github.com/samueltuoyo15/AR-Object-Scanner) · [官网](https://ar-object-scanner.vercel.app/) · 个人维护

**浏览器端实时物体检测应用：摄像头画面叠加 AR 检测框**

基于 TypeScript、Vite 与 ONNX Runtime Web 构建的网页应用：读取摄像头实时视频流，在浏览器本地运行 YOLOv8 nano/small ONNX 模型做物体检测，以 AR 叠加层显示检测框、标签与置信度，覆盖 80 个 COCO 类别（检测仅限这些类别）。支持切换摄像头、切换模型、调节置信度阈值，并显示 FPS 的性能 HUD。通过 git clone 源码配合 pnpm 安装依赖并运行开发服务器，面向需要在无服务器环境下体验实时检测的开发者与用户。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内运行 YOLOv8 nano/small ONNX 模型做实时检测
- AR 叠加层显示检测框、标签与置信度百分比
- 支持切换摄像头设备、模型与置信度阈值
- 检测范围限 80 个 COCO 类别，README 明确列出限制说明

## 适用场景

- 打开摄像头实时识别身边的常见物体
- 体验 ONNX Runtime Web 在浏览器内的客户端推理
- 作为浏览器端 AI 检测应用的演示与开发参考

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L4: The AR Object Scanner is an innovative augmented reality application that leverages real-time computer vision to ide
> L10: - **Client-side Inference**: Executes machine learning models directly in the browser using ONNX Runtime Web, ensur

## 星数曲线

```mermaid
xychart-beta
    title "samueltuoyo15/AR-Object-Scanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-26 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `871caa1a5e0d` · [字段定义](../../DATASET.md)*
