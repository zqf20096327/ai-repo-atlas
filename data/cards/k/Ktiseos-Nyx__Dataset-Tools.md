# Ktiseos-Nyx/Dataset-Tools

⭐ 84 · TypeScript · GPL-3.0 · 推送 2026-11-19 · [GitHub](https://github.com/Ktiseos-Nyx/Dataset-Tools) · [官网](https://dataset-tools-three.vercel.app) · 个人维护

**查看 AI 生成图片与照片 EXIF 元数据的本地优先 Web 应用**

基于 Next.js 16/React 19 的本地优先 Web 应用，用于读取和展示 AI 生成图片（ComfyUI/A1111/Forge/NovelAI/Civitai）及普通照片中的 EXIF/IPTC/XMP 元数据。对 ComfyUI 工作流采用图遍历引擎做节点溯源与自定义节点解析（含 GitHub 代码搜索回退），支持 Safetensors 模型/LoRA 元数据提取，并可编辑 PNG 中的提示词写回磁盘。提供 Windows 独立 exe（安装版与便携版），Web 版需 Node.js 20.9+ 从源码构建运行。旧 Python 版本不再受支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ComfyUI 节点图溯源引擎 + 自定义节点 GitHub 查找回退
- Safetensors 完整元数据提取（rank/alpha/训练参数/数据集标签）
- PNG 提示词与参数编辑并写回磁盘
- Windows 独立 exe（NSIS 安装版与便携版）

## 适用场景

- 查看 AI 生成图片用了什么模型、提示词和工作流
- 检查 LoRA/模型文件的训练参数与数据集标签
- 浏览普通照片的相机 EXIF 信息

## 场景标签

 · 领域:AI 图像元数据/工具

## 证据(README 行号)

> L23: **Dataset Tools NextJS Edition** is a **local-first web application** for viewing EXIF metadata from AI-generated i
> L33: |**Metadata Parsing**|✅|Graph-tracing engine for ComfyUI, field-based detection for A1111/Forge/NovelAI.|

## 星数曲线

```mermaid
xychart-beta
    title "Ktiseos-Nyx/Dataset-Tools 星数(近 3 点)"
    x-axis ["2026-11-16", "2026-11-19", "2026-11-20"]
    y-axis "stars" 82 --> 85
    line [83, 84, 84]
```

2026-11-16 83 → 2026-11-20 84（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `35c4121e6318` · [字段定义](../../DATASET.md)*
