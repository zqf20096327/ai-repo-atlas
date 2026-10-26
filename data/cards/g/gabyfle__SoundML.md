# gabyfle/SoundML

⭐ 30 · OCaml · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/gabyfle/SoundML) · [官网](https://soundml.dev) · 个人维护

**OCaml 音频 DSP 库：对音频文件做高层读写与处理**

以两个 opam 包（soundml 核心库与 soundml-io 音频编解码/重采样）形式分发的 OCaml 音频处理库。README 声明项目正从零重建、公共 API 不稳定、尚未可投入使用；功能列表（快速 I/O、特征提取、音效、时间拉伸与变调、IIR/FIR 滤波）均为计划项而非已实现特性。构建采用 dune 包管理，自动解析依赖并自行编译所需版本的 OCaml 编译器；依赖 Raven（nx 张量库）的固定 fork 修订，要求 OCaml >= 5.5.0。面向 OCaml 开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 分为 soundml 核心库与 soundml-io（音频编解码、重采样）两个 opam 包
- 计划功能包括特征提取、时间拉伸与变调、IIR/FIR 滤波
- 基于 dune 包管理构建，自动编译所需的 OCaml 编译器
- 依赖 Raven/nx 张量栈的固定 git pin，可直接零拷贝读取张量存储

## 适用场景

- 在 OCaml 项目中对音频文件做读取、解码与重采样
- 在 OCaml 生态内做音频特征提取与滤波（计划功能）
- 跟踪基于 nx 张量库的音频 DSP 开发进展

## 场景标签

 · 领域:音频信号处理

## 证据(README 行号)

> L4:  A little and very high level library to perform basic operations on audio files in the OCaml language
> L26:  - Feature extraction

## 星数曲线

```mermaid
xychart-beta
    title "gabyfle/SoundML 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-26 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `677cc22cf379` · [字段定义](../../DATASET.md)*
