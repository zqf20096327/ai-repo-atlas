# The-Focus-AI/nano-banana-cli

⭐ 20 · TypeScript · 推送 2026-07-07 · [GitHub](https://github.com/The-Focus-AI/nano-banana-cli) · 组织维护

**调 Gemini API 做 AI 图像生成/编辑的 CLI 与 Claude 插件**

基于 Node.js 的命令行工具，调用 Google Gemini 与 Veo API 完成图像生成、图像编辑（传入已有图片加提示词修改）与视频生成，支持自定义提示词、批处理（附 Makefile，可批量处理幻灯片照片等）以及 EXIF 相关处理。以 npx 直接运行或 npm 全局安装，需设置 GEMINI_API_KEY。同时打包为 Claude Code 插件，提供 nano-banana-imagegen 技能，使 Claude 在对话中自动调用 CLI 生成和编辑图片。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本提示生成图像、传文件编辑现有图像、视频生成
- Makefile 批处理多图（示例为幻灯片照片提取）
- 附 Claude Code 插件与 prompting-guide 技能文档

## 适用场景

- 命令行批量生成或编辑图片素材
- 把幻灯片照片批量转成干净图像
- 在 Claude Code 对话中直接生成和修改图片

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: CLI and Claude Code plugin for AI image generation, editing, and video generation with Google Gemini and Veo.
> L73: Edit existing images by providing an input file:
> L84: This package includes a Claude Code plugin with the `nano-banana-imagegen` skill. When installed, Claude can genera

## 星数曲线

```mermaid
xychart-beta
    title "The-Focus-AI/nano-banana-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `35d346a6547d` · [字段定义](../../DATASET.md)*
