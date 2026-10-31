# VeryMath/VeryMath-textbook-copilot

⭐ 19 · TypeScript · Apache-2.0 · 推送 2026-09-20 · [GitHub](https://github.com/VeryMath/VeryMath-textbook-copilot) · 个人维护 · 中文 README

**个人自部署的课程学习工作台：读教材并与 AI 生成讲解、习题与课件**

本地 HTTP 服务加浏览器界面（另有 macOS/Windows 桌面安装包）的课程学习工作台：导入教材 PDF，连接用户自有 LLM API（Anthropic/OpenAI/Google/DeepSeek 或 OpenAI 兼容接口），由课程 Agent 调用内置 Skill 完成教材解析、分层讲解、知识点出题、思维导图、知识图谱与 LaTeX Beamer 课件生成；支持辅助资料上传、全文搜索与 OCR。所有教材与生成资料保存在本机个人目录，文件权限 0600/0700。OCR 需 Tesseract，课件编译需 XeLaTeX，均为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 左侧读 PDF 教材、右侧与 Copilot 对话的工作台布局
- 内置课程 Skill：教材解析、讲解、出题、思维导图、知识图谱、LaTeX Beamer 课件
- 支持多家 LLM Provider 及任意 OpenAI 兼容自定义接口，使用自有 API Key
- 个人数据全部保存在本机，目录权限 0700、文件 0600

## 适用场景

- 用自己的教材 PDF 建立本地课程学习工作台
- 针对章节生成讲解、练习题与思维导图、知识图谱
- 把章节内容编译成 16:9 LaTeX Beamer 课件

## 场景标签

`文档问答` `知识图谱` `文档解析` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L3: 个人部署的课程学习工作台：左侧阅读教材，右侧与 Copilot 交互。导入自己的教材 PDF，连接一个 LLM API，就能针对任意章节提问、讲解、出题，并生成思维导图、知识图谱和 LaTeX 课件。所有数据保存在你自己的电脑上，使
> L13: - **内置课程 Skill**：教材解析、讲解、知识点出题、思维导图、知识图谱、LaTeX Beamer 课件随项目提供；讲解视频可接入自定义 Skill。
> L26: 教学任务统一交给所选 LLM 完成，Agent 调用项目内置的 Skill 处理具体工作。每个用户用自己的 API 账号，路径已配置不代表任务已执行成功。

## 星数曲线

```mermaid
xychart-beta
    title "VeryMath/VeryMath-textbook-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-31 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c58629d8ebf8` · [字段定义](../../DATASET.md)*
