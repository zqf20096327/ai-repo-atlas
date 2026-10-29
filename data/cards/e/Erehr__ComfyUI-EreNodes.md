# Erehr/ComfyUI-EreNodes

⭐ 83 · JavaScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Erehr/ComfyUI-EreNodes) · 个人维护

**ComfyUI 提示词管理节点集：可切换标签、标签库与 booru 浏览器**

面向 ComfyUI 用户的提示词构建节点包：以可切换、可拖拽的标签（pill）组装提示词，提供 Cloud/Toggle/MultiSelect/Gallery/Randomizer/Multiline 等多种节点并可互相转换，Prompt Composer 将角色、服装等分类折叠到单节点。内置 Danbooru/e621 标签自动补全、侧边栏管理标签组/LoRA/嵌入、Safebooru/Gelbooru/e621 图片标签浏览，以及从提示词中应用 <lora:...> 的 LoRA 加载器和从生成图片反提取提示词的节点。通过 ComfyUI Manager 或 git clone 到 custom_nodes 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标签以 pill 形式选择、拖拽、跨节点复用，标签/文本/LoRA/嵌入/标签组统一为 pill
- Danbooru/e621 标签自动补全，含 artist:/char:/lora: 等过滤与预览
- 侧边栏可搜索 booru（Safebooru/Gelbooru/e621）并将标签拖入提示词
- Prompt Extractor 从生成图片反提取正向提示词为 pill

## 适用场景

- 用可切换标签快速搭建与调整文生图提示词
- 保存角色/画风标签组复用到不同工作流
- 浏览 booru 图片并把标签直接拖入提示词

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L4: **Tag-based prompting for ComfyUI.** Build prompts from pills you can toggle, drag and reuse, with a built-in prompt
> L79: All nodes work in the classic canvas and in Nodes 2.0, and inside subgraphs.

## 星数曲线

```mermaid
xychart-beta
    title "Erehr/ComfyUI-EreNodes 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-29"]
    y-axis "stars" 81 --> 84
    line [82, 83, 83]
```

2026-10-18 82 → 2026-10-29 83（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `86076aa6f7d3` · [字段定义](../../DATASET.md)*
