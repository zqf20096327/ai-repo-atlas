# vllm-project/vllm-gguf-plugin

⭐ 55 · Python · Apache-2.0 · 推送 2026-10-24 · [GitHub](https://github.com/vllm-project/vllm-gguf-plugin) · 组织维护

**为 vLLM 提供树外 GGUF 量化支持的插件**

vLLM 官方项目下的树外量化插件：在 vLLM 移除树内 GGUF 支持后，通过 vLLM 的模型实现与通用 GGUF 权重适配器恢复 GGUF 量化模型加载，支持文本、视觉语言与图像生成模型，含 MTP投机解码的 nextn 块加载。安装需 CUDA 或 ROCm 工具链，经 uv 从源码构建 CUDA 扩展并编译到 vLLM 所用的 PyTorch。仓库列出经生成测试的模型清单，其他架构在张量名可映射时也可尝试，但不保证兼容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 vLLM 模型实现与通用 GGUF 权重适配器，兼容范围超出固定清单
- 支持从 GGUF 内嵌 nextn 块加载 MTP 投机解码，无需单独下载 MTP 权重
- 覆盖文本、视觉语言、图像生成三类模型，如 Qwen 3、Gemma 3、FLUX.2-klein

## 适用场景

- 在 vLLM 中继续加载 GGUF 量化模型（树内支持废弃后）
- 用单份 GGUF 文件同时运行主干与 MTP 投机解码
- 以多种量化格式（Q4/Q6/Q8/IQ4 等）部署已测试模型

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: This plugin provides out-of-tree GGUF quantization support for vLLM after
> L78: The plugin uses vLLM's model implementations and a generic GGUF weight

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/vllm-gguf-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 53 --> 55
    line [54, 54]
```

2026-10-18 54 → 2026-10-24 54（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6fdf8878d090` · [字段定义](../../DATASET.md)*
