# T8mars/Comfyui-Flux3-PE-GGUF-T8

⭐ 5 · Python · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/T8mars/Comfyui-Flux3-PE-GGUF-T8) · [官网](https://huggingface.co/t8star/Flux3-PE-GGUF-Comfy) · 组织维护 · 中文 README

**ComfyUI 本地 FLUX 3 提示词增强节点，支持参考图与布局**

面向 ComfyUI 的自定义节点：以 Q4_K_M GGUF 格式的 FLUX 3 Image Klein PUP 模型在本地运行，将简短请求、最多 10 张参考图与布局框转换为详细提示词，输出 STRING 供文本编码器使用。支持 llama-cpp-python 进程内推理或可选的 llama-server 预编译后端（Windows x64/CUDA），模型文件与运行均在本地，不上传提示词与参考图。提供四种示例工作流与缓存、恢复机制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 最多 10 张参考图输入，支持图像顺序与锁定对象框
- 归一化坐标布局输入（新增/移除对象的 bbox 描述）
- 双后端：llama-cpp-python 进程内推理或可选 llama-server 预编译运行时
- 结果缓存与最多一次恢复尝试，details_json 报告计时信息

## 适用场景

- 在 ComfyUI 中将简短描述扩写为 FLUX 3 详细提示词
- 基于参考图生成图像编辑指令
- 用布局框控制画面元素位置的工作流

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L5: Local prompt enhancement for ComfyUI, powered by Black Forest Labs' **FLUX 3 Image Klein PUP** and a **Q4_K_M GGUF**
> L13: - Text enhancement, reference-image editing instructions and both layout modes.
> L60: **Backend selection:** `auto` prefers a compatible installed Python wheel and otherwise uses the packaged server if

## 星数曲线

```mermaid
xychart-beta
    title "T8mars/Comfyui-Flux3-PE-GGUF-T8 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-11-24"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-22 5 → 2026-11-24 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `663881be2814` · [字段定义](../../DATASET.md)*
