# emapco/rk-transformers

⭐ 28 · Python · Apache-2.0 · 推送 2025-12-02 · [GitHub](https://github.com/emapco/rk-transformers) · [官网](https://emapco.github.io/rk-transformers/) · 组织维护

**在 Rockchip NPU 上导出并运行 Hugging Face 模型的运行时库**

连接 Hugging Face transformers/sentence-transformers 与 Rockchip RKNPU2 的 Python 运行时库。功能分两部分：在 x86_64/arm64 开发机上将模型自动导出为 ONNX 并转换为 RKNN 格式（支持 0-3 级优化、INT8 w8a8 量化、校准数据集、推送 Hub）；在 RK3588/RK3576 等 Rockchip 设备上通过 rknn-toolkit-lite2 加载 .rknn 文件到 NPU 推理，提供 RKSentenceTransformer/RKCrossEncoder 替代类与兼容 transformers pipeline 的 API，支持多 NPU 核分配（core_mask）。限制：需 Linux、Python 3.10-3.12、特定版本的 torch/rknn-toolkit2 组合。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动 ONNX 导出与 RKNN 转换，支持 INT8 (w8a8) 量化与校准数据集
- RKSentenceTransformer / RKCrossEncoder 替代 sentence-transformers 接口
- 兼容标准 Hugging Face pipelines 的 RKModel 系列 API
- 多 NPU 核 core_mask 配置（auto/单核/多核并行）与 RKNN 配置存于 config.json

## 适用场景

- 把 embedding/交叉编码器模型部署到 RK3588 边缘设备的 NPU 上推理
- 在开发机上把 Hugging Face 模型导出为 RKNN 格式并量化
- 在 Rockchip 边缘设备上运行 transformers pipeline 任务

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L12: **RK-Transformers** is a runtime library that seamlessly integrates Hugging Face `transformers` and `sentence-trans
> L31: - **Sentence Transformers**: Drop-in replacement with `RKSentenceTransformer` and `RKCrossEncoder`

## 星数曲线

```mermaid
xychart-beta
    title "emapco/rk-transformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `d321b6b7d3cd` · [字段定义](../../DATASET.md)*
