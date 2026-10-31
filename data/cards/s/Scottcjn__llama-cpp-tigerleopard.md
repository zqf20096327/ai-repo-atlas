# Scottcjn/llama-cpp-tigerleopard

⭐ 70 · C++ · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/Scottcjn/llama-cpp-tigerleopard) · [官网](https://rustchain.org) · 个人维护

**在 Mac OS X Tiger/Leopard 的 PowerPC G4/G5 上运行 llama.cpp 推理的移植**

将 llama.cpp 移植到 2005 年前后的 PowerPC G4/G5 Mac（Tiger 10.4 / Leopard 10.5），纯 CPU 推理并利用 AltiVec SIMD 加速，无需 GPU。提供在四款实测机型上运行 TinyLlama、Phi-2 等小模型的成绩表，并给出按 RAM 分档的量化模型建议。安装路径为源码编译：需自行在目标机器上用 GCC 从源码构建 CMake 3.14+（预编译 CMake 工具包已被报告不可用），再以 CMake 命令编译；旧 make 构建已随上游移除。属 Sophiacord 分布式 AI 系统的复古计算节点。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PowerPC G4/G5 上纯 CPU + AltiVec SIMD 的 LLM 推理
- 四款 G4/G5 机型实测可运行（TinyLlama 1.1B 约 1-5 t/s）
- 按 RAM 分档的 Q4_0 量化模型推荐表
- 提供在 Tiger/Leopard 上从源码构建 CMake 3.14+ 的完整流程

## 适用场景

- 让收藏的 PowerPC 老Mac 运行小参数量 LLM
- 复古计算社区验证 20 年前硬件的 AI 推理
- 作为 Sophiacord 分布式系统的复古计算节点

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # llama.cpp for Mac OS X Tiger & Leopard (PowerPC G4/G5)
> L6: This is a working port of llama.cpp for Mac OS X Tiger (10.4) and Leopard (10.5) running on PowerPC G4 and G5 proces
> L129: gone. The `Makefile` in `llama.cpp_source` is now a deprecation stub, so running

## 星数曲线

```mermaid
xychart-beta
    title "Scottcjn/llama-cpp-tigerleopard 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-10-31"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-29 70 → 2026-10-31 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3f7b020dbd2d` · [字段定义](../../DATASET.md)*
