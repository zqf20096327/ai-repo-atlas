# Entrpi/ds4-on-spark

⭐ 410 · Shell · MIT · 推送 2026-08-27 · [GitHub](https://github.com/Entrpi/ds4-on-spark) · 组织维护

**在 DGX Spark 上一键部署 DeepSeek-V4-Flash 推理服务的安装器**

打包并固定 Entrpi/ds4 fork（antirez/ds4 的 Blackwell CUDA 性能分支）v0.6.5，通过一条 curl 安装脚本在 NVIDIA DGX Spark（GB10/SM121）上克隆、编译引擎并下载 DeepSeek-V4-Flash 0731 GGUF 模型（约 81 GiB）与 DSpark drafter，启动 ds4-server 提供 OpenAI completions/Responses 与 Anthropic Messages 四种 API 的连续批处理服务。声称相对上游取得 2.4-3.3x prefill 吞吐与 1.33-1.47x 解码速度，支持前缀缓存、投机解码与 v0.6 内存记账机制。面向拥有 DGX Spark 等 Blackwell 硬件的开发者，需 CUDA 13 与至少 120 GiB 可用磁盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令完成引擎编译、约 87.5 GiB 模型下载与服务启动
- 同一连续批处理同时服务 OpenAI chat/completions、Responses 与 Anthropic Messages 四种 API
- DSpark 无损投机解码与磁盘持久化 KV 前缀缓存
- v0.6 内存记账：按需映射上下文、LRU bank 淘汰、超限返回类型化拒绝而非崩溃

## 适用场景

- 在 DGX Spark 上本地部署 DeepSeek-V4-Flash 供局域网使用
- 将 Codex、Claude Code、opencode 等编码代理指向自建推理服务
- 长文档（最高 1M token 上下文）推理与深度代理循环任务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L7: `antirez/ds4` (DwarfStar 4) that builds
> L8: the upstream engine into a batched multi-request server for Blackwell
> L48: - **Engine:** `Entrpi/ds4` pinned at `v0.6.5`, cloned and built native `sm_121` by the installer.

## 星数曲线

```mermaid
xychart-beta
    title "Entrpi/ds4-on-spark 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 409 --> 411
    line [410, 410]
```

2026-10-18 410 → 2026-10-24 410（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3013b9f1743f` · [字段定义](../../DATASET.md)*
