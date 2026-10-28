# IgnitionAI/ignition

⭐ 25 · TypeScript · 推送 2026-10-18 · [GitHub](https://github.com/IgnitionAI/ignition) · [官网](https://ignitionai.dev/) · 组织维护

**浏览器内训练强化学习智能体的 JS/TS 框架，ONNX 部署**

面向 Three.js/React Three Fiber 等 JS 创意开发者的开源强化学习框架：实现 5 个方法的 TrainingEnv 接口后调用 env.train() 即可训练 DQN、PPO 或 Q-Table 智能体，训练在浏览器中基于 TensorFlow.js（WebGPU>WebGL>WASM>CPU 自动选择）运行，无需 Python、服务器或 CUDA。训练后的模型可导出 TF.js JSON，经独立 Python 3.11 转换脚本生成 ONNX，用于 Unity/Unreal/Python/C++ 等部署；支持 HuggingFace Hub 模型存取与 setSpeed 加速训练。限制：ONNX 导出依赖 Python 转换步骤，v0.1 首个公开版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 实现 TrainingEnv 接口（5 个方法）即可训练 DQN/PPO/Q-Table
- 基于 TensorFlow.js 的浏览器内训练，WebGPU/WebGL/WASM/CPU 自动选择
- TF.js → ONNX 导出管线，可在 JS 中直接用 OnnxAgent 推理
- HuggingFace Hub 模型保存/加载与 setSpeed 训练加速

## 适用场景

- 在 Three.js/R3F 3D 场景中实时训练并观看智能体学习
- 浏览器训练后导出 ONNX 到 Unity/Unreal/边缘设备部署
- 用 CartPole、GridWorld、MountainCar 等内置环境入门强化学习

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L10: IgnitionAI is an open-source RL framework built for creative developers working with **Three.js**, **React Three Fi
> L17: - **Browser-native.** TensorFlow.js with WebGPU > WebGL > WASM > CPU auto-selection. No install, no CUDA, no server

## 星数曲线

```mermaid
xychart-beta
    title "IgnitionAI/ignition 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `78a91f30f37c` · [字段定义](../../DATASET.md)*
