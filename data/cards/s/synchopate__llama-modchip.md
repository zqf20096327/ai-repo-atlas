# synchopate/llama-modchip

⭐ 1,407 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/synchopate/llama-modchip) · [官网](https://synchopate.github.io/) · 个人维护

**在纯 CPU 上运行 30B-284B 级 MoE 大模型的本地推理引擎**

基于 llama.cpp 的推理引擎与量化检查点集合，提供 16/32/64 GB 三档 RAM 分级的预量化 MoE 模型（Qwen3.8、DeepSeek-V4 284B、Nemotron-30B），通过 RouteCrack 2.0、量化 Split-KV 解码与 HARP-Cache 实现零 GPU 的 CPU 推理。单一二进制自动检测 CPU ISA（AVX-512/AVX2/NEON/Metal）、内存档位与模型家族，附带 ./modchip 脚本完成下载、启动 llama-server/SSE 网关、终端聊天、基准测试与 Claude Code 接线。需按预设采样参数运行。

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

- 零 GPU 纯 CPU 解码，附 Cold Cgroup v2 内存峰值与 tok/s 基准数据
- 单一二进制自动检测 CPU ISA 与 16/32/64 GB RAM 档位
- 预量化 MaxQ 检查点含 512/512 未剪枝专家与 MTP 模块
- ./modchip 一条命令完成下载、服务启动、聊天与评测

## 适用场景

- 在没有 GPU 的机器上本地运行 30B-284B 级 MoE 模型
- 按内存档位选择能完整装入本机 RAM 的量化检查点
- 把本地引擎接到 Claude Code CLI 做终端编码助手
- 跑 CPU 推理基准并生成可分享的评分卡

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L27: One unified `llama-modchip v3.2.0` binary (`GLIBC <= 2.30`, static `libstdc++` & `libgomp`, zero external OpenMP `.
> L43: ./modchip setup    # Auto-detects 16GB / 32GB / 64GB RAM + CPU ISA, verifies SHA-256, writes start_server.sh
> L79: |**`./modchip claude`**|Launches Claude Code CLI wired to the local engine with `/dev/shm` Slot-0 warm restore|

## 星数曲线

```mermaid
xychart-beta
    title "synchopate/llama-modchip 星数(近 16 点)"
    x-axis ["2026-11-02", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 0 --> 1540
    line [71, 375, 882, 938, 1095, 1187, 1231, 1263, 1320, 1342, 1356, 1380, 1389, 1399, 1403, 1407]
```

2026-11-02 71 → 2026-11-25 1,407（+1,336）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 mid · 依据 README sha `5414f02b2f62` · [字段定义](../../DATASET.md)*
