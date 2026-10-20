# modelscope/DiffSynth-Studio

⭐ 13,259 · Python · Apache-2.0 · 推送 2026-10-16 · [GitHub](https://github.com/modelscope/DiffSynth-Studio) · 组织维护 · 中文 README

**为开发者提供的开源 Diffusion 模型推理与训练引擎**

由 ModelScope 社区团队维护的 Diffusion 模型引擎，集成图像生成、视频生成、音频生成与图像质量评估类开源模型。框架提供跨磁盘/内存/显存的动态参数调度，使低显存消费级 GPU 可运行大模型推理；支持 NF4、INT8 等量化以降低推理与 LoRA 训练的显存需求；推理支持的模型基本均可训练，训练过程可拆分为两阶段。相关派生项目包括 ComfyUI 节点包与 LoRA 训练 WebUI。README 说明开发人力有限，旧版本功能不再维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
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

- 集成图像/视频/音频生成与图像质量评估模型
- 跨磁盘、内存、显存的动态参数调度，低显存 GPU 可推理大模型
- NF4/INT8 等量化后端（含自研 EntroPack 压缩库）
- 提供 Agent Skills 用于自动化模型集成流程

## 适用场景

- 在消费级 GPU 上运行大参数量扩散模型的推理与 LoRA 训练
- 通过 ComfyUI 节点搭建扩散模型工作流
- 对音乐、视频、图像生成模型做量化与低显存部署

## 场景标签

`图像生成` `视频生成` `微调` `模型量化` · 领域:内容生成

## 证据(README 行号)

> L16: Welcome to the magical world of Diffusion models! DiffSynth-Studio is an open-source Diffusion model engine develop
> L20: * Model Support: The framework integrates mainstream open-source Diffusion models, covering image generation, video
> L21: * VRAM Management: Dynamically schedules model parameters across disk, memory, and VRAM, allowing consumer-grade GP

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `5720e9a8cadf` · [字段定义](../../DATASET.md)*
