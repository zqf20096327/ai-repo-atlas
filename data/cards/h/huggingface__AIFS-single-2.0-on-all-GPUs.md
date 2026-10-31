# huggingface/AIFS-single-2.0-on-all-GPUs

⭐ 14 · Jupyter Notebook · 推送 2026-07-24 · [GitHub](https://github.com/huggingface/AIFS-single-2.0-on-all-GPUs) · 组织维护

**让 AIFS 气象预报模型在任意 GPU/CPU 上本地运行的补丁与教程**

围绕 ECMWF 发布的 aifs-single-2.0 权重提供轻量封装与教程：通过在 sys.modules 注入 flash_attn 桩模块，把注意力计算路由到 PyTorch SDPA，从而摆脱仅支持 Ampere 架构的 flash-attn 依赖，可在 CUDA、Apple MPS 与 CPU 上用 anemoi-inference 做推断。流程包括从 ECMWF Open Data 拉取初始场、运行 6 小时步长预报、绘图与流式长时效运行，也可用 Hugging Face jobs 托管运行。限制：SDPA 路径与参考 CUDA 实现非逐位一致，不支持 AIFS Ensemble，明确禁止用于业务与安全关键决策。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- flash_attn 桩模块把注意力路由到 PyTorch SDPA，支持 CUDA/MPS/CPU
- 从 ECMWF Open Data 自动下载并缓存初始条件（t-6h 与 t）
- 提供预报、绘图、CLI 与流式长时效运行接口
- 支持通过 Hugging Face jobs 托管运行（如 t4-small）

## 适用场景

- 在没有 Ampere GPU 的设备上本地运行 AIFS 单模型预报
- 不配置本地环境时用 Hugging Face jobs 生成并存储预报结果
- 生成并绘制全球中期天气预报场（温度、风、波高等）

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L15: Therefore, we developed this tutorial and a lightweight wrapper to simplify running aifs-single-2.0 with `anemoi-in
> L123: Each call to `run_forecast` returns a list of state dicts — one per

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/AIFS-single-2.0-on-all-GPUs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `b8a6046dc99b` · [字段定义](../../DATASET.md)*
