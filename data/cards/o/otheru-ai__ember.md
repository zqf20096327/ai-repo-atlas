# otheru-ai/ember

⭐ 28 · C++ · MIT · 推送 2026-09-11 · [GitHub](https://github.com/otheru-ai/ember) · [官网](https://otheru.ai/) · 组织维护

**面向 AMD Strix Halo 的 DeepSeek-V4-Flash 本地推理服务器**

用 C 编写的推理服务器，在 AMD Strix Halo（gfx1151）APU 上本地运行 DeepSeek-V4-Flash 模型（默认视觉版），在单一端点提供 OpenAI Chat Completions/Responses、Anthropic Messages 与旧版 Completions API。通过 Docker Compose 部署，首次启动自动下载并校验固定版本模型（约 96 GiB）。针对该平台做 CPU/GPU/统一内存联合调优，支持投机解码与前缀缓存，另提供实验性的 opt-in XDNA2 NPU 异构路径。限制：不支持其他 GPU/NPU 架构，需约 128 GiB 统一内存与 100-120 GiB 磁盘。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单端点兼容 OpenAI 与 Anthropic 消息 API
- 针对 Strix Halo 的 CPU/GPU/统一内存/XDNA2 NPU 联合调优
- 投机解码与前缀缓存（缓存命中后 194 ms 暖 TTFT）
- 模型下载自动校验与完整性记录，拒绝未固定 revision 启动

## 适用场景

- 在 Ryzen AI Max 395+ 本地跑 DeepSeek-V4-Flash 供聊天或编程 agent 使用
- 把本地端点接入 Claude Code / Codex CLI 等编码客户端
- 在单台 Strix Halo 机器上部署带图像问答能力的本地 LLM 服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L14: Ember is a C inference server for DeepSeek-V4-Flash. It provides OpenAI Chat
> L8: > **Ember is designed exclusively for AMD Strix Halo (`gfx1151`).** It is an
> L32: - Native x86_64 Linux on AMD Strix Halo (`gfx1151`)

## 星数曲线

```mermaid
xychart-beta
    title "otheru-ai/ember 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 25 --> 29
    line [26, 28, 28]
```

2026-10-18 26 → 2026-10-31 28（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `be2b5df9ba93` · [字段定义](../../DATASET.md)*
