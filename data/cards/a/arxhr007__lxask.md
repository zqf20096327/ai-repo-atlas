# arxhr007/lxask

⭐ 229 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/arxhr007/lxask) · [官网](https://arxhr007.github.io/lxask/) · 个人维护

**本地离线 Linux 命令助手：自然语言生成 shell 命令并核对文档**

在用户机器上运行的 Linux 命令助手：基于 Qwen2.5-Coder-1.5B（LoRA 与强化学习微调），用 Rust 与 llama.cpp/GGUF 实现，纯 CPU 推理，约占 1 GB 磁盘与 1.3 GB 内存，每答约 2 秒。每条生成的命令对照 man pages 与 tldr 做核验，无法确认的部分会标注；支持多步请求、'without X' 限制、模糊请求追问，并可通过 Ctrl+G 在提示符处将自然语言转为命令。安装后离线运行，无需账户或 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1.5B 模型本地 CPU 推理，约 1.1 GB 磁盘、1.3 GB 内存峰值
- 每条命令对照 man pages 与 tldr 核验，标注无法确认的内容
- Ctrl+G 在 shell 提示符处将自然语言行转为命令
- 在 NL2SH-ALFA 基准（300 任务）上报告 62% 解决率

## 适用场景

- 忘记命令时用自然语言直接查询 Linux 用法
- 无网络环境下获取带文档核验的命令建议
- 对命令有约束需求（如'不用 lsof'）时生成替代方案
- 用 --explain 逐部分解释并核验已有命令

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L6:  A Linux command assistant that runs on your own machine:
> L16:  llama.cpp, GGUF
> L32: - ✅ **Checks its own work.** Every command is checked against the man pages and tldr, then — where there is enough 

## 星数曲线

```mermaid
xychart-beta
    title "arxhr007/lxask 星数(近 9 点)"
    x-axis ["2026-10-30", "2026-11-08", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 0 --> 251
    line [3, 4, 8, 62, 109, 140, 179, 220, 229]
```

2026-10-30 3 → 2026-11-27 229（+226）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `270e18d673bf` · [字段定义](../../DATASET.md)*
