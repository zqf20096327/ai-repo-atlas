# ScriTech/gtx1070-llm-benchmarks

⭐ 3 · HTML · CC-BY-4.0 · 推送 2026-10-30 · [GitHub](https://github.com/ScriTech/gtx1070-llm-benchmarks) · 个人维护

**双 GTX 1070 上本地 LLM 的质量/速度/长上下文基准数据**

该仓库记录了在两张 NVIDIA GTX 1070 8 GB（共 16 GB VRAM）上对 14 个本地 LLM 的基准测试结果：其中 10 个模型（17 种配置）跑完同一套 72 分制质量测试，部分配置推送至 128K–256K 上下文，并附 KV cache 类型对比与推荐配置。全部结果来自单台 Dell 工作站（Proxmox LXC 容器、CUDA 12.8），作者明确说明数字仅代表该硬件上的相对排序而非绝对质量分。原始数据以 CSV/XLSX 形式提供，另附可离线打开的 report.html。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 14 个模型的速度测试与 17 种配置的 72 分制质量评分
- 128K–256K 长上下文测试（含 prefill/decode 速度与峰值显存）
- 多种 KV cache 量化类型（q4/q5/q8/f16）的可行性与速度对比
- 附 llama.cpp 可用启动命令与原始 CSV 数据

## 适用场景

- 手头只有 GTX 1070 级旧显卡，想知道哪些本地模型能跑
- 挑选在 16 GB VRAM 内 65K 上下文可用的量化与 KV 配置
- 查看 MTP draft 模型对解码速度的提升幅度

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: We tested 14 models on a pair of **NVIDIA GTX 1070 8 GB** cards (Pascal, 16 GB of VRAM in total), mostly with **llam
> L148: - One machine, two identical GTX 1070s, and a suite we wrote ourselves. A 1-point difference on a 72-point score i
> L174: - `data/quality.csv`, `data/speed.csv`, `data/long_context_sweep.csv`, `data/kv_cache.csv`: the raw tables behind 

## 星数曲线

```mermaid
xychart-beta
    title "ScriTech/gtx1070-llm-benchmarks 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `213428199ca5` · [字段定义](../../DATASET.md)*
