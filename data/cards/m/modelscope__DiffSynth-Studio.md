# modelscope/DiffSynth-Studio

⭐ 13,442 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/modelscope/DiffSynth-Studio) · 组织维护 · 中文 README

**为开发者提供扩散模型推理与训练的开源引擎**

ModelScope 社区团队维护的扩散模型引擎，集成主流开源扩散模型，覆盖图像生成、视频生成、音频生成与画质评估。框架提供显存管理（参数在磁盘/内存/显存间动态调度）、NF4/INT8 量化、几乎全模型的训练支持（基模型/LoRA/Adapter）与基于计算图的分阶段训练。支持多 GPU 并行推理；开发人力有限，旧版本功能不再维护需回退历史版本。可通过 PyPI 安装，并有 ComfyUI 节点包与 WebUI 训练工具等衍生项目。

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

## 动量与使用信号

- 维护:`active` — 距上次 push 1.9 天,年发版 1,69 位贡献者
- 涨星:近 1 天 **+3**(自 20261016 起算)
- 平台:WEB · 协议:—

## 能力要点

- 集成图像/视频/音频生成与画质评估类扩散模型
- 显存动态调度使低显存消费级 GPU 可运行大模型
- NF4/INT8 等量化降低推理与 LoRA 训练显存需求
- 支持多 GPU 并行推理与计算图拆分训练

## 适用场景

- 在消费级 GPU 上运行大型扩散模型推理
- 训练或微调 LoRA / Adapter 模型
- 在 ComfyUI 中搭建扩散模型工作流

## 场景标签

`图像生成` `视频生成` `微调` `模型量化` · 领域:内容生成

## 证据(README 行号)

> L16: Welcome to the magical world of Diffusion models! DiffSynth-Studio is an open-source Diffusion model engine develop
> L20: * Model Support: The framework integrates mainstream open-source Diffusion models, covering image generation, video
> L21: * VRAM Management: Dynamically schedules model parameters across disk, memory, and VRAM, allowing consumer-grade GP

## 星数曲线

```mermaid
xychart-beta
    title "modelscope/DiffSynth-Studio 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 13282 --> 13456
    line [13296, 13299, 13302, 13305, 13313, 13318, 13324, 13325, 13332, 13333, 13299, 13351, 13354, 13360, 13363, 13364, 13367, 13368, 13373, 13378, 13385, 13411, 13422, 13424, 13429, 13438, 13442]
```

2026-10-24 13,296 → 2026-11-26 13,442（+146）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `7d69506fd7e8` · [字段定义](../../DATASET.md)*
