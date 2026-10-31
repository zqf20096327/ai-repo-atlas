# chickadee-project/chickadee_studio

⭐ 16 · Python · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/chickadee-project/chickadee_studio) · 组织维护

**检测公共网站隐藏广告的桌面应用：OCR+本地ML+DOM分析**

面向公共部门网站内容审查的 Electron 桌面应用：用 Playwright/Chromium 采集页面、帖文、评论与图片，结合 Unicode/DOM/CSS 分析识别形近字符替换、拆分韩文字母、透明文字与屏幕外内容等隐匿手法；图片内韩文文字与位置用 PaddleOCR 提取，页面与 OCR 文本的广告语境由 TF-IDF、随机森林与 Laya 模型在本地 CPU 上判定，可选接入 GPT、Claude、Groq 复核。结果可查看原文、截图与检测证据并导出 JSON/CSV。Windows 发布包内置 Python 引擎与模型，无需单独安装 Python 或 GPU；界面为韩语。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 扫描页面文本、帖文、评论、iframe 与图片内文字
- 检测形近字符、拆分韩文字母、透明文字等隐匿手法
- PaddleOCR 韩文识别与坐标框；RF/Laya 模型本地 CPU 分析
- 可选 GPT/Claude/Groq 复核，结果导出 JSON/CSV 与报告

## 适用场景

- 审查公共部门网站帖文与评论中的疑似广告
- 核查图片内隐藏的韩文广告文字
- 将模型评分与原文证据一并复核并导出审查结果

## 场景标签

`网页抓取` `OCR` · 领域:效率与自动化

## 证据(README 行号)

> L15: Chickadee Studio is a desktop app for reviewing suspected advertising in posts, comments and images on public-secto
> L20: - **Context analysis**: RF and Laya models on the local CPU, with optional AI Model(GPT, Claude, Groq) review
> L67: |Local context analysis|Advertising context in page and OCR text|TF-IDF, Random Forest, Laya|

## 星数曲线

```mermaid
xychart-beta
    title "chickadee-project/chickadee_studio 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-28 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `f8b3850dcfde` · [字段定义](../../DATASET.md)*
