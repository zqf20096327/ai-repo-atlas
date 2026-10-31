# AngelDev2343/WhyAI

⭐ 15 · HTML · 推送 2026-07-18 · [GitHub](https://github.com/AngelDev2343/WhyAI) · [官网](https://www.whyai.live/) · 组织维护

**浏览器内在线/离线双模式的生成式 AI 聊天助手**

WDG Technologies 的私有软件产品，本仓库仅存放项目文档。以网页/PWA 形式提供 AI 聊天：在线模式经云端推理，离线模式下载一次模型后在浏览器本地运行聊天；Pro 计划支持基于 WebGPU（ONNX Runtime Web，Tiny-SD FP16 约 950 MB）的本地图像生成，云端图像生成由 Pollinations 提供，聊天云推理使用 Groq。面向不接触命令行的终端用户，免费计划含每日 5 条高级消息。限制：离线与本地生图需 Chrome/Edge/Safari（WebAssembly/WebGPU），源码不公开。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一站点内在线/离线双模式切换，离线聊天在浏览器本地运行
- Pro 计划支持 WebGPU 本地图像生成（ONNX + Tiny-SD FP16，约 950 MB）
- 无广告、不售卖数据，本地生成时 prompt 不上云
- 西班牙语/英语界面，可免注册试用演示消息

## 适用场景

- 无信号或旅行时离线继续使用 AI 聊天
- 在浏览器内直接生成图像（云端或本机 GPU）
- 注重隐私、不希望对话离开设备的日常问答与图像分析

## 场景标签

`聊天机器人` `图像生成` · 领域:对话与助手

## 证据(README 行号)

> L29: **WhyAI** es un chat con inteligencia artificial que puedes usar **con internet** o **completamente sin él** — desd
> L117: **WhyAI** is an AI chat you can use **online** or **fully offline** — same website, no weird installs, no command 
> L205: - **wllama** — local chat engine in the browser (WASM)

## 星数曲线

```mermaid
xychart-beta
    title "AngelDev2343/WhyAI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d58c22f2898d` · [字段定义](../../DATASET.md)*
