# drmihirbrahme/midge

⭐ 13 · Python · Apache-2.0 · 推送 2026-08-21 · [GitHub](https://github.com/drmihirbrahme/midge) · 个人维护

**在低配机器上运行 100B+ MoE LLM 的磁盘流式推理引擎**

C 语言编写的 MoE 推理引擎加转换器，通过将稠干常驻内存、专家权重按需从磁盘流式读取，使 gpt-oss、Mixtral、Qwen3-MoE 系模型能在数 GB RAM 的普通 CPU 机器上运行；gpt-oss-120b 需约 75 GB 磁盘与 8 GB 内存。提供 OpenAI 兼容服务器（流式、会话前缀缓存、工具调用）、可中继至云端或局域网 GPU 的混合模式及 Web 引导界面。另含 Apple Silicon/NVIDIA 的 MLX 引擎（同一模型目录，无需重转换）、midge check 可在下载前判定本机能否运行某 Hugging Face 模型。CUDA 路径未在物理硬件上验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 稠干常驻 + 专家从磁盘流式读取，8 GB RAM 可运行 gpt-oss-120b
- OpenAI 兼容服务器：流式、工具调用、会话前缀缓存
- 混合模式可中继到云端/局域网上游并按请求锁定本地
- midge check 在下载前测本机内核/磁盘/RAM 并给出能否运行判定

## 适用场景

- 在无 GPU 的普通电脑上本地运行 gpt-oss/Mixtral/Qwen3-MoE 大模型
- 给 agent 框架提供本地 OpenAI 兼容后端
- 敏感请求留在本地、其余走云端上游的混合推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L6: **Tiny engine, immense models.** Run 100B+ mixture-of-experts LLMs on an
> L22: * an **OpenAI-compatible server** with streaming, a session prefix cache,
> L265: ./midge serve models/gpt-oss-20b --port 8420 --preload-gb 4

## 星数曲线

```mermaid
xychart-beta
    title "drmihirbrahme/midge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `dcc7e4a3d931` · [字段定义](../../DATASET.md)*
