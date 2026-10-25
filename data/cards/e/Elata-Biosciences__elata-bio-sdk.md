# Elata-Biosciences/elata-bio-sdk

⭐ 92 · TypeScript · MIT · 推送 2026-10-05 · [GitHub](https://github.com/Elata-Biosciences/elata-bio-sdk) · [官网](https://docs.elata.bio/sdk/overview) · 组织维护

**跨平台生物信号 SDK：EEG 管线与浏览器 rPPG 处理**

面向构建神经技术与远程生理感知应用的开发者的跨平台生物信号 SDK。内容覆盖 EEG 核心 crate 与信号处理、EEG/rPPG 的 WebAssembly 绑定、Web Bluetooth 耳机传输（内置 Muse）、iOS/Android 原生 FFI 层，以及摄像头 rPPG 处理。以 npm 的 @elata-biosciences 作用域包与计划发布到 crates.io 的 Rust crate 交付，推荐通过 create-elata-demo 脚手架起步。限制：Safari/iOS 不支持 Web Bluetooth 工作流；rppg-models-web 不捆绑模型权重，需调用方提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- EEG 核心 crate、信号处理与模型的 WebAssembly 绑定
- Web Bluetooth EEG 传输，内置 Muse，支持扩展其他设备
- 摄像头 rPPG 处理包（rppg-web）与可选诊断波形适配器（rppg-models-web）
- create-elata-demo 应用脚手架，含 rppg/eeg/ble 模板

## 适用场景

- 在浏览器应用中接入 EEG 头环并处理脑电信号
- 基于摄像头的 rPPG 远程生理信号测量应用开发
- 在 iOS/Android 原生应用中集成生物信号能力

## 场景标签

 · 领域:生物信号处理/神经技术

## 证据(README 行号)

> L10: - EEG core crates, signal processing, and models
> L11: - WebAssembly bindings for EEG and rPPG
> L81: |Run camera-based rPPG in a browser app|`@elata-biosciences/rppg-web`|Includes processor, backend loader, and demo 

## 星数曲线

```mermaid
xychart-beta
    title "Elata-Biosciences/elata-bio-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-25 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `439b1bc1fc4a` · [字段定义](../../DATASET.md)*
