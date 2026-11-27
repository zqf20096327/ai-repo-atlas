# PedroMarinhoDev/ComfyUI-KandinskySR

⭐ 7 · Python · GPL-3.0 · 推送 2026-11-26 · [GitHub](https://github.com/PedroMarinhoDev/ComfyUI-KandinskySR) · [官网](https://huggingface.co/PedroMarinhoDev/Kandinsky-SR-ComfyUI) · 个人维护

**在 ComfyUI 内原生运行 Kandinsky 视频/图像超分辨率**

将 kandinskylab 的 Kandinsky 6.0 Video SR 2.0 与 ImageSR 2.0 以 ComfyUI 自定义节点形式接入 ComfyUI，提供视频 x2/x2.25/x4 与图像 x2/x4 放大。视频采用 2-step 蒸馏扩散 transformer、3D VAE 与 latent upscaler，长片段按重叠窗口分块处理，内存不随片长增长；提供自定义 attention/norm/decode CUDA+Triton 内核、bf16 与 int8 ConvRot 权重、可选双 GPU 分块。经 ComfyUI Manager/CLI/git 安装，模型文件从 Hugging Face 下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频任意长度：重叠窗口分块，内存不随片长增长
- bf16 与 int8 ConvRot 两种精度权重，自定义 CUDA+Triton 内核
- second_gpu 选项让第二块显卡处理下一个分块
- 四个节点，含视频/图像示例 workflow 与模板浏览器入口

## 适用场景

- 在 ComfyUI 中把低分辨率视频放大到 1080p/4K
- 批量放大图像并获得全尺寸输出
- 在单卡显存有限时用 int8 权重降低 VRAM 占用

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **ComfyUI-KandinskySR** runs kandinskylab's Kandinsky 6.0 Video Super-Resolution 2.0 and Kandinsky ImageSR 2.0
> L110: Video runs a 2-step pi-Flow distilled diffusion transformer with NABLA sparse attention, the KVAE 3D video VAE and
> L118: - **Kandinsky Video SR Upscale:** a video (or images) in, a video file out, with the source's audio and frame rate


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `6603e3030e67` · [字段定义](../../DATASET.md)*
