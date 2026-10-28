# NeuroBrix/neurobrix

⭐ 49 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/NeuroBrix/neurobrix) · [官网](https://neurobrix.es) · 组织维护

**多模态模型推理引擎：一种容器格式运行语言/语音/图像/视频模型**

面向希望在自有 GPU/CPU 上运行已发布模型的开发者的开源推理引擎。模型以 .nbx 容器分发（含计算图、权重、拓扑与运行时默认值），同一运行时通过少量通用执行流程（自回归解码、迭代去噪、编码器-解码器等）运行 LLM、视觉语言、语音识别/合成、图像/视频生成与超分模型。提供 PyTorch（ATen/cuDNN/cuBLAS）与自研 Triton 两条计算分支；硬件放置由引擎根据设备与内存自动规划，可多卡、显存流式与主机内存卸载。当前 0.5.4 支持 NVIDIA GPU（Linux/CUDA）与 x86-64 CPU，Apple Silicon 计划 0.5.5，AMD/Windows 未支持。通过 pip 安装，模型从 NeuroBrix Hub 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 .nbx 容器格式与 CLI 覆盖 10 类模型（LLM/VLM/STT/TTS/图像与视频生成/超分等）
- PyTorch 与 Triton 两条独立计算分支可互相对照验证
- 放置由引擎自动规划：多卡、显存流式、主机内存卸载，--explain-plan 可查看计划
- 请求无法容纳时明确报错给出所需/可用资源数字，而非静默降级

## 适用场景

- 在自有 NVIDIA GPU 或 CPU 上本地运行 LLM、语音与视频生成等各类模型，免去逐模型管线维护
- 跨多个模型家族统一用一套命令行工具做推理与服务
- 通过双计算分支交叉验证推理结果

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: NeuroBrix is an open-source inference engine that runs AI models (language models,
> L6: It is for developers who want to run these models on their own GPUs or CPUs without
> L33: - **Two independent compute branches over the same container.** The default branch runs

## 星数曲线

```mermaid
xychart-beta
    title "NeuroBrix/neurobrix 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-28 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `72afef5ce4d5` · [字段定义](../../DATASET.md)*
