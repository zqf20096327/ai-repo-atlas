# sophgo/LLM-TPU

⭐ 318 · C++ · NOASSERTION · 推送 2026-10-12 · [GitHub](https://github.com/sophgo/LLM-TPU) · 组织维护 · 中文 README

**在 SOPHGO TPU 芯片上一键部署主流 LLM/VLM 的开源工程**

由 SOPHGO 官方维护的模型部署仓库：通过 llm_convert.py（依赖 TPU-MLIR 环境）将 HuggingFace/GGUF 权重编译为量化 bmodel，再以 Python/C++ demo 在 BM1684X / BM1688 / CV186X TPU 上运行推理。覆盖 Qwen、Llama、DeepSeek、InternVL、MiniCPM、ChatGLM 等数十个模型家族及多模态（图像/视频/音频/TTS/嵌入/重排），支持动态编译、KV Cache 历史、多芯片并行、模型加密。也提供免编译的预编译 bmodel 下载；旧流程 demo 移入 legacy 目录不再维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- llm_convert.py 一键将 HuggingFace 权重编译为 bmodel
- 覆盖 LLM/VLM/音频/嵌入/重排数十个模型家族，Python+C++ 双语 demo
- 动态编译、分块 KV Cache、多芯片并行、bmodel 加密等进阶特性
- 提供预编译 bmodel，无需本地编译即可运行

## 适用场景

- 在算能 TPU 开发板上运行 Qwen/DeepSeek 等开源模型
- 将 HuggingFace 量化权重量化编译为 bmodel 部署
- 多芯片并行运行 32B 级模型

## 场景标签

 · 领域:AI 推理硬件/模型部署

## 证据(README 行号)

> L49: **LLM-TPU** is an open-source project officially maintained by SOPHGO, dedicated to deploying mainstream **generati
> L51:  LLM-TPU deployment pipeline: HuggingFace / GGUF weights compiled to a quantized bmodel by llm_convert.py (tpu-mlir

## 星数曲线

```mermaid
xychart-beta
    title "sophgo/LLM-TPU 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 314 --> 317
    line [315, 316, 316]
```

2026-10-18 315 → 2026-10-21 316（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `e10b90bbb572` · [字段定义](../../DATASET.md)*
