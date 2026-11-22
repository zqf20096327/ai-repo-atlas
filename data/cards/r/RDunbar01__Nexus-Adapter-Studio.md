# RDunbar01/Nexus-Adapter-Studio

⭐ 3 · HTML · NOASSERTION · 推送 2026-10-23 · [GitHub](https://github.com/RDunbar01/Nexus-Adapter-Studio) · 个人维护

**面向本地模型用户：浏览器内训练/评估 GGUF 适配器**

面向使用本地语言模型的用户：自带 GGUF 模型与语料，在浏览器或桌面环境训练并评估适配器；训练前做架构、tokenizer、张量格式和内存检查。浏览器版以单 HTML 分发并含 WGSL 内核，试用无需 Python/PyTorch；原生 PyTorch 后端需完整下载并用 Python 启动。许可允许个人与内部商业测试，其他分发、修改和生产部署需书面同意。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自带本地模型与语料输入，提供训练与评估控制
- 训练前进行架构、tokenizer、张量格式与内存准入检查
- 浏览器版以单 HTML 文件分发，包含 WGSL 内核并在兼容 WebGPU 浏览器中使用
- 原生 PyTorch 后端通过 releases 2.7.1 组件分发，并用 python Start_Nexus.py 启动

## 适用场景

- 我想在浏览器里用自己的本地模型和语料试验适配器训练
- 我想在训练前确认模型架构、格式和内存是否符合要求
- 我想下载完整组件，在本地用 PyTorch 后端运行训练流程

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: Train and evaluate experimental adapters for supported local language models using your own corpus.
> L18: - Training and evaluation controls in a browser interface.
> L38: **The native PyTorch backend requires the full download.** Get every file in releases/2.7.1, keep the numbered data

## 星数曲线

```mermaid
xychart-beta
    title "RDunbar01/Nexus-Adapter-Studio 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-22"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-22 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `83eaf03f1091` · [字段定义](../../DATASET.md)*
