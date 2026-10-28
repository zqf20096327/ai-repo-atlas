# julep-ai/steadytext

⭐ 46 · PLpgSQL · MIT · 推送 2026-02-21 · [GitHub](https://github.com/julep-ai/steadytext) · [官网](https://steadytext.julep.ai/) · 组织维护

**零配置的确定性文本生成与嵌入库，同一输入每次输出相同结果**

由 Julep 维护的 Python 库与 CLI（st 命令），提供本地运行的文本生成、嵌入与重排序，通过固定默认 seed（42）、贪心解码、8-bit 量化模型与 frecency 缓存实现同一输入跨机器产出相同结果。默认模型为 Qwen3-4B/30B 与 Jina-v4 嵌入，支持 JSON/schema/正则约束的结构化生成，可选 daemon 常驻模式减少加载开销。另有 PostgreSQL 扩展 pg_steadytext、Zsh 插件与 Cloudflare Worker 组成生态。远程模型（OpenAI/Cerebras 等）以实验性 unsafe 模式支持，不保证可复现；采用日期式版本号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- seed 参数（默认 42）+ 贪心解码 + 8-bit 量化实现跨平台确定性输出
- 结构化生成：JSON schema/Pydantic/正则/多选约束（基于 llama.cpp 语法）
- daemon 常驻模式与 frecency 缓存减少模型加载开销
- mini 模型（Gemma-3-270M 等约 530MB）用于 CI 与测试

## 适用场景

- 为测试与 CI 提供可复现的 AI 输出，避免随机失败
- 在 CLI 脚本中获得每次一致的生成结果
- 在 SQL 中通过 pg_steadytext 执行确定性生成与嵌入

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: *Deterministic text generation and embeddings with zero configuration*
> L99: SteadyText achieves determinism via:
> L249: * Generation (Small): `Qwen3-4B-Instruct` (3.9GB) - High-quality 4B parameter model

## 星数曲线

```mermaid
xychart-beta
    title "julep-ai/steadytext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 45 --> 47
    line [46, 46]
```

2026-10-18 46 → 2026-10-28 46（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c9674b1789b2` · [字段定义](../../DATASET.md)*
