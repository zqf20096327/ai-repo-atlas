# TranDangKhoaAutomation/FaceAutoVN

⭐ 19 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/TranDangKhoaAutomation/FaceAutoVN) · 个人维护 · 中文 README

**用 YOLOv10 视觉检测自动注册 Facebook 账号的 Android 自动化框架**

Python 自动化框架，结合 ADB 控制与 YOLOv10 图像检测，在 Android 设备上端到端自动完成 Facebook 注册：scrcpy 取帧、360×800 预处理、约 200ms/帧推理识别 UI 元素、ADB 执行点击与输入，并经 tempmail.id.vn API 自动获取验证码。模型在约 1,000 标注帧上微调，报告 mAP@0.5=0.87。支持本地模型 data/best.pt、SAFE_DRY_RUN 只检测模式，附 Qt6 模型测试 GUI。运行需 ADB/scrcpy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 端到端注册流水线：UI 检测→ADB 点击输入→临时邮箱验证码轮询
- YOLOv10 在约 1,000 标注 Facebook UI 帧上微调，报告 mAP@0.5=0.87
- SAFE_DRY_RUN=1 支持仅检测不操作设备的干跑模式
- Qt6/PySide6 模型测试 GUI，可调置信度并保存检测输出图

## 适用场景

- 在 Android 设备/模拟器上自动化 Facebook 注册流程
- 测试微调后 YOLOv10 模型对 Facebook UI 的检测效果
- 通过 ADBController API 做线程安全的设备操控

## 场景标签

`GUI 自动化` `目标检测` · 领域:效率与自动化

## 证据(README 行号)

> L3: **FaceAutoVN** is a Python-based automation framework combining ADB control and AI-driven image processing (YOLOv10)
> L12:  3. Perform real-time inference (200ms/frame) to detect UI elements.

## 星数曲线

```mermaid
xychart-beta
    title "TranDangKhoaAutomation/FaceAutoVN 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-30 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `733b373730a7` · [字段定义](../../DATASET.md)*
