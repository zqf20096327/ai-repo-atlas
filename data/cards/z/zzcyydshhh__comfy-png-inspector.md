# zzcyydshhh/comfy-png-inspector

⭐ 16 · HTML · MIT · 推送 2026-11-03 · [GitHub](https://github.com/zzcyydshhh/comfy-png-inspector) · [官网](https://zzcyydshhh.github.io/comfy-png-inspector/) · 个人维护 · 中文 README

**解析 ComfyUI PNG 元数据，提取工作流与 LoRA 链参数的单页工具**

面向 ComfyUI 用户的本地单页应用与 CLI：解析 PNG 中的 tEXt/zTXt/iTXt chunk，提取 seed/steps/CFG/sampler、底模/CLIP/VAE、正负提示词，并从 KSampler.model 反向追踪 LoRA 链的真实执行顺序；支持原样导出 workflow JSON、CSV/JSON 参数表、zip 批量打包，以及以现有工作流为模板注入参数重建新工作流（含自检与变更清单）。同一解析核心以 DeepSeek Harness 插件形式提供 comfy_png_inspect 工具。仅支持 PNG，模板重建受模板内已有节点类限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PNG chunk 解析与 LoRA 链执行顺序追踪（区分画布节点与实际参与渲染节点）
- 提示词 link 回溯解析，标注运行时生成的槽位
- 模板重建：注入参数并重建 LoRA 链，附变更清单与自检
- 同一解析核心复用为 DSH 插件 comfy_png_inspect 与纯标准库 Python CLI

## 适用场景

- 查看某张 ComfyUI 生成图的完整参数与 LoRA 链
- 批量导出旧图的参数表或打包工作流 JSON
- 把已解析参数注入自己的模板工作流复现效果

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L17: |"How was this image made?"|Drop the PNG (or a whole `output` folder) → LoRA order and strengths, seed / steps / CF
> L39: - **DeepSeek Harness plugin**: the same parser ships as a DSH bundle exposing `comfy_png_inspect` to the model.
> L94: 2. **Chain tracing**: start at `KSampler.model` and follow `inputs.model` backwards, bucketing by node class (`Lora

## 星数曲线

```mermaid
xychart-beta
    title "zzcyydshhh/comfy-png-inspector 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-24"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-11-08 16 → 2026-11-24 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `82364bc2d133` · [字段定义](../../DATASET.md)*
