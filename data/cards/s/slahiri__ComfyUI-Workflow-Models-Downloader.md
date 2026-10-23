# slahiri/ComfyUI-Workflow-Models-Downloader

⭐ 154 · Python · MIT · 推送 2025-11-29 · [GitHub](https://github.com/slahiri/ComfyUI-Workflow-Models-Downloader) · [官网](https://registry.comfy.org/publishers/slahiri/nodes/comfyui-workflow-models-downloader) · 个人维护

**ComfyUI 扩展：扫描工作流并下载缺失模型**

面向 ComfyUI 用户的自定义节点扩展：扫描当前工作流引用的模型，从工作流元数据、热门模型注册表、ComfyUI Manager 列表及 HuggingFace/CivitAI API 检索下载链接，支持一键下载、后台下载、aria2 加速与并行下载队列。另提供本地模型浏览器（未使用模型识别、用量追踪）、直接 URL 下载、模糊匹配（70% 阈值）与基于 Tavily 的模型来源搜索。支持 Checkpoints、LoRA、ControlNet 等多种模型类型，门控模型需配置 API key。

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

- 扫描工作流自动检测缺失模型并多源检索下载 URL
- 本地模型浏览器含未使用模型识别与全工作流用量追踪
- aria2 加速下载与 0-50 并行下载队列
- GGUF/fp16/量化变体自动检测与模糊匹配（70% 置信阈值）

## 适用场景

- 导入他人工作流后批量补齐缺失模型
- 整理本地模型库并找出未被任何工作流使用的模型
- 为来源未知的模型通过 Tavily 搜索下载源

## 场景标签

 · 领域:AI 工具链/模型管理

## 证据(README 行号)

> L8: A powerful ComfyUI extension that automatically detects models in your workflow and helps download missing ones from
> L63: - **Auto-detect models** - Scans your active workflow for all model references
> L91: Search for "Workflow Models Downloader" in ComfyUI Manager and click Install.

## 星数曲线

```mermaid
xychart-beta
    title "slahiri/ComfyUI-Workflow-Models-Downloader 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 152 --> 155
    line [153, 154]
```

2026-10-18 153 → 2026-10-23 154（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `1b4d9f0648bf` · [字段定义](../../DATASET.md)*
