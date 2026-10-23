# rixinhahaha/snip

⭐ 347 · JavaScript · MIT · 推送 2026-05-07 · [GitHub](https://github.com/rixinhahaha/snip) · [官网](https://snipit.dev) · 个人维护

**截图标注工具，兼作 AI 编程代理的可视化输出与审核层**

基于 Electron 的 macOS/Linux 菜单栏应用：本身是完整的截图+标注工具（区域选择、矩形/箭头/文字/模糊/AI 抠图等标注），内置通过 Ollama 运行的本地视觉 LLM 为截图命名、分类、打标签并支持语义搜索。同时提供 CLI 与 MCP server，供 Claude Code、Cursor、Windsurf、Cline 等 AI 编程代理调用：代理可将 Mermaid/HTML 渲染为图供用户屏幕上标注审核，返回结构化 JSON。所有 AI 均本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 编程代理可调用 snip render 渲染 Mermaid/HTML 图表并获用户审核结果（结构化 JSON）
- Ollama 本地视觉 LLM 自动命名/分类/打标签截图，支持语义搜索与 OCR 转录
- 完整截图+标注功能（矩形/箭头/文字/模糊/AI segment）
- 提供 CLI 与 MCP server 两种接入方式

## 适用场景

- 让 Claude Code 等编程代理用图表而非文字说明架构与数据模型
- 在截图上圈画标注并反馈给 AI 代理迭代
- 用语义搜索在截图库中按内容描述查找历史截图

## 场景标签

`语义搜索` `OCR` `图像视频处理` · 领域:知识与检索

## 证据(README 行号)

> L87: Snip is a full screenshot + annotation app on its own:
> L95: AI organization uses a local vision LLM (via Ollama) to name, categorize, and tag every saved screenshot. Semantic 
> L133: Electron 33 / Fabric.js 7 / Mermaid.js 11 / Ollama (local LLM) / HuggingFace Transformers.js / SlimSAM (ONNX)

## 星数曲线

```mermaid
xychart-beta
    title "rixinhahaha/snip 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-23"]
    y-axis "stars" 345 --> 348
    line [346, 347, 347]
```

2026-10-18 346 → 2026-10-23 347（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `6d0094ac4bff` · [字段定义](../../DATASET.md)*
