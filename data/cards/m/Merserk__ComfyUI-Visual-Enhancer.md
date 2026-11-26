# Merserk/ComfyUI-Visual-Enhancer

⭐ 3 · Python · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/Merserk/ComfyUI-Visual-Enhancer) · [官网](https://visualenhancer.merserk.com) · 个人维护

**ComfyUI 自定义节点：接入 Visual Enhancer 做图像视频增强**

为 ComfyUI 提供 Visual Enhancer（VE_CLI.exe 命令行工具）的官方集成节点集，安装后按 git clone 源码方式放入 custom_nodes 目录即可使用。免费节点包括 DLSS 5 神经渲染、DLSS 超分/光线重建、RTX 视频超分与 HDR、DLSS/FSR 3 帧生成、LUT 调色、锐化、颗粒合成等；去噪、去模糊、AI 超分与帧插值节点标记为 (Paid)，需通过桌面应用登录有效的 Visual Enhancer 许可证。Connection 节点自动探测 VE_CLI.exe 路径并选择目标 GPU。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DLSS 5 神经渲染、DLSS 超分/光线重建、RTX 视频超分与 HDR 转换节点
- DLSS 与 FSR 3 帧生成、场景切割检测的视频帧生成节点
- 3D .cube LUT 加载与参数化调色、AMD CAS/NVIDIA NIS 锐化
- 22 个内置示例工作流自动出现在 ComfyUI 模板中

## 适用场景

- 在 ComfyUI 工作流中对图像和视频做超分辨率放大
- 为视频生成插帧提升到目标帧率
- 对素材做 HDR 转换、调色与颗粒效果处理
- 需要许可证时调用 AI 去噪、去模糊与插值节点

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Official ComfyUI integration for **Visual Enhancer** (`VE_CLI.exe`).
> L62: > Listed at the bottom of the node menu. Requires an active Visual Enhancer license signed in via the desktop app.
> L66: |**Denoising (Paid)**|`Image` / `Video`|**ClearMagnetar** AI Denoising with optional Noise Adaptation translator.|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4e1f16b8ba87` · [字段定义](../../DATASET.md)*
