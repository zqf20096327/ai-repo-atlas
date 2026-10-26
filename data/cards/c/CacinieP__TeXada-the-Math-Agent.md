# CacinieP/TeXada-the-Math-Agent

⭐ 40 · Python · AGPL-3.0 · 推送 2026-10-22 · [GitHub](https://github.com/CacinieP/TeXada-the-Math-Agent) · 个人维护 · 中文 README

**本地数学公式转 LaTeX 的桌面 AI 代理：自然语言/图片/残缺 TeX→有效 LaTeX**

面向终端用户的桌面应用，将自然语言描述、截图/手写公式或残缺 TeX 转换为可预览、可复制的 LaTeX。采用双模型角色（规划/文本与视觉 OCR），内置 llama-server 后端默认使用 MiniCPM-V-4.7-1B 单一检查点承担两角色，也可配置本地 Ollama 或 OpenAI 兼容端点。六个确定性 TeX 工具负责解析、编译、修复、语义 diff、渲染与导出，Agent 只做规划不做修复。产品范围明确排除计算、求解与证明，仅保留表达式转写；候选直接提交且编译不保证转写正确。macOS/Windows 提供安装包，模型权重安装后单独下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言/图像 OCR/残缺 TeX 三种输入统一到同一 Agent 运行时
- 六个独立可测试的确定性 TeX 工具（解析/编译/修复/语义diff/渲染/导出）
- 内置 llama-server 本地后端，单一 MiniCPM-V-4.7-1B 检查点兼任文本与 OCR
- macOS DMG 与 Windows NSIS 安装包，含历史记录与运行日志

## 适用场景

- 把口头描述的公式转成可复制的 LaTeX
- 从截图或手写公式 OCR 提取 LaTeX
- 修复残缺的 TeX 表达式并预览渲染结果
- 在其他应用光标处一键输入生成的公式

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L15:  Recognize, transcribe and typeset math formulas locally.
> L33: TeXada helps transcribe formulas into LaTeX. Describe notation in
> L39: TeXada is a local tool for formula recognition, transcription and typesetting.

## 星数曲线

```mermaid
xychart-beta
    title "CacinieP/TeXada-the-Math-Agent 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-26"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-22 40 → 2026-10-26 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1d42106b7e97` · [字段定义](../../DATASET.md)*
