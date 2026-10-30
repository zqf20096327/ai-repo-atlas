# T8mars/Comfyui-SenseNova-U1.5-Wrapper-T8

⭐ 25 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/T8mars/Comfyui-SenseNova-U1.5-Wrapper-T8) · [官网](https://registry.comfy.org/nodes/sensenova-u15-t8) · 个人维护 · 中文 README

**SenseNova U1.5 图像生成/多参考图编辑的 ComfyUI 原生节点**

为 SenseNova U1.5 图像模型提供 ComfyUI 原生节点：模型加载、采样、调度、显存卸载均走 ComfyUI 管道，支持文生图、thinking 文生图、文本/图片交错生成、单图与 1～10 张参考图编辑、批量生成（batch_size 2～16）。提供 Final/SFT 两套官方权重及五种 GGUF 量化权重加载，支持官方 8-step LoRA，执行期内做 prefix KV cache。只读取本地模型，运行时不联网下载。实机验证范围为 NVIDIA CUDA + BF16（RTX 5090 Laptop 24 GB、64 GB 内存），FP16/ROCm/MPS 等暂未验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文生图、thinking 文生图、文本/图片交错生成、1～10 张参考图编辑
- Final/SFT 官方权重及 Q2_K～Q8_0 五种 GGUF 量化加载，含 SHA256/tensor 严格校验
- 官方 8-step LoRA 走 ComfyUI 原生 LoRA/ModelPatcher 管道
- 采样任务内文字/参考图 prefix KV cache，批量时 KV 按分支复用

## 适用场景

- 在 ComfyUI 中本地运行 SenseNova U1.5 进行文生图与图像编辑
- 人物换装等多参考图编辑与结构化编辑提示词
- 低显存设备用 GGUF 量化权重生成图像
- 同一提示词批量生成多个不同结果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L9: 这是 SenseNova-U1.5 的 ComfyUI 原生节点。模型、采样器、调度器、显存卸载和工作流都走 ComfyUI 管道，支持：
> L25: 节点只读取本地模型，运行时不会联网下载文件。
> L318: - 实机 ComfyUI `v0.33.x`

## 星数曲线

```mermaid
xychart-beta
    title "T8mars/Comfyui-SenseNova-U1.5-Wrapper-T8 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 23 --> 26
    line [24, 25, 25]
```

2026-10-18 24 → 2026-10-30 25（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `4a7e7c1125e6` · [字段定义](../../DATASET.md)*
