# frantic0/sema-engine

⭐ 32 · JavaScript · MIT · 推送 2026-04-28 · [GitHub](https://github.com/frantic0/sema-engine) · [官网](https://frantic0.github.io/sema-engine/) · 组织维护

**面向实时编程的浏览器端 JS 音频信号引擎，带 ML 集成钩子**

JavaScript 音频信号引擎，为实时编程、交互音乐、机器聆听与浏览器 DSP 应用提供支持。核心机制：封装 Web Audio AudioWorklet 处理器（maxi-processor.js，需自行部署在可访问 URL）、基于 Maximilian 的 C++ DSP 对象编译为浏览器可用、Nearley 语法编译管线将实时代码文本转为可求值的 DSP 代码；并提供采样加载、分析器、共享缓冲与 Learner 机器学习集成类。状态标注为 experimental，API 可能变动。npm 安装，需 HTTPS 或 localhost 安全文境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Web Audio AudioWorklet 处理器封装（音频线程脱离主线程）
- Nearley 语法编译管线：实时代码→DSP 代码
- Learner 集成钩子与共享缓冲支持机器学习工作流
- 提供 ES module 与 UMD 双构建及分析器工具

## 适用场景

- 在浏览器中构建实时编程音乐/DSP 应用
- 搭建自定义实时编码语言并即时求值音频代码
- 将机器学习组件（Learner）接入音频引擎做交互音乐

## 场景标签

 · 领域:音频信号处理/创意编程

## 证据(README 行号)

> L11: **sema-engine** is a JavaScript audio signal engine for live coding, interactive music, machine listening, and brow
> L25: - Shared buffer support for communication between the audio engine, UI, and learners.
> L147: `Learner` can be connected to the engine for machine learning workflows and shared-buffer communication.

## 星数曲线

```mermaid
xychart-beta
    title "frantic0/sema-engine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-31 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2cbccedb5a11` · [字段定义](../../DATASET.md)*
