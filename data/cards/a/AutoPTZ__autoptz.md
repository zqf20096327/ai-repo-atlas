# AutoPTZ/autoptz

⭐ 117 · Python · AGPL-3.0 · 推送 2026-10-05 · [GitHub](https://github.com/AutoPTZ/autoptz) · 组织维护

**AI 驱动的 PTZ 摄像头自动跟踪桌面应用**

基于 Qt Widgets / PySide6 的跨平台桌面应用，为每路摄像头运行实时视觉流水线（检测→跟踪→重识别→姿态→瞄准→PTZ 驱动），向 PTZ 摄像头发送云台/变焦指令使选定人物保持在画面内。支持多摄像头、遮挡后身份重绑定、模型或设备缺失时保留实时预览。推理使用 ONNX Runtime，按平台选择 CoreML/TensorRT/CUDA/DirectML/OpenVINO/CPU 加速器；PTZ 支持 VISCA over USB/IP、ONVIF、NDI。需 Python 3.12+，提供 macOS/Windows/Linux 预构建安装包与 GitHub Releases 应用内更新；许可为 AGPLv3。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多摄像头并行，每路独立 worker，身份按相机保持稳定
- 点击选人 + 人脸识别与外观 ReID 实现遮挡后重绑定
- ONNX Runtime 自动选择平台加速器（CoreML/TensorRT/DirectML/OpenVINO/CPU）
- VISCA over USB/IP、ONVIF、NDI 四种 PTZ 后端

## 适用场景

- 让 PTZ 摄像头自动跟拍选定人物，如直播或录制场景
- 多机位环境下保持目标身份稳定跟踪
- 在无独显设备上用 CPU/OpenVINO 等方式运行跟踪流水线

## 场景标签

`人脸识别` `目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: **AI-driven PTZ camera tracking — detect people, lock onto a target, and move the camera to follow them automaticall
> L10: a real-time vision pipeline per camera — **detect → track → re-identify → pose →

## 星数曲线

```mermaid
xychart-beta
    title "AutoPTZ/autoptz 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-28"]
    y-axis "stars" 112 --> 115
    line [113, 114, 114]
```

2026-10-18 113 → 2026-10-28 114（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `115bfc7d2a28` · [字段定义](../../DATASET.md)*
