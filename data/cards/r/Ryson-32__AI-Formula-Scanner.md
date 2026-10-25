# Ryson-32/AI-Formula-Scanner

⭐ 67 · Svelte · Apache-2.0 · 推送 2026-06-14 · [GitHub](https://github.com/Ryson-32/AI-Formula-Scanner) · 个人维护 · 中文 README

**Windows 桌面公式 OCR 工具：识别图像公式为 LaTeX 并分析管理**

基于 Tauri + Rust + SvelteKit 的桌面应用，面向科研写作、教材排版、笔记整理等场景。通过 3 次 LLM 调用完成三阶段流水线：从截图或导入图片提取 LaTeX、生成标题/摘要/变量表/术语表与建议、以及带置信度（0-100）的校验比对。识别记录本地保存，支持搜索、排序、收藏。目前仅支持 Google Gemini API，需在设置中填入 API Key；仅面向 Windows 平台，从源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三阶段流水线：LaTeX 提取 → 智能分析 → 置信度校验（ok/warning/error 与覆盖率）
- 截图快捷键（Ctrl+Shift+A）或导入 PNG/JPG 识别，阶段失败可单独重试
- 生成标题、摘要、变量表（符号/单位）、术语表与建议
- 识别记录本地存储，支持搜索、排序、收藏与详情抽屉

## 适用场景

- 科研写作时把图片公式快速转成 LaTeX
- 课堂或会议照片中的公式快速转录
- 整理学习笔记并查阅变量含义与术语解释

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L37: 1. **LaTeX Extraction**: Extract LaTeX text from image only

## 星数曲线

```mermaid
xychart-beta
    title "Ryson-32/AI-Formula-Scanner 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 66 --> 69
    line [68, 67, 67]
```

2026-10-18 68 → 2026-10-25 67（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `be734805fde4` · [字段定义](../../DATASET.md)*
