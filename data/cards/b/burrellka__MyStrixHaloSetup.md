# burrellka/MyStrixHaloSetup

⭐ 31 · 推送 2026-07-25 · [GitHub](https://github.com/burrellka/MyStrixHaloSetup) · 个人维护

**面向非 ML 工程师的 Strix Halo 本地 LLM 搭建指南（8 步）**

一份 Linux 教程，面向购买 AMD Ryzen AI Max+ 395（Strix Halo）128GB 迷你主机的普通技术用户，目标是在两天内完成本地 LLM 运行环境：BIOS 内存 carve-out 调整、GRUB 提升 GTT 上限至约 120GB、NPU 固件/驱动修复、安装 Lemonade-server 并通过 OpenAI 兼容端点同时驱动 GPU（ROCm 版 llama.cpp）与 NPU（FastFlowLM）。内容含逐步命令、故障排查（traps）与实测性能数字。仅适用于 Ubuntu 24.04 基础的 Linux 环境，不覆盖 Windows。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 步流程：BIOS 设置→GRUB→memlock→NPU 固件→Lemonade→后端安装
- 一个 OpenAI 兼容端点同时服务 GPU 与 NPU 两个引擎
- NPU 经 FastFlowLM 与 GPU 推理并行运行（附 GPU 占用验证命令）
- Lemonade 提供 gfx1150/1151/1152 预编译 llama.cpp+ROCm 二进制，无需源码构建

## 适用场景

- Strix Halo 迷你主机上解锁完整 ~120GB 内存池供模型使用
- 让 NPU 与 GPU 同时运行模型并通过统一 API 调用
- 排查 62GB 幻影内存、NPU 不识别等常见故障

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: **This is a Linux guide.** The first thing I did with this machine was wipe Windows and install Linux Mint. Everythi
> L5: A working setup for AMD Ryzen AI Max+ 395 ("Strix Halo") mini PCs, written by someone who is not an ML engineer and 
> L15: That was me. It took nine days. This is the two-day version.

## 星数曲线

```mermaid
xychart-beta
    title "burrellka/MyStrixHaloSetup 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-27 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1e3dd448ed5e` · [字段定义](../../DATASET.md)*
