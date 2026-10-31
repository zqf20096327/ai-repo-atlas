# setu4993/convert-labse-tf-pt

⭐ 15 · Python · MIT · 推送 2026-01-15 · [GitHub](https://github.com/setu4993/convert-labse-tf-pt) · [官网](https://huggingface.co/setu4993/LaBSE) · 个人维护

**将 LaBSE 等模型从 TensorFlow 转换为 PyTorch 的转换工具**

提供 Google LaBSE 模型从 TensorFlow 到 PyTorch 的转换实现，并扩展支持 smaller-LaBSE 与 LEALLA 系列模型（base/small/large）。转换后的模型以 PyTorch HF 兼容（原始与 safetensors）、TensorFlow 与 Flax 格式上传至 HuggingFace Model Hub，附带兼容 tokenizer。通过 poetry 安装并运行 convert_labse / convert_lealla 命令完成本地导出，仓库代码采用 MIT 许可，模型本体为 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 LaBSE、smaller-LaBSE 与 LEALLA 三类模型的 TF→PyTorch 转换
- 产出 PyTorch（含 safetensors）、TensorFlow、Flax 多格式及兼容 tokenizer
- 提供按模型区分的导出命令与 HuggingFace Hub 上传流程

## 适用场景

- 在 PyTorch/HuggingFace 生态中使用 LaBSE 或 LEALLA 嵌入模型
- 批量导出多尺寸 LEALLA 模型并上传 Model Hub
- 复现转换流程生成 safetensors 格式权重

## 场景标签

 · 领域:NLP 嵌入模型/模型工程

## 证据(README 行号)

> L5: This project is an implementation to convert Google's LaBSE model from TensorFlow to PyTorch. It also offers extensi
> L7: The models are uploaded to the HuggingFace Model Hub in the PyTorch HF-compatible (original and `safetensors`), Tens

## 星数曲线

```mermaid
xychart-beta
    title "setu4993/convert-labse-tf-pt 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `cfd1ce86c0a8` · [字段定义](../../DATASET.md)*
