# pennyzhaozhao/AI-interview-Assistant

⭐ 15 · Swift · MIT · 推送 2026-11-23 · [GitHub](https://github.com/pennyzhaozhao/AI-interview-Assistant) · 个人维护 · 中文 README

**给求职者的桌面端 AI 面试准备与实时辅助工具**

macOS（SwiftUI）与 Windows（WPF/.NET 10）双端桌面应用，功能覆盖面试前资料整理、多知识库管理、悬浮提示板实时语音识别与回答生成、截图问答、模拟面试逐题评分与 PDF 复盘导出。内置端侧 3D-Speaker CAMPPlus 说话人识别区分候选人与面试官；语音识别可用系统本地方案或豆包流式 ASR；模型请求由应用直连用户自选服务商，数据本地存储（SwiftData/Keychain），维护者声明无自建数据服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 悬浮提示板支持麦克风/系统音频识别并流式输出 Markdown 回答（macOS）
- 端侧 3D-Speaker CAMPPlus 声纹识别区分候选人与面试官，比对不上传音频
- 支持 Ollama、OpenAI、Claude、DeepSeek、Gemini、火山方舟六类服务商配置
- 多知识库管理，支持导入 PDF/TXT/Markdown/网页等并按面试启用

## 适用场景

- 面试前整理岗位 JD、公司资料并生成调研摘要
- 实时面试中通过悬浮提示板获取语音识别的问题与回答建议
- 用模拟面试功能练习并导出评估 PDF 复盘
- 在本地知识库中管理个人项目经历供 AI 参考引用

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L7:  **本地优先、开源的桌面端（macOS / Windows）AI 面试准备与辅助工具**
> L24: - 通过悬浮提示板识别语音、分析截图并生成回答建议；
> L198: 1. 在“服务商”中选择 Ollama、DeepSeek、OpenAI、Claude、Gemini 或火山方舟；


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `f85c82f0531c` · [字段定义](../../DATASET.md)*
