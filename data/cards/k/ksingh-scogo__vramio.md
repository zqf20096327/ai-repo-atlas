# ksingh-scogo/vramio

⭐ 14 · Python · 推送 2026-01-07 · [GitHub](https://github.com/ksingh-scogo/vramio) · [官网](https://vramio.ksingh.in/model?hf_id=microsoft/phi-2) · 个人维护

**估算任意 HuggingFace 模型显存需求的 API 服务**

提供一个 HTTP API，输入 HuggingFace 模型 ID 即返回各精度下的 GPU 显存估算：拉取 safetensors 元数据（仅请求头，不下载权重），解析 tensor 形状与 dtype 计算内存，并附加 20% 推理开销（激活与 KV cache）给出 recommended_vram。无需 GPU 或下载模型。面向需要在运行前判断模型是否适配本地 GPU、选择量化方案的开发者。以约 160 行 Python 实现，依赖仅 httpx，支持 git clone 自托管与 Render 一键部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一次 API 调用返回任意 HuggingFace 模型的显存估算
- 仅读取 safetensors 元数据头，不下载权重、无需 GPU
- 按精度计算并附加 20% 推理开销（激活 + KV cache）
- 160 行 Python、零框架、单依赖，附 render.yaml 支持 Render 部署

## 适用场景

- 运行模型前确认它是否放得进我的 24GB 显卡
- 选择合适的量化精度以适配本地 GPU
- 在 CI 或选型流程中批量查询模型显存需求

## 场景标签

 · 领域:LLM 基础设施/模型运维工具

## 证据(README 行号)

> L5: A dead-simple API to estimate GPU memory requirements for any HuggingFace model.
> L38: 1. Fetches safetensors metadata from HuggingFace (just headers, not weights)
> L39: 2. Parses tensor shapes and dtypes

## 星数曲线

```mermaid
xychart-beta
    title "ksingh-scogo/vramio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `70f4413b681f` · [字段定义](../../DATASET.md)*
