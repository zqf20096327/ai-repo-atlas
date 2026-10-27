# l-nmch/hailo-10h-llm-compiler

⭐ 23 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/l-nmch/hailo-10h-llm-compiler) · 个人维护

**把 Hugging Face LLM 编译为 Hailo-10H HEF 的逆向工程流水线**

面向边缘 AI 硬件 Hailo-10H 开发者的开源编译流水线：将 Hugging Face checkpoint 经 ONNX 导出、图手术、量化等六步编译为自包含 HEF（内嵌 tokenizer 与生成配置），并通过 hailo-ollama 注册部署。方法为对 Hailo Dataflow Compiler 5.3.0 未公开 LLM 编译流的逆向文档化，自我声明高度实验性；仅 TinyStories-25M 端到端验证连贯生成，hidden≥576 的模型存在保真度差距；DFC wheel 与固件不含于仓库、不随附分发，需自行从 Hailo 开发者门户获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 六步流水线（s1→s6）从 HF checkpoint 生成自包含 HEF
- 支持 LLaMA2/Qwen2/Qwen2.5/Qwen3/Mistral 架构（15M-500M 参数）
- 整理并修复了十余项 HF 导出与 Hailo LLM 栈的不兼容问题（docs/findings/）
- 提供 NVIDIA CUDA / AMD ROCm / Jupyter 三种 Docker 镜像

## 适用场景

- 把自己的小型 LLM 编译成 Hailo-10H 可运行的 HEF
- 在边缘设备上经 hailo-ollama 提供自有模型服务
- 研究 Hailo DFC LLM 编译流的未公开机制与限制

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: Compile **your own** small LLM into a Hailo-10H HEF and run it with
> L7: This repository documents and packages an experimental, reverse-engineered
> L61: generation config embedded in the binary) that hailo-ollama can register and

## 星数曲线

```mermaid
xychart-beta
    title "l-nmch/hailo-10h-llm-compiler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `0ed2fe8b98d1` · [字段定义](../../DATASET.md)*
