# Astro-Han/pawwork

⭐ 203 · TypeScript · Apache-2.0 · 推送 2026-10-12 · [GitHub](https://github.com/Astro-Han/pawwork) · [官网](https://pawwork.ai) · 个人维护 · 中文 README

**面向非技术用户的桌面 AI agent，基于 DSH 做文档与自动化**

基于 DeepSeek Harness（DSH）运行时封装的 macOS/Windows 桌面 AI agent 应用，目标用户为未使用过终端的知识工作者。内置 Web 搜索与 Office 文档技能（Word/Excel/PPT/PDF，捆绑 Python 3.12 与 LibreOffice 引擎离线运行），支持 cron 定时自动化任务，原生 Electron 外壳带系统菜单、文件选择器与自动更新。首次启动引导选择模型供应商并粘贴 API key，不随附模型凭证，任何 DSH 模型适配器支持的供应商均可使用；社区 DSH 插件可安装运行。macOS 构建已签名公证，Windows x64 未签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 内置 .docx/.xlsx/.pptx/PDF 技能，捆绑 Python 3.12 与 LibreOffice 引擎离线运行
- Automations 按 cron 计划执行保存的任务并输出到工作区
- 引导式首次配置：选择供应商、粘贴 API key，本地存储
- 使用真实的 DSH 运行时，社区 DSH 插件可安装运行

## 适用场景

- 用日常语言让 AI 处理发票提取、CSV 汇总、PDF 合并等文档工作
- 定时自动执行文件夹摘要、夜间导出等重复任务
- 联网检索资料并整理成决策备忘或草稿

## 场景标签

`AI 助手` `文档解析` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: **A free, open-source desktop AI agent for macOS and Windows, built on DeepSeek Harness (DSH) and packaged as a fini
> L11: PawWork turns a DSH agent runtime into a desktop application you could hand to someone who has never opened a termi
> L79: 3. PawWork works with the files, tools, models, and search it needs.

## 星数曲线

```mermaid
xychart-beta
    title "Astro-Han/pawwork 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 200 --> 204
    line [201, 203, 203]
```

2026-10-18 201 → 2026-10-24 203（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fae7c6036544` · [字段定义](../../DATASET.md)*
