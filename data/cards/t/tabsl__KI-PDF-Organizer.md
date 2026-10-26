# tabsl/KI-PDF-Organizer

⭐ 27 · Python · MIT · 推送 2026-05-27 · [GitHub](https://github.com/tabsl/KI-PDF-Organizer) · 个人维护 · 中文 README

**用 AI 自动重命名、拆分、排序和校验 PDF 文件的命令行工具**

Python 命令行脚本集合，面向个人文档整理场景：调用 OpenAI、Anthropic 云端 API 或本地 Ollama 生成结构化文件名（日期+发件人+文档类型）、识别扫描堆叠 PDF 中的文档边界并拆分为单页命名文档、用 KI 归一化发件人与文档类型后按多种策略分文件夹排序。另含 SHA256/文件名/大小三种查重、文件校验和 JPG/PNG 转 OCR 可搜索 PDF。OCR 依赖 Tesseract；使用云端 API 会将 PDF 前 1000 字符发送给第三方，README 建议敏感数据用本地 Ollama。通过 git clone 与 setup.sh 安装，各项功能以 shell 脚本调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- KI 生成结构化文件名（日期+发件人+文档类型），支持 OpenAI/Anthropic/Ollama 本地三种 provider
- 逐页 AI 判定文档边界，将堆叠扫描 PDF 拆分为命名单文档
- KI 归一化发件人与文档类型后按 sender/year/type 等策略排序，支持 custom 文件夹由 KI 选择
- OCR 回退机制：文本层不足时自动调用 Tesseract；JPG/PNG 可转为可搜索 PDF

## 适用场景

- 批量整理多年积累的扫描账单、合同等 PDF 档案
- 把多份文档扫成的一个 PDF 拆回独立命名文件
- 敏感文档在本地 Ollama 上完成整理，避免数据外发
- 找出重复和无效 PDF，统一命名为日期前缀格式

## 场景标签

 · 领域:文档管理/文件自动化

## 证据(README 行号)

> L3: Ein Python-Script zum automatischen Organisieren von PDF-Dateien. Das Tool nutzt KI (OpenAI, Anthropic oder Ollama l
> L11: - 🤖 **KI-basierte Dateinamensgenerierung** mit OpenAI, Anthropic oder Ollama (lokal)

## 星数曲线

```mermaid
xychart-beta
    title "tabsl/KI-PDF-Organizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `b7a49531d829` · [字段定义](../../DATASET.md)*
