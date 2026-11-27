# a2zrr/hand-controller

⭐ 3 · Python · MIT · 推送 2026-11-24 · [GitHub](https://github.com/a2zrr/hand-controller) · 个人维护

**用摄像头手势生成方向状态并通过 UDP 输出的游戏控制工具**

通过摄像头读取单手手势，经 MediaPipe Hand Landmarker 检测 21 个关键点，由规则分类器（或自训练模型）输出 RIGHT/LEFT/UP/DOWN/STOP 五种状态，每帧以 JSON 通过 UDP 发送到 127.0.0.1:5005，供任意语言或引擎的程序读取。内置状态平滑（120 ms 稳定判定）与调试窗口；支持录制数据、训练小型神经网络并评估。默认需 uv 安装 Python 3.12 与 MediaPipe，模型文件需单独下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MediaPipe 关键点检测 + 规则分类器，无需训练即可使用
- 每帧输出 JSON 到 UDP 127.0.0.1:5005，与接收程序解耦
- 可选录制-训练-评估流程，支持自训练模型替换规则分类
- 提供 C#/.NET、Python、JavaScript 三种现成客户端

## 适用场景

- 在 Unity/Godot 等游戏中接入手势方向控制
- 无需手柄，用摄像头手势操作任意支持 UDP 的程序
- 针对个人手型与光照录制数据训练自定义手势模型

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L15: Webcam (OpenCV) -> MediaPipe Hand Landmarker -> classifier -> smoothing -> UDP JSON on 127.0.0.1:5005
> L19: 2. **Detection:** MediaPipe Hand Landmarker finds up to one hand and its 21 landmarks.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `bf2618a4ca2b` · [字段定义](../../DATASET.md)*
