# iamNCJ/RenderFormer-Studio

⭐ 40 · Python · MIT · 推送 2026-09-09 · [GitHub](https://github.com/iamNCJ/RenderFormer-Studio) · [官网](https://renderformer.github.io/v2/) · 组织维护

**RenderFormer/V2 神经渲染官方实现：数据生成、训练与推理一体化**

RenderFormer（SIGGRAPH 2025）与 RenderFormer-V2（ECCV 2026）的官方代码仓库，统一两代模型的场景数据准备、模型定义、训练配方与推理管线，通过单一 renderformer CLI 提供分阶段编号的工作流和可复现的机器可读回执。V1 场景可由 JSON 描述在 CPU 上组合生成，V2 场景需经 Blender/Cycles 生成并后处理为 H5；推理从 Hugging Face 加载发布模型（含 microsoft 官方 V1 检查点），支持 Python API 调用。CUDA 12.6 训练/推理与 Blender 数据生成使用相互独立的 Conda 环境，V2 打包序列依赖 flash-attn。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- V1/V2 共享一套模型实现，单一 CLI 覆盖 data/train/infer
- Hugging Face 发布多个检查点，含组件化 V2 仓库
- V1 场景可纯 CPU 由 JSON 组合，无需 Blender 与 GPU
- Blender 扩展源码包可从 Blender UI 导出场景

## 适用场景

- 用发布模型对自定义场景做神经渲染出图
- 复现或微调 RenderFormer/V2 模型
- 生成并后处理训练用场景 H5 数据

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L44: RenderFormer Studio unifies the maintained public implementation of both
> L196: Both the pipelines and the `renderformer infer` command consume a scene H5

## 星数曲线

```mermaid
xychart-beta
    title "iamNCJ/RenderFormer-Studio 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24", "2026-10-25"]
    y-axis "stars" 36 --> 40
    line [37, 38, 39, 39]
```

2026-10-18 37 → 2026-10-25 39（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `debea2acf6fd` · [字段定义](../../DATASET.md)*
