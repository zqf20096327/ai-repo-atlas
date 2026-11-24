# zeitmaschinen/GalleryFlow

⭐ 39 · TypeScript · NOASSERTION · 推送 2026-11-04 · [GitHub](https://github.com/zeitmaschinen/GalleryFlow) · 个人维护

**自托管 ComfyUI 图片画廊：浏览并检视生成图的提示词与工作流元数据**

面向 ComfyUI 用户的自托管 Web 画廊与元数据检视器：连接到 ComfyUI 输出文件夹后，可浏览含子文件夹的全部图片，从 PNG 元数据中读取提示词、负向提示词、模型、LoRA、seed、steps、CFG、采样器等信息，并以带颜色编码的节点可视化完整 ComfyUI 工作流，支持复制工作流 JSON 与一键复制提示词。前端 React 18 + TypeScript，后端 FastAPI + Python 3.11+，通过 git clone 后分别 pip/npm 安装依赖，用 python 脚本同时启动前后端。许可证为 CC BY-NC 4.0（非商业）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 PNG 元数据读取 prompt、模型、LoRA、seed、CFG、采样器等生成参数
- 以颜色编码节点可视化每张图片的完整 ComfyUI 工作流，可复制工作流 JSON
- 保持图片原始比例的瀑布式画廊、全屏浏览与键盘导航
- 按子文件夹、文件名或日期排序，按文件类型过滤

## 适用场景

- 管理大量 ComfyUI 生成图片并快速检索特定提示词或模型
- 查看某张图对应的完整工作流节点以便复现
- 对比不同 LoRA、seed 与采样参数下的生成结果

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L3: A self-hosted ComfyUI image gallery and metadata viewer for browsing, sorting and managing your ComfyUI-generated AI
> L5: Connect GalleryFlow to your ComfyUI output folder to instantly sort and filter your images, read prompts, seeds, mod
> L25: - 📋 Generation details for each image: prompt, negative prompt, model, seed, steps, CFG, sampler, scheduler, LoRAs

## 星数曲线

```mermaid
xychart-beta
    title "zeitmaschinen/GalleryFlow 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-19", "2026-11-24"]
    y-axis "stars" 37 --> 40
    line [38, 39, 39]
```

2026-11-08 38 → 2026-11-24 39（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 mid · 依据 README sha `ce4bfebc9d54` · [字段定义](../../DATASET.md)*
