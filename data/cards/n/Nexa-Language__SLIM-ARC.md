# Nexa-Language/SLIM-ARC

⭐ 16 · Python · Apache-2.0 · 推送 2026-08-22 · [GitHub](https://github.com/Nexa-Language/SLIM-ARC) · [官网](https://slim.nexa-lang.com/) · 组织维护 · 中文 README

**内存受限端侧设备的 MoE 推理运行时优化系统**

中山大学参加 2026 年全国大学生操作系统设计赛的作品：在 llama.cpp 之上打补丁实现的 MoE 推理运行时，通过 mmap 按需加载、阶段感知页建议、专家预测与回收、压力感知驻留和统一 I/O 预算，使模型体积远大于物理内存的 MoE 模型能在 x86、RK3588、Raspberry Pi、macOS 等平台运行；不改变模型权重与 Router 语义。构建需 Git、CMake、C++17 编译器、Python 3.10+ 和 uv，从源码编译，比赛阶段已结束但仍接受贡献。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- mmap 按需加载与阶段感知页建议（加载/Prefill/Decode/MoE Decode 分别配置）
- MoE 专家预测反馈闭环与安全页回收（只回收专家切片内部页面）
- 压力感知驻留与统一资源预算（普通权重/专家/KV cache 共享内存）
- 对 llama.cpp 固定提交应用可重复 patch，支持 x86/RK3588/Raspberry Pi/macOS

## 适用场景

- 在物理内存远小于模型体积的设备上运行 MoE 大模型推理
- RK3588、树莓派等开发板上部署 Qwen3-Next 类 MoE 模型
- 研究受限内存下页缓存与专家驻留策略对推理吞吐的影响

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L23: Proj59“内存受限环境的大语言模型推理优化”的作品。系统通过 mmap 按需加载、阶段感知
> L24: 页建议、MoE 专家预测与回收、压力感知驻留、统一 I/O 预算和 KV cache 管理，让模型体积
> L25: 远大于物理内存的 MoE 模型能够在 x86、RK3588、Raspberry Pi 和 macOS 等平台运行。

## 星数曲线

```mermaid
xychart-beta
    title "Nexa-Language/SLIM-ARC 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-31 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7a7f1ea143d8` · [字段定义](../../DATASET.md)*
