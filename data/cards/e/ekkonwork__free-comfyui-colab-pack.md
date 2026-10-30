# ekkonwork/free-comfyui-colab-pack

⭐ 18 · Jupyter Notebook · NOASSERTION · 推送 2026-10-06 · [GitHub](https://github.com/ekkonwork/free-comfyui-colab-pack) · 个人维护

**免费 Colab 上运行热门 ComfyUI 工作流的笔记本合集**

面向 Google Colab 免费 T4 显卡的 ComfyUI 笔记本集合，收录 Flux SRPO、Flux2 Klein、Z-Image、Qwen Image、Chroma1、Anima/Illustrious 系列等约 14 个工作流。每个笔记本自动安装 ComfyUI、下载对应 GGUF/权重并注入一个捆绑 workflow；按 VRAM 预算自动选量化档，内置 Hugging Face/Civitai token 提示与 Cloudflare 隧道启动逻辑。部分笔记本（ltx2、wan22）暂停维护。使用方式：在 Colab 打开笔记本顺序运行单元格。

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

- 约 14 个针对 Colab 免费 T4 调优的 ComfyUI 笔记本，每台自动安装捆绑 workflow
- 按 VRAM 预算自动选择 GGUF 量化档，含 --novram 超低显存模式
- 内置 Hugging Face / Civitai token 提示与带重试健康检查的 Cloudflare 隧道
- 安装 ComfyUI-Manager 与 Workflow Models Downloader 自定义节点

## 适用场景

- 没有本地 GPU 时在 Colab 免费跑文生图/图像编辑工作流
- 低显存环境下用 GGUF 量化运行 Flux/Z-Image/Qwen Image 等模型
- 对比多个动漫系 SDXL/Illustrious 模型的出图效果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L8: Free Google Colab notebooks for popular ComfyUI workflows on low VRAM GPUs (focused on Colab Free T4).
> L24: - Every supported notebook installs exactly one bundled workflow into ComfyUI automatically.

## 星数曲线

```mermaid
xychart-beta
    title "ekkonwork/free-comfyui-colab-pack 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `8d6ab421a38f` · [字段定义](../../DATASET.md)*
