# giriss/comfy-image-saver

⭐ 348 · Python · MIT · 推送 2026-07-17 · [GitHub](https://github.com/giriss/comfy-image-saver) · 个人维护

**ComfyUI 保存图像及生成元数据的自定义节点**

为 ComfyUI 提供的自定义节点集合：保存 png/jpeg/webp 格式图像时同时写入生成元数据，兼容 Civitai 与 Prompthero 的 geninfo 自动检测，便于将图像上传后自动生成元数据。附带示例工作流文件 example-workflow.json。安装途径为 ComfyUI-Manager 搜索安装，或 git clone 到 custom_nodes 目录后 pip 安装依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 保存图像时写入生成元数据，支持 png/jpeg/webp
- 兼容 Civitai 与 Prompthero geninfo 自动检测
- 提供示例工作流文件 example-workflow.json
- 支持通过 ComfyUI-Manager 安装

## 适用场景

- 在 ComfyUI 中保存带完整生成参数的图像
- 上传图像到 Civitai/Prompthero 时自动带上元数据

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: All the tools you need to save images with their **generation metadata** on ComfyUI. Compatible with *Civitai* & *Pr
> L12: If you have *ComfyUI-Manager*, you can simply search "**Save Image with Generation Metadata**" and install these cu

## 星数曲线

```mermaid
xychart-beta
    title "giriss/comfy-image-saver 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 346 --> 349
    line [347, 348, 348]
```

2026-10-18 347 → 2026-10-28 348（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `5745e50b25e2` · [字段定义](../../DATASET.md)*
